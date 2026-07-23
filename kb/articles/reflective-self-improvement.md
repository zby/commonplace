---
description: "First outward article: bootstrapping with the author inside — the compiler as foil, verification as the missing half, theories with reach as the goal; Commonplace supplies the structure"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/self-improving-system.md
  - kb/notes/definitions/reflective-system.md
  - kb/notes/definitions/reach-assessment.md
  - kb/notes/reflection-buys-addressability.md
  - kb/notes/retrieval-failure-is-reflection-failure.md
  - kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/reference/commonplace-as-a-reflective-system.md
---

# Reflective self-improvement

Your agent can read its own source. Not metaphorically: the prompts that steer it, the instruction files it obeys, the skills it loads, the code of its validators — all plain text, sitting in a repository the agent itself can open, search, and criticize. That makes possible something software never had before: a system that [improves itself](../notes/definitions/self-improving-system.md) by analyzing and rewriting its own definition. The name for this is **reflective self-improvement**, and Commonplace is a framework for doing it systematically.

## The bootstrap, with the author inside

The nearest precedent is the self-hosting compiler — and the differences are the point. Once a language compiles itself, every improvement to the compiler is written in the language it improves. But the compiler never analyzes its own source. It has no opinion about its code; every improvement was searched for, judged, and adopted by humans, and self-hosting contributed only the causal wire from artifact to behavior. Agents move the author inside the system. An agent can analyze its own instructions and code, find what is wrong with them, and propose better ones — and the improved artifacts define the next run, without touching a single weight.

This is *reflection* in the older, computational sense — [a system containing a causally connected representation of itself](../notes/definitions/reflective-system.md) — not "the model reflects on its mistakes." And it buys what fine-tuning cannot: [addressability](../notes/reflection-buys-addressability.md). A lesson retained as an artifact can be inspected, explained, revised, or deleted one at a time. Nothing can do that to a weight update.

## What the compiler had and the agent loses

Two guarantees do not survive the transfer. The compiler's wire is exhaustive: every line of source reaches the binary. The agent's wire is retrieval, and retrieval is best-effort — a retained lesson counts only if a later run finds it, so [retrieval failure is reflection failure](../notes/retrieval-failure-is-reflection-failure.md). And the compiler bootstrap carries its own verification: recompile the compiler with itself, and if the output reproduces, the bootstrap is sound. There is no fixed-point check for "this rewritten instruction is better." Worse, the agent judges its proposed changes using the very instructions being changed — Thompson's [trusting-trust problem](https://dl.acm.org/doi/10.1145/358198.358210), with fuzzier tools.

## Structure supplies the missing half

So a serious agent bootstrap must supply what the fixed point supplied: contracts for what counts as a claim, validation that runs as code rather than as self-assessment, review that can independently say no, navigation that makes retrieval reliable. Commonplace is that structure — a framework for agent-operated knowledge bases, with [typed artifacts](../notes/why-notes-have-types.md), validators, [review gates](../reference/README-REVIEW-SYSTEM.md), and curated indexes. And its goal is not accumulation. A memory file that piles up lessons is a junk drawer whatever its format; the loop is aimed at theories with [explanatory reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) — retained claims that explain why something works and hold beyond the episodes that produced them — and review exists to test [whether a claimed reach is genuine](../notes/definitions/reach-assessment.md) rather than a coincidence dressed as an explanation.

And it practices what it sells: [Commonplace retains its own methodology as a Commonplace knowledge base and improves through it](../reference/commonplace-as-a-reflective-system.md). [One traced episode](../reference/tag-readme-trace-observed-causal-connection.md): an index page outgrew its completeness claim; the strain became a recorded decision; the decision became validator code; and the validator then caught a case the prose search recipe had missed — which corrected the prose. Operation revised the system's definition, and the revised definition changed operation. The whole trail is in the commit history, checkable against the definitions.

## Where to go next

If your agent stack keeps notes it also reads, you are already running one of these — loosely. [Two questions](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) measure how loosely: where can your loop say no, and which artifact absorbs the accepted change? The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the theory, and [the repository](https://github.com/zby/commonplace) is the framework itself, bootstrapping in public.

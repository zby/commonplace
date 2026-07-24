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

Your agent can read its own source. Not metaphorically: the prompts that steer it, the instruction files it obeys, the skills it loads, the code of its validators — all plain text, sitting in a repository the agent itself can open, search, and criticize. Systems that act on a representation of themselves are not new — *computational reflection* has a decades-old literature. What is new is the surface: with LLM agents, natural language itself became operative, so a system that keeps its definition in prose can [improve itself](../notes/definitions/self-improving-system.md) by analyzing and rewriting that definition. The name for this is **reflective self-improvement**, and Commonplace is a framework for doing it systematically.

## The bootstrap, with the author inside

The nearest precedent is the self-hosting compiler — and the differences are the point. Once a language compiles itself, every improvement to the compiler is written in the language it improves. But the compiler never analyzes its own source. It has no opinion about its code: every improvement was searched for, judged, and adopted by humans; self-hosting contributed only the causal wire from artifact to behavior. Agents move part of the author inside the system. An agent can analyze its own instructions and code, find what is wrong with them, and propose better ones — and once a proposal is accepted, the improved artifacts define the next run, without touching a single weight.

This is *reflection* in the older, computational sense — [a system containing a causally connected representation of itself](../notes/definitions/reflective-system.md) — not "the model reflects on its mistakes." It also buys what fine-tuning cannot: [addressability](../notes/reflection-buys-addressability.md). A lesson retained as an artifact can be inspected, explained, revised, or deleted one at a time. A weight update can be trained over, rolled back wholesale, or steered against from outside — but never addressed one lesson at a time.

## What the compiler had and the agent loses

Two guarantees do not survive the transfer. The compiler's wire is exhaustive: every line of source reaches the binary. The agent's wire is retrieval, and retrieval is best-effort — a retained lesson counts only if a later run finds it, so [retrieval failure is reflection failure](../notes/retrieval-failure-is-reflection-failure.md). The compiler bootstrap also carries at least a fixed-point check: recompile the compiler with itself and compare the outputs. Ken Thompson [showed in his Turing Award lecture](https://dl.acm.org/doi/10.1145/358198.358210) that even this check can be fooled — a compiler corrupted in the right spot reproduces its own corruption while passing cleanly — so it was never proof of soundness, only a tripwire for accidental breakage. The agent has no tripwire at all: there is no fixed-point check for "this rewritten instruction is better," and the agent judges its proposed changes using the very instructions being changed — trusting trust again, with fuzzier tools.

## Structure makes the missing half explicit

So a serious agent bootstrap must supply the verification that self-hosting never had built in. It needs contracts for what counts as a claim, and validation that runs as code rather than as self-assessment. It needs review that can say no from outside the text it judges, and navigation that makes retrieval reliable. Commonplace is that structure: a framework for agent-operated knowledge bases. Its [typed artifacts](../notes/why-notes-have-types.md) declare what kind of claim a note makes; its validators run as code; its [review gates](../reference/README-REVIEW-SYSTEM.md) apply fixed criteria in a fresh context, so a note never grades itself; its curated indexes give retrieval a maintained map. Yet its goal is not accumulation. A memory file that piles up lessons is a junk drawer whatever its format. The loop is aimed at theories with [explanatory reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) — retained claims that explain why something works and hold beyond the episodes that produced them. Review exists to test [whether a claimed reach is genuine](../notes/definitions/reach-assessment.md) rather than a coincidence dressed as an explanation.

The framework practices what it sells, too: [Commonplace retains its own methodology as a Commonplace knowledge base and improves through it](../reference/commonplace-as-a-reflective-system.md). [One traced episode](../reference/tag-readme-trace-observed-causal-connection.md): an index page promised to list every note carrying its tag, and grew until that promise quietly broke. The strain became a recorded decision; the decision became validator code; and the new validator caught a case the old prose search instructions had missed — which corrected the instructions. At every step, the operative "no" belonged to a human maintainer reviewing and merging: the structure produced the artifacts and the evidence; a person outside the loop accepted them. That gate is a stage, not a refutation: the structure makes each acceptance cheap, evidenced, and reversible, and how much of the judging can migrate inward is what running the loop is meant to find out. Operation revised the system's definition, and the revised definition changed operation. The whole trail is in the commit history, checkable against the definitions.

## Where to go next

If your agent stack retains lessons about its own operation and later uses them to alter that operation, you are already running one of these — loosely. [Two questions](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) measure how loosely: where can your loop say no, and which artifact absorbs the accepted change? The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the theory, and [the repository](https://github.com/zby/commonplace) is the framework itself, bootstrapping in public.

---
description: Positioning direction (2026-06-12) — lead with self-hosting; the theory of LLM wikis runs as the executable LLM wiki that contains it, which no competitor can copy without first having a theory
type: kb/types/note.md
traits: []
tags: []
status: seedling
---

# Self-hosting as the flagship claim

Direction (2026-06-12): position Commonplace primarily on the self-hosting property — we develop a theory about LLM wikis, and that theory ships as an executable LLM wiki. The repo is not documentation *of* the system; it *is* the system: theory notes define the methodology, the methodology is prose, prose is executable by LLMs, and the executing agents maintain the wiki the theory lives in. Gates review the notes that define gates.

## Why this is the lead

- **Uncopyable.** Any markdown-memory product can claim types, links, and skills. "Our theory of LLM wikis runs as one" requires having the theory. It converts the KB's academic weight from a liability ("too theoretical") into the differentiator.
- **Verifiable by inspection.** Self-hosting is demonstrated, not asserted — a skeptic can read the repo and watch the loop close. Strongest possible answer to "does the methodology actually do anything."
- **The engineer's prestige signal.** Self-hosting compilers, metacircular evaluators — the audience already has the slot, and ours is literal.
- **It operationalizes "prose is executable."** The deepest theoretical claim of the project becomes the marketing claim; positioning and theory stop being separate texts.
- It subsumes the earlier showcase argument ([related-systems-as-showcase](./related-systems-as-showcase.md)): the reviews demo one workflow; self-hosting makes the entire repo the demo.

## Hazards

- **"LLM wiki" is ambiguous** — parses as "wiki about LLMs" as easily as "wiki operated by LLMs," and this repo is partly both. Every use needs a disambiguator in reach ("agent-operated," "that agents run"). Candidate category terms to keep scrutinizing: *LLM wiki*, *agent-operated wiki*, *executable wiki*.
- **Self-hosting proves the how, not the why.** Reflexivity alone tells a buyer nothing about their problem (agents forget, hallucinate, produce shallow work). The flagship claim needs a "for what" clause beside it; self-hosting is the proof, not the pitch.
- **"Wiki" connotations** — anyone-edits, low ceremony — partially conflict with the review-gated quality story; partially help (organic growth, links). Watch whether "wiki" or "knowledge base" wins in reader reactions.

## Decision (2026-06-12)

Adopted option 2: **"The theory of LLM wikis, running as one. A framework for agent-operated knowledge: typed, linked, review-gated markdown your agents execute."** The "LLM wiki" ambiguity is accepted: [Karpathy's gist](../../sources/karpathy-llm-wiki.md) made it a current term with the agent-operated reading attached, so the term now buys recognition rather than confusion.

Rejected candidates, kept for reuse in other surfaces:

1. "A framework for wikis that AI agents write, link, review, and run — self-hosting: its theory of LLM-operated wikis ships as one, running."
2. "Executable knowledge for AI agents: a wiki framework whose own theory runs as the wiki it describes — prose agents execute, gates that review it, git that audits it."

## Propagation

- [x] `pyproject.toml` `description` + `llm-wiki` keyword (2026-06-12)
- [x] README opening — leads with the flagship line, cites Karpathy for the term, explains self-hosting in the compiler sense (2026-06-12)
- [x] [the-knowledge-layer-for-ai-agents](./the-knowledge-layer-for-ai-agents.md) pitch draft — rewritten 2026-06-12: leads with Karpathy/LLM-wiki + self-hosting; RAG strawman replaced by "not another memory service" (no second runtime, audit-by-diff), per [gbrain-is-the-category-sibling](./gbrain-is-the-category-sibling.md)
- [ ] GitHub repo description/topics

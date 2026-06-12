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

## The analogy, drilled (2026-06-12)

Why self-hosting matters for compilers — four separable reasons, each translating differently:

1. **Proof by demonstration.** A self-compiling compiler has processed one large, demanding, real program: its own source. Capability shown, not claimed; historically *the* maturity milestone (C, Rust, Go).
2. **Forced feedback loop.** Developers live inside their own language; deficiencies hurt them first and daily.
3. **Compounding independence.** Post-bootstrap, compiler improvements are written in the language and built by the previous compiler — the system improves itself using itself.
4. **Coherence at the fixed point.** Self-application is a consistency test: a compiler bug tends to break the compiler's own build. Dark side: Thompson's *Trusting Trust* — self-hosting also self-propagates flaws.

**The tight form for Commonplace is the self-hosting interpreter — the metacircular evaluator — not the compiler.** Compilation has a translation step producing a different artifact that then runs; nothing here does that. Agents read conventions and skills fresh each session and follow them directly (the "externalized methodology" idea): the methodology is source that runs by being read. Structurally:

- The **LLM + harness is the host machine** — the evaluator beneath the metacircular one. Lisp's `eval`-in-Lisp never bootstraps the hardware either; a host beneath is constitutive of the form, not a defect of the analogy.
- **Metacircularity is the actual claim**: the methodology for operating LLM wikis is expressed in the medium it governs — wiki artifacts, with writing conventions applying to their own files. Lisp showed the language can state its own semantics; Commonplace shows the wiki format can carry the rules of its own operation.
- **Codification is the JIT.** Stable prose rules promote into validators, schemas, and `commonplace-*` commands — an interpreter compiling its hot, stable paths to native code while the rest stays interpreted and cheap to change. The constraining gradient *is* the interpreted/compiled boundary, and the analogy predicts where it sits: compile what is stable and frequently executed, keep interpreting what is still moving.

All four compiler benefits carry over: (1) the methodology runs a real demanding wiki — its own; (2) every methodology deficiency hits us first, with the loop institutionalized (log, workshops, gap rule); (3) methodology improvements are made using the methodology; (4) a wrong convention produces bad files *including its own*, so incoherence surfaces fast. Trusting Trust translates as a live caveat: an agent following a flawed instruction to revise instructions propagates the flaw — which is why our promotion loops keep a human oracle where GBrain's SkillOpt accepts on benchmark scores.

Honest disanalogy: compiler self-hosting is a binary milestone; ours is partial and gradual — a human directs the inquiry and accepts edits. "Self-hosting with a human in the loop" is the accurate form (humans write the bootstrapped compiler's patches too).

**Copy guidance:** keep "self-hosting" on outward surfaces — the term covers interpreters (the metacircular evaluator is the canonical self-hosting interpreter) and owns the prestige slot. README now says "in the bootstrapping sense" (was "in the compiler sense"). The interpreter/JIT machinery stays internal.

**Extraction candidate:** the transferable claim — LLM-executed methodologies run as metacircular interpreters: rules interpreted per session, codification as their JIT, trusting-trust as the characteristic failure mode, a human oracle as the mitigation — is `kb/notes/` material once it has carried weight beyond positioning.

## Propagation

- [x] `pyproject.toml` `description` + `llm-wiki` keyword (2026-06-12)
- [x] README opening — leads with the flagship line, cites Karpathy for the term, explains self-hosting in the compiler sense (2026-06-12)
- [x] [the-knowledge-layer-for-ai-agents](./the-knowledge-layer-for-ai-agents.md) pitch draft — rewritten 2026-06-12: leads with Karpathy/LLM-wiki + self-hosting; RAG strawman replaced by "not another memory service" (no second runtime, audit-by-diff), per [gbrain-is-the-category-sibling](./gbrain-is-the-category-sibling.md)
- [x] GitHub repo description/topics — description set to the pyproject line; topics: llm-wiki, ai-agents, knowledge-base, markdown, context-engineering, agent-skills, claude-code (2026-06-12)

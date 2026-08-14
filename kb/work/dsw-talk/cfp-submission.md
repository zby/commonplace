# DSW CFP submission — fill-in

Standard CFP field superset (the real Data Summit Warsaw form may differ; map fields as needed). Content is assembled from `abstract.md`.

## Speaker

- **Name:** Zbigniew Łukasiak
- **Email:** zbigniew@lukasiak.me
- **Sole author / speaker:** yes

## Session

- **Title:** Strange-Loop Knowledge Base: An LLM Wiki That Rewrites Its Own Rules
- **Format / length:** conference talk, 35 min
- **Level:** Intermediate
- **Track / topic:** AI / LLM applications, knowledge & context engineering, RAG (map to DSW's actual track list)
- **Language:** [English / Polish — confirm]

## Abstract — SHORT (form submission, ~120 words)

Most teams treat an LLM knowledge base or RAG store as something to *search*. But generated knowledge is unreliable — fluent output can be confidently wrong — and overfilling the context degrades the very agent meant to use it. Can the model instead *develop* the knowledge base continuously, even revise its own rules, while staying reliable? This is a field report from Commonplace, an open-source, LLM-operated but human-directed knowledge base that is also self-hosting — a knowledge base about building knowledge bases, so it can rewrite its own method. Through two worked cases I show the hybrid design that keeps it trustworthy: reviewable generation, stable rules moved into deterministic code, task-scoped retrieval. You'll leave with four patterns for your own LLM knowledge system — and an honest line on what still needs a human.

## Abstract — structured/compressed (~200 words, if the form has room for the four labelled beats)

**Problem.** Teams back LLM applications with a knowledge base or RAG store and treat it as something to search. But generated knowledge is unreliable — fluent output can be wrong — and overfilling the context degrades the agent meant to use it. Can a knowledge base instead be *developed* continuously by the model, even revise its own rules, while staying reliable? These systems are reaching production now, and they rot where a human used to check them.

**Methodology.** A field report from Commonplace, an open-source, LLM-operated but human-directed knowledge base that is also self-hosting — a knowledge base about building knowledge bases, so it can revise its own method. I trace two worked cases: one where the model sharpened an idea but quietly got three things wrong, and one where an operational strain led the agents to turn a prose convention into a validator that caught a real gap.

**Conclusions.** Reliability comes from a hybrid design: generation stays reviewable, stable rules move into deterministic code, retrieval loads only what the task needs. The self-hosting loop is real, but a human is in every step — self-hosting, not autonomous self-improvement.

**Implications for practitioners and business.** Four patterns for your own LLM knowledge or RAG system: develop knowledge, don't just draft it; treat fluent output as a candidate, not a certificate; codify only stable, checkable rules; and "write for reuse, load for the task." They cut maintenance cost while keeping the system trustworthy in production.

## Short description / elevator pitch (~40 words, if the form has a separate short field)

A field report from Commonplace, an LLM-operated wiki *about* building wikis. Watch one loop where the system rewrites its own rules — turning a prose convention into a validator — and learn the hybrid design that keeps LLM-generated knowledge reliable.

## Key takeaways

- Use the LLM to *develop* knowledge — retrieve, distinguish, propose, test scope, connect — not just draft prose.
- Treat fluent output as a candidate, not a certificate: separate generation from review.
- Move a rule into code only once it's stable and checkable; keep genuine judgment with the human or model.
- **Write for reuse; load for the task** — the context you fill is the capacity you spend.

## Agenda / talk outline (for the form; ~35 min)

Short promise that matches the abstract's strange-loop framing. The full internal build-outline is a separate, later job — see the stale-notice at the top of `outline.md`; do not submit from that file.

1. **The trap** (~4 min) — Most LLM knowledge bases / RAG are treated as search. Why that rots, misleads, and stops scaling where a human used to check it.
2. **A different idea** (~3 min) — A knowledge base the model *develops* — and one that is *about building knowledge bases*, so it can revise its own method. Set up the strange loop.
3. **Generation is not certification** (~7 min) — Case A: the model genuinely sharpened a rough idea, and in the same artifact quietly got three things wrong. Why generated knowledge must stay reviewable.
4. **The loop closes** (~9 min) — Case B, the spine: an operational strain leads the agents to turn a prose convention into a schema and validator, which catches a real gap the manual recipe missed and changes how future agents work. The system rewrote its own rules.
5. **Why it stays reliable** (~6 min) — The hybrid design: reviewable generation, deterministic rules, task-scoped loading (the context you fill is the capacity you spend).
6. **The honesty line + four patterns** (~4 min) — Which arrows are automated, which still need a human; self-hosting is not autonomous self-improvement. Four patterns to apply next week.
7. Timing slack (~2 min).

## Speaker bio

Adapted from the LLM Day 2026 bio (`../llm-do/kb/notes/meta/llm-day-2026-presentation.md`), retargeted to Commonplace and leading with PhilPapers — a real, worldwide knowledge index that is the ideal credibility anchor for a knowledge-base talk.

**Standard (~70 words):**

Zbigniew Łukasiak has been building software since the dot-com era — across startups, large corporations, and academia, including the University of London, where he helped build PhilPapers, a philosophy research index used by academics worldwide. He approaches LLMs not as an AI specialist but as an engineer who has watched fragile early systems mature into disciplined ones. He is the author of Commonplace, an open-source framework for LLM-operated knowledge bases.

**Short (~35 words):**

Zbigniew Łukasiak has built software since the dot-com era, including PhilPapers, a philosophy index used by academics worldwide. He is the author of Commonplace, an open-source framework for LLM-operated knowledge bases.

> Verify still-current: employer/role today, and whether to keep the third-person voice (matches most CFP forms).

## Notes for organizers (optional field, if present)

- The talk is a concrete case study, not a product pitch; Commonplace is open source.
- Slides include short before/after artifact excerpts (no live coding required); standard projector is sufficient.

## Still to confirm before submitting

- **Abstract length cap** — this is ~180 words; a ~40-word short version is above if the form is tight.
- **Field structure** — whether title / abstract / short description / takeaways / bio are separate fields or one blob.
- **Language** of the talk.
- **Track** name from the DSW form.
- **Bio** — reused from LLM Day 2026; confirm current employer/role and that PhilPapers/University of London details are still how you want to be described.

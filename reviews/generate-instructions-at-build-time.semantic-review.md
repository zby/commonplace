=== SEMANTIC REVIEW: generate-instructions-at-build-time.md ===

Claims identified: 9

1. "Since indirection is costly in LLM instructions, KB skills should be generated from templates rather than parameterised with runtime variables." (opening sentence)
2. "Skills in `kb/instructions/` hardcode paths dozens of times — in grep commands, script invocations, save targets." (paragraph 2)
3. "Making the KB reusable across projects requires these paths to vary." (paragraph 2)
4. Two options presented: runtime variables vs. build-time generation. (paragraphs 3–4)
5. "Runtime variables… Adds interpretation overhead to every skill use, across every substitution site. Occasionally the LLM gets it wrong." (paragraph 3)
6. "Build-time generation is the right choice." (paragraph 5)
7. "It's constraining applied to configuration — the template is soft, the generated output is hard." (paragraph 5)
8. "You pay the flexibility cost once at setup time, not on every use." (paragraph 5)
9. "The canonical form for skills is standalone (paths relative to KB root: `./notes/`, `./scripts/`). Embedding a knowledge base in a parent project (like `commonplace/`) is the special case that requires a path prefix." (paragraph 6)

WARN:
- [completeness] The note presents exactly two options — runtime variables and build-time generation — as the solution space for making KB paths portable. A third option exists that does not cleanly map to either: **symlinks or filesystem-level aliasing**, where the KB is always mounted at a canonical path regardless of the parent project. This avoids both runtime interpretation overhead and a build step. It is an infrastructure-level solution rather than a content-level one, so the note's framing (which is about what the LLM reads) may exclude it by design, but the note does not state that scope restriction — it says "Two options" without qualification.
- [completeness] A second unstated option: **convention over configuration** — all projects adopt the same directory structure so paths never vary. The note assumes paths must vary ("Making the KB reusable across projects requires these paths to vary") without considering whether the variation requirement could be eliminated entirely by standardizing the embedding location. This would be a zero-cost alternative that avoids both runtime and build-time overhead.

INFO:
- [completeness] The note claims "Skills in `kb/instructions/` hardcode paths dozens of times." This is presented as the premise for why paths must vary. But if the skills are designed for the KB's own use (as they currently are), the "dozens of hardcoded paths" are correct as-is. The note's argument depends on a future use case (reusability across projects) that may or may not materialize. The reasoning is sound given that premise, but the note presents the reusability requirement as established fact rather than a design choice.
- [grounding] The note claims it is "constraining applied to configuration" and links to methodology-enforcement-is-constraining.md. That source defines constraining as a gradient from underspecified/indeterministic to deterministic enforcement. The note's usage fits — templates are soft, generated output is hard — but the source's constraining gradient is about methodology enforcement (instructions → skills → hooks → scripts), not about configuration resolution. The note extends the constraining concept to a new domain (configuration portability) without flagging this as an extension. The fit is reasonable but not a direct application of the source's framework.
- [grounding] The link to `001-generate-topic-links-from-frontmatter.md` in the Relevant Notes section describes it as an "earlier case of the same move — replacing LLM-interpreted output with a deterministic build step." The linked file does not exist at the specified path (it may have been moved or deleted). This is a structural issue more than a semantic one, but it means the claimed exemplification cannot be verified.

PASS:
- [grounding] The foundation link to indirection-is-costly-in-llm-instructions.md is accurate. That source explicitly discusses the same KB skill portability scenario in its "Example: KB skill portability" section, uses the same runtime-vs-build-time framing, and even links back to this note. The two notes are tightly co-developed and mutually consistent. The note's central claim (build-time generation avoids per-read interpretation overhead) is directly supported by the source's cost model analysis.
- [grounding] The link to instruction-specificity-should-match-loading-frequency.md is used with the relationship "motivates: always-loaded context should be slim; variable interpretation adds complexity." The source does argue that always-loaded context competes for attention, which supports the note's argument that adding variable interpretation to frequently-loaded skills is costly. The attribution is accurate.
- [internal-consistency] The note is internally consistent. The canonical-form claim (paragraph 6) complements the build-time generation argument — if the canonical form is standalone with relative paths, and embedding is the special case, then generation is the right mechanism to bridge between them. No definition drift or pairwise contradiction found.
- [internal-consistency] The description field ("KB skills should be generated from templates at setup time, not parameterised with runtime variables — applying the general principle that indirection is costly in LLM instructions") faithfully represents the body. No elision of tensions.

Overall: 2 warnings, 3 info
===

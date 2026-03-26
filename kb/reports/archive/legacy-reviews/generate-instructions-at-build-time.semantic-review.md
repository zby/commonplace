<!-- REVIEW-METADATA
note-path: kb/notes/generate-instructions-at-build-time.md
last-full-review-note-sha: f4e57a1b148ac69cee43c1a0f1ef9df55b9057ff
last-full-review-note-commit: cc365676b30ed9f3d77958177ab9107a32e2f046
last-full-review-at: 2026-03-24T12:00:00+01:00
last-accepted-note-sha: f4e57a1b148ac69cee43c1a0f1ef9df55b9057ff
last-accepted-note-commit: cc365676b30ed9f3d77958177ab9107a32e2f046
last-accepted-at: 2026-03-24T12:00:00+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->
=== SEMANTIC REVIEW: generate-instructions-at-build-time.md ===

Claims identified: 14

1. "Since indirection is costly in LLM instructions, KB skills should be generated from templates rather than parameterised with runtime variables." (opening sentence)
2. "Skills in `kb/instructions/` hardcode paths dozens of times — in grep commands, script invocations, save targets." (paragraph 2)
3. "Making the KB reusable across projects requires these paths to vary." (paragraph 2)
4. Two options presented as the complete solution space: runtime variables vs. build-time generation. (paragraphs 3-4)
5. "Runtime variables… Adds interpretation overhead to every skill use, across every substitution site. Occasionally the LLM gets it wrong." (paragraph 3)
6. "Build-time generation is the right choice." (paragraph 5)
7. "It's constraining applied to configuration — the template is soft, the generated output is hard." (paragraph 5)
8. "You pay the flexibility cost once at setup time, not on every use." (paragraph 5)
9. "The canonical form for skills is standalone (paths relative to KB root: `./notes/`, `./scripts/`). Embedding a knowledge base in a parent project (like `commonplace/`) is the special case that requires a path prefix." (paragraph 6)
10. "Not all build-time inputs need to be committed to the repo. A second category exists: values that are static within one installation but vary between installations." (Installation-specific inputs, paragraph 1)
11. "The mechanism is identical: templates contain placeholders, a setup or build step resolves them from a local (gitignored) config file." (Installation-specific inputs, paragraph 2)
12. "The build step should resolve only what the task declares it needs — the typed-callable pattern applied to configuration dependencies." (Injection scope)
13. "When a config value is missing, the generated output should state what's unavailable rather than silently omitting it." (Graceful absence)
14. For recurring tasks, configuration separates "the stable procedure… from the variable environment." (Installation-specific inputs, paragraph 3)

WARN:
- [completeness] The note presents exactly two options for making paths portable: runtime variables and build-time generation. At least two alternatives are unaddressed: (a) **convention over configuration** -- all projects adopt the same embedding path (e.g., always `kb/`), so variation never arises and no generation step is needed; (b) **symlinks or filesystem aliasing**, where the KB is mounted at a canonical path regardless of the host project. The note says "Two options" without qualifying that scope. If the enumeration is implicitly restricted to "content-level solutions visible to the LLM," that restriction should be stated.
- [completeness] The "Installation-specific inputs" section defines two categories of build-time input: repo-committed values and installation-specific values (static within one installation but varying between installations). A boundary case falls between these: **values that are mostly static within an installation but occasionally change** (e.g., a sibling repo that gets moved, a tool path that changes after a version upgrade). These are not "static within one installation" in the full sense, but they also do not vary per-run, so they are not "runtime parameters" either. The note's two-category taxonomy has no mechanism for detecting that a previously-valid resolved value has gone stale. The "Graceful absence" paragraph acknowledges the problem of missing values at build time but not the problem of values that become wrong after build time.
- [grounding] The link to `001-generate-topic-links-from-frontmatter.md` in the Relevant Notes section claims it "exemplifies: an earlier case of the same move -- replacing LLM-interpreted output with a deterministic build step." This file does not exist at the specified relative path, nor anywhere in the repository. The claimed exemplification cannot be verified and the link is dead. (This was flagged in the prior review and persists in the current revision.)

INFO:
- [grounding] The note claims build-time generation is "constraining applied to configuration" and links to methodology-enforcement-is-constraining.md. That source defines constraining as a gradient from underspecified/indeterministic to deterministic enforcement of methodology (instructions -> skills -> hooks -> scripts), specifically about methodology enforcement. The note extends constraining to a different domain: configuration resolution. The mapping is plausible (template = soft, generated output = hard), but this is an analogical extension rather than a direct application of the source's framework. The source does not discuss configuration.
- [grounding] The "Injection scope" paragraph invokes the typed-callable pattern: "the build step should resolve only what the task declares it needs." The linked source (instructions-are-typed-callables.md) defines typed callables as skills with document type signatures (e.g., `/ingest: source -> source-review`). It does not discuss configuration dependency declarations. The note extends the concept from "skills declare which document types they accept" to "tasks declare which config values they need." This is a reasonable analogy but the source does not support it directly; it would be more precise to frame this as extending the typed-callable pattern to a new domain rather than applying it.
- [completeness] The note's core premise ("Skills in `kb/instructions/` hardcode paths dozens of times") grounds the need for portability. But the need for portability -- that the KB should be reusable across projects -- is presented as established fact rather than as a design aspiration that may or may not be pursued. The reasoning is sound given the premise, but the note does not mark the dependency on that external decision.

PASS:
- [grounding] The foundation link to indirection-is-costly-in-llm-instructions.md is accurate and reciprocal. That source explicitly discusses the same KB skill portability scenario in its "Example: KB skill portability" section, uses the identical runtime-vs-build-time framing, and links back to this note. The central claim (build-time generation avoids per-read interpretation overhead) is directly supported by the source's cost model: "a variable like `{{claw_root}}` doesn't just occupy the tokens for its name -- it requires the LLM to maintain the mapping in working memory, recognise substitution sites, perform the replacement mentally, and act on the result."
- [grounding] The link to instruction-specificity-should-match-loading-frequency.md with relationship "motivates: always-loaded context should be slim; variable interpretation adds complexity" accurately reflects the source. That note argues always-loaded context competes for attention with the actual task, which directly supports the argument that adding variable interpretation to frequently-loaded skills is a cost to avoid.
- [grounding] The link to scenario-decomposition-drives-architecture.md with relationship "motivates: the recurring 'review related systems' scenario revealed the need for installation-specific paths" is accurate. That source discusses two operating contexts (commonplace repo vs. installed project), sibling repo paths, and installation-specific context requirements, which directly motivates the "Installation-specific inputs" section.
- [internal-consistency] The note is internally consistent. The canonical-form claim (standalone with relative paths) complements the build-time generation argument: if the canonical form uses relative paths and embedding is the special case, then generation is the correct mechanism to bridge between them. The "Installation-specific inputs" section extends the same template-and-build-step mechanism to a broader class of inputs without contradicting the original framing.
- [internal-consistency] The description field ("KB skills should be generated from templates at setup time, not parameterised with runtime variables -- applying the general principle that indirection is costly in LLM instructions") faithfully captures the body's primary argument. The description omits the "Installation-specific inputs" extension, but since the description captures the note's central claim, this is acceptable compression.
- [internal-consistency] The "Graceful absence" recommendation ("the generated output should state what's unavailable rather than silently omitting it") is consistent with the build-time model. It correctly places absence handling at build time, following from the overall argument that resolution should happen before the LLM encounters the output.

Overall: 3 warnings, 3 info
===

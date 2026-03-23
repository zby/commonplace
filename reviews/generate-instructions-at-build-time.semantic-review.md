<!-- REVIEW-METADATA
note-path: kb/notes/generate-instructions-at-build-time.md
last-full-review-note-sha: 19b0ccf8d94a1f6c337372eaf0f5cfbc27b5631b
last-full-review-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-full-review-at: 2026-03-23T09:32:55+01:00
last-accepted-note-sha: 19b0ccf8d94a1f6c337372eaf0f5cfbc27b5631b
last-accepted-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-accepted-at: 2026-03-23T09:32:55+01:00
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
- [completeness] The note presents exactly two options for path portability: runtime variables and build-time generation. At least two alternatives are not considered: (a) **symlinks or filesystem aliasing**, where the KB is mounted at a canonical path regardless of the host project, avoiding both runtime interpretation and a build step; (b) **convention over configuration**, where all projects adopt the same embedding path so that variation never arises. The note says "Two options" without scoping this to content-level solutions. If the enumeration is implicitly scoped to "what the LLM reads," that scope restriction should be stated.
- [completeness] The "Installation-specific inputs" section identifies two categories of build-time input (repo-committed values vs. installation-specific values) and describes the mechanism as "identical." But the section does not address a boundary case: **values that are mostly static but occasionally change between runs within a single installation** (e.g., a sibling repo that was moved, or a tool whose path changes after a version upgrade). These are not truly "static within one installation" but also not "runtime parameters" in the note's sense. The note's two-category taxonomy (committed vs. local-config) has a gap for values that need re-resolution without a full rebuild. This matters because the "graceful absence" paragraph hints at runtime discovery ("the agent discovering the path doesn't exist mid-task"), but the build-time model has no mechanism for detecting that a previously-valid value has gone stale.
- [grounding] The link to `001-generate-topic-links-from-frontmatter.md` in the Relevant Notes section claims it "exemplifies: an earlier case of the same move — replacing LLM-interpreted output with a deterministic build step." This file does not exist at the specified path (`./001-generate-topic-links-from-frontmatter.md` relative to `kb/notes/`), nor anywhere else in the repository. The claimed exemplification cannot be verified and the link is dead. (This was also flagged in the prior review; the note has been updated since but the dead link persists.)

INFO:
- [completeness] The note claims "Skills in `kb/instructions/` hardcode paths dozens of times." The premise that these paths need to vary depends on a future use case (reusability across projects). The note presents this as established fact rather than a design aspiration. The reasoning is sound given the premise, but the note would be more honest about its dependency if it framed this as a design goal.
- [grounding] The note claims build-time generation is "constraining applied to configuration" and links to methodology-enforcement-is-constraining.md. That source defines constraining as a gradient from underspecified/indeterministic to deterministic enforcement of methodology (instructions -> skills -> hooks -> scripts). The note extends constraining to a different domain: configuration resolution. The fit is reasonable (template = soft, generated output = hard) but the source's framework is specifically about methodology enforcement, not about configuration portability. The note treats this as a direct application rather than an analogical extension.
- [completeness] The "Injection scope" paragraph invokes the typed-callable pattern: "the build step should resolve only what the task declares it needs." But the linked source (instructions-are-typed-callables.md) is about document type signatures for skills (e.g., `/ingest: source -> source-review`), not about configuration dependency declarations. The note is extending the concept from "skills declare which document types they accept" to "tasks declare which config values they need." This is a reasonable analogy but the source does not discuss configuration dependencies at all. The note presents this as an application of the typed-callable pattern rather than an extension to a new domain.

PASS:
- [grounding] The foundation link to indirection-is-costly-in-llm-instructions.md is accurate and bidirectional. That source explicitly discusses the same KB skill portability scenario in its "Example: KB skill portability" section, uses the same runtime-vs-build-time framing, and links back to this note. The central claim (build-time generation avoids per-read interpretation overhead) is directly supported by the source's cost model analysis: "a variable like `{{claw_root}}` doesn't just occupy the tokens for its name — it requires the LLM to maintain the mapping in working memory, recognise substitution sites, perform the replacement mentally."
- [grounding] The link to instruction-specificity-should-match-loading-frequency.md with relationship "motivates: always-loaded context should be slim; variable interpretation adds complexity" is accurate. The source argues that always-loaded context competes for attention with the actual task, which supports the note's argument that adding variable interpretation to frequently-loaded skills is costly.
- [grounding] The link to scenario-decomposition-drives-architecture.md with relationship "motivates: the recurring 'review related systems' scenario revealed the need for installation-specific paths" is accurate. That source discusses installation-specific context (sibling repos, two operating contexts) and the need for paths that vary between installations, which directly motivates the "Installation-specific inputs" section.
- [internal-consistency] The note is internally consistent. The canonical-form claim (standalone with relative paths) complements the build-time generation argument: if the canonical form uses relative paths and embedding is the special case, then generation is the correct mechanism to bridge between them. The "Installation-specific inputs" section extends the same mechanism (templates + build step) to a broader class of inputs without contradicting the original framing. No definition drift detected.
- [internal-consistency] The description field ("KB skills should be generated from templates at setup time, not parameterised with runtime variables — applying the general principle that indirection is costly in LLM instructions") faithfully represents the body's core argument. The description does not mention installation-specific inputs, which is the main addition since the description was written, but since the description captures the note's primary claim accurately, this is acceptable compression rather than misrepresentation.
- [internal-consistency] The "Graceful absence" paragraph ("When a config value is missing, the generated output should state what's unavailable rather than silently omitting it") is consistent with the build-time model. The note correctly identifies that absence handling belongs at build time rather than runtime, which follows from the overall argument that resolution should happen before the LLM sees the output.

Overall: 3 warnings, 3 info
===

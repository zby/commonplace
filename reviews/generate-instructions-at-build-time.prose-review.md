=== PROSE REVIEW: generate-instructions-at-build-time.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note asserts "Build-time generation is the right choice" as settled fact. The reasoning is plausible but it is the note's own argument, not a cited finding. It is also an architecture note in seedling status, which makes the assertive framing especially premature. Similarly, "Occasionally the LLM gets it wrong" presents a failure mode as given without evidence or frequency data.
  Recommendation: Soften "is the right choice" to something like "is the better fit here" or "is preferable for this case." For the LLM-gets-it-wrong claim, either add an example or hedge ("risks occasional misresolution" or similar).

INFO:
- [Source residue] The note uses "commonplace/" and "claw_root" as concrete path names. These are project-specific details, but the note's title and description claim a general principle ("KB skills should be generated from templates at setup time"). The specifics are useful as illustration but are not framed as examples — they read as the note's primary substance. Worth checking whether a reader outside this project would understand the note's point without knowing what `commonplace/` or `claw_root` refers to.
- [Proportion mismatch] The core claim — that build-time generation is preferable to runtime variables — is well-covered in the first three paragraphs. However, the final paragraph about canonical form and the "special case" of embedding introduces a distinct sub-topic (what the canonical path form should be and when a prefix is needed) that gets only two sentences. This idea either deserves development or could be a separate note, since it makes an independent claim about what counts as the canonical case.

CLEAN:
- [Pseudo-formalism] No formal notation or symbolic apparatus is present. The note uses prose throughout.
- [Orphan references] No specific figures, data points, or empirical claims appear without sourcing. The note's claims are architectural/design-level, not empirical.
- [Unbridged cross-domain evidence] The note does not cite cross-domain studies or empirical findings. Its evidence is internal to its own domain (LLM instruction design), so no bridging is needed.
- [Redundant restatement] The note is compact (four paragraphs plus a link section). Each paragraph advances a new point: the grounding principle, the problem, the two options, the verdict, and the canonical-form corollary. No section re-explains what a prior section already established.
- [Anthropomorphic framing] "The LLM reads and acts directly" and "the LLM substitutes on every invocation" use "reads," "acts," and "substitutes" — these describe observable processing behavior rather than implying mental states. The language is precise enough for the note's purpose.

Overall: 1 warning, 2 info
===

=== PROSE REVIEW: text-testing-framework.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note presents a detailed seven-section framework — contracts, test pyramid, metamorphic tests, corpus compatibility, production workflow, failure modes, minimal checklist — entirely with assertive framing ("Software tests work because there's a spec," "Once you have contracts, you can test them," the numbered production workflow as a definitive pipeline). The title calls this "source material" and the opening says "Full framework for automated testing of text artifacts, received 2026-02-21," but there is no attribution of who produced it or what evidence backs the specific decompositions. The framework reads as authoritative yet its provenance is opaque.
  Recommendation: Add a brief attribution line (who produced this, in what context) so readers can calibrate trust. If it was an LLM-generated brainstorm, say so; if it came from a practitioner with production experience, say that instead.

- [Proportion mismatch] The note's title foregrounds "framework" and the description highlights "contracts per document type, test pyramid, production workflow." The contracts section (Section 1) and the test pyramid (Section 2) receive the most development, which is appropriate. However, Section 3 ("Testing meaning indirectly") introduces metamorphic testing and claim extraction — arguably the hardest and most novel part of text testing — in a terse bullet list with no explanation of how any of these techniques actually work. Meanwhile Section 4 ("Compatibility with a collection of texts") covers corpus-level checks with similar brevity but is less central. The load-bearing novelty (how do you test meaning?) gets thinner treatment than the more familiar structural/rubric layers.
  Recommendation: If this is meant as raw reference material to be consumed later, this may be acceptable as-is. But if the note is meant to inform implementation decisions, Section 3 needs development — at minimum, one sentence per technique explaining what it actually does.

INFO:
- [Source residue] The note claims general applicability to "text artifacts" but uses software-engineering framing throughout: "pre-commit / local lint," "CI unit tests," "CI integration tests," "regression suite with golden notes." The production workflow (Section 5) is entirely structured around a software CI/CD pipeline. This is not necessarily a problem — the note's context is a knowledge base that lives in a git repo — but a reader outside that context might find the framing assumes a software development workflow rather than a general text production workflow.

- [Redundant restatement] Section 7 ("Minimal starting checklist") partially recapitulates items already listed in Sections 1 and 2 (required sections, max length, no PII, clarity rubric, main point in first 2 sentences). As a checklist it serves a different purpose (quick-start subset), but the items are not marked as drawn from the earlier sections, so the relationship between the checklist and the full framework is implicit.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus present. The note uses plain prose and bullet lists throughout. Clean.

- [Orphan references] No specific figures, percentages, named studies, or empirical claims appear without context. The note stays at the level of categories and techniques rather than citing specific data. Clean.

- [Unbridged cross-domain evidence] The note draws an analogy between software testing and text testing ("Software tests work because there's a spec. Free text can have specs too") but frames it explicitly as an analogy rather than asserting direct equivalence. No cross-domain empirical findings are cited without bridging. Clean.

- [Anthropomorphic framing] The note discusses LLM judges in Section 6 ("LLM judges not deterministic," "Judges can be lenient") but uses "judge" as a functional role label, not an anthropomorphic attribution. No verbs implying mental states or agency are applied to models. Clean.

Overall: 2 warnings, 2 info
===

=== PROSE REVIEW: maintenance-operations-catalogue-should-stage-distillation-into-instructions.md ===

Checks applied: 8

WARN:

INFO:
- [Proportion mismatch] The title claim is about the staging/distillation mechanism — how catalogue entries graduate into instructions. The "Distillation pipeline" section that carries this argument is four numbered steps with no elaboration, while the "Catalogue" section (which demonstrates the mechanism by example) is roughly four times longer. The proportions reflect the note's dual role as both argument and working artifact, so this is defensible, but the pipeline steps could benefit from brief elaboration — particularly step 3 ("Mark as ready when inputs, outputs, and decision points are stable"), which asserts a readiness criterion without explaining how to judge stability.
  Recommendation: Consider adding one sentence per pipeline step clarifying the judgment call involved, or split the readiness criteria into a short subsection. This would bring the load-bearing mechanism closer in weight to the illustrative catalogue entries.

CLEAN:
- [Source residue] The note is about KB maintenance operations and all terminology — orphan notes, frontmatter, `kb/notes/`, `kb/instructions/`, `kb/log.md` — belongs to that domain. No leaked framing from a narrower or different source context.
- [Pseudo-formalism] The bash code blocks are executable scripts serving practical purposes (orphan detection, raw text detection, link enumeration). They are tools, not decorative notation.
- [Confidence miscalibration] The note proposes its own pipeline and catalogue structure. The language is appropriately prescriptive for a process note: "should be distilled," "mark as ready when," imperative procedure steps. No speculative framework is presented as established fact, and no established findings are hedged unnecessarily.
- [Orphan references] No specific figures, data points, percentages, or empirical claims appear in the note. All claims are procedural and self-contained.
- [Unbridged cross-domain evidence] No cross-domain evidence is cited. All examples and procedures are within the KB maintenance domain.
- [Redundant restatement] The opening paragraph sets up the staging-ground concept, "This note is that staging ground" closes the introduction, and each subsequent section starts with its own contribution. No section re-explains what a prior section established.
- [Anthropomorphic framing] No references to models or agents with human-like attributions. The note addresses human-driven maintenance procedures.

Overall: 0 warnings, 1 info
===

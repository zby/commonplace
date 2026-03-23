=== PROSE REVIEW: evaluation-automation-is-phase-gated-by-comprehension.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The three-phase framework (comprehension, specification, generalization) is the note's own construction, not cited from a source. Yet it is introduced with assertive language: "Evaluation automation in practice follows a characteristic sequence: **comprehension first, specification second, generalization third**." The phrase "in practice follows" and "characteristic sequence" present a proposed decomposition as an observed empirical regularity. The "three phases" section header and numbered list reinforce this by presenting the framework as definitional rather than proposed. The note does cite one practitioner report as matching the pattern ("This sequencing matches a practitioner pattern described in one detailed field report"), but a single field report is thin evidence for "in practice follows a characteristic sequence."
  Recommendation: Hedge the framing to match the epistemic status. E.g., "a plausible sequencing is: comprehension first, specification second, generalization third" or "in the cases we've examined, evaluation automation tends to follow..." The phases section could be introduced as "A proposed decomposition" rather than "The three phases."

- [Proportion mismatch] The core claim is that comprehension gates the other phases — it must come first and cannot be skipped. The section that carries the most weight for this claim is "Why this is a gate, not a style preference," which is only ~70 words across two short paragraphs. Meanwhile, "Scope limits" (~70 words) and "Practical implication" (~60 words) get comparable space. The gate argument — the note's central and most distinctive claim — deserves more development. Why exactly does skipping comprehension leave specification "unconstrained by observed reality"? What does that look like concretely? The mechanism connecting missing comprehension to proxy-quality amplification is asserted in one sentence but not unpacked.
  Recommendation: Develop the "Why this is a gate" section with at least one concrete example of how skipping comprehension leads to proxy-quality amplification. Consider whether the practical implication section's checklist partly belongs inside the gate argument as evidence.

INFO:
- [Source residue] The note references "auto-generated tests and judges" and "score gains" in the paragraph about the practitioner report. These terms are evaluation-domain vocabulary, which matches the note's claimed scope (evaluation automation). However, the phrase "the loop functioned correctly; the objective did not" uses a slightly opaque shorthand — "the loop" and "the objective" are referencing specifics from the source without enough local context for a reader unfamiliar with that report. A reader might need to follow the link to understand what loop and what objective. This is mild — the sentence is intelligible in context — but the referent is underspecified.

CLEAN:
- [Source residue] The note claims to be about evaluation automation, and its vocabulary stays within that domain throughout. Terms like "evaluation loop," "score," "verifiers," "judges," "failure taxonomy," "calibration," "hard-oracle," "soft-oracle" all belong to the evaluation and measurement domain the note addresses. No unframed leakage from a narrower source domain.
- [Pseudo-formalism] No formal notation, equations, variables, or symbolic apparatus present. The note uses prose and a numbered list to describe its framework.
- [Orphan references] No specific figures, percentages, or named studies appear without sourcing. The one empirical reference ("one detailed field report") is linked to its source ingest in the Relevant Notes section. No unsupported quantitative claims.
- [Unbridged cross-domain evidence] The note stays within the evaluation/optimization domain. The one cited source (a practitioner field report about AI skill improvement via evals) is in the same domain as the note's claims. No cross-domain transfer without bridging.
- [Redundant restatement] Each section opens with new content. "Why this is a gate" does not restate the phases — it adds the argument for why the ordering is mandatory. "Scope limits" introduces new distinctions (hard-oracle vs. soft-oracle). "Practical implication" introduces a concrete checklist. No section opens by re-explaining prior sections.
- [Anthropomorphic framing] No language attributing human-like mental states to models. The note discusses evaluation pipelines, optimization loops, and failure taxonomies — all described in process/systems language. The one mention of human involvement ("usually human-led") correctly attributes human agency to humans.

Overall: 2 warnings, 1 info
===

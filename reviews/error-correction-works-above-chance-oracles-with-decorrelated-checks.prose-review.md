=== PROSE REVIEW: error-correction-works-above-chance-oracles-with-decorrelated-checks.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] "The ceiling on reliability is the product of signal strength and independence." (line 51) — This is stated as a mathematical fact, but it is the note's own formulation. Reliability under correlated checks does not literally equal "the product of signal strength and independence"; the relationship is more complex (it depends on the correlation structure, not a single scalar "independence" value). The sentence reads as a precise law but is actually an informal summary. Similarly, "the number of repetitions needed grows as 1/(TPR - FPR)²" (line 38) is presented as "the scaling law" — a definite article suggesting a known, named result — but the derivation offered is a sketch (separating two binomials), and the constant factor and confidence level are unstated. The claim is directionally correct but the framing overstates its precision.
  Recommendation: Hedge the ceiling-as-product sentence to "roughly proportional to" or "determined by." For the scaling law, either state the assumptions (desired confidence level, equal variances) or soften to "scales roughly as."

- [Proportion mismatch] The core claim in the title has two halves: (1) above-chance oracles and (2) decorrelated checks. The amplification condition (section 1) gets ~440 words of careful development with a table, worked examples, and a scaling law. The decorrelation section (section 2) — which the note itself calls "the binding constraint" — gets ~350 words of its own before delegating to the content-bias subsection. That subsection (~200 words) is grounded in a cited source, but the decorrelation strategies list (lines 55-58) is a bullet list of one-liners without the same depth of analysis that the TPR/FPR section receives. Given that the note explicitly identifies decorrelation as the harder, more important constraint, its treatment is thinner than the amplification section's.
  Recommendation: Develop the decorrelation strategies with the same analytical depth as the amplification section — e.g., sketch how effective gap degrades under correlation, or provide a concrete example showing how a nominal gap of 0.3 collapses to near-zero under correlated checks.

INFO:
- [Pseudo-formalism] The TPR/FPR notation and the table (lines 29-34) do genuine work: they make the "always-accept oracle" failure mode concrete and the gap concept visually intuitive. The "1/(TPR - FPR)²" scaling law is borderline — it is doing more work than plain prose would, but its derivation (lines 38-44) is a verbal argument dressed in notation rather than a rigorous proof. The gap-to-repetitions list (lines 40-43) is the load-bearing part; the formula itself adds modest precision beyond what the list already shows. Worth checking whether the formula earns its keep or whether the list alone suffices.

- [Source residue] The note is framed at a general level (error correction for LLM output), and the MAKER paper is explicitly introduced as a motivating example. However, the "Ways to construct above-chance oracles" section (lines 68-76) includes "self-consistency" described as "MAKER's core approach" without a general framing sentence first. This is minor — MAKER is named as an example — but the pattern of leading with MAKER rather than the general concept creates a slight source-first feel in that bullet.

CLEAN:
- [Orphan references] All specific claims are sourced. Condorcet's jury theorem is cited with a link (line 14). The Lampinen et al. finding is cited with a link to the ingest file (line 62). The MAKER paper is cited in the opening paragraph. The specific numbers in the table (0.8, 0.3, etc.) are illustrative examples, not empirical claims requiring sourcing. No orphan references found.

- [Unbridged cross-domain evidence] The Lampinen et al. citation (lines 62-66) is about LLM reasoning, and the note's domain is LLM error correction — same domain, no bridge needed. Condorcet's jury theorem and boosting are classical results cited for their formal structure, not as empirical findings from a foreign domain. The note correctly identifies Condorcet's equiprobable-class assumption and explains why TPR > FPR is the proper generalization. No unbridged transfers found.

- [Redundant restatement] Each section opens with new content. The decorrelation section (line 49) does not re-explain TPR > FPR; it states the new constraint directly. The "Ways to construct above-chance oracles" section (line 70) opens with the design question, not a recap. The "Implications" section (line 80) connects to the knowledge system without restating the theory. No redundant restatement found.

- [Anthropomorphic framing] The note avoids attributing mental states to models. LLMs "have systematic biases" (line 53), "reason more accurately" (line 62) — "reason" could be flagged, but in context it refers to performance on reasoning tasks, matching the Lampinen et al. paper's own terminology. No anthropomorphic framing that misrepresents the note's claims.

Overall: 2 warnings, 2 info
===

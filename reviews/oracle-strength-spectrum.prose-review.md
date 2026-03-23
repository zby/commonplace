=== PROSE REVIEW: oracle-strength-spectrum.md ===

Checks applied: 8

WARN:
- [Pseudo-formalism] The amplification section introduces formal-looking notation: "TPR > FPR" and "1/(TPR-FPR)^2" scaling. The scaling formula is stated without derivation, assumptions, or a source citation. A reader cannot use it to make a quantitative prediction because the note never defines what population the rates are measured over, what the checks are, or how decorrelation is quantified. The surrounding prose ("even a weak spec is useful" and "you need above-chance discrimination, not certainty") conveys the same insight without the formula. The TPR > FPR condition itself does genuine conceptual work (it sets the manufacturing bar), but the scaling formula is decorative.
  Recommendation: Either remove the 1/(TPR-FPR)^2 formula and keep only the qualitative claim that weaker oracles cost more to amplify, or cite the error-correction note for the derivation and state the formula's assumptions (independence of checks, binary classification setting).

- [Orphan references] "Quant firms pay $600k for 'research taste'" appears in the open questions section with no source, date, or context. It reads as a specific empirical claim (a salary figure) but is unsupported. The Tam et al. source linked in the same passage discusses automation of engineering vs. research, but the $600k figure does not appear to originate from that source.
  Recommendation: Either cite the source for this figure (compensation survey, job posting data, specific article) or replace it with a qualitative statement ("Quant firms pay premiums for research taste").

- [Confidence miscalibration] The three-step decomposition "Manufacture, amplify, monitor" is the note's own construction, and the maturation path (item 3) explicitly flags it as "invented here" and "unverified." However, the section heading and the body prose present it with assertive framing: "Oracle hardening decomposes into three steps" and "The steps have different failure modes: manufacturing without amplification gives a single fragile check; amplification without manufacturing leaves you voting over noise." The maturation path's hedge arrives too late to recalibrate a reader who has already absorbed the framework as established.
  Recommendation: Add hedged framing at the point of introduction. E.g., "One way to decompose oracle hardening is into three steps..." or "A plausible decomposition:". The maturation path can stay as-is; the issue is that the body prose needs the same epistemic marking.

INFO:
- [Proportion mismatch] The core claim is in the title: oracle strength is a spectrum. The section that establishes this ("The spectrum") is 8 lines — a bullet list with one-sentence descriptions per level. The "Manufacture, amplify, monitor" section is roughly 3x longer and develops a secondary framework (the pipeline) rather than the primary claim (the spectrum itself). The spectrum section could benefit from more development: what makes something move along the gradient? Are the five levels discrete or continuous? Are there intermediate positions? The note's weight currently sits on the pipeline, not the spectrum.
  Recommendation: Consider whether the spectrum section deserves more development (e.g., worked examples of tasks at each level, discussion of what determines position) or whether the pipeline section should be extracted to its own note to restore proportionality.

- [Source residue] The term "bitter-lessoning" in the open questions ("Does oracle strength predict bitter-lessoning?") is an informal verb form coined from the bitter lesson concept. While this is consistent with the note's own vocabulary (the bitter lesson boundary is its foundation), the verb form "bitter-lessoning" may read as jargon to anyone not already familiar with this KB's framing. This is borderline — the note defines its relationship to the bitter lesson in the opening paragraph, and the term appears only in the open questions section, which is exploratory.
  Recommendation: No action needed if the audience is internal to this KB. If broader readability matters, consider "Does oracle strength predict which components will be bitter-lessoned?" or "Does oracle strength predict where the bitter lesson applies?"

CLEAN:
- [Source residue] The note claims generality across engineering domains and uses examples from multiple domains (cryptography, schema validation, user churn, regression testing, code review). No single source domain dominates the framing. The bitter lesson / vision features vocabulary is appropriate since it is the explicit foundation being refined.

- [Unbridged cross-domain evidence] The Rabanser et al. finding (capability gains yield small reliability improvements) is from an AI-systems study applied to AI-systems claims — no domain bridge is needed. The note hedges appropriately: "If this pattern holds broadly — and it may not, since such findings are sensitive to the specific models and benchmarks used." The Karpathy verifiability framing is likewise applied within its native domain.

- [Redundant restatement] Sections are well-delineated. Each opens with its own contribution. The "Generator/verifier pattern" section references oracle strength from the spectrum section but does so to make a new claim (the pattern requires sufficient oracle strength), not to restate prior material. No redundant setup paragraphs found.

- [Anthropomorphic framing] The note avoids anthropomorphic language about models. The closest case is the Rabanser finding about "model self-assessment" which is a technical term for a model scoring its own outputs, not an attribution of mental states. Language throughout uses "stores," "encodes," "surfaces" — no "knows," "understands," or "believes."

Overall: 3 warnings, 2 info
===

=== PROSE REVIEW: spec-mining-as-codification.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The core claim is that spec mining is codification's operational mechanism — the "how" of converting blurry-zone components into calculators. The section that most directly serves this claim is "The pattern" (4 steps, ~100 words). Meanwhile "Why this matters for the bitter lesson boundary" (~150 words) and "Concrete workflow" (~150 words including the extended Lopopolo paragraph) each get comparable or greater treatment, and the Lopopolo production example alone is nearly as long as the core pattern section. The load-bearing section ("The pattern") is thinner than its downstream applications.
  Recommendation: Develop "The pattern" with more substance — what makes step 2 (identifying repeated micro-actions) work, what "deterministic artifact" means in practice beyond listing examples, why step 4 (re-running with constraints) produces reliability gains. Alternatively, consider whether the Lopopolo production narrative belongs in a separate note that this one links to rather than inlines.

- [Confidence miscalibration] "The calculator surface grows monotonically" (end of Concrete workflow, step 5) asserts a mathematical property — monotonic growth — as fact. This is only true if mined specs are never removed, which the Risks section itself contradicts: specs that "break under distribution shift" are "candidates for relaxing, not permanent codification." The note's own framework allows the calculator surface to shrink.
  Recommendation: Hedge: "The calculator surface tends to grow over time" or "grows monotonically as long as mined specs survive validation." The current phrasing contradicts the Risks section.

INFO:
- [Source residue] The note claims generality ("codification's operational mechanism") but all concrete examples are software engineering: "production logs," "verifier or deterministic helper," "linter rules," "refactoring PRs," "unit tests." The methodology-level parallel (instruction-to-script maturation) is mentioned in passing but not developed. This is mild — the note's tags place it in learning-theory, and the software framing is arguably the primary domain — but readers coming from the methodology angle may find the note narrower than its title promises.

- [Pseudo-formalism] The phrase "codification as compilation" in the first body paragraph uses a CS metaphor ("compilation") that implies more structure than the note delivers. Compilation has a specific meaning (source language to target language via formal grammar). The note's pattern — watch, identify, extract, re-run — is closer to refactoring or extraction than compilation (there is no grammar, no formal source language). The metaphor is suggestive but slightly misleading.

CLEAN:
- [Orphan references] All empirical claims are sourced. The Lopopolo (2026) reference is cited with a link and context. The "20% of engineering time (Fridays)" figure is attributed to that source. No floating numbers or uncited studies.

- [Unbridged cross-domain evidence] The Lopopolo source describes software engineering practice and is applied to software engineering claims — no domain bridge is needed. The methodology-level parallel (instruction-to-script) is explicitly framed as a parallel ("The same pattern appears at the methodology level"), not as direct evidence. The cybernetics reference is attributed to a specific source with a specific claim ("externalizing system-specific judgment"). No unbridged transfers found.

- [Redundant restatement] Sections are compact and each opens with new content. "Why this matters for the bitter lesson boundary" opens with a new claim (calculators survive scaling because the spec is the problem), not a restatement of the pattern. "Concrete workflow" opens with a new framing (agentic system failure clustering), not a recap. No redundant restatement detected.

- [Anthropomorphic framing] The note consistently uses mechanistic language: "the system does tasks," "the system becomes more reliable," "the system distills stochastic regularities." No anthropomorphic attribution of mental states to models. "Watch the system do tasks" uses "watch" for the human observer, not the system. Clean.

Overall: 2 warnings, 2 info
===

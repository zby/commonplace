## Grounding alignment — agent-context-is-constrained-by-soft-degradation-not-hard-token-limits

**Verdict: PASS (2 INFO)**

Followed 5 links: GSM-DC ingest, Chung et al. web-agent ingest, ConvexBench ingest, effective-context note, indirection note. Also checked Paulsen MECW snapshot. All central causal claims are accurately grounded. Source attributions are correct and scope is generally well-matched.

### Claims checked

**GSM-DC (Yang et al., 2025) — power-law error scaling.** The note claims "power-law error scaling with distractor count in math problems." The ingest confirms: error scales as a power law with distractor count, exponent grows with reasoning depth (delta from 0.11 to 0.49). Accurate.

**Chung et al. (2025) — agent-level collapse.** The note claims "injecting irrelevant task sequences into a web agent benchmark collapses success rates from 40–50% to under 10%." The ingest confirms: "success rates collapse from 40-50% at baseline to under 10% at 150k tokens." Numbers are accurate. See INFO-1 for a scope nuance.

**Chung et al. — iRAG mitigation.** The note says "Bolt-on retrieval (iRAG) provided only modest improvement, suggesting irrelevant context needs to be excluded, not compensated for." The ingest confirms iRAG "provides modest improvements but does not resolve the fundamental degradation." The "suggesting" language is appropriately tentative for the inference drawn. The ingest's own limitations section notes that dismissing retrieval based on one implementation is premature, which the note's tentative framing respects.

**ConvexBench (Liu et al., 2026) — complexity collapse.** The note says "F1 dropped from 1.0 at depth 2 to ~0.2 at depth 100, even though total tokens (5,331 at depth 100) were far below context limits." The ingest confirms all numbers exactly. "Compositional depth, not volume, was the bottleneck" accurately summarizes the source finding.

**Paulsen MECW (2025) — volume varies by task.** The note says "usable context can be far below advertised windows and is task-dependent." The source abstract reports MECW differs from MCW by "as much as >99%" and "shifts based on the problem type." Conservative, accurate attribution.

**Indirection note — complexity mechanism.** The note says "every layer of indirection costs context and interpretation overhead." This matches the linked note's thesis. The broader claim that "LLMs pay interpretation overhead proportional to context complexity" uses the indirection note as one mechanism example rather than as full evidence for proportionality — this is legitimate synthesis, not over-attribution.

**Effective-context note — relationship descriptor.** The note describes the relationship as "sharpens: the soft bound is not a single number but a task-dependent degradation surface." The effective-context note does argue exactly this. Accurate.

### Domain coverage

The note's two-dimensions framework (volume, complexity) with irrelevant context as a candidate third dimension is its own theoretical synthesis. Each dimension is grounded in at least one empirical source. The open questions section honestly flags where dimensions are confounded and where empirical isolation is lacking. The "invisible" section's claims about providers and practitioners are observational rather than source-grounded, but they are clearly framed as observations, not empirical findings.

### INFO

**INFO-1: Chung et al. collapse range compressed.** The note says irrelevant task sequences "collapses success rates from 40–50% to under 10%" without noting this is at the upper end of the tested range (150k tokens). The source measures progressive degradation across 25k–150k tokens. The note's phrasing could be read as an immediate effect of any irrelevant injection rather than a gradual curve across context lengths. The numbers themselves are accurate — the framing omits the scale dimension.

**INFO-2: GSM-DC "too small for attention dilution" is inference, not finding.** The open questions section states "GSM-DC's degradation occurs at token counts too small for attention dilution, suggesting the distractors interfere with reasoning directly." The GSM-DC paper does not characterize its token counts relative to attention-dilution thresholds. The inference is plausible (grade-school math problems with distractors are indeed short), and the hedging ("may be", "suggesting") is appropriate. But the causal mechanism (direct reasoning interference vs. attention dilution) is the note's interpretation, not the source's claim.

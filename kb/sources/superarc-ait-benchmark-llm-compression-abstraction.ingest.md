---
description: Ingest of SuperARC — AIT-grounded benchmark where frontier LLMs score phi ~0.03 while neuro-symbolic CTM/BDM achieves 1.000 on recursive compression; newer models regress; print-statement-only outputs demonstrate zero algorithmic abstraction
source_snapshot: superarc-ait-benchmark-llm-compression-abstraction.md
ingested: 2026-03-26
type: scientific-paper
domains: [evaluation-methodology, learning-theory, algorithmic-information-theory, LLM-limitations]
---

# Ingest: SuperARC — Can Complexity and Uncomputability Explain Intelligence?

Source: superarc-ait-benchmark-llm-compression-abstraction.md
Captured: 2026-03-26
From: https://arxiv.org/html/2503.16743v5

## Classification

Type: **scientific-paper** — peer-reviewed research with formal methodology (AIT-grounded benchmark design), quantitative results across multiple frontier LLMs, mathematical proofs (compression-prediction equivalence via Martingale theory), and systematic evaluation using a novel metric (phi).

Domains: evaluation-methodology, learning-theory, algorithmic-information-theory, LLM-limitations

Author: Hernández-Espinosa, Ozelim, Abrahão, and Zenil (Oxford Immune Algorithmics / Algorithmic Dynamics Lab). Zenil is a recognized researcher in algorithmic information theory and complexity science, with a track record in CTM/BDM methods applied to cognition. The group has published prior work on AIT-based evaluation of human and animal cognition. Credible in the AIT domain; less established in mainstream ML evaluation.

## Summary

SuperARC is an open-ended benchmark grounded in Algorithmic Information Theory that tests AI models' capacity for recursive compression and abstraction on binary sequences of increasing algorithmic complexity. The central finding is stark: frontier LLMs (GPT-4.5, Claude 3.5, Gemini, etc.) score phi = 0.007–0.042 while a neuro-symbolic AIXI/BDM/CTM baseline scores 1.000 (perfect). Most LLM-generated "correct" programs are bare print statements that reproduce sequences without any compression — zero abstraction. Newer model versions often regress on this benchmark despite improving on standard human-centric benchmarks. LLMs perform dramatically better on integer sequences, which the authors attribute to memorization of common mathematical sequences from training data — confirming that binary sequences strip away statistical shortcuts. The paper argues that recursive compression and optimal prediction are mathematically equivalent (proved via Martingale theory), and that current LLM architectures are fundamentally limited to the statistical subspace of their training distribution.

## Connections Found

The `/connect` discovery identified 8 genuine connections and rejected 7 candidates (including distillation, structure-activates, and discovery — all surface-vocabulary matches without mechanistic overlap).

**Strongest connections:**

1. **[From Entropy to Epiplexity](./from-entropy-to-epiplexity-rethinking-information-computationally-bounded.md)** — complements: both papers address the gap between statistical and algorithmic information measures, from opposite directions. Epiplexity formalizes what bounded observers CAN extract; SuperARC benchmarks what they CANNOT. SuperARC's explicit finding that Shannon entropy and GZIP/LZW "cannot capture algorithmic complexity" is precisely what epiplexity's framework predicts.

2. **[EsoLang-Bench](./esolang-bench-evaluating-genuine-reasoning-via-esoteric-programming-languages.md)** — complements: sibling benchmarks both stripping away training-distribution shortcuts to expose the gap between standard benchmark performance and genuine reasoning. EsoLang-Bench strips familiar syntax; SuperARC strips statistical shortcuts. Both find frontier LLMs scoring near zero.

3. **[First-principles reasoning selects for explanatory reach over adaptive fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md)** — exemplifies: the integer-vs-binary performance gap is a clean empirical demonstration of adaptive fit without explanatory reach. LLMs "reach" on integer sequences (familiar territory) but collapse on binary sequences (where no training-distribution fit exists). The "newer models regress" finding strengthens this: models are becoming better adapted while losing general compression capability.

4. **[Bitter lesson boundary](../notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md)** — exemplifies: recursive compression is an arithmetic-regime problem (the spec IS the problem, solutions are algorithmically determined). The neuro-symbolic AIXI/BDM/CTM approach is the calculator analogy from the note — a purpose-built system scoring perfectly where general-methods-plus-scale scores near zero.

5. **[Information value is observer-relative](../notes/information-value-is-observer-relative.md)** — exemplifies: same binary sequences, dramatically different extractability depending on computational architecture. AIXI/BDM/CTM extracts all structure; LLMs extract none.

6. **[Reverse-compression](../notes/reverse-compression-is-when-llm-output-expands-without-adding-information.md)** — exemplifies: print-statement-only code generation is reverse-compression at its most extreme — the output (program) is longer than the input (sequence) with zero compression. This is the first example outside the KB-writing domain.

7. **[Oracle-strength spectrum](../notes/oracle-strength-spectrum.md)** — exemplifies: SuperARC sits at the hard-oracle end with deterministic, exact verification of both correctness and compression quality.

8. **[Pathway/Sudoku-Bench](./pathway-beyond-transformers-sudoku-bench.md)** and **[Induction bias in sequence models](./induction-bias-sequence-models-ebrahimi-2026.md)** — complement: convergent evidence from different problem domains (constraint satisfaction, state tracking) reaching the same conclusion about fundamental transformer limitations.

**Synthesis opportunity flagged:** The "LLMs score zero on well-specified problems" cluster now spans four independent sources and problem domains (recursive compression, esoteric code, constraint satisfaction, state tracking). A synthesis note cataloging these converging findings, identifying shared structural properties, and mapping them onto the bitter lesson boundary could be high-value.

## Extractable Value

1. **The integer-vs-binary performance gap as a reach diagnostic** — LLMs dramatically improve on integer sequences (training-distribution match) while scoring near zero on binary sequences (no match). This is the cleanest empirical operationalization of the adaptive-fit-vs-explanatory-reach distinction the KB has seen. Could sharpen the [first-principles reasoning](../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) note with a concrete example. High reach — the diagnostic pattern (performance drops when training-distribution cues are removed) transfers to any evaluation domain. [quick-win]

2. **Print-statement-only generation as formal evidence of reverse-compression** — the KB's [reverse-compression](../notes/reverse-compression-is-when-llm-output-expands-without-adding-information.md) note currently has examples only from KB writing. SuperARC provides a formally measured instance in code generation: programs that are longer than the sequences they reproduce, with zero compression. The finding that temperature variation doesn't change this behavior is additionally informative — it rules out sampling as a factor. High reach — reverse-compression as a named failure mode applies wherever LLMs generate structured output. [quick-win]

3. **The phi metric as a benchmark design pattern** — the three-axis metric (correctness, compression quality via nBDM, solution type classification) deliberately privileges non-trivial solutions over correct-but-uncompressed ones. This is a concrete implementation of the hard-oracle idea from [oracle-strength spectrum](../notes/oracle-strength-spectrum.md): verification that checks not just whether the answer is right, but whether it demonstrates the target capability. Moderate reach — the pattern (verify capability, not just output) transfers broadly, but the specific nBDM weighting is AIT-specific. [just-a-reference]

4. **Newer models regress while improving on standard benchmarks** — if corroborated, this is a significant finding for evaluation theory. It suggests that standard benchmark optimization may actively trade away algorithmic reasoning capability. Low reach until independently confirmed — the finding could reflect SuperARC-specific tuning artifacts or measurement noise rather than a general trend. [deep-dive]

5. **Compression-prediction equivalence via Martingale theory** — the paper includes a mathematical proof that recursive compression and optimal prediction are equivalent. If this proof is sound, it grounds the intuitive connection between compression and intelligence in formal mathematics, going beyond the informal arguments the KB currently relies on. High reach if valid — it would mean any system that can't compress can't predict (in the algorithmic sense). [deep-dive]

6. **The AIXI/BDM/CTM perfect-score existence proof** — a neuro-symbolic system achieving phi = 1.000 on tasks where LLMs score ~0.03 is an existence proof that the problem is solvable, not just a demonstration that LLMs fail. This matters for the [bitter lesson boundary](../notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) argument: the calculator exists for this domain. Moderate reach — the existence proof is domain-specific but the pattern (purpose-built symbolic methods dominating on well-specified problems) transfers. [just-a-reference]

7. **Benchmark contamination resistance through uncomputability** — SuperARC's open-endedness (sequences of increasing complexity, with uncomputability at the limit) means the benchmark can't be saturated by training. This is a stronger contamination defense than EsoLang-Bench's unfamiliarity-based approach. The design principle transfers: ground benchmarks in mathematical limits, not merely in obscurity. High reach. [experiment]

## Limitations (our opinion)

**What was not tested:**

1. **The AIXI/BDM/CTM baseline is not a fair comparison.** AIXI is a theoretical construct instantiated specifically for algorithmic compression tasks — it is purpose-built for exactly this problem class. Comparing it to LLMs on recursive compression is like comparing a calculator to a language model on arithmetic. The comparison establishes that the problem is solvable (existence proof) but says nothing about whether general-purpose systems *could* solve it with appropriate prompting, tool use, or fine-tuning. The authors present this as evidence of LLM architectural limitations, but the real conclusion is narrower: LLMs-as-deployed, with standard prompting, cannot do this.

2. **No chain-of-thought, tool-use, or agentic configurations were tested.** The paper evaluates LLMs in single-turn generation mode. Current practice (and this KB's methodology) emphasizes that agent architectures with tool access, iterative refinement, and verification loops can solve problems that single-turn generation cannot. SuperARC's finding that LLMs "cannot compress" may be more precisely: LLMs in single-turn mode don't produce compressed solutions. Whether an LLM-with-Python-interpreter or an LLM-orchestrating-a-search-loop could improve is untested.

3. **The "newer models regress" claim is based on a small version comparison** without controlling for prompting strategy, temperature, or system prompt differences across model generations. It could reflect changes in default behavior (e.g., newer models are more verbose or more cautious about code generation) rather than loss of algorithmic capability.

4. **Binary sequences may not generalize to all forms of abstraction.** The paper claims to test "abstraction and prediction" broadly, but it specifically tests recursive compression of binary/integer sequences. Other forms of abstraction — analogical reasoning, conceptual generalization, structural transfer — are not measured. The conclusion that LLMs lack abstraction capability is stronger than the evidence supports; the evidence supports only that LLMs lack *algorithmic compression* capability.

5. **No ablation on sequence difficulty distribution.** The 100 binary sequences were categorized by algorithmic complexity, but the paper doesn't report how performance varies across the complexity spectrum in a way that would reveal whether there's a threshold effect or a smooth degradation. This matters for understanding whether the failure is total or partial.

6. **Author positioning.** The research group develops CTM/BDM methods and has a clear interest in demonstrating that their approach outperforms LLMs. The benchmark was designed by the same team that builds the winning baseline. This is common in ML research but worth noting — independent replication on the SuperARC benchmark would strengthen the findings substantially.

## Recommended Next Action

Write a note titled "LLMs fail categorically on well-specified problems that strip training-distribution cues" connecting to [bitter-lesson-boundary](../notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md), [first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md), and [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md). It would catalog the converging evidence from SuperARC, EsoLang-Bench, Pathway/Sudoku-Bench, and Ebrahimi's induction-bias work, identify the shared structural properties of these problem domains (well-specified, hard-oracle verifiable, no training-distribution shortcuts), and argue that these failures map to the arithmetic regime of the bitter lesson boundary — where purpose-built symbolic methods are the calculator, not a stopgap.

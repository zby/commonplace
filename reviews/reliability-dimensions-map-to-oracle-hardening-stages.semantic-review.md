=== SEMANTIC REVIEW: reliability-dimensions-map-to-oracle-hardening-stages.md ===

Claims identified: 14

1. [Table] Each of four Rabanser et al. reliability dimensions (consistency, robustness, predictability, safety) maps to a distinct "oracle question" and "hardening move."
2. [Table — Consistency] Consistency asks "Does this work?" and hardens by repetition, converting interactive oracle to hard oracle.
3. [Table — Robustness] Robustness asks "Does this still work?" and hardens by perturbation, converting soft oracle to hard oracle.
4. [Table — Predictability] Predictability asks "Will this work next time?" and hardens by calibrating confidence; discrimination would push it toward hard oracle.
5. [Table — Safety] Safety asks "What happens when it doesn't work?" and is "already a hard oracle by design: either the failure is bounded or it isn't."
6. [Why this mapping matters] The oracle-strength note says invest in telemetry/eval before capability because guidance is the bottleneck; the reliability framework shows where to invest.
7. [Why this mapping matters] "The empirical finding that capability gains have outpaced reliability gains over 18 months of model releases is the oracle-strength prediction confirmed at scale."
8. [Why this mapping matters] MAKER's million-step zero-error result "demonstrates what happens when you take this seriously for consistency."
9. [Why this mapping matters] The MDAP framework works "precisely because per-step oracle strength is hard (each Towers of Hanoi move has a deterministic correct answer)."
10. [Spec mining] Spec mining is the operational mechanism for consistency and robustness hardening.
11. [Spec mining] Rabanser Table 3 — mapping failures to reliability metrics — "is spec mining applied to evaluation itself."
12. [Predictability gap] Discrimination requires the model to know what it doesn't know at the individual-task level; the paper finds calibration improving but discrimination stagnant.
13. [Predictability gap] Predictability will be the last oracle to harden.
14. [Predictability gap] An approval gate converts a weak predictability oracle into an interactive one — the human provides the discrimination the model lacks.

---

WARN:
- [Completeness — Consistency oracle classification] The table says consistency "converts interactive oracle to hard oracle via repetition." In the oracle-strength spectrum note, an interactive oracle is defined as one where "you can ask for feedback" (user edits, thumbs up/down, preference pairs). Repetition of the same task and checking same-input/same-output is not asking for feedback — it is closer to manufacturing a hard oracle from a stochastic process. The "interactive" label for the starting oracle is a stretch; the starting point is better described as "no oracle" or "soft oracle" (you don't know whether a single run's output is correct without running it again). The mapping elides what the pre-hardening state actually is.

- [Completeness — Safety as "already a hard oracle by design"] The note claims safety "is the only dimension that's already a hard oracle by design: either the failure is bounded or it isn't." But Rabanser et al. define safety via compliance (S_comp) and harm severity (S_harm), computed using LLM-based judging. The source explicitly acknowledges this introduces "its own reliability concerns" (Section 6, Limitations). Furthermore, harm severity uses a graded scale (low = 0.25, medium = 0.5, high = 1.0) — this is a continuous score, not a binary gate. The note's characterization ("a gate, not a gradient") contradicts the source's operationalization, which is a weighted product of violation probability and expected severity, i.e., a gradient.

- [Grounding — MAKER and consistency] The note says MAKER "demonstrates what happens when you take this seriously for consistency." But MAKER does not address consistency as Rabanser et al. define it (same input, same output across runs). MAKER addresses correctness — achieving zero errors across a million steps. The MAKER system itself is stochastic (temperature > 0, voting across samples) and its consistency across runs is not evaluated. The note silently shifts "consistency" from the Rabanser definition (repeatability) to a different sense (reliable correctness through voting). This vocabulary mismatch risks readers thinking MAKER demonstrates Rabanser-consistency when it demonstrates correctness via error correction.

- [Grounding — Discrimination "stagnant"] The note says "The paper finds calibration improving but discrimination stagnant." Rabanser et al. actually report a more nuanced finding: "discrimination trends diverge across benchmarks: on tau-bench it has generally improved in recent models, whereas on GAIA it has in fact mostly worsened." Calling this "stagnant" collapses a divergent finding (improved on one benchmark, worsened on another) into a single characterization. "Stagnant" understates the GAIA worsening and erases the tau-bench improvement.

INFO:
- [Completeness — Boundary case: overlapping dimensions] Several boundary cases sit between dimensions. For example, a model that gives different answers to semantically identical questions (the NYC chatbot case from Rabanser Table 3) is classified under both consistency (C_out) and predictability (P_cal). The note's table presents the four dimensions as mapping to "distinct" oracle questions, but in practice the same failure can implicate multiple dimensions. The note's framing of "each dimension is a separate oracle that can be hardened independently" may overstate the independence.

- [Completeness — Boundary case: hardening without moving on the oracle spectrum] The note frames each dimension as a "hardening move" that converts weaker oracles to stronger ones. But some of Rabanser's robustness sub-metrics (fault robustness, environment robustness) already show "ceiling effects — most models handle these perturbations well" (Section 4.2). If they are already at ceiling, these are already hardened — the interesting engineering question is prompt robustness, which the note does not single out despite Rabanser identifying it as "a key differentiator."

- [Grounding — "the oracle-strength prediction confirmed at scale"] The note calls the Rabanser finding about capability outpacing reliability "the oracle-strength prediction confirmed at scale." The oracle-strength spectrum note itself hedges this: "If this pattern holds broadly — and it may not, since such findings are sensitive to the specific models and benchmarks used." The reviewed note drops that hedge entirely and presents the finding as confirmation, not suggestive evidence.

- [Internal consistency — "a gate, not a gradient" vs. elsewhere] The note describes safety as "a gate, not a gradient" and "a hard constraint" but the preceding three rows treat their dimensions as gradients that move along the oracle spectrum. This categorical difference (binary vs. continuous) is not acknowledged as breaking the parallel structure of the mapping. The note's title claims dimensions "map to oracle-hardening stages" (implying movement along a spectrum), but safety is then excluded from this pattern.

PASS:
- [Internal consistency — Title claim and body] The title claim ("reliability dimensions map to oracle-hardening stages") is consistently supported throughout. The table maps each dimension to an oracle question and hardening move. The body sections develop implications of this mapping. No section contradicts the central framing.

- [Grounding — Rabanser four dimensions] The note correctly identifies the four dimensions from Rabanser et al. (consistency, robustness, predictability, safety) and their definitions are faithful to the source. The characterization that these dimensions are "independent of raw capability" matches the source's Section 2 ("all four dimensions are independent of raw capability").

- [Grounding — Spec mining connection] The claim that Rabanser Table 3 maps real-world failures to reliability metrics is accurate. Describing this as "spec mining applied to evaluation" is the note's own interpretive move, but it is a reasonable one — extracting testable properties from observed failure classes is close to the spec mining pattern.

- [Grounding — Augmentation/automation boundary] The predictability gap paragraph's claim that a 90%-accurate agent with poor discrimination is "fine as augmentation but dangerous as automation" aligns with Rabanser Recommendation 4, which makes the same distinction.

- [Internal consistency — Predictability gap] The note's claim that predictability will be "the last oracle to harden" is consistent with its earlier table entry showing predictability as the dimension with the most uncertain hardening path (calibration is a soft oracle; discrimination would push toward hard, but discrimination is what's not improving).

Overall: 4 warnings, 4 info
===

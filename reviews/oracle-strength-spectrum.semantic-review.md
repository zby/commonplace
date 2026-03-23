=== SEMANTIC REVIEW: oracle-strength-spectrum.md ===

Claims identified: 14

## Claims extracted

1. **The bitter lesson boundary is better understood as a gradient of oracle strength** — "the boundary is better understood as a gradient of oracle strength — how cheaply and reliably you can check whether output is correct" (The spectrum, opening paragraph)
2. **Five-point enumeration of oracle types:** hard, soft, interactive, delayed, no oracle (The spectrum, bullet list)
3. **The bitter lesson is strongest at the hard-oracle end and weakest at the no-oracle end** (The spectrum)
4. **The oracle spectrum maps to the Karpathy verifiability framing** — "resettable, efficient to retry, and rewardable — three properties that strengthen as oracle strength increases" (The spectrum)
5. **The core engineering move is to harden the oracle** — "Convert no-oracle into some-oracle, then tighten" (The engineering move)
6. **This is codification applied to the objective itself** (The engineering move)
7. **Verification quality is the bottleneck, not generation quality** — "invest in telemetry and eval harnesses before investing in capability" (The engineering move)
8. **Rabanser et al. evidence: capability gains yield only small reliability improvements** (The engineering move)
9. **Rabanser et al.: model self-assessment improves in calibration but not reliably in discrimination** (Manufacture, amplify, monitor — Amplify step)
10. **Oracle hardening decomposes into three steps: manufacture, amplify, monitor** (Manufacture, amplify, monitor)
11. **Error correction works whenever TPR > FPR and checks are decorrelated** — cited from the error-correction note (Amplify step)
12. **The generator/verifier pattern only works when oracle strength is sufficient** (The generator/verifier pattern depends on this)
13. **Oracle strength predicts bitter-lessoning** — framed as open question but with supporting argument via Deutsch's explanatory reach (Open questions)
14. **Oracle strength is itself hard to assess** — "you don't always know whether your oracle is hard or soft until you test at scale" (Open questions)

---

## Step 2: Completeness and boundary cases

### The five-point oracle spectrum (Claim 2)

The grounding definition is the note's own: oracle strength is "how cheaply and reliably you can check whether output is correct." The five points are: hard, soft, interactive, delayed, no oracle.

**Boundary cases tested:**

1. **Simplest instance: a spell checker.** Spell checking has a dictionary lookup (hard oracle for known words) but also a "did you mean X?" suggestion (soft oracle for intent). It maps cleanly to a hybrid of hard and soft. PASS.

2. **Between interactive and delayed: asynchronous human review with a turnaround of hours.** A code review that comes back the next morning is not truly "interactive" (you can't iterate in real time) but it's not "delayed" in the sense of "did the bug surface months later" either. The spectrum jumps from "you can ask for feedback" to "you only know later" without a clear boundary for asynchronous review loops with moderate latency. INFO.

3. **Adversarial oracle: a checker that is actively gamed.** Goodhart's law scenarios where the oracle is technically cheap and deterministic (a metric) but the system optimizes against it until it stops correlating with the real objective. The note's own open question ("Oracle strength is itself hard to assess") gestures at this, but the spectrum itself classifies by cost and reliability of checking, not by whether the check measures the right thing. An adversarial oracle looks "hard" on the spectrum but behaves like "soft" in practice. INFO.

4. **Composite oracles: a test suite that covers 80% of cases exactly and leaves 20% to heuristics.** This is a blend of hard and soft oracle within a single verification step. The spectrum treats oracle types as discrete points, not as compositions. The note's examples of "oracle hardening" (e.g., schema validation turning soft into hard) implicitly acknowledge composition, but the five-point list doesn't accommodate a single oracle that is partly hard and partly soft. INFO.

5. **Probabilistic hard oracle: statistical hypothesis tests.** A/B testing gives you a p-value — the check is deterministic and cheap to run, but the answer is probabilistic (confidence intervals, not boolean). It's more rigorous than "proxy score that correlates" (soft) but not "exact, cheap, deterministic" (hard). It falls between hard and soft without a clear home. INFO.

### The manufacture/amplify/monitor decomposition (Claim 10)

The grounding definition is the note's own: these are "three steps, each with its own methods and failure modes" that compose into a pipeline for oracle hardening.

**Boundary cases tested:**

1. **Missing step: calibrate.** The amplify step assumes the oracle's TPR and FPR are known or estimable. In practice, you often need to calibrate the oracle — determine its actual discriminative power — before you can decide how many repetitions to use. Calibration is neither manufacturing (creating the oracle) nor amplifying (voting over it) nor monitoring (checking for drift). It sits between manufacture and amplify. WARN.

2. **Missing step: compose.** Combining oracles that target different aspects (one checks format, another checks semantic consistency, a third checks factual accuracy) into a single quality gate is a design problem the note doesn't address. The error-correction note discusses decorrelation but oracle composition — weighting, sequencing, and resolving conflicts between oracles — is not manufacturing, amplifying, or monitoring. WARN.

3. **Monitor feeding back into manufacture.** The note says monitoring "detect[s] when a hardened oracle encodes a vision feature" and the component "may need to move back toward the learned regime." But the feedback loop — where monitoring findings trigger a new round of manufacturing — is not described as part of the pipeline. The three steps are presented linearly, though the note's failure modes section hints at interaction ("either without monitoring risks locking in a vision feature"). INFO.

### The engineering prescription: invest in verification before capability (Claim 7)

**Boundary case:** A domain where oracle strength is fundamentally limited (e.g., creative writing, long-horizon strategic decisions). Investing in eval harnesses first may be wasteful if no oracle above chance can be constructed. The note's own open question about "no oracle" domains partially addresses this, but the prescription "invest in telemetry and eval harnesses before investing in capability" is stated as general, not conditional on oracle constructability. INFO.

---

## Step 3: Grounding alignment

### Rabanser et al. — capability gains vs. reliability (Claims 8, 9)

The note says: "across 14 models and 18 months of releases, capability gains yielded only small reliability improvements." The source says: "despite 18 months of rapid capability gains have produced only small improvements in reliability." Attribution is accurate.

The note says: "model self-assessment improves in calibration (aggregate confidence alignment) but not reliably in discrimination (per-instance separation of correct from incorrect)." The source says: "Calibration has improved noticeably in recent models... In contrast, discrimination trends diverge across benchmarks: on tau-bench it has generally improved in recent models, whereas on GAIA it has in fact mostly worsened." The note's phrasing "not reliably in discrimination" is a fair summary of "diverges across benchmarks" — the source confirms improvement on one benchmark and worsening on another. PASS.

**Domain coverage check:** The note uses Rabanser et al. to support the claim that "verification quality is the bottleneck, not generation quality" and that "generation and verification improve on independent tracks." The source measures reliability (consistency, robustness, predictability, safety) as distinct from capability (accuracy). The note equates "reliability" with "verification quality," which is a move the source does not make. Rabanser et al. treat reliability as a property of the agent's own behavior (does it behave consistently, robustly, predictably, safely?), not as a property of external verification infrastructure. An agent can be reliable without external verification, and external verification can be strong for an unreliable agent. The note's inference — that the reliability-capability gap evidences a verification bottleneck — is plausible but is the note's own analytical move, not something Rabanser et al. claim. The note hedges this ("If this pattern holds broadly — and it may not"), which mitigates. INFO.

### Karpathy verifiability framing (Claim 4)

The note says the Karpathy verifiability framing — "resettable, efficient to retry, and rewardable" — is an oracle-strength argument, and that "three properties that strengthen as oracle strength increases." This is sourced through the deploy-time-learning note, which quotes Karpathy directly: "a task is verifiable to the extent it is resettable, efficient to retry, and rewardable."

The mapping is: hard oracle -> all three properties strong; no oracle -> none. This is reasonable — a deterministic test is resettable, efficient, and rewardable; a "vibes" check is none. But "interactive oracle" (user edits, thumbs up/down) is resettable and rewardable but not necessarily efficient. "Delayed oracle" is rewardable (eventually) but not efficient or easily resettable. The mapping doesn't break but it's not as clean as "strengthen as oracle strength increases" suggests — the three Karpathy properties don't move in lockstep along the spectrum. INFO.

### Tam et al. — engineering vs research as oracle prediction (Open questions)

The note says Tam et al. "observe that agentic coding tools automate engineering (hard oracle — tests, specs, benchmarks) while research problem selection (no oracle — 'you can't know in advance whether a solution exists') resists automation entirely." The ingest file confirms: Tam argues engineering has "built-in verification — tests, specs, benchmarks — that enables RL-driven automation, while research lacks ground truth." Attribution accurate. The note's parenthetical reframing into oracle-strength vocabulary is transparent. PASS.

### Codification link (Claim 6)

The note says "This is codification applied to the objective itself, not just to the implementation" and links to deploy-time-learning-the-missing-middle.md. The link target discusses codification as a phase transition of prompts to deterministic code — codification of implementation, not of objectives. The note's claim that oracle hardening is codification of the objective is its own extension. The link creates an impression that deploy-time-learning grounds this specific claim, but the target discusses a different application of codification. WARN.

---

## Step 4: Internal consistency

1. **Pairwise contradiction check:** No contradictions found between sections. The spectrum section defines oracle types; the engineering move prescribes hardening; the manufacture/amplify/monitor section operationalizes hardening; the generator/verifier section identifies a dependency; the maturation path and open questions acknowledge limitations. The progression is logically coherent.

2. **Definition drift check:** "Oracle strength" is used consistently throughout as "how cheaply and reliably you can check whether output is correct." No drift detected.

3. **Tension between prescription and open questions:** The engineering move section states confidently "invest in telemetry and eval harnesses before investing in capability, because verification quality is the bottleneck." The open questions section asks "Does oracle strength predict bitter-lessoning?" and notes "Oracle strength is itself hard to assess." If oracle strength is hard to assess, the confident prescription to invest in verification first rests on being able to identify where on the spectrum you are — which the note itself flags as uncertain. This is a tension, not a contradiction, and the maturation path section acknowledges the prescription is "plausible" but ungrounded. INFO.

4. **Summary faithfulness:** The note has no compressed summary section distinct from the body. The description field ("Exploratory framework — proposes oracle strength as a gradient underlying the bitter lesson boundary, with hypotheses about engineering priorities and an oracle-hardening pipeline") faithfully represents the body content. PASS.

---

WARN:
- [Completeness] The manufacture/amplify/monitor decomposition is missing a **calibration** step. Amplification requires knowing or estimating the oracle's TPR and FPR to determine the number of repetitions needed. The note jumps from "mine a spec" (manufacture) to "vote over it" (amplify) without addressing how you determine the oracle's discriminative power. Calibration is distinct from all three named steps.
- [Completeness] The manufacture/amplify/monitor decomposition is missing a **composition** step. Combining multiple oracles targeting different quality dimensions into a single gate — weighting, sequencing, conflict resolution — is a design problem not covered by manufacturing individual oracles, amplifying them, or monitoring for drift.
- [Grounding] The link from "codification applied to the objective itself" points to deploy-time-learning-the-missing-middle.md, which discusses codification of *implementation* (prompts to code), not codification of *objectives*. The linked source does not ground the specific claim made.

INFO:
- [Completeness] The oracle spectrum's jump from "interactive" to "delayed" leaves a gap for asynchronous review with moderate latency (hours, not real-time, not months). This zone has distinct engineering properties — you can iterate, but slowly — that neither category captures well.
- [Completeness] Probabilistic hard oracles (statistical tests, A/B experiments) fall between "hard" and "soft" — they are rigorous and automated but deliver confidence intervals, not booleans. The spectrum doesn't accommodate this.
- [Completeness] Adversarial/Goodharted oracles look hard on the spectrum (cheap, deterministic check) but fail to track the real objective. The spectrum classifies by verification cost, not verification validity. The open questions section partially addresses this.
- [Completeness] Composite oracles (partly hard, partly soft within a single verification step) don't map cleanly to any single point on the five-point spectrum.
- [Completeness] The prescription to invest in verification before capability is stated generally but may not apply where oracle strength is fundamentally limited (no-oracle domains).
- [Grounding] The note equates Rabanser et al.'s "reliability" (agent behavioral properties) with "verification quality" (external infrastructure). These are related but distinct concepts; the inferential step from one to the other is the note's own move.
- [Grounding] The Karpathy verifiability properties (resettable, efficient, rewardable) don't strengthen uniformly along the oracle spectrum — interactive oracles are resettable and rewardable but not efficient; delayed oracles are eventually rewardable but neither efficient nor easily resettable.
- [Consistency] The engineering move section prescribes investing in verification first with confidence, while the open questions section flags that oracle strength is itself hard to assess. If you can't reliably determine where on the spectrum you are, the prescription to invest in verification first becomes harder to act on.

PASS:
- [Completeness] The core five-point spectrum (hard, soft, interactive, delayed, no oracle) covers the most common verification scenarios. Standard engineering examples (unit tests, BLEU scores, user feedback, churn metrics, subjective quality) all map cleanly to one of the five points.
- [Grounding] Rabanser et al. attribution is accurate: "capability gains yielded only small reliability improvements" and "calibration improves but discrimination diverges across benchmarks" both faithfully represent the source. The note's hedging ("if this pattern holds broadly — and it may not") is appropriate.
- [Grounding] Tam et al. attribution is accurate: engineering automation vs. research resistance to automation is correctly characterized and the oracle-strength reframing is transparent.
- [Consistency] No pairwise contradictions between sections. No definition drift — "oracle strength" is used consistently throughout.
- [Consistency] The description field faithfully represents the body content.
- [Consistency] The maturation path section accurately identifies all major speculative claims and their current grounding status, which demonstrates honest self-assessment.

Overall: 3 warnings, 8 info
===

---
description: Scholarly-review automation should decompose reviewer work into separately verifiable subroles before giving an AI system reviewer-level authority
type: kb/types/note.md
traits: [title-as-claim, has-external-sources, synthesis]
tags: [evaluation, llm-interpretation-errors]
status: seedling
---

# Review automation should target verifiable subroles before reviewer identity

Automating "a reviewer" is the wrong first target. A reviewer bundles several operations with different oracle strength: checking cited facts, finding related work, tracing proofs, comparing novelty, judging methodology, weighing significance, and recommending acceptance. Those operations do not cross the automation boundary together. The durable design rule is: automate the subroles whose outputs can be independently checked, and keep reviewer identity, final judgment, and publication authority outside the automated surface until the checks for those subroles become discriminative.

[Google's Paper Assistant Tool](../sources/towards-automating-scientific-review-google-paper-assistant.ingest.md) is valuable because it nearly follows this rule despite using broad "review" language. PAT segments a manuscript, assigns deeper review to logical sections, uses specialized agents, and grounds and deduplicates synthesized findings. Its strongest evaluation surface is not generic review quality but a filtered SPOT subset of equation and proof errors with verified errata or retractions. That makes the result a partial oracle-hardening case: technical-error detection is narrower than peer review, but it is easier to verify.

[Beyond "Not Novel Enough"](../sources/beyond-not-novel-enough-llm-assisted-scholarly-critique.ingest.md) shows the same move on a softer subrole. Novelty assessment is not hard-oracle work, so the pipeline first studies human novelty reviews, extracts reviewer patterns, performs related-work discovery, builds landscape and novelty-delta structure, and then evaluates both reasoning alignment and conclusion agreement. That does not make novelty judgment automatic in the same way a proof-error check can be automatic. It does show how an oracle-poor review subrole can be made more inspectable before being delegated.

## Review subroles have different oracle strength

The automation target should be the review operation, not the social role. At least four subroles separate:

| Subrole | Verification surface | Automation posture |
|---|---|---|
| Evidence and citation checking | source text, quoted spans, bibliographic matches | Strong candidate for automation when evidence is accessible and linkable |
| Technical error detection | proofs, equations, code, tests, retractions, errata | Automate narrow checks first; report findings with evidence |
| Novelty and related-work comparison | retrieved prior work, extracted contributions, delta analysis | Use as augmented analysis unless judge calibration is measured |
| Significance, methodology, and acceptance judgment | taste, norms, risk tolerance, venue fit, social accountability | Keep human-authoritative unless a narrower verifier is built |

This is an application of [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md). The word "reviewer" hides the boundary because it names a role rather than a verifiable task. The role-level framing tempts a system designer to compare AI output with human reviews as a whole. The subrole framing asks which claim was checked, what evidence the check consumed, and whether a human can reject the output without redoing the whole review.

## Output quality is not enough

Pass@k-style review expansion illustrates the failure mode. PAT reports that independent repeated calls can improve recall while degrading precision, which leaves a human to inspect a larger pile of candidate problems. That is why [synthesis is not error correction](./synthesis-is-not-error-correction.md): merging many critiques is not the same as selecting supported ones. A review system needs an aggregation rule whose verifier matches the subrole. Redundant proof checks can be adjudicated by agreement plus source evidence; complementary section reviews need synthesis, but synthesis must preserve grounding and expose uncertainty rather than launder every candidate into a single confident report.

The same issue appears inside semantic review. [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md) warns that a model can reconstruct a plausible route to a true conclusion instead of checking the route the artifact actually took. A review subrole therefore needs process evidence, not just final-answer agreement. [An outcome check licenses replay; a rule needs the process verified](./an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md) generalizes the point: outcome and process checks inspect different things, and only process checks can license transferring authority to a reusable review rule.

## The implication for Commonplace gates

Commonplace should treat "review this note" as a bundle of narrow, inspectable subroles rather than as one generic judgment. The existing semantic gates already move in that direction: grounding alignment checks source-to-claim fit, internal consistency checks contradiction, boundary-case gates test enumerations, and explanatory-reach gates ask whether the mechanism constrains the claim. This is the process-structure side of [process structure and output structure are independent levers](./process-structure-and-output-structure-are-independent-levers.md): the gate should force a particular reasoning check before it emits a verdict.

Two shipped Commonplace decisions already model the split. [ADR-012](../reference/adr/012-types-for-structure-traits-for-review.md) keeps validation structural and routes semantic expectations through traits and gates. [ADR-023](../reference/adr/023-quote-anchored-citations-for-code-grounded-reviews.md) splits citation grounding into a deterministic quote-resolution check and the [grounding alignment gate](../instructions/review-gates/semantic/grounding-alignment.md), which spends LLM judgment on whether a cited source actually supports a claim. That is the subrole pattern in miniature: harden the structural piece, isolate the semantic piece, and state what authority each check grants.

The next step is not to make a stronger all-purpose reviewer. It is to make each gate's inspected object explicit:

- what claim, source, or framework the gate reads
- what evidence would falsify the note's route
- whether the gate checks an outcome, a process, or both
- what authority a pass grants: readability, source alignment, local consistency, or promotion readiness

That matches [evaluation automation is phase-gated by comprehension](./evaluation-automation-is-phase-gated-by-comprehension.md). For a new review subrole, first inspect failures manually, then specify the gate, then calibrate whether the gate discriminates before treating it as automated authority. Until that calibration exists, the gate is augmentation: useful pressure on the writer, not a replacement for accountable judgment. The [composition friction gate](../instructions/composition-friction-gate.md) is a useful extreme: it explicitly refuses an overall pass verdict and only routes attention to the central claim and weakest inferential joints.

## Scope

This note does not claim AI systems cannot perform high-quality peer-review tasks. The PAT and novelty-assessment sources both show useful automated or semi-automated review work. The claim is about authority assignment. A system can help authors, surface likely errors, retrieve overlooked prior work, and organize novelty deltas before it can be trusted as a reviewer. The boundary is not model capability in the abstract; it is whether each delegated subrole has a verifier strong enough for the authority being granted.

---

Relevant Notes:

- [The augmentation-automation boundary is discrimination not accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) -- mechanism: aggregate review quality is insufficient without per-instance discrimination over unsupported findings
- [Oracle strength spectrum](./oracle-strength-spectrum.md) -- defined-in: supplies the hard/soft/interactive/delayed/no-oracle vocabulary for review subroles
- [Error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- mechanism: explains why repeated review calls need discriminative, decorrelated checks rather than mere aggregation
- [Semantic review catches content errors that structural validation cannot](./semantic-review-catches-content-errors-that-structural-validation.md) -- applies: Commonplace semantic review already names the content-level subroles this note wants to keep separate
- [Structured output is easier for humans to review](./structured-output-is-easier-for-humans-to-review.md) -- mechanism: separating evidence from reasoning makes review subroles independently checkable
- [Agentic Code Reasoning ingest](../sources/agentic-code-reasoning.ingest.md) -- evidence: semi-formal process templates improve execution-free verification by forcing premises, traces, and conclusions


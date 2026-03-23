=== SEMANTIC REVIEW: systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing.md ===

Claims identified: 12

1. [Intro] "the underlying operations are distinct" — controlled variation appears across multiple contexts but the operations differ.
2. [Intro] The note groups "two main uses of controlled prompt variation as analysis": verification and diagnosis.
3. [Intro] "Both vary what the model sees. Deutsch's explanatory-reach test does something different: it varies the explanation itself."
4. [Verification] Prompt variation is "a way to manufacture independent signal from a soft oracle." Success criterion is "less-correlated signal," not invariance.
5. [Verification] "Some verification methods, especially metamorphic checks, also use invariance as part of the signal" — invariance is secondary in verification, not absent.
6. [Diagnosis] Paraphrase/reordering tests ask "whether a component is stable under semantically equivalent surface changes." Success criterion is invariance.
7. [Diagnosis] "large output swings indicate the system is tracking surface cues instead of underlying structure."
8. [Reach] Deutsch's test is "a quality test for ideas, not for model behavior." Desired result is "structured sensitivity."
9. [Table] "The three operations separate cleanly" — enumerated with what-is-varied, what-is-held-fixed, what-counts-as-success.
10. [Ablation] Prompt ablation is "a fourth nearby use" closest to "optimization/search."
11. [Why it matters] Three specific misreadings that occur without the separation.
12. [Meta] "The object of variation determines the epistemic role."

---

WARN:
- [Completeness] The note claims to group "the two main uses of controlled prompt variation as analysis" (line 11), then identifies a fourth use (ablation) that is also controlled prompt variation — and also analytical in some sense (it learns which framing works). The framing "two main uses" followed by a third prompt-variation use and then Deutsch's non-prompt variation makes the claimed scope ambiguous. Is the scope "uses of prompt variation" (in which case there are at least three: verification, diagnosis, ablation) or "uses of controlled variation" (in which case reach testing is also included, making four)? The title suggests the note is about prompt variation specifically, but the body integrates Deutsch's reach test as a co-equal third operation in the summary table. The note's own table contradicts the "two main uses of prompt variation" framing by placing reach testing on the same footing.

- [Completeness] The boundary case of **prompt variation for diversity/ensemble generation at inference time** is not covered. Using multiple prompt variants to generate a diverse set of candidate outputs and then selecting the best one (e.g., best-of-N sampling with varied prompts) is a common practice that shares mechanics with verification (multiple prompts) but has a different goal (performance improvement, not verification). It could arguably be folded into verification or ablation, but neither fits cleanly — it is not decorrelating judges, not measuring brittleness, and not optimizing framing against a known target. This is an INFO-level gap because the note does not claim exhaustiveness, but the "two main uses" framing implies coverage of the primary uses.

- [Grounding — scope mismatch] The note attributes to the PromptSE ingest (line 26): "emotion and personality prompt variants preserve the task while changing expression style, so performance shifts are interpreted as prompt sensitivity, not as evidence from multiple judges." The PromptSE paper measures performance (Pass@1) and stability (AUC-E) as decoupled objectives. The note's characterization as purely diagnostic ("interpreted as prompt sensitivity") is accurate for the stability axis, but the paper also uses the same variation to measure confidence miscalibration (ECE analysis) and performance-stability decoupling — findings that go beyond diagnosis of brittleness. The note selectively reads PromptSE through the diagnosis lens, which is fair for this note's purpose but slightly narrows the source.

INFO:
- [Completeness] The note acknowledges that "some verification methods, especially metamorphic checks, also use invariance as part of the signal" (line 22), which complicates the clean separation between verification (success = decorrelation) and diagnosis (success = invariance). If a metamorphic check in a verification context interprets invariance violation as "likely error," the check is simultaneously using the diagnostic logic (stability under equivalent transformation) within the verification framework. The note flags this but does not resolve how to classify a single check that serves both functions. This is an honest acknowledgment rather than a flaw, but it slightly weakens the "separate cleanly" claim in the table.

- [Completeness] Adversarial prompt variation (red-teaming, jailbreaking) is a use of controlled prompt variation where the goal is finding failure modes — neither decorrelation, nor brittleness diagnosis, nor reach testing, nor framing optimization. It sits closest to diagnosis but the intent is different: diagnosis measures how much brittleness exists, while red-teaming searches for exploitable failure modes. The note does not claim exhaustive coverage, so this is not a gap in the argument, but it is worth noting that the "two main uses" framing excludes a prominent real-world use.

- [Grounding — inference step] The note claims (line 16) that Deutsch's test "varies the explanation itself — change a premise and ask whether the conclusion changes predictably. That tests whether an idea captures causal structure." Checking against the reach note (first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md), the source describes Deutsch's test as three questions: (1) Can you vary the explanation? (2) Does it reach new contexts? (3) Can it be criticized? The reviewed note focuses on question 1 and frames the whole test as "vary the explanation." This is a reasonable compression but elides the reach and criticizability components, which are co-equal in the source. The note's framing makes the distinction sharper (vary prompt vs. vary explanation) at the cost of compressing a three-part test into one part.

- [Internal consistency] The closing meta-pattern states "vary the prompt -> learn about model robustness or judge correlation" (line 60), collapsing verification and diagnosis into a single bullet under "vary the prompt." This is consistent with the note's thesis that both are prompt-variation operations, but the elision removes the distinction the entire note exists to make. A reader encountering only the closing summary might not see why verification and diagnosis need separating.

- [Grounding — prompt ablation] The note says prompt ablation "uses a hard target like verification" (line 48). Checking the ablation note: the ablation pattern uses a human-discovered finding as ground truth — a hard oracle. But verification as described in the error-correction note does not necessarily use a hard target; it uses above-chance oracles (TPR > FPR), which can be soft. The comparison "hard target like verification" slightly mischaracterizes the verification section's own grounding, which emphasizes soft oracles. The intended contrast is probably "has a known correct answer" vs. diagnosis which has no target, but the word "verification" in this sentence points back to the note's own verification section, which is about soft oracles.

PASS:
- [Grounding — verification section] The attribution to the error-correction note is accurate. That note does describe prompt variation as a decorrelation strategy for manufacturing independent signal from soft oracles (lines 53-55 of the source: "Vary the prompt — rephrase the question, change the framing, alter the instruction style"). The success criterion of "less-correlated signal" faithfully represents the source's emphasis on decorrelation as the binding constraint.

- [Grounding — diagnosis section] The attribution to the operational-signals note is accurate. That note does describe paraphrase brittleness as the first signal for detecting theory-encoding components, and does characterize stability under semantically equivalent changes as the success criterion (source line 13: "If the component breaks when inputs are rephrased, reordered, or padded with irrelevant content, it's relying on surface patterns").

- [Grounding — reach section] The attribution to the first-principles-reasoning note accurately represents Deutsch's distinction. The source does describe a test where you vary premises and predict downstream changes (source lines 29-30: "Can you vary the explanation? If you changed one premise, could you predict what changes in the conclusion?"). The note correctly identifies this as a test of ideas rather than model behavior.

- [Grounding — ablation section] The ablation note does describe a pattern of varying prompt framing against a known target to find which framing reliably elicits desired reasoning (source lines 11-12: "tests which prompt framings let agents reach a similar conclusion reliably"). The characterization as "optimization/search" is reasonable — the ablation note's own framing is "converts human insight into deployable agent framing," which is selection/optimization.

- [Internal consistency] The core three-way distinction (verification/diagnosis/reach) is internally consistent throughout the note. The table accurately reflects the prose in each section. The what-is-varied column (framing / surface form / premises) matches the section descriptions. The what-counts-as-success column (less-correlated signal / stable behavior / predictable downstream changes) matches the stated success criteria.

- [Internal consistency] The note's treatment of prompt ablation as "adjacent but distinct" is consistent — it is correctly positioned as a fourth operation that shares mechanics with the other three but differs in goal. The note does not try to force it into the three-way taxonomy.

Overall: 2 warnings, 4 info
===

=== SEMANTIC REVIEW: execution-indeterminism-is-a-property-of-the-sampling-process.md ===

Claims identified: 15

1. "Execution indeterminism is a property of the sampling process" / "a property of the execution engine" (title + opening paragraph)
2. Indeterminism is "conceptually simpler than underspecification" (opening paragraph)
3. Indeterminism is "theoretically eliminable via deterministic decoding (temperature=0)" (opening paragraph)
4. "True determinism is hard to guarantee (floating-point non-determinism, batching effects, infrastructure changes)" (second paragraph)
5. Temperature > 0 "helps explore reasoning paths, enables self-consistency techniques, and avoids degenerate repetitive outputs" — three benefits (second paragraph)
6. "All deployed systems exhibit indeterminism" (second paragraph)
7. Indeterminism is "engineering noise — variation in how a chosen interpretation is executed, not variation in which interpretation is chosen" (Why this matters section)
8. "At temperature=0, the LLM still picks one interpretation from the space the spec admits; you just get the same one every time" (Why this matters section)
9. "Lowering temperature alone doesn't solve the 'wrong interpretation' problem" (Why this matters section)
10. Indeterminism "obscures" the deeper issue of underspecification (Why this matters section)
11. People "attribute the variation to randomness" and "reach for familiar tools: temperature tuning, retries, sampling strategies" (Why this matters section)
12. "This framework avoids confronting the real difference from traditional programming: that the specification language doesn't have precise semantics" (Why this matters section)
13. "The remedy is sampling control: temperature adjustment, deterministic decoding, best-of-N selection" — three-item enumeration (closing paragraph)
14. Sampling control leaves "both underspecification and interpretation error untouched" (closing paragraph)
15. Ma et al. provides "cleanest empirical separation of indeterminism from underspecification: by varying prompt framing (emotion/personality) while holding task constant, they isolate the effect of interpretation choice from run-to-run sampling noise" (Sources section)

WARN:
- [Completeness — claim 7] The note defines indeterminism as "variation in how a chosen interpretation is executed, not variation in which interpretation is chosen." The parent note (agentic-systems-interpret-underspecified-instructions) explicitly acknowledges the two are not fully separable: "The two are not entirely orthogonal — indeterminism is the mechanism by which different interpretations get surfaced across runs." Temperature changes can shift which interpretation the model selects (the parent note: "Lowering temperature concentrates the sampling distribution — which can change *which interpretation* you see, not just how noisily you see it"). The reviewed note's clean separation of "how" vs. "which" overstates the boundary. At non-zero temperature, a single run's sampling path can cross interpretation boundaries — the variation is not purely within one interpretation but can surface different interpretations. The note's framing as pure "engineering noise" is a useful simplification but elides the coupling the parent note takes care to acknowledge.

- [Grounding — claim 15] The note claims Ma et al. provides "cleanest empirical separation of indeterminism from underspecification: by varying prompt framing (emotion/personality) while holding task constant, they isolate the effect of interpretation choice from run-to-run sampling noise." This is a scope mismatch. Ma et al. vary prompt *style* (emotional tone, personality), not task specification. What they isolate is the effect of surface framing variation on performance — which the paper itself frames as "prompt sensitivity" and "stability," not as an indeterminism-vs-underspecification separation. The paper's methodology (16 samples per prompt at temperature=0.2) does measure within-prompt sampling variation, but the paper's primary finding is about cross-variant performance differences, not about cleanly separating the two phenomena the KB taxonomy defines. The mapping from the paper's concepts to the KB's taxonomy is the ingest note's interpretation, not the paper's own framing. This is a reasonable inference but presented as attribution.

INFO:
- [Completeness — claim 5] The three benefits of temperature > 0 ("helps explore reasoning paths, enables self-consistency techniques, and avoids degenerate repetitive outputs") are reasonable but may be incomplete. A fourth benefit present in the literature is diversity for creative/generative tasks where multiple distinct outputs are desired (e.g., brainstorming, code suggestions in IDE completions). This is adjacent to "explore reasoning paths" but functionally distinct — exploring reasoning paths aims to find a better answer, while diversity aims to present multiple valid alternatives simultaneously.

- [Completeness — claim 13] The remedy enumeration ("temperature adjustment, deterministic decoding, best-of-N selection") omits some sampling-control techniques that are widely deployed: nucleus sampling (top-p), top-k sampling, and repetition penalties. These are arguably subsumed under "temperature adjustment" in a loose sense, but they are distinct mechanisms that control the sampling distribution differently. The note's enumeration could be read as exhaustive when it is illustrative.

- [Completeness — claim 4] The three sources of non-determinism even at temperature=0 ("floating-point non-determinism, batching effects, infrastructure changes") are real but the list omits one that is increasingly prominent in production: non-deterministic attention kernels (e.g., Flash Attention implementations that use non-deterministic reductions for performance). This is arguably covered by "infrastructure changes" but is a distinct mechanism that persists even with identical infrastructure across runs.

- [Internal consistency — claims 7 and 8] Claim 7 says indeterminism is "variation in how a chosen interpretation is executed" (implying the interpretation is fixed, only execution varies). Claim 8 says "at temperature=0, the LLM still picks one interpretation... you just get the same one every time" (implying at temperature > 0, you might get different interpretations). These two claims create a mild tension: if indeterminism can surface different interpretations (claim 8 implies this for temperature > 0), then it is not purely "variation in how a chosen interpretation is executed" (claim 7). The parent note handles this tension explicitly; this note compresses it away.

PASS:
- [Internal consistency — claims 3 and 4] The note correctly qualifies the theoretical eliminability of indeterminism (claim 3: "theoretically eliminable via deterministic decoding") with the practical difficulty (claim 4: "true determinism is hard to guarantee"). These form a coherent hedge rather than a contradiction.
- [Internal consistency — claims 9 and 14] The claim that "lowering temperature alone doesn't solve the 'wrong interpretation' problem" is consistent with the claim that sampling control "leaves both underspecification and interpretation error untouched." Both correctly identify the boundary of what sampling control can and cannot do.
- [Grounding — claim 10] The "obscures" argument (indeterminism hides underspecification by providing a familiar "it's stochastic" explanation) is faithfully represented from the parent note, which develops the same argument at greater length. The note does not overstate the parent's position.
- [Grounding — relationship semantics] The links to sibling notes (interpretation-errors, underspecification) and the parent index (llm-interpretation-errors-index) are accurate. The note correctly positions itself as one element of a three-phenomena taxonomy, and the relationship labels (sibling, parent area, elaborates) are appropriate.
- [Internal consistency — overall] The note's compressed structure (opening definition, "why this matters" section, remedy, links) is internally consistent. The summary accurately represents the body — no elided tensions beyond those noted above.

Overall: 2 warnings, 4 info
===

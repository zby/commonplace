<!-- REVIEW-METADATA
note-path: kb/notes/epiplexity-eli5.md
last-full-review-note-sha: 265052ccae24e9e23bf98c17eb73b41674bb3e41
last-full-review-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-full-review-at: 2026-03-23T09:32:55+01:00
last-accepted-note-sha: 265052ccae24e9e23bf98c17eb73b41674bb3e41
last-accepted-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-accepted-at: 2026-03-23T09:32:55+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->
=== SEMANTIC REVIEW: epiplexity-eli5.md ===

Claims identified: 15

1. [Title/Lede] "Entropy asks how surprising the symbols are. Complexity asks how short the best exact recipe is. Epiplexity asks how much structure *this observer* can actually extract with the tools and time they have."
2. [Four measures table] The four measures are information content, Shannon entropy, Kolmogorov complexity, and epiplexity — and the first three do not depend on a practical observer once formal setup is fixed.
3. [Four measures table] Epiplexity is calculated as "area under a bounded learner's loss curve above final loss."
4. [Four measures table] Epiplexity requires "a learner, its tools, and a compute budget."
5. [Warm-up] For `ABABABABABABABAB` under a naive i.i.d. model, I = 16 bits.
6. [Warm-up] Kolmogorov complexity of `ABABABABABABABAB` is ~30 bytes of code for a 16-byte string.
7. [Warm-up] Epiplexity of the AB sequence for a bounded learner is approximately 2.6 bits.
8. [Warm-up] For a truly random binary sequence, epiplexity is 0 because loss stays flat and area above final loss is zero.
9. [Example 1] AES-encrypted patterned message has low Kolmogorov complexity "if the plaintext and key have short descriptions."
10. [Example 1] "Neither entropy nor complexity can express 'Bob can read it but Eve cannot.' Epiplexity can."
11. [Example 2] Ordered and shuffled textbooks have "nearly identical" Kolmogorov complexity.
12. [Example 2] "This is why distillation creates value: rearranging and compressing knowledge can raise epiplexity for the target reader even while reducing token count."
13. [Example 3] CSPRNG output has "still near zero" epiplexity even with the seed, because "regenerating the bytes does not reveal hidden meaning."
14. [Example 4] Chess notation has four levels of epiplexity depending on observer (zero / low / moderate / high).
15. [The pattern] Epiplexity's "What it misses" column says "Nothing — observer-dependence is the point."

---

WARN:
- [Completeness] The "What it misses" column for epiplexity says "Nothing — observer-dependence is the point." This is a strong scope claim. However, epiplexity as defined by Finzi et al. measures learnable structure from sequential data via prequential coding — it captures pattern extraction but not fact-level observer-relativity. The parent note (information-value-is-observer-relative.md) explicitly flags this gap in its Open Questions: "Observer-relativity applies to both patterns (require computational depth to extract) and facts (require prior knowledge to interpret). Are these the same phenomenon or two phenomena that share a surface shape?" The same note's Relevant Notes section describes the paper as capturing "the pattern-extraction aspect" but not "fact-level observer-relativity." The ELI5 note's "misses nothing" claim is stronger than what the KB's own grounding note asserts. The chess example (Example 4) actually illustrates this tension: the non-chess-player's inability to extract meaning is a fact-level gap (not knowing what the symbols denote), not a pattern-extraction gap.

- [Grounding] The four-measures table says epiplexity requires "a learner, its tools, and a compute budget," but the note's own examples define the observer far more broadly — as including side information (encryption keys, decompressors, domain expertise) that go beyond computational budget. The Finzi et al. paper defines epiplexity in terms of a model class with bounded computation time. The note silently extends "bounded computation" to encompass possession of cryptographic keys (Example 1) and domain knowledge (Example 4). These are different kinds of observer-dependence: a key is not more compute, it is side information. The note's locked-box framing ("intelligence, side information, prior knowledge, keys, decompressors, domain expertise, and time") is more accurate than the table. A reader trusting the table's "compute budget" framing will be surprised when the examples invoke non-computational observer properties.

- [Grounding] The note says Kolmogorov complexity of the encrypted message "can still be low if the plaintext and key have short descriptions." Standard (unconditional) Kolmogorov complexity K(ciphertext) must include the key in the generating program. If the key is a 128-bit random string, K(ciphertext) is at least ~128 bits just for the key, which is not obviously "low" for a message whose plaintext is only 16 bytes (128 bits). The claim holds for K(ciphertext | key) (conditional complexity) or when both plaintext and key happen to have short descriptions (e.g., both are derived from short seeds). The note does not clarify which reading it intends. The pedagogical point survives — K does not capture who can read the message — but the intermediate claim about K being "low" is imprecise enough to mislead a technically careful reader.

INFO:
- [Grounding] The note says "Finzi et al. use CSPRNGs as the canonical example of zero-epiplexity data," which the ingest confirms. However, Example 3 adds a claim not in the source: that CSPRNG output has "still near zero" epiplexity even when the observer possesses the seed. The note's reasoning ("regenerating the bytes does not reveal hidden meaning") is plausible but elides a subtlety. An observer with the seed can predict every byte perfectly, so their loss curve would drop to zero immediately — the area above final loss would be near zero, but for a different reason than the seedless case (near-instant convergence to zero loss, rather than permanently flat high loss). Both yield near-zero epiplexity, but the mechanism differs from what the note implies.

- [Completeness] The chess notation example assigns "Zero" epiplexity to someone who does not know chess. In the prequential coding framework, even an observer ignorant of chess would see statistical regularities in the string (`1. e4 e5 2. Nf3 Nc6 ...`) — letter-digit patterns, restricted character set, positional structure. A bounded learner would extract some loss-curve improvement from surface-level regularities. The note's "zero" is colloquial (meaning no chess knowledge extracted), not literally zero in the formal sense. This is a pedagogical simplification that could confuse a reader who tries to reconcile it with the prequential definition.

- [Completeness] The warm-up computes epiplexity as a total (summed bits across all symbols) rather than a rate (bits per symbol). The note never clarifies which convention it uses. For qualitative comparisons (zero vs. nonzero across examples), this does not matter. But a careful reader would notice that a 16-symbol and a 10,000-symbol AB string would have very different total epiplexities under the note's formula despite having the same per-symbol learning structure. The note's examples work because they compare presence-vs-absence of learnability, but the ambiguity would bite anyone trying to compare magnitudes across sequences of different lengths.

- [Grounding] The distillation link claim ("This is why distillation creates value: rearranging and compressing knowledge can raise epiplexity for the target reader even while reducing token count") is consistent with the distillation note and the epiplexity ingest. However, the shuffled-textbook example that motivates this claim only demonstrates arrangement (reordering), while distillation also encompasses selection and compression. The example is a partial illustration, not a full grounding, of the distillation link.

PASS:
- [Internal consistency] The four measures are applied consistently across all four examples and the summary table. Each example holds three measures approximately constant while varying the observer or access conditions to show the fourth (epiplexity) changing. No contradictions between sections.
- [Internal consistency] The definition of epiplexity as "area under loss curve above final loss" is stated in the table, demonstrated in the warm-up calculation, and applied qualitatively in all subsequent examples. No definition drift.
- [Grounding] The central framing — entropy and complexity are observer-independent while epiplexity is observer-dependent — aligns with the Finzi et al. ingest, which describes the paper as separating information into "time-bounded entropy (irreducible randomness given computational constraints) and epiplexity (learnable structural patterns visible within those constraints)."
- [Grounding] The link to reverse-compression.md is sound. The note claims "expanding text without adding extractable structure" is a failure mode; the reverse-compression note defines exactly this.
- [Grounding] The link to context-efficiency.md is sound. The note claims "identical tokens can differ in usable structure depending on observer and arrangement." The context-efficiency note's volume-vs-complexity decomposition supports this.
- [Completeness] The warm-up section's four-measure walk-through for a single string is pedagogically complete — it covers each measure, shows model-dependence for information content and entropy, program-length for Kolmogorov complexity, and the loss-curve computation for epiplexity.

Overall: 3 warnings, 4 info
===

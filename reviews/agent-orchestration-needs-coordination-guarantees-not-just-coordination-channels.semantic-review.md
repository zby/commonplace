=== SEMANTIC REVIEW: agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md ===

Claims identified: 13

1. (Title/intro) Architectures should be discriminated by coordination guarantees, not just coordination channels.
2. (Intro) "Two systems can use the same channel and have very different reliability properties" — channel type is insufficient to predict reliability.
3. (Contamination section) Flat accumulated context without scoping/isolation produces contamination.
4. (Inconsistency section) Multi-agent memory without visibility/ownership/conflict-resolution rules produces inconsistency.
5. (Amplification section) Output aggregation without adjudication produces amplification.
6. (Design implication) "These are not four names for one bug" — four distinct failure modes, each requiring a different primitive.
7. (Table) Four-row enumeration: contamination, inconsistency, amplification, accountability vacuum — claimed as the set of failure modes from uncoordinated composition.
8. (Design implication) "The first three rows are failures over shared semantic substrates. The fourth is a governance failure."
9. (Accountability section) In delegation chains, intermediaries pass authority without retaining liability — the accountability vacuum.
10. (Accountability section) Liability firebreaks are the proposed remedy.
11. (Accountability section) Verification strength determines whether accountability stays local or must be refreshed from a human principal.
12. (Shared question) "These cases do not share one remedy, but they share one architectural question."
13. (Intro) The note scopes the space as: "what prevents one step from corrupting shared meaning, diverging from peers, amplifying a bad result, or diffusing responsibility downstream."

---

WARN:

- [Completeness] The four-row enumeration claims to cover uncoordinated composition failures, but **timing/ordering failures** are not clearly covered. Consider a race condition: two agents read the same state, compute independently valid updates, and write back — both writes succeed but the combined result is incoherent. This is not contamination (no scoping failure within a single context), not inconsistency as described (the note's inconsistency is about visibility rules and "when writes become visible," which is close but focuses on the multi-agent memory paradigm from Yu et al. rather than temporal ordering in any shared substrate), not amplification (no merging of outputs), and not accountability vacuum (no delegation chain). It sits between inconsistency and a missing "serializability" or "ordering" primitive. The note's inconsistency row could arguably absorb this, but the cited source (Yu et al.) frames inconsistency around memory coherence, not execution ordering. This is a boundary case that strains the "inconsistency" category.

- [Completeness] The enumeration does not clearly account for **cascading/compounding errors in sequential pipelines**. The note's four modes cover parallel composition (contamination in flat context, inconsistency across agents, amplification in merged outputs) and delegation chains (accountability vacuum). But a sequential pipeline where agent A's output becomes agent B's input and errors compound through the chain is a distinct failure pattern — not contamination (each agent has its own context), not inconsistency (no shared mutable state), not amplification (no merging), and not accountability vacuum (the chain may have clear ownership). The missing primitive would be something like "pipeline validation" or "stage-gate verification." This is related to the error amplification Kim et al. observe but is structurally different from the output-aggregation amplification the note describes.

- [Grounding] The note states that the Intelligent AI Delegation paper "calls this the accountability vacuum." Checking the ingest, the paper does discuss accountability diffusion in delegation chains and liability firebreaks, and the ingest confirms the concepts are present. However, the specific two-word phrase "accountability vacuum" does not appear in the ingest's summary or extractable value sections — the ingest uses "accountability vacuum" only in the recommended-next-action section, which is the KB's own synthesis, not the paper's vocabulary. The note may be attributing KB-coined vocabulary to the source. This is a potential vocabulary mismatch — the concept is genuinely present in the paper, but the label may be the note's own.

INFO:

- [Completeness] The simplest possible instance of "uncoordinated composition" is a two-step pipeline: one agent generates, another consumes. In the degenerate case where the second agent simply passes through the first agent's output unchanged, there is no composition failure at all. The note implicitly assumes composition involves meaningful transformation or merging. This assumption is reasonable but unstated — the framework does not distinguish "trivial composition" (pass-through) from "substantive composition" (transformation/merging/delegation), and trivially composed systems may not need coordination guarantees at all. This is an edge case, not a flaw.

- [Completeness] The note groups the first three failure modes as "failures over shared semantic substrates" but the substrates are quite heterogeneous: flat token context, multi-agent shared memory, and combined output artifacts. Whether these share enough structure to justify grouping as "shared semantic substrates" depends on how broadly one defines "substrate." The grouping is useful for exposition but could be challenged — one could argue that the output artifact in amplification is not a "substrate" in the same sense as a persistent shared memory, since it is produced once rather than continuously read/written.

- [Grounding] The note claims the amplification failure mode means "the system does not merely retain an error; it gives the error another path to survive by folding it into the merged result." The linked note synthesis-is-not-error-correction frames the problem differently: synthesis "propagates" errors and "folds" them into merged output. The coordination-guarantees note's framing as "gives the error another path to survive" adds an evolutionary/survival metaphor not present in the source note. The inference is reasonable — propagation does give errors a survival path — but the metaphor subtly shifts the emphasis from "errors are not filtered" to "errors are actively helped," which is slightly stronger than what the source supports.

- [Internal consistency] The intro lists four questions: "what prevents one step from corrupting shared meaning, diverging from peers, amplifying a bad result, or diffusing responsibility downstream." These map to contamination, inconsistency, amplification, and accountability vacuum respectively. The mapping is clean, but "corrupting shared meaning" is broader than "contamination within context" — corrupting shared meaning could also describe inconsistency (agents diverging corrupts their shared meaning). The intro's framing slightly overpromises compared to the table's narrower definitions.

- [Grounding] The note's connection to the-boundary-of-automation-is-the-boundary-of-verification states: "Where verification is strong, a node can plausibly accept downstream liability because it can audit what follows." The verification note itself focuses on automation boundaries and oracle construction, not on liability or accountability. The note is making a novel inference — connecting verification strength to liability pricing — that goes beyond what the verification note argues. The inference is plausible but is the note's own contribution, not something grounded in the cited source.

PASS:

- [Grounding] The contamination failure mode accurately reflects the linked note llm-context-is-composed-without-scoping. The source note explicitly discusses "spooky action at a distance, name collision, and inability to reason locally" as consequences of flat context without scoping — matching the coordination-guarantees note's characterization of contamination as "information that should have been frame-local remains live in the global substrate."

- [Grounding] The inconsistency failure mode accurately reflects the ingest of Yu et al. The ingest confirms the paper identifies memory consistency as the critical unsolved problem, discusses visibility rules and conflict resolution, and frames multi-agent memory as shared mutable state without coordination primitives — matching the note's characterization.

- [Grounding] The amplification failure mode accurately reflects the synthesis-is-not-error-correction note, which explicitly distinguishes synthesis (error propagation) from voting (error correction) and identifies the missing adjudication primitive.

- [Grounding] The accountability vacuum concept is genuinely present in the Intelligent AI Delegation ingest, which discusses responsibility diffusion in delegation chains and proposes liability firebreaks as a remedy. The concept attribution is accurate even if the specific label may be the KB's own (see WARN above).

- [Internal consistency] The note's two-part structure — three semantic failure modes plus one governance failure mode — is internally consistent. The note explicitly flags the fourth row as categorically different ("a governance failure, not a semantic one") rather than silently treating all four as equivalent. The design-implication table and the body text agree on this distinction.

- [Internal consistency] The unification claim in "The shared question" section is carefully scoped: "these cases do not share one remedy, but they share one architectural question." This avoids overclaiming — the note does not assert that one framework solves all four problems, only that one question ("what coordination guarantee matches this composition mode?") applies across all four. The body supports this: each row has a different missing primitive.

Overall: 3 warnings, 5 info
===

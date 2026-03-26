=== PROSE REVIEW v2: baseline.md ===

Checks applied: 8

WARN:
- [pseudo-formalism] The notation `K`, `select(K)`, and `P` fails the standalone readability test. Precision test: "storage in `K` is cheap" names a specific concept (the orchestration model's state store) — arguably more precise than plain prose. But standalone readability test: a reader who has not read the orchestration model note cannot parse "storage in `K` is cheap" or "letting `select(K)` choose." The notation serves as insider shorthand, not formal apparatus doing formal work.
  Recommendation: Replace notation with plain language. "The scheduler's state can store everything" instead of "storage in `K` is cheap."

- [redundant-restatement / bridge-paragraph-duplication] The paragraph at L18 ("The conflation arises one layer above the model itself. The orchestration model only requires bounded calls whose outputs are written into external symbolic state — it does not require chat history or a tool loop. But when higher-level interfaces package those bounded calls as chat sessions or framework-managed tool loops, session history becomes the path of least resistance for passing state forward.") previews exactly what the next section "Where the problem actually appears" then enumerates with its three bullets (chat sessions, framework-owned tool loops, continuing agent sessions). The bridge paragraph and the section cover the same ground.
  Recommendation: Delete the bridge paragraph and go straight from the opening to "Where the problem actually appears" (or merge into a single section).

- [confidence-miscalibration] The three trace types taxonomy (conversation transcripts, tool/action traces, reasoning traces) is presented as an established decomposition: "History conflates at least three trace types with different loading profiles." This is the note's own construction, not cited from a source. The ordering claim — "the argument against loading traces as next-context is sharpest for reasoning traces, strong for conversation transcripts, and most nuanced for tool traces" — is stated as fact rather than as a proposed framework.
  Recommendation: Flag as the note's own analysis: "We can distinguish at least three trace types..." or "A useful decomposition..."

INFO:
- [anthropomorphic-framing] "Interactive sessions want continuity and visibility. Orchestration wants selective loading." — attributes desires to abstractions. Not seriously misleading (common rhetorical shorthand), but "interactive sessions are optimized for continuity" would be more precise.

- [proportion-mismatch] The trace-types taxonomy section ("The right split: storage vs next-context loading") receives ~15 lines plus a substantial failure-handling subsection, while the central argument (why transcript inheritance is wrong) gets comparable space. The taxonomy may be overdeveloped relative to its load-bearing role in the argument.

CLEAN:
- [source-residue] The note's generality level (agent orchestration, LLM systems) is consistent throughout. No domain-specific residue from a narrower source.

- [orphan-references] No unsourced empirical claims, specific numbers, or named studies.

- [unbridged-cross-domain] Evidence stays within the LLM agent orchestration domain. Cross-references to Spacebot and Slate are within-domain.

Overall: 3 warnings, 2 info
===

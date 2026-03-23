=== PROSE REVIEW: storing-llm-outputs-is-constraining.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The core claim — that storing an LLM output is a constraining decision — is the title and the note's reason for existing. It is fully established in the opening two paragraphs (~180 words). The "Generator/verifier" section (~250 words) and "Verbatim risk" section (~170 words) together outweigh the core claim's development. Both sections are valuable but are largely self-contained arguments (generator/verifier as alternative to prompt constraining; verbatim repetition as a verification blind spot) that could each be their own notes. The note's center of gravity has drifted from "storing is constraining" to "strategies for managing variable generators," which is a different topic.
  Recommendation: Consider extracting the generator/verifier section and the verbatim-risk section into separate notes. The current note would then focus tightly on what storing does (resolves underspecification + freezes indeterminism), with links outward to the generator/verifier pattern and the verbatim-risk failure mode.

- [Confidence miscalibration] The note's frontmatter says `status: speculative`, but the core claim uses assertive language throughout: "you're doing two things at once," "The semantic commitment is the deeper operation," "storing an artifact is itself a constraining decision." These are stated as established facts, not proposed framings. The note is marked speculative at the metadata level but reads as confident in the prose. This is a mismatch in the other direction from typical miscalibration — the hedging is in the frontmatter, not the text.
  Recommendation: Either upgrade status to `current` if the core claim is now considered established within the KB's framework, or add hedging language to the prose ("we can read this as a constraining decision" rather than "storing an artifact is itself a constraining decision"). Pick one voice and be consistent across metadata and prose.

INFO:
- [Source residue] The phrase "The parent note already says" and "The parent note covers" appear in the opening section and in "Testing implications." The term "parent note" is a navigational/editorial term from the writing process — it tells the reader about the note's genealogy rather than its content. A reader encountering this note independently (e.g., via search) would not know which note is "the parent" without following context clues. The link to the parent note is present, but the framing assumes the reader arrived from it.
  Recommendation: Replace "The parent note" with the actual note's claim or a brief description, e.g., "The underspecification note already says..." or cite it by link text. This makes the note self-contained without losing the connection.

- [Redundant restatement] The second paragraph ("The parent note already says...") partially restates what the first paragraph established. The first paragraph introduces the two operations (resolving underspecification, freezing indeterminism) and identifies constraining as the deeper one. The second paragraph quotes the parent note to re-establish that regeneration is not a deterministic rebuild, then restates: "storing an artifact is itself a constraining decision. You're not just saving a file — you're committing to one interpretation..." This echoes the first paragraph's "When you choose to keep a specific output, you're doing two things at once." The second paragraph does add the "why that matters" framing, but it arrives via restatement.
  Recommendation: Trim the second paragraph to its unique contribution (the "why it matters" reframe) and cut the re-explanation of the two operations.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus. The note relies entirely on prose and examples. Clean.

- [Orphan references] The Koylanai data-loss example cites its source inline: "[Koylanai lost 3 months of engagement data](../sources/koylanai-personal-brain-os.ingest.md)." All other empirical or specific claims are either sourced (Evans' framing links to its ingest) or are the note's own framework. No orphan numbers or unsupported specifics.

- [Unbridged cross-domain evidence] The note stays within a single domain (LLM-based agentic systems). The Evans reference is explicitly framed as "a specific instance" of the constraint strategy, not cross-domain evidence. The Koylanai example is from the same domain (agent-operated knowledge bases). No unbridged transfers.

- [Anthropomorphic framing] The note uses "the agent produces," "the agent can add," and "an agent asked to extract" — all appropriate agency language for agentic systems. No attribution of mental states ("understands," "believes," "knows") to models. Clean.

Overall: 2 warnings, 2 info
===

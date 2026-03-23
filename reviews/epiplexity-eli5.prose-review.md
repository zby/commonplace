=== PROSE REVIEW: epiplexity-eli5.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The warm-up loss curve presents specific numerical loss values — "≈ 0.5 bits (hedging)," "≈ 0.1 bits" — and computes "≈ 2.6 bits" of epiplexity as though these are derivable from the setup, but they are fabricated illustrative numbers. A reader could mistake them for values that follow from the formalism. The note does use "≈" but does not flag these as chosen-for-illustration rather than calculated.
  Recommendation: Add a brief parenthetical or sentence making explicit that the loss values are illustrative guesses chosen to show the curve shape, not outputs of a specific learner. Something like: "The exact numbers depend on the learner; the shape is what matters."

- [Orphan references] "Finzi et al." appears three times in the body (lines 45, 123, and implicitly via "Finzi et al.'s measurement method") but is never cited inline with a title, year, or link. The source link exists only in the Relevant Notes footer. A reader encountering "Finzi et al. use CSPRNGs as the canonical example" in the middle of the note has no way to locate the paper without scrolling to the end.
  Recommendation: Add an inline link on first mention: "[Finzi et al.](../../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md)" or at minimum "(Finzi et al., YEAR)." This is especially important because epiplexity is not a widely known term — the reader needs to know where to go.

INFO:
- [Pseudo-formalism] The Kolmogorov complexity paragraph says "Something like `for i in range(8): print("AB")` — call it ~30 bytes of code for a 16-byte string." The ~30-byte estimate is a rough hand-wave for a Python snippet that would actually be shorter (~28 characters as written, but Kolmogorov complexity is defined over a fixed universal machine, not Python). The approximation is fine for ELI5 purposes, but conflating Python code length with Kolmogorov complexity could mislead a careful reader into thinking K is defined in terms of a specific language.
  Recommendation: Consider a brief qualifier like "measured by a fixed reference machine, not literally Python — but this gives the intuition."

- [Proportion mismatch] Example 1 (encrypted message) receives roughly 30 lines of development including a detailed loss-curve breakdown. Example 4 (chess notation) gets 8 lines with no loss-curve analysis. The chess example is arguably the most intuitive illustration of observer-dependence for a general audience, yet it is the thinnest. This is not severe — the note is structured to frontload the formal machinery and then accelerate — but the chess example could carry more weight for readers who are less comfortable with cryptographic framing.
  Recommendation: No change required if the intended audience is technical. If the note is meant to be a true ELI5 for mixed audiences, consider expanding the chess example with one concrete contrast (e.g., what the beginner sees vs. what the grandmaster extracts from the same move).

CLEAN:
- [Source residue] The note claims ELI5 generality and delivers it. All four examples (encryption, textbook, CSPRNG, chess) are explicitly framed as illustrative domains. The final paragraph connects to KB-specific concepts (distillation, context arrangement, reverse-compression) but frames them as applications, not as the note's scope. No domain-specific residue leaks through unframed.

- [Unbridged cross-domain evidence] The note does not cite empirical studies from one domain and apply them to another without bridging. The crypto and textbook examples are thought experiments, not empirical claims. The one empirical reference (Finzi et al. on CSPRNGs) is used within its own domain (formal information theory). The final paragraph's connection to KB design is framed as implication ("This is why..."), which is appropriate for a note that is itself within the KB methodology.

- [Redundant restatement] Each section advances the argument without re-explaining prior sections. The "Pattern" summary section at the end does restate the core contrast, but this is intentional synthesis, not redundant setup — it compresses the four examples into a comparison table and draws the concluding implication. No section opens by re-explaining what the previous section already established.

- [Anthropomorphic framing] The note discusses human observers (Bob, Eve, students, chess players) and abstract "bounded learners," not LLMs. No language attributes mental states to models. The word "observer" is defined explicitly in the second paragraph as "the full toolkit — intelligence, side information, prior knowledge, keys, decompressors, domain expertise, and time." This is precise and appropriate.

Overall: 2 warnings, 2 info
===

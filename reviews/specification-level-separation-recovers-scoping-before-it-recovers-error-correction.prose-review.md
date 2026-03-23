=== PROSE REVIEW: specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md ===

Checks applied: 8

WARN:
- [Source residue] The note claims to identify an intermediate regime applicable to specification-level separation in general, but the entire argument is built through a single concrete system — OpenProse — whose specific artifacts leak into the framing as structural elements rather than illustrative examples. References like "`.prose` files," "`prose compile`," "`prose.md`," "`compiler.md`," "`**...**` conditions," and "agent memory files" are OpenProse-specific implementation details presented as the substance of the argument rather than as one instance of a general pattern. The note does not frame these as "for instance, in OpenProse..." — it uses them as the primary evidence throughout. A reader unfamiliar with OpenProse gets a case study rather than the general intermediate-regime claim the title promises.
  Recommendation: Restructure so the general claim (specification-level separation recovers scoping before error correction) is argued in domain-neutral terms first, then use OpenProse as an illustrative example. Alternatively, retitle to make the OpenProse focus explicit ("OpenProse shows that specification-level separation recovers scoping before error correction").

- [Confidence miscalibration] The three-level regime (flat prompting / specification-level separation / architectural separation) is the note's own construction, but it is presented with assertive taxonomy framing: "This creates an intermediate regime:" followed by a definitional list. No hedging marks it as a proposed decomposition. Similarly, the claim "This ordering — scoping first, error correction second — is specific to specification-level approaches" asserts a general ordering rule derived from a single case.
  Recommendation: Flag the three-level regime as proposed ("One way to characterize the intermediate regime is...") or acknowledge it is derived from the OpenProse case and may not generalize. Hedge the ordering claim or cite additional evidence for it.

INFO:
- [Proportion mismatch] The core claim — that scoping benefits arrive before error-correction benefits — is stated but not extensively developed. The note spends roughly equal space on (a) describing what OpenProse does, (b) observing what it does not yet do, and (c) the three-level taxonomy. The mechanism explaining *why* scoping arrives first (naming structure within the LLM's own execution gives the model frame boundaries to work with, but doesn't give it a substrate that can enforce them) gets only a sentence or two. The penultimate paragraph about tool-use frameworks taking a different path is interesting but secondary to the title claim, and it receives comparable space to the core mechanism.
  Recommendation: Consider developing the "why scoping first" mechanism more explicitly — what is it about naming structure that recovers scoping, and what would it take for the same approach to recover error correction? The tool-use contrast paragraph could be shortened or split into its own note.

- [Anthropomorphic framing] "tries to make an LLM session behave like a symbolic executor" — "tries" attributes intentionality to a system/specification rather than to its designers. Minor, and arguably conventional usage.
  Recommendation: Could be rephrased to "is designed to make" or "aims to make" with a human subject implied, but this is low priority.

CLEAN:
- [Pseudo-formalism] No formal notation or mathematical apparatus is used. The argument is conducted entirely in prose. Clean.
- [Orphan references] No unsourced empirical claims, specific numbers, or named studies appear. All references are to other notes in the KB or to the OpenProse system itself. Clean.
- [Unbridged cross-domain evidence] The note stays within a single domain (LLM orchestration / agent architecture). No cross-domain transfer claims are made. Clean.
- [Redundant restatement] Each paragraph advances the argument without re-explaining what the previous paragraph established. The final paragraph ("The cost of staying in that middle ground...") could be read as partial restatement of the "what does not arrive yet" paragraph, but it adds the specific framing about where the asymmetry still applies, so it carries its own weight. Clean.

Overall: 2 warnings, 2 info
===

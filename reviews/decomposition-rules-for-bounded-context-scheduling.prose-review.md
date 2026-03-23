=== PROSE REVIEW: decomposition-rules-for-bounded-context-scheduling.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The rules are presented as imperative directives ("Separate selection from joint reasoning," "Use symbolic operations wherever exactness is available," etc.) — the same register used for established engineering principles. Yet the note's own opening paragraph says "They are preliminary — we expect to discover more as the model develops," and the frontmatter marks the note as `status: seedling`. The imperative framing conflicts with the self-declared epistemic status. A reader who skips the opening sentence and reads only the Rules section will take these as settled design principles rather than proposed heuristics from a developing model.
  Recommendation: Either reframe the rules section header and lead-in to mark these as proposed heuristics (e.g., "Proposed rules" or "Working heuristics"), or soften the individual rule statements to match the seedling status (e.g., "Prefer separating selection from joint reasoning" instead of the bare imperative). The two empirically grounded rules could keep stronger language; the ungrounded ones should be hedged.

- [Proportion mismatch] The core claim lives in the eight rules (Rules section), which occupy roughly 12 lines of terse imperatives with one-sentence rationales. The Empirical grounding section is nearly as long (~10 lines) but covers only two of the eight rules. The "What is being optimised" section (~16 lines) is the longest section and serves as preamble rather than carrying the title's claim. The result: the rules themselves — the load-bearing content — get the thinnest development. Several rules (e.g., "Commit low-degree-of-freedom choices first," "Do not compress away needed interfaces") would benefit from a concrete example or a sentence explaining when the rule bites and when it doesn't.
  Recommendation: Develop the rules that lack empirical grounding with at least one illustrative scenario or failure mode each. Consider whether the "What is being optimised" framing section could be trimmed — it establishes context already handled by the linked parent note.

INFO:
- [Source residue] The note's claimed generality level is "bounded-context scheduling" — a domain-neutral framing within the symbolic scheduling model. The vocabulary stays within that frame: "scheduler state," "bounded call," "prompt assembly," "token traffic." The term "notes" appears once in the Rules section ("not which notes to load") — this is a KB-specific artifact rather than a general scheduling term, but it reads as a lightweight example rather than a domain leak. Worth a glance on revision but not a real problem.

- [Pseudo-formalism] The notation is light: `M` for the per-call bound, `m=1`, `O(s ln s)`, `F1=1.0`, `F1≈0.2`. These all appear in the Empirical grounding section and carry specific quantitative meaning from the cited sources. The "What is being optimised" section uses prose bullet points rather than formal apparatus. No decorative formalism detected. However, the phrase "optimisation problem" in the opening of that section frames the problem as if a formal objective exists, then immediately concedes "even before underspecified semantics enter" — the note gestures at a formal problem without stating one. This is a minor framing tension, not a pseudo-formalism finding per se.

CLEAN:
- [Orphan references] All specific empirical claims carry citations. The F1 scores (1.0 and 0.2), the depth-100 result, the 5,331-token figure, the O(s ln s) scaling, and the 1,048,575-step task are all attributed to named sources (Liu et al. 2026 and Meyerson et al. 2025) with links to ingest files. No unsupported numbers or unnamed studies.

- [Unbridged cross-domain evidence] Both cited sources are computational/LLM studies applied to a note about LLM scheduling — the domains match. ConvexBench is about LLM performance on compositional tasks; MAKER is about LLM multi-step task execution. No cross-domain transfer requiring a bridge sentence.

- [Redundant restatement] Each section opens with new material. The Rules section does not re-explain the optimisation framing. The Empirical grounding section does not re-state the rules before citing evidence for them — it names each rule inline and immediately provides the grounding. No restatement detected.

- [Anthropomorphic framing] The note consistently uses mechanistic language: "scheduler," "bounded call," "symbolic operations," "LLM window," "prompt assembly." No verbs implying agency or mental states are attributed to models. Clean.

Overall: 2 warnings, 2 info
===

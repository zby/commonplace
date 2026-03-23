=== PROSE REVIEW: semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note presents its decomposition pattern as the only viable response: "The canonical response is a runtime component that can spawn another tool loop — a sub-agent — for the decomposed sub-goal." The word "canonical" asserts established consensus, but this is the note's own proposed architecture. No source is cited for this being the canonical approach. The rest of the note correctly uses descriptive/analytical framing ("typically arise," "becomes awkward"), but this final paragraph shifts into assertive mode without grounding.
  Recommendation: Replace "The canonical response is" with hedged framing such as "A natural response is" or "One clean solution is" — or cite a source that establishes this as the standard approach.

- [Proportion mismatch] The core claim is in the title: sub-goals that overflow a context window become scheduling problems. The first paragraph states this clearly, but the note then spends roughly equal space on three topics — collection work (paragraph 2), generative search (paragraph 3), and framework tension (paragraph 4) — before the resolution (paragraph 5) gets a single short paragraph. The framework-tension paragraph (paragraph 4) is the longest and most developed, yet it is a consequence/implication rather than the core claim. The resolution paragraph, which introduces the recursive sub-agent pattern that the note builds toward, is the thinnest section.
  Recommendation: Develop the resolution paragraph — explain what "spawn another tool loop" means concretely (what state crosses the boundary, how results return). Consider whether the framework-tension discussion (paragraph 4) belongs in this note or is better handled by the already-linked notes on hidden schedulers and tool-loop exposure.

INFO:
- [Source residue] The note uses "files, candidates, examples" and "note pairs" as concrete illustrations. "Note pairs" (paragraph 3: "the list of candidate note pairs may not fit in one prompt") is specific to knowledge-base operations. This is minor — the note's tags include `context-engineering` and the corpus-contradiction example is framed as a "suppose" scenario — but a reader outside the KB domain might find "note pairs" unexplained.

CLEAN:
- [Pseudo-formalism] No formal notation or mathematical apparatus appears. The note argues entirely in prose and keeps its abstractions verbal. Clean.
- [Orphan references] No specific figures, data points, named studies, or empirical claims appear without attribution. The note is a conceptual analysis that does not rely on external evidence. Clean.
- [Unbridged cross-domain evidence] The note does not cite evidence from a different domain and apply it without bridging. All reasoning stays within the agent-systems domain. Clean.
- [Redundant restatement] Each paragraph advances the argument: definition (paragraph 1), standard case (paragraph 2), generative variant (paragraph 3), framework consequence (paragraph 4), resolution (paragraph 5). No paragraph reopens ground already covered. Clean.
- [Anthropomorphic framing] The note uses "the agent decides," "the agent is already in its tool loop," and "discovers the set is too large." In this KB's vocabulary, "agent" refers to a software system with a tool loop, and "decides"/"discovers" describe observable control-flow events (tool calls, branching). These are standard usage in the codebase, not unintended mental-state attributions. Clean.

Overall: 2 warnings, 1 info
===

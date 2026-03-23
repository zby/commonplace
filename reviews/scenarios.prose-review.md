=== PROSE REVIEW: scenarios.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note presents its two-scenario taxonomy ("Upstream change analysis" and "Proposing our own changes") as if it exhaustively covers what the knowledge system is used for. The opening line asks "What do we actually use the knowledge system for?" and the implicit answer is: these two things. But there is no hedge indicating these are the primary or initial scenarios rather than a complete enumeration. If more scenarios exist (e.g., onboarding, audit, knowledge maintenance), the framing overstates coverage.
  Recommendation: Add a brief qualifier — e.g., "Two scenarios dominate current usage" or "The main scenarios so far" — to signal this is a working inventory, not a closed list.

- [Proportion mismatch] The first scenario ("Upstream change analysis") gets substantially more development than the second ("Proposing our own changes"). The upstream section includes a detailed breakdown of what step 4 requires (scan code, read notes, find prior decisions) and poses a concrete evaluation question. The "Proposing our own changes" section ends with a single sentence summarizing the knowledge system's role ("what have we already decided, what constraints exist, what prior art is relevant") without the same depth. Given that the note frames both scenarios as equally important use cases, the second one is underdeveloped relative to the first.
  Recommendation: Either develop the second scenario to comparable depth (what does "building the case" concretely require from the KB?) or note explicitly that the second scenario is structurally similar and refer back to the first, so the asymmetry is intentional rather than accidental.

INFO:
- [Source residue] The examples in parentheses — "e.g. traits API, deferred tool results handler" — are specific to the Claude Code / agent-SDK domain. The note's title and description ("Concrete use cases for the knowledge system") are domain-neutral, but these examples assume familiarity with a particular codebase. This is borderline: the note lives in a project-specific KB, so these references are arguably in-scope. But a reader navigating from the generic title may find them unexplained.
  Recommendation: No action required if the KB audience is assumed to know these terms. If the note is meant to be methodology-level (which the description's generality suggests), consider either generalizing the examples or adding a brief gloss.

CLEAN:
- [Pseudo-formalism] No formal notation, variables, or equations present. The numbered lists are organizational, not pseudo-formal. Clean.

- [Orphan references] No specific figures, data points, percentages, or named studies appear. The one empirical-adjacent claim ("we don't yet have enough logged usage") is self-referential and appropriately hedged. Clean.

- [Unbridged cross-domain evidence] No cross-domain evidence is cited. Both scenarios stay within the knowledge-system domain. Clean.

- [Redundant restatement] The second scenario's closing paragraph ("Same documentation need as upstream analysis, but the direction is reversed") explicitly bridges to the first scenario without restating it. This is a transition, not redundancy. Clean.

- [Anthropomorphic framing] No language attributing human mental states to models. The note discusses human workflows, not model behavior. Clean.

Overall: 2 warnings, 1 info
===

=== PROSE REVIEW: why-directories-despite-their-costs.md ===

Checks applied: 8

WARN:
- [Source residue] The note references `claw-design/` as a directory throughout — in the "Operational costs" section ("Skills hardcode directory lists — `/connect` searches across three hardcoded directories (`notes/`, `claw-design/`, `sources/`)") and in the "Types and directories are orthogonal" section ("A `structured-claim` works identically whether it lives in `notes/`, `notes/related-systems/`, or `claw-design/`") and in the agent routing cost item ("The `notes/` vs `claw-design/` heuristic is already non-trivial"). However, `claw-design/` no longer exists as a directory in the KB, and `CLAUDE.md` does not mention it. These references are residue from an earlier state of the project. A reader encountering this note today would be confused by examples that cite a directory they cannot find.
  Recommendation: Replace `claw-design/` references with directories that currently exist (e.g., `instructions/`, `sources/`, `tasks/`), or explicitly note that `claw-design/` was a former directory used as an illustration.

- [Confidence miscalibration] The "Operational costs" section presents a specific numbered list (7 items) of registration costs with concrete details ("Currently 11 entries" for qmd-collections.yml, "`/connect` searches across three hardcoded directories"). These are stated as current facts, but several are stale: the `claw-design/` directory no longer exists, and the skill behavior described may have changed since writing. Presenting point-in-time implementation details as current facts without dating them creates false confidence in their accuracy.
  Recommendation: Either verify and update the concrete details, or frame them as "at time of writing" snapshots that illustrate the pattern rather than document the current state. The argument (each directory imposes registration tax) is sound and doesn't depend on the specific numbers being current.

INFO:
- [Proportion mismatch] The core claim is in the title: directories are worth their costs. The "What directories give us" section (the positive case) gets roughly 150 words across three brief points. The "Operational costs" section gets roughly 250 words with a detailed 7-item enumeration. The cost side is more developed than the benefit side. This isn't necessarily wrong — the note's rhetorical stance is "despite their costs," so the costs need thorough treatment — but the benefit arguments ("Scale without tooling," "Local conventions," "Different metabolic rates") are each only one or two sentences. The "metabolic rates" point in particular introduces an interesting concept that gets thin treatment.
  Recommendation: Consider whether "Different metabolic rates" deserves a bit more development — it is the most original of the three benefits and currently gets the least elaboration.

CLEAN:
- [Pseudo-formalism] No formal notation or mathematical apparatus is used. The note makes its arguments in plain prose throughout.

- [Orphan references] No unsourced specific numbers, percentages, or empirical claims appear. The numbers used ("30 files," "300," "200-file," "~6 top-level directories," "Currently 11 entries") are either illustrative round numbers or verifiable by inspecting the repo.

- [Unbridged cross-domain evidence] The note stays within its domain (knowledge base architecture and file system organization) throughout. No cross-domain evidence transfer occurs.

- [Redundant restatement] Each section opens with its own contribution. The "Current stance" section briefly references the registration tax but uses it as a launch point for the mitigation discussion rather than restating the costs section.

- [Anthropomorphic framing] No language attributes human-like cognitive properties to models or systems. The note discusses system design, not model behavior.

Overall: 2 warnings, 1 info
===

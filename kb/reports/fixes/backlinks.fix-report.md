## Fix Report: backlinks

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | prose/orphan-references | verify-and-ground | Fixed filename typo and grounded "40+" with verified count (48 notes via grep) | fixed |
| 2 | prose/orphan-references | verify-and-ground | Replaced "~16%" with verified 30/224 (13%) with date stamp | fixed |
| 3 | semantic/completeness-boundary-cases | boundary-case-acknowledged | Rewrote orphan-detection entry to distinguish threshold and purpose from hub identification | fixed |
| 4 | semantic/grounding-alignment | hedge-strength-mismatch | Changed linking-theory relationship from "foundation" to "extends" and acknowledged extrapolation | fixed |

### Warning-to-fix mapping

- **#1 (orphan-references):** "referenced by 40+ files — No source or method given. If this came from a grep at writing time, it may no longer be accurate." Verification found the filename was also wrong (`the` → `is-the`); corrected and grounded with actual count.
- **#2 (orphan-references):** "~16% of notes still lack even outbound Relevant Notes sections — No source or method." Verified via grep: 30 of 224 notes lack a `Relevant Notes:` section (13%). Stamped with date since the number will drift.
- **#3 (completeness-boundary-cases):** "the sentence equates hub identification and orphan detection by their data substrate while the actual distinction is threshold and purpose."
- **#4 (grounding-alignment):** "linking-theory.md doesn't address inbound links or backlink visibility. The connection is the backlinks note's own extrapolation, not a claim grounded in the cited source."

### Deferred items
- (none)

### New patterns
- **verify-and-ground** (#1, #2): A specific number or statistic is used without sourcing. Rather than softening to approximate language, verify the claim against the repo and replace with the grounded figure plus method or date. Produces stronger prose than hedging and catches stale data (as in #1, where the filename was also wrong).

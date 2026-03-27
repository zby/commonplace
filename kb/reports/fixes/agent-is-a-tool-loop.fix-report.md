## Fix Report: agent-is-a-tool-loop

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | structural/bullet-capitalization | new-pattern: bullet-initial-cap | Capitalized first word of each Relevant Notes link text: `tool` → `Tool`, `bounded-context` → `Bounded-context`, `subtasks` → `Subtasks` | fixed |

### Warning-to-fix mapping

- **#1 (structural/bullet-capitalization):** "All three Relevant Notes bullets begin with lowercase link text that reads as prose, not identifiers." Recommendation was to capitalize the first word of each link text.

### Deferred items
- (none)

### New patterns
- **bullet-initial-cap:** Link text at the start of a bullet list item begins with a lowercase word that reads as a prose fragment, not a code identifier or slug. Fix: capitalize the first letter of the link text to match sentence-fragment capitalization conventions.

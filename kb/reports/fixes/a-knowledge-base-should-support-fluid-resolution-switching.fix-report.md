## Fix Report: a-knowledge-base-should-support-fluid-resolution-switching

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Connection inflation | deflate-body-covered-links | Removed 5 inflated footer entries whose relationships are already articulated with inline links in the body; kept 1 entry that adds a new framing | fixed |

### Warning-to-fix mapping

- **#1 (Connection inflation):** "5 of 6 entries are inflated. The footer largely duplicates the body's argument structure. Consider trimming footer entries to only those that add navigational value beyond what the body provides (entry 3 is the model)."

### Deferred items
- (none)

### New patterns
- **deflate-body-covered-links**: When the body already inline-links to a note and fully articulates the relationship, the footer entry for that same note is pure duplication. Fix: remove the inflated footer entries, keeping only those that add a connection or framing absent from the body. The body's inline links preserve all navigational value.

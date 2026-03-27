---
gate_id: prose/redundant-restatement
name: Redundant restatement
lens: prose
watches: [body]
staleness: changed
---

## Failure mode

A paragraph re-explains what a nearby section already establishes, either by restating the previous section's conclusion or by previewing what the next section will enumerate.

## Test

Check every section boundary for both patterns. Report all instances found, not just the first.

1. **Section-opening restatement.** Read the first paragraph of each section. If it can be deleted and the section still works from the second paragraph onward, it is restating rather than advancing.
2. **Bridge-paragraph duplication.** Check the last paragraph before each section heading. Does it preview what the next section then enumerates? If the preview and the section's own content cover the same ground, the preview is redundant.

A one-sentence transition is fine. A full paragraph that duplicates adjacent content is not.

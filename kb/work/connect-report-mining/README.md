# Mining recent connect reports + kb/log.md

## Goal

`cp-skill-connect` reports accumulate `Synthesis Opportunities`, `Maintenance Observations`, `Flags`, `Off-authorisation Candidates`, and `Rejected Candidates` sections that are rarely read back across reports. `kb/log.md` already captures some cross-artifact patterns (ABSTRACTION/SYNTHESIS/DUPLICATION/CONTRADICTION/FIX) by hand. This workshop mines the 45 connect reports dated within the last two weeks of 2026-07-18 (`kb/reports/connect/**/*.connect.md`, `mtime -14`) together with the current `kb/log.md`, looking for recurring patterns across reports that no single connect run would surface on its own: repeated synthesis candidates, systemic collection/authorization gaps, recurring rejected-candidate themes, and anything that reads as a missing `kb/log.md` entry.

## What closes it

Every candidate pattern found is triaged to one of: appended to `kb/log.md` as a new entry, promoted directly to a note/ADR/proposal if it's already clear enough, or explicitly discarded as noise. The batch raw-findings files are scratch — safe to delete once their content is merged or discarded. The workshop closes when the merged pattern list has been triaged and the scratch files are gone.

## Evaluation boundary

Scope is exactly the connect reports captured by `find kb/reports/connect -type f -mtime -14 -name "*.md"` as of 2026-07-18 (45 files) plus the current `kb/log.md`. This workshop does not re-run `cp-skill-connect` on anything, and does not resolve the individual design/theory questions a pattern surfaces — those become their own note or workshop if they earn it. This pass is preliminary: a first read for recurring shape, not a final verdict on any candidate.

## Bookkeeping

- `batch-N-raw-findings.md` — scratch, one per subagent batch, safe to regenerate from the source connect reports at any time.
- `preliminary-analysis.md` — the actual deliverable: merged/deduped patterns with a triage recommendation each.

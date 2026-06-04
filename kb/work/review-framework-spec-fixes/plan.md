# Plan: reconcile the write/read-side spec change with its consumers
Fixes for the five findings from reviewing the uncommitted `agent-memory-system-review.md` / `.schema.yaml` change against its decision log (`review-framework-design.md` D3/D4), the parser, the schema, and the 190 existing reviews. Comment inline; I'll act on your marks.
## The gap in one line
The spec was edited to its decided end-state (write side / read side, no read-back "timing"), but its **consumers were not moved with it**: the parser still has the timing axis, the schema description string still names the old section, and D3 claims work that isn't done. The spec is ahead of the code.
## Findings → fixes
### Fix 1 — Remove the read-back timing axis from the parser (Finding 1, the real defect)
D3 says the `rb_pre_action`/`rb_post_action` columns "are removed" — they are not. The spec now forbids authoring the token, so the axis is dead. Remove it.

`src/commonplace/lib/systems_matrix.py`:

- delete the `"Read-back timing"` entry from `ONEHOT_AXES` (lines ~55–56)
  
- drop `"Read-back timing"` from `PUSH_AXES` (line ~70)
  
- drop `*ONEHOT_AXES["Read-back timing"]` from `COLUMNS` (line ~91)
  

`test/commonplace/lib/test_systems_matrix.py`:

- remove the `rb_pre_action`/`rb_post_action` assertions
  

`test/commonplace/lib/fixtures/zikkaron_review.md`:

- strip the `**Read-back timing:**` token so the fixture matches the new spec
  

Then rebuild and confirm the two columns disappear:

- `python3 scripts/build_systems_matrix.py` (or the documented command)
  
- `pytest test/commonplace/lib/test_systems_matrix.py`
  
- verify `kb/agent-memory-systems/systems.csv` header no longer has `rb_pre_action` / `rb_post_action`
  

**Decision point:** removing the axis is the decided end-state and makes D3 true. The alternative is to _defer_ — keep the parser as-is and reword D3's consequence to "pending" (matching D4). I recommend removing now; it's bounded and the columns are already meaningless under the new spec.
### Fix 2 — Update the schema's stale heading description (Finding 2)
`agent-memory-system-review.schema.yaml`, `headings.description` still reads "## Trace-derived learning placement and ## Read-back placement are optional…". Reword to name `## Write-side placement` (with `### Trace-derived learning` as its sub-section) and `## Read-back placement`. Description-only, not enforced, but it's drift inside the edited file.
### Fix 3 — Tighten the Operations wording in the spec (Finding 4)
In `## Write-side placement`, the Operations bullet says "Note for each whether it is manual or automatic," but the `**Curation operations:**` token rule is automatic-only. Reword so curation operations are the _automatic_ ones and manual maintenance is recorded as agency only — removing the invitation to tag manual ops that the token then discards.
### Fix 4 — Make D3 accurate (depends on Fix 1)
If Fix 1 lands, D3's "are removed" becomes true — no edit needed beyond a last-checked bump if desired. If we defer Fix 1 instead, change D3's consequence to "pending" so the decision log stops claiming finished work.
## Out of scope here (tracked, not blocking)
- **84 active reviews still carry** `**Read-back timing:**` **tokens** and ~190 carry the old `## Trace-derived learning placement` heading. After Fix 1 the tokens are inert prose and the schema relaxation keeps the headings valid. Stripping the dead tokens and renaming headings is **retrofit work** — fold it into the existing `comparative-review-data-refresh` / `agent-memory-matrix-retrofit` passes, not this one. `kb/work/agent-memory-matrix-retrofit/runbook.md` also references timing and should be updated in that pass.
  
- **Wiring** `**Write agency:**` **/** `**Curation operations:**` **into the parser as one-hot columns (Finding 3 / D4).** Authored-in-prose now, extract-later — same precedent as read-back signal. New axes + columns + retrofit; a separate unit.
  
## Suggested commit shape
1. **Commit A — spec + schema** (the currently-uncommitted change plus Fixes 2 & 3): the spec and its own schema move together. Self-consistent on its own.
  
2. **Commit B — parser + tests + fixture + rebuilt CSV** (Fix 1): the consumer catches up; D3 becomes accurate.
  

Splitting keeps the prose contract and the code contract reviewable separately. They can also go as one commit if you prefer a single atomic "spec end-state" landing.
## Verification checklist
- [ ] 
  
  `pytest test/commonplace/lib/test_systems_matrix.py` green
  
- [ ] 
  
  `pytest` full suite green
  
- [ ] 
  
  `systems.csv` rebuilds with no `rb_*_action` columns and otherwise no diff
  
- [ ] 
  
  `commonplace-validate` clean on a `trace-derived` review and a `push-activation` review (schema relaxation still admits old headings)
  
- [ ] 
  
  no remaining `Read-back timing` reference in `src/` or `test/`
  
## Open questions for you
- Fix 1 now (remove axis) or defer (reword D3 to pending)?
  
- One atomic commit or the A/B split above?
  
- Do the 84-review token cleanup here as a mechanical sweep, or leave it entirely to the data-refresh pass?

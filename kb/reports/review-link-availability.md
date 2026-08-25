# Review-link available-cost baseline

Measured 2026-08-25 against committed corpus snapshot
`ebf33f25870ecf37a1cfbac3cbfbe1f992d19306`.

## Population and method

The population is the 337 top-level, frontmatter-bearing artifacts under the
review system's `kb/notes/` and `kb/reference/` scan roots: 311 notes and 26
reference artifacts. Every artifact had at least one resolved local Markdown
link.

For each artifact, the measurement retained every resolved link occurrence,
resolved it to a repository-relative path, recorded the target's whole-file byte
size, and summed each distinct path once. Missing direct targets and absent
snapshots required by link text were reported but excluded from the resolved
counts and byte totals. Percentiles below use nearest ranks across the 337
artifacts.

| Available cost | p50 | p75 | p90 | p95 | max |
| --- | ---: | ---: | ---: | ---: | ---: |
| Resolved link occurrences | 10 | 17 | 23 | 27 | 56 |
| Distinct artifacts | 7 | 11 | 16 | 19 | 35 |
| Whole-file bytes | 67,009 | 104,431 | 148,267 | 171,295 | 355,344 |

Repeated targets occurred in 258 of 337 artifacts (76.6%). Forty-six artifacts
had more than five resolved link occurrences but at most five distinct targets.
The committed snapshot also had 19 unavailable target occurrences across seven
notes; all were reported rather than treated as sizing errors.

The largest available cost was 355,344 bytes over 35 distinct artifacts and 56
link occurrences in `kb/notes/designing-agent-memory-systems.md`.

## Interpretation limit

This is offered cost, not consumed cost. It shows the distribution a review
budget would have to cover and confirms that occurrence count commonly
overstates artifact count. It does not show what reviewers opened, why they
stopped, or whether switching cost or byte volume better predicts a stopping
point. Therefore it cannot identify the α/β ratio in
`attention ≈ α · artifacts + β · bytes`. That requires the separately deferred
actual-opens measurement and its reviewer behavior change.

Whole-file sizing also retains the accepted V1 mispricing: it overprices an
ingest's Quotes route and prices a `(snapshot required)` link by the resolved
ingest rather than by the derived snapshot.

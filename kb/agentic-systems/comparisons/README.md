# Memory comparisons from the main analysis

The matrix builder, table renderer and analyzer enumerate current accepted sets
under `kb/agentic-system-analyses/retained/<system-slug>/` through the same
library function as the site. The accepted overview supplies the entry point,
boundary and synthesis. The manifest, `ARTIFACT.yaml`, pins every member.
Readers validate membership and take the comparison profile from `memory-profile.md`.
They reject duplicate sources and directory names that disagree with sources.
Old `agentic-systems/reports/` and the new `retained-archive/` do not participate
in current validation or comparison. No local run state, source checkout,
legacy review or prior CSV is required. The
[memory profile contract](../../agentic-system-analyses/types/agent-memory-profile.md#memory-comparison-fields)
defines the scoped fields and per-value evidence assessments.

Run from the repository root:

```bash
uv run python scripts/build_systems_matrix.py
uv run python scripts/render_systems_table.py
uv run python scripts/analyze_matrix.py
```

The first two commands write `memory-systems.csv` and `memory-systems-table.md`
in this directory. All three read the retained sets directly; the renderer and
analyzer do not depend on the CSV being present. Repeat `--review <current-overview-path>`
to select a bounded population. Otherwise every current accepted analysis is
selected, and missing or invalid evidence blocks the operation. Select only one
review per source identity; repeat runs do not count as distinct systems.
Builder and renderer accept `--output <path>` for an isolated trial.

Each CSV row records the source, run, boundary, tier, compared scope, and the
hashes of the review and the manifest (`artifact_sha256`). Axis values are JSON arrays with
separate coverage assessment, JSON per-value evidence maps, and
canonical-record columns. Each evidence entry retains its basis, supporting
records and rationale. The members carry the source evidence.
The table separates code-grounded and doc-grounded sets and links the accepted overview. Statistics count code-grounded wired, observed,
or causally supported values, including supported positives under partial
coverage; the remainder is not inferred absent. Weaker bases and coverage
assessments are reported separately. Entropy and redundancy require known
coverage and strong evidence for every member, treating the complete set as one
category. Evidenced absences remain a separate category. Denominators describe this selected population only.

Existing reviews without a retained set and normalized comparison fields
need regeneration through the main analysis before inclusion. Do not
patch generated findings, reuse an old CSV value, or infer absence from an
omission. Use an explicit review list to compare only regenerated inputs.
The old matrix and table under `kb/agent-memory-systems/` remain historical
snapshots; these commands no longer rebuild them. Public landscape synthesis uses the same inputs through
`synthesize-agent-memory-landscape`. It records the commit whose tree holds
the selected reviews, retained sets, contracts and reader code instead of
preparing a separate bundle; an analysis publishes only with its method
committed and the worktree clean outside the publication outputs, so that
commit identifies the method and inputs.
Quantitative claims retain their population, evidence filters, and exclusions;
qualitative claims require reading and citing the retained members.

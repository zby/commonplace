# Memory comparisons from the main analysis

The matrix builder, table renderer and analyzer enumerate current accepted sets
under `kb/agentic-system-analyses/retained/<system-slug>/` through the same
library function as the site. The code-written overview supplies the entry
point, identity, disposition, member links, amendment index and deterministic
validation. The evidence boundary and source register live in `boundary.md`;
the cross-lens account and limitations live in `synthesis.md`. A complete set
also retains the analyst reports, reconciliation, memory profile and three
independent verification judgments. The manifest, `ARTIFACT.yaml`, pins every
member. Readers validate membership and take the comparison profile from
`memory-profile.md`.
They reject duplicate sources and directory names that disagree with sources.
Old `agentic-systems/reports/` and the new `retained-archive/` do not participate
in current validation or comparison. No local run state, source checkout,
legacy review or prior CSV is required. The
[memory profile contract](../../agentic-system-analyses/types/agent-memory-profile.md#memory-comparison-fields)
defines scoped findings, evidence bases and coverage assessments. New profiles
use revision 2; immutable unversioned profiles retain revision-1 interpretation.
Do not silently pool changed write-agency semantics across revisions.

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
hashes of the review and the manifest (`artifact_sha256`), plus the profile
revision. Axis unions are JSON arrays with separate coverage assessment,
coverage rationale, derived existence-evidence maps, canonical records and
JSON unit data. Revision-2 units preserve each finding's scope, basis, records
and limitation; a strong witness in the union does not upgrade another unit.
Revision-1 rows preserve their original assessment and rationale without
reclassification. The members carry the source evidence.
The table separates code-grounded and doc-grounded sets, displays revision and
unit limitations, and links the accepted overview. Statistics separate revisions
and count code-grounded wired, observed, or causally supported values, including
supported positives under partial coverage; the remainder is not inferred
absent. Weaker bases and coverage assessments are reported separately. Entropy
and redundancy require known coverage and strong evidence for every finding,
not just the strongest witness per value. Evidenced absence, inapplicability and
incomplete coverage remain distinct. Denominators describe this selected
revision-specific population only.

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

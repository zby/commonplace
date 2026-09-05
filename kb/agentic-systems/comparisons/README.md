# Memory comparisons from the main analysis

The matrix builder, table renderer, and analyzer read the exact results produced
by `analyse-agentic-system`. Their common input is each generated review under
`kb/agentic-systems/reviews/`, its `analysis-result` path and SHA-256, and the
byte-identical result retained under `kb/reports/retained/agentic-system-analysis/`.
They do not require local run state, source checkouts, legacy reviews, or a prior
CSV. The [result contract](../../types/agentic-system-analysis-result.md#memory-comparison-fields)
defines the scoped comparison fields and evidence assessments.

Run from the repository root:

```bash
uv run python scripts/build_systems_matrix.py
uv run python scripts/render_systems_table.py
uv run python scripts/analyze_matrix.py
```

The first two commands write `memory-systems.csv` and `memory-systems-table.md`
in this directory. All three read the main results directly; the renderer and
analyzer do not depend on the CSV being present. Repeat `--review <main-review-path>`
to select a bounded population. Otherwise every generated main review is
selected, and missing or invalid evidence blocks the operation. Select only one
review per source identity; repeat runs do not count as distinct systems.
Builder and renderer accept `--output <path>` for an isolated trial.

Each CSV row records the source, run, boundary, tier, compared scope, and hashes
of both inputs. Axis values are JSON arrays with separate assessment, evidence
basis, and canonical-record columns. The exact result retains the rationale.
The table separates code-grounded and doc-grounded results and links both the
public review and full result. Statistics count code-grounded wired, observed,
or causally supported values and evidenced absences; they report weaker bases
and uncertain assessments separately. Their entropy and redundancy measures
treat each complete value set as a category, not each member as an independent
observation. Denominators describe this selected population only.

Existing reviews without retained-result metadata and normalized comparison
fields need regeneration through the main analysis before inclusion. Do not
patch generated findings, reuse an old CSV value, or infer absence from an
omission. No production comparison has yet been built with this contract.
The old matrix and table under `kb/agent-memory-systems/` remain historical
snapshots; these commands no longer rebuild them. Public landscape synthesis
still needs migration to this input contract before a current refresh.

# C04 acceptance — landscape synthesis from main results

Accepted on 2026-09-05 for procedure migration. The preceding five consumer
migrations were committed in `c1490415`; C04 was committed in `c589b981`.
The later [one-system production pilot](./production-pilot.md) regenerates
Apache Maka and verifies the migrated procedures. Broader corpus regeneration
and a public landscape synthesis remain outstanding.

## Changed consumption path

`synthesize-agent-memory-landscape` is still loaded through its existing
repo-local skill projections. It now takes a selected population of generated
main reviews and reads the full retained results for qualitative claims. Its
bundle command builds the CSV from those same results; no legacy parser,
review, old CSV, or transfer report supplies a value or example.

The bundle retains canonical relative paths, byte lengths and hashes, result
contracts, producer/consumer instructions, relevant implementation files, and
dependency declarations. Additional ontology inputs are explicit. Rebuilding
its matrix from bundled results must reproduce the exact CSV bytes. Current
verification also compares source bytes and the selected population; historical
verification does not require the current corpus to remain unchanged.

Missing or malformed required inputs fail the selected build. Explicit
unknown, uninspected, and inapplicable assessments remain data: they withhold
unsupported claims without blocking unrelated findings. The query ledger must
state its evidence filters, denominator, run IDs, and exclusions. Qualitative
claims use the full result's canonical records and evidence limits. Both the
article and comparison collection contracts now permit citations to the
published exact main results.

## Bounded replay

The [trial synthesis](./c04-trial.md) follows the migrated skill on four
synthetic main-review results built by the fixture in
`tests/commonplace/lib/test_landscape_bundle.py`. The input repository lacks
legacy reviews, ignored run state, source checkouts, and a public CSV. It has
three code-grounded fixtures with respectively wired, claimed, and uninspected
storage findings, plus one doc-grounded fixture.

The query finds **one eligible fixture and one match**, preserving the
multi-store fixture as one system. It excludes the claimed, uninspected, and
doc-grounded rows explicitly. Reading `OBJ-1` in the full wired result supports
the primary Markdown notes and derived SQLite index account. Reading its
Runtime account withholds observed behavior and causal benefit. Verification
was local. These are fixture assertions, never evidence about real systems.

This executable query recomputes the numerator, denominator, and run identities
from the frozen CSV; pass the bundle path as its first argument:

```python
import csv
import json
import sys
from pathlib import Path

rows = list(csv.DictReader((Path(sys.argv[1]) / "matrix.csv").open()))
eligible = [row for row in rows
            if row["source_tier"] == "code-grounded"
            and row["storage_substrate_assessment"] == "known"
            and row["storage_substrate_basis"] in {"wired", "observed", "causally supported"}]
matched = [row for row in eligible if "files" in json.loads(row["storage_substrate"])]
print(json.dumps({
    "numerator": len(matched), "denominator": len(eligible),
    "included_runs": [row["analysis_run"] for row in eligible],
    "matched_runs": [row["analysis_run"] for row in matched],
    "excluded_runs": [row["analysis_run"] for row in rows if row not in eligible],
}, indent=2))
```

The accepted local bundle is `/tmp/commonplace-c04-ao19i4vg/evidence`. Its
manifest SHA-256 is
`f3a118a842b37f2b62123c8962bba29cb3d5cecdbdf2671a07143d640e4fdb46`;
its matrix SHA-256 is
`f778407205bcd3c6db209eff6757b175d3a474a14b1dea6e3bd1cded2ee6755f`.
The final verification uses that manifest hash and the isolated source root.
The automated fixture recreates the same population and assertions; its
newly created Git source commit may change exact replay hashes.

## Acceptance checks

- Four-result capture succeeds without legacy reviews, local run state, or a
  prior public matrix. Verification still succeeds after deleting the source
  fixture repository entirely.
- Changed result, matrix, manifest, or added bundle files are rejected against
  the externally recorded hash.
- A recomputed manifest cannot conceal a CSV inconsistent with its main results.
- Current verification detects population growth for all-generated selection;
  an explicitly selected subset remains stable when an unrelated review appears.
- Changed ontology bytes invalidate current verification but leave the original
  historical bundle usable.
- Missing results leave no completed bundle; an existing bundle is preserved.
- The additional-input interface rejects transfer reports and legacy evidence.
- The CLI requires an externally recorded hash and returns failure on mismatch.
- `uv run pytest -q --tb=short`: **722 passed**.
- Ruff: passed for the new script/tests and the existing source/test trees.
- Changed Markdown and this workshop's trial/acceptance records:
  `commonplace-validate`, zero failures and warnings.

A real default prepare against this checkout exits 1 at Apache Maka:
`missing or mismatched retained result; regenerate the main review`.
It writes no bundle and leaves existing public comparisons untouched. No
production output was manufactured from incomplete or legacy data.

## Remaining work

The next production trial needs main-review regeneration under the current
result and retention contract. It can then use the migrated matrix, table, and
synthesis path on that bounded population. The remaining maintenance
procedures, surveys, citations, and mandatory duplicate legacy publication
retain their separate queue entries; this acceptance does not retire them.

# Production pilot: Apache Maka

Status: completed on 2026-09-05. C04's procedure migration was committed in
`c589b981`; this pilot regenerates one real main analysis and exercises
C01–C04 against it. The population is deliberately one system. Pond and the
historical legacy corpus are excluded pending source regeneration.

## Evidence boundary

- Main run: `AAS-2026-09-05-apache-maka-01`.
- Frozen source: `https://github.com/apache/maka` at
  `ece69ab3e7a1629a6073831005711d8aa7160ca4`; analysis cutoff `2026-09-05`.
- [Public review](../../agentic-systems/reviews/apache-maka.md), SHA-256
  `cf2f80113c2c21074cdc07e149b9a9cb3a764f0ff5b6fb39728deee633eac76c`.
- [Exact retained result](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-apache-maka-01/result.md), SHA-256
  `fcd16d145d4ee6730eedab994478c8a320fd98f79123dd2df145c3cb6b8d3c18`.
- Temporary frozen bundle:
  `/tmp/commonplace-maka-production-pilot-20260905`.
- Manifest SHA-256:
  `62fe2cd60a45144d96080b5cc7523ea8b442576fb90ca4d7679803aa4ec86355`.
- Matrix SHA-256:
  `eaa7c7aca2d5218dff5f517a33e13fe2cc8514ec7ddfba75214c8957b8b35aa7`.
- Explicit selection: only `kb/agentic-systems/reviews/apache-maka.md`;
  one code-grounded result, zero doc-grounded results. No extra ontology input.

The bundle captures contracts and reader code along with those exact evidence
bytes. Its recorded repository HEAD is advisory: the regenerated result and
publication fix were uncommitted when captured, so that commit is not their
reconstruction boundary. This is a workshop trial, not a new public landscape
article. Public synthesis would first require the skill's durable bundle/input
retention condition. The main exact result itself is retained by the normal
publication workflow.

## Executable query ledger

Run this standard-library query with the frozen bundle directory as its first
argument. It queries that bundle's CSV, reads every selected full result,
checks result hashes and canonical support, and returns included/excluded run
identities. It never opens local run state, source checkouts or legacy reviews.

```python
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

bundle = Path(sys.argv[1])
rows = list(csv.DictReader((bundle / "matrix.csv").open(newline="")))
strong = {"wired", "observed", "causally supported"}
assert len({row["source_identity"] for row in rows}) == len(rows)
for row in rows:
    evidence = (bundle / row["result_file"]).read_bytes()
    assert hashlib.sha256(evidence).hexdigest() == row["result_sha256"]
    text = evidence.decode("utf-8")
    assert all(record in text for record in ("OBJ-1", "OBJ-2", "OBJ-3", "OBJ-4", "ABS-1", "RTE-8", "RTE-11", "RTE-13"))

def eligible(row, axis):
    return (row["source_tier"] == "code-grounded"
            and row[axis + "_assessment"] == "known"
            and row[axis + "_basis"] in strong)

def query(axis, wanted):
    admitted = [row for row in rows if eligible(row, axis)]
    matched = [row for row in admitted if wanted <= set(json.loads(row[axis]))]
    excluded = [row for row in rows if not eligible(row, axis)]
    return {
        "axis": axis,
        "test": "set contains " + json.dumps(sorted(wanted)),
        "numerator": len(matched),
        "denominator": len(admitted),
        "included_runs": [row["analysis_run"] for row in admitted],
        "matched_runs": [row["analysis_run"] for row in matched],
        "excluded_runs": [row["analysis_run"] for row in excluded],
        "exclusions": dict(Counter(row["source_tier"] + ":" + row[axis + "_assessment"] + ":" + row[axis + "_basis"] for row in excluded)),
    }

output = {
    "selected_rows": len(rows),
    "storage": query("storage_substrate", {"files", "sqlite"}),
    "readback": query("read_back_direction", {"pull"}),
    "unknowns": {axis: dict(Counter(row[axis + "_assessment"] for row in rows))
                 for axis in ("representational_form", "lineage", "distilled_form", "curation_operations", "faithfulness_tested")},
}
print(json.dumps(output, indent=2, sort_keys=True))
```

The storage query asks set membership for both files and SQLite, with one
system counted once. Its denominator is code-grounded known storage at wired
or stronger basis. The pull query uses the identical tier/basis filter for
read-back direction; afforded unions are excluded rather than counted negative.
Unknown-assessment counts include the entire explicit population and imply
nothing about omitted systems.

Query output: [pilot-query-output.json](./pilot-query-output.json).

## Bounded synthesis

The selected result has both file and SQLite memory storage: **1 of 1 eligible
selected systems**, counted once despite the two stores. This comes from
OBJ-1 through OBJ-4 in the exact result. The qualitative account matters more
than the count: file-backed local memory is injected into the task prompt,
while atomic SQLite memory is written without a production recall caller found
within the recorded search boundary. RTE-8, RTE-11 and ABS-1 prevent combining
those into an extraction-to-prompt loop. Checkpoint replay is a third consumer
path, RTE-12/RTE-13. See the [full memory lens and reconciliation](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-apache-maka-01/result.md#lens-outputs).

The aggregate read-back surface contains wired push and storage-API pull at
only afforded basis. The strong-evidence pull query therefore has **zero
eligible rows and one excluded row**; no proportion is defined. That exclusion
must not be paraphrased as absence of memory retrieval. The table preserves
the weaker basis, while the analyzer excludes the union from implementation
statistics.

Representational form, lineage and distilled form are not determinable as
complete sets; curation and faithfulness testing remain uninspected as aggregate
assessments. Each disposition occurs in the one selected result. Opaque
provider checkpoint content prevents a complete form classification without
making the known text checkpoint disappear. Source checks, approval and summary
format validation do not supply a recall-dependence experiment.

This pilot supports no prevalence across systems, historical-corpus coverage,
change over time, benchmark ranking or causal benefit from memory. The full
result's scoped records supply the qualitative findings; the legacy corpus and
transfer scans supply none. Synthesis verification was local; the producing
analysis separately used two scoped lens workers and parent reconciliation.

## Procedure checks and disposition

The matrix builder and table renderer each read the main-review inputs directly
with the identical explicit review argument. Their workshop outputs are
[pilot-matrix.csv](./pilot-matrix.csv) and [pilot-table.md](./pilot-table.md).
The matrix matches the bundled CSV byte for byte. The analyzer reports
one code-grounded row, preserves the files/SQLite set, and excludes the afforded
read-back union from its strong-evidence statistics. A one-row entropy or
column-selection heuristic is not a meaningful landscape conclusion.

The captured bundle contains no legacy reviews, ignored main-run state, or
source checkout. Its own verification rebuilds the CSV from captured retained
results. Final verification against the live source root checks the externally
recorded manifest hash, matrix agreement and current input bytes.

A default all-generated build fails at Pond with missing/mismatched retained
result metadata and writes no output. There is no fallback to the historical
CSV or old review. Public comparison defaults remain unbuilt; the historical
legacy matrix/table and syntheses remain unchanged.

The production publication trial found and fixed one reader defect: relative
links to another supplied prospective output were checked only against disk.
Link validation now also uses the current validation run's normalized content
overrides. The regression test prepares a review linked to its not-yet-written
retained result, still rejects an unrelated missing target, then publishes and
validates the complete bundle. No early retained-file write or validation waiver
is required. All 723 tests pass; Ruff and changed Markdown validation pass.

The production pilot is complete. Pond remains unregenerated, and broader
population comparisons remain blocked on selected-input regeneration.
Next procedure migration: C10, replacing or retiring direct taxonomy patching;
C05–C07 still need sufficient main-review evidence or explicit historical
status. C12/C14 have not retired mandatory legacy publication for targets whose
primary offered work is memory.

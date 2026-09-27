# Trial query ledger

This ledger queries exactly the three bundled results selected by the commission. It uses no prior corpus or source checkout. Manifest SHA-256, recorded before interpretation: `44f4ef62bda8116eeac568daae97207931a6cd4ad93f459151091a00903a76cd`. Matrix SHA-256: `fb2f5e4554e24e9514afe71ea6c75b7f6e7b12e0f0082de02d92a0d4f097ed06`.

The executable query below is the supplied query logic plus an assertion fixing the expected matrix hash. Run its Python block with the bundled `matrix.csv` path and this literal hash as positional arguments. It checks the bytes before parsing CSV. JSON arrays and evidence maps are decoded; code-grounded values count only at wired, observed or causally supported basis. Known and partial coverage support positive membership; only known profiles whose every member has a strong basis qualify as complete strong profiles. No set-equality prevalence claim is selected for this trial.

Each of the fourteen axis records is a value-membership query over the selected code-grounded population. Its `membership_counts` are numerators over that population, with coverage for every selected run and weaker values separately disclosed. Each of Q1–Q6 tests the conjunction of its named axis/value memberships, reports matched run IDs and exclusions, and counts a system once. Uncounted rows are not negative. The axis witness table below supplies included run IDs for the per-value counts. Empty assessment categories have zero selected rows; no selected row is dropped.

## Input identities

| System/run | Review SHA-256 | Retained result SHA-256 | Revision | Cutoff |
|---|---|---|---|---|
| Dynamic Cheatsheet / `AAS-2026-09-26-dynamic-cheatsheet-02` | `76c76c5e7e2aea281012933a60b42b338f68e6363f98e0b5a02ff7cad0a36445` | `69cf228433d975ac518c02f315ac81aaa26a6b29c3e3db63b932e6a199194cfa` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | 2026-09-26 |
| Mem0 / `AAS-2026-09-26-mem0-02` | `f0ed4295059b4885a886892e7731bda966eb8a89dba4c51366cfb5aac70abfe4` | `b4a541c5e6a90e37dbb0115bf9e230c41c5fc635023b519a57c447d4b7ffabd1` | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | 2026-09-26 |
| Napkin / `AAS-2026-09-27-napkin-01` | `1d5b8e3ef19c834de3242ebf99002010e83fd7413256bcd6995f66fb4c3fdae7` | `8484f622335c134237968326c9971d8fbb1e71f97128e411f96b8d46ccba41db` | `7582d6a46f5a11995956e60a59c41a5b242109f1` | 2026-09-27 |

Original query-source SHA-256: `e09336a25fa3dff1065842625dc6737d1467441357e5272da5010185e7e6f2ea`. Snapshot-specific executable SHA-256: `745a90eaced52d4e8eabf2e8b1470a6a3d722edb3d512f7e8455697d9937c193`. Query process exit: 0; stderr empty.

## Executable query

```python
import csv
import hashlib
import io
import json
import sys
from collections import Counter
from pathlib import Path

assert sys.argv[2] == "fb2f5e4554e24e9514afe71ea6c75b7f6e7b12e0f0082de02d92a0d4f097ed06", "wrong trial snapshot"
raw = Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(raw).hexdigest() == sys.argv[2]
rows = list(csv.DictReader(io.StringIO(raw.decode())))
strong = {"wired", "observed", "causally supported"}
axes = [key.removesuffix("_assessment") for key in rows[0] if key.endswith("_assessment")]
assert len(rows) == 3 and len(axes) == 14
assert len({r["source_identity"] for r in rows}) == len(rows)

def support(row, axis, value):
    return json.loads(row[axis + "_evidence"]).get(value)

def implemented(row, axis, value):
    evidence = support(row, axis, value)
    return row["source_tier"] == "code-grounded" and evidence is not None and evidence["basis"] in strong

print(json.dumps({"population": len(rows), "source_tiers": dict(Counter(r["source_tier"] for r in rows))}, sort_keys=True))
for axis in axes:
    code = [r for r in rows if r["source_tier"] == "code-grounded"]
    counts = Counter(v for r in code for v in json.loads(r[axis]) if implemented(r, axis, v))
    complete = [r["analysis_run"] for r in code if r[axis + "_assessment"] == "known" and
                all(implemented(r, axis, v) for v in json.loads(r[axis]))]
    weaker = {r["analysis_run"]: {v: e["basis"] for v, e in json.loads(r[axis + "_evidence"]).items()
                                if e["basis"] not in strong} for r in code}
    print(json.dumps({"axis": axis, "selected_code_grounded": len(code), "membership_counts": dict(sorted(counts.items())),
        "complete_strong_profiles": complete,
        "coverage": {r["analysis_run"]: r[axis + "_assessment"] for r in rows},
        "weaker_values": {k: v for k, v in weaker.items() if v}}, sort_keys=True))
queries = {
    "Q1_trace_writes": [("trace_learning", "yes")],
    "Q2_push": [("read_back_direction", "push")],
    "Q3_automatic_and_push": [("write_agency", "automatic"), ("read_back_direction", "push")],
    "Q4_natural_language_and_symbolic": [("representational_form", "natural-language"), ("representational_form", "symbolic")],
    "Q5_files": [("storage_substrate", "files")],
    "Q6_no_faithfulness_test_in_boundary": [("faithfulness_tested", "no")],
}
for name, tests in queries.items():
    matched, uncounted = [], {}
    for row in rows:
        run = row["analysis_run"]
        if all(implemented(row, axis, value) for axis, value in tests):
            matched.append(run)
        else:
            uncounted[run] = [{"axis": axis, "value": value, "assessment": row[axis + "_assessment"],
                               "evidence": support(row, axis, value), "tier": row["source_tier"]}
                              for axis, value in tests if not implemented(row, axis, value)]
    print(json.dumps({"query": name, "tests": tests, "numerator": len(matched),
        "selected_population": len(rows), "selected_code_grounded": sum(r["source_tier"] == "code-grounded" for r in rows),
        "matched_runs": matched, "uncounted_not_assumed_negative": uncounted}, sort_keys=True))
```

## Exact 21 JSON output records

```jsonl
{"population": 3, "source_tiers": {"code-grounded": 3}}
{"axis": "storage_substrate", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02", "AAS-2026-09-27-napkin-01"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-27-napkin-01": "known"}, "membership_counts": {"files": 2, "in-memory": 2, "service-object": 1, "sqlite": 2, "vector": 2}, "selected_code_grounded": 3, "weaker_values": {}}
{"axis": "representational_form", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02", "AAS-2026-09-27-napkin-01"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-27-napkin-01": "known"}, "membership_counts": {"natural-language": 3, "symbolic": 3}, "selected_code_grounded": 3, "weaker_values": {}}
{"axis": "lineage", "complete_strong_profiles": [], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-27-napkin-01": "known"}, "membership_counts": {"authored": 1, "imported": 3, "other-compiled": 2, "trace-extracted": 2}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-dynamic-cheatsheet-02": {"authored": "afforded"}, "AAS-2026-09-26-mem0-02": {"authored": "afforded"}, "AAS-2026-09-27-napkin-01": {"trace-extracted": "afforded"}}}
{"axis": "behavioral_authority", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-27-napkin-01": "known"}, "membership_counts": {"instruction": 1, "knowledge": 2, "ranking": 3, "routing": 1}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-27-napkin-01": {"instruction": "afforded", "knowledge": "afforded", "routing": "afforded"}}}
{"axis": "write_agency", "complete_strong_profiles": ["AAS-2026-09-27-napkin-01"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-27-napkin-01": "known"}, "membership_counts": {"automatic": 3, "manual": 1}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-dynamic-cheatsheet-02": {"manual": "afforded"}, "AAS-2026-09-26-mem0-02": {"manual": "afforded"}}}
{"axis": "curation_operations", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-27-napkin-01": "known"}, "membership_counts": {"consolidate": 1, "decay": 3, "dedup": 2, "evolve": 3, "invalidate": 1, "promote": 1, "synthesize": 1}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-27-napkin-01": {"consolidate": "afforded", "dedup": "afforded", "invalidate": "afforded", "promote": "claimed", "synthesize": "afforded"}}}
{"axis": "read_back_direction", "complete_strong_profiles": [], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-27-napkin-01": "known"}, "membership_counts": {"pull": 1, "push": 2}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-mem0-02": {"pull": "afforded"}, "AAS-2026-09-27-napkin-01": {"pull": "afforded", "push": "afforded"}}}
{"axis": "read_back_signal", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-27-napkin-01": "partial"}, "membership_counts": {"coarse": 1, "identifier": 1, "inferred-embedding": 2, "inferred-judgment": 1}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-27-napkin-01": {"coarse": "afforded"}}}
{"axis": "trace_learning", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-27-napkin-01": "known"}, "membership_counts": {"yes": 2}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-27-napkin-01": {"yes": "afforded"}}}
{"axis": "trace_source", "complete_strong_profiles": [], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-27-napkin-01": "known"}, "membership_counts": {"session-logs": 1, "tool-traces": 1, "trajectories": 1}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-mem0-02": {"tool-traces": "afforded", "trajectories": "afforded"}, "AAS-2026-09-27-napkin-01": {"session-logs": "afforded"}}}
{"axis": "learning_scope", "complete_strong_profiles": [], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "partial", "AAS-2026-09-27-napkin-01": "known"}, "membership_counts": {"cross-task": 1, "per-task": 1}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-mem0-02": {"per-task": "afforded"}, "AAS-2026-09-27-napkin-01": {"cross-task": "afforded", "per-project": "afforded"}}}
{"axis": "learning_timing", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-27-napkin-01": "known"}, "membership_counts": {"online": 2}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-27-napkin-01": {"offline": "afforded", "online": "afforded"}}}
{"axis": "distilled_form", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-27-napkin-01": "known"}, "membership_counts": {"natural-language": 2, "symbolic": 1}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-27-napkin-01": {"natural-language": "afforded"}}}
{"axis": "faithfulness_tested", "complete_strong_profiles": [], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "not-determinable", "AAS-2026-09-26-mem0-02": "not-determinable", "AAS-2026-09-27-napkin-01": "not-determinable"}, "membership_counts": {}, "selected_code_grounded": 3, "weaker_values": {}}
{"matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-02", "AAS-2026-09-26-mem0-02"], "numerator": 2, "query": "Q1_trace_writes", "selected_code_grounded": 3, "selected_population": 3, "tests": [["trace_learning", "yes"]], "uncounted_not_assumed_negative": {"AAS-2026-09-27-napkin-01": [{"assessment": "known", "axis": "trace_learning", "evidence": {"basis": "afforded", "note": "External agent skill transforms conversation into durable knowledge and updated context for later reads.", "records": ["RTE-8"]}, "tier": "code-grounded", "value": "yes"}]}}
{"matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-02", "AAS-2026-09-26-mem0-02"], "numerator": 2, "query": "Q2_push", "selected_code_grounded": 3, "selected_population": 3, "tests": [["read_back_direction", "push"]], "uncounted_not_assumed_negative": {"AAS-2026-09-27-napkin-01": [{"assessment": "known", "axis": "read_back_direction", "evidence": {"basis": "afforded", "note": "Documented session context delivers the pinned NAPKIN note each session; no package session loader is shown.", "records": ["RTE-11"]}, "tier": "code-grounded", "value": "push"}]}}
{"matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-02", "AAS-2026-09-26-mem0-02"], "numerator": 2, "query": "Q3_automatic_and_push", "selected_code_grounded": 3, "selected_population": 3, "tests": [["write_agency", "automatic"], ["read_back_direction", "push"]], "uncounted_not_assumed_negative": {"AAS-2026-09-27-napkin-01": [{"assessment": "known", "axis": "read_back_direction", "evidence": {"basis": "afforded", "note": "Documented session context delivers the pinned NAPKIN note each session; no package session loader is shown.", "records": ["RTE-11"]}, "tier": "code-grounded", "value": "push"}]}}
{"matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-02", "AAS-2026-09-26-mem0-02", "AAS-2026-09-27-napkin-01"], "numerator": 3, "query": "Q4_natural_language_and_symbolic", "selected_code_grounded": 3, "selected_population": 3, "tests": [["representational_form", "natural-language"], ["representational_form", "symbolic"]], "uncounted_not_assumed_negative": {}}
{"matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-02", "AAS-2026-09-27-napkin-01"], "numerator": 2, "query": "Q5_files", "selected_code_grounded": 3, "selected_population": 3, "tests": [["storage_substrate", "files"]], "uncounted_not_assumed_negative": {"AAS-2026-09-26-mem0-02": [{"assessment": "known", "axis": "storage_substrate", "evidence": null, "tier": "code-grounded", "value": "files"}]}}
{"matched_runs": [], "numerator": 0, "query": "Q6_no_faithfulness_test_in_boundary", "selected_code_grounded": 3, "selected_population": 3, "tests": [["faithfulness_tested", "no"]], "uncounted_not_assumed_negative": {"AAS-2026-09-26-dynamic-cheatsheet-02": [{"assessment": "not-determinable", "axis": "faithfulness_tested", "evidence": null, "tier": "code-grounded", "value": "no"}], "AAS-2026-09-26-mem0-02": [{"assessment": "not-determinable", "axis": "faithfulness_tested", "evidence": null, "tier": "code-grounded", "value": "no"}], "AAS-2026-09-27-napkin-01": [{"assessment": "not-determinable", "axis": "faithfulness_tested", "evidence": null, "tier": "code-grounded", "value": "no"}]}}
```

## Axis membership witnesses

Abbreviations in this table: DC = `AAS-2026-09-26-dynamic-cheatsheet-02`; M = `AAS-2026-09-26-mem0-02`; N = `AAS-2026-09-27-napkin-01`. They are local display labels, not canonical record IDs. Each denominator is the three selected code-grounded systems.

| Axis | Strong positive value memberships (run labels) |
|---|---|
| `storage_substrate` | files: DC, N; in-memory: DC, N; service-object: DC; sqlite: M, N; vector: DC, M |
| `representational_form` | natural-language: DC, M, N; symbolic: DC, M, N |
| `lineage` | authored: N; imported: DC, M, N; other-compiled: M, N; trace-extracted: DC, M |
| `behavioral_authority` | instruction: DC; knowledge: DC, M; ranking: DC, M, N; routing: M |
| `write_agency` | automatic: DC, M, N; manual: N |
| `curation_operations` | consolidate: DC; decay: DC, M, N; dedup: DC, M; evolve: DC, M, N; invalidate: M; promote: DC; synthesize: DC |
| `read_back_direction` | pull: DC; push: DC, M |
| `read_back_signal` | coarse: DC; identifier: M; inferred-embedding: DC, M; inferred-judgment: DC |
| `trace_learning` | yes: DC, M |
| `trace_source` | session-logs: M; tool-traces: DC; trajectories: DC |
| `learning_scope` | cross-task: DC; per-task: DC |
| `learning_timing` | online: DC, M |
| `distilled_form` | natural-language: DC, M; symbolic: DC |
| `faithfulness_tested` | none |

## Independent local recomputation

This separate implementation reads the bundled result frontmatter directly, checks every matrix axis, reconstructs every output field, reruns the query for byte identity, and compares both other script outputs. This is computational cross-checking by the same worker, not independent agent review. Run this block with `uv run python` from the repository root.

```python
from pathlib import Path
import ast, collections, csv, hashlib, io, json, re, subprocess, sys
import yaml

bundle = Path("kb/reports/retained/agentic-analysis-reliability-20260927/trial-bundle")
cache = bundle.parent / "outputs"
ledger = Path("kb/reports/retained/agentic-analysis-reliability-20260927/trial-query-ledger.md").read_text()
matrix_hash = "fb2f5e4554e24e9514afe71ea6c75b7f6e7b12e0f0082de02d92a0d4f097ed06"
raw = (bundle / "matrix.csv").read_bytes()
assert hashlib.sha256(raw).hexdigest() == matrix_hash
assert (cache / "trial-matrix.csv").read_bytes() == raw
rows = list(csv.DictReader(io.StringIO(raw.decode())))
query_code = re.search(r"## Executable query\n\n```python\n(.*?)```", ledger, re.S).group(1)
recorded = re.search(r"## Exact 21 JSON output records\n\n```jsonl\n(.*?)```", ledger, re.S).group(1)
rerun = subprocess.run([sys.executable, "-", str(bundle / "matrix.csv"), matrix_hash], input=query_code, text=True, capture_output=True)
assert rerun.returncode == 0 and not rerun.stderr
assert rerun.stdout == recorded
records = [json.loads(line) for line in recorded.splitlines()]
assert len(records) == 21
strong = {"wired", "observed", "causally supported"}
docs = {}
expected_inputs = {}
for row in rows:
    content = (bundle / row["result_file"]).read_bytes()
    assert hashlib.sha256(content).hexdigest() == row["result_sha256"]
    doc = yaml.safe_load(content.decode().split("---", 2)[1])
    docs[row["analysis_run"]] = doc
    assert doc["run-id"] == row["analysis_run"]
    assert doc["evidence-tier"] == row["source_tier"]
    for axis, entry in doc["memory-comparison"]["axes"].items():
        assert sorted(entry["values"]) == json.loads(row[axis])
        assert entry["assessment"] == row[axis + "_assessment"]
        assert entry["evidence"] == json.loads(row[axis + "_evidence"])
        assert ";".join(entry["records"]) == row[axis + "_records"]
    expected_inputs[row["review_file"]] = row["review_sha256"]
    expected_inputs[row["result_file"]] = row["result_sha256"]
assert records[0] == {"population": len(docs), "source_tiers": dict(collections.Counter(d["evidence-tier"] for d in docs.values()))}
for rec in records[1:15]:
    axis = rec["axis"]
    coverage, weak, complete, counts = {}, {}, [], collections.Counter()
    for run, doc in docs.items():
        entry = doc["memory-comparison"]["axes"][axis]
        coverage[run] = entry["assessment"]
        if doc["evidence-tier"] != "code-grounded":
            continue
        witnesses = {v for v in entry["values"] if entry["evidence"][v]["basis"] in strong}
        counts.update(witnesses)
        if entry["assessment"] == "known" and witnesses == set(entry["values"]):
            complete.append(run)
        excluded = {v: entry["evidence"][v]["basis"] for v in entry["values"] if v not in witnesses}
        if excluded:
            weak[run] = excluded
    assert rec == {"axis": axis, "selected_code_grounded": 3, "membership_counts": dict(counts), "complete_strong_profiles": complete, "coverage": coverage, "weaker_values": weak}
for rec in records[15:]:
    matches, exclusions = [], {}
    for run, doc in docs.items():
        missing = []
        for axis, value in rec["tests"]:
            entry = doc["memory-comparison"]["axes"][axis]
            ev = entry["evidence"].get(value)
            if doc["evidence-tier"] != "code-grounded" or value not in entry["values"] or ev["basis"] not in strong:
                missing.append({"axis": axis, "value": value, "assessment": entry["assessment"], "evidence": ev, "tier": doc["evidence-tier"]})
        if missing:
            exclusions[run] = missing
        else:
            matches.append(run)
    assert rec["matched_runs"] == matches
    assert rec["uncounted_not_assumed_negative"] == exclusions
    assert rec["numerator"] == len(matches)
    assert rec["selected_population"] == len(docs) == rec["selected_code_grounded"]
statistics = (cache / "trial-statistics.txt").read_text()
reported_inputs = dict(re.findall(r"^input: (\S+) sha256=([0-9a-f]{64})$", statistics, re.M))
assert reported_inputs == expected_inputs
for rec in records[1:15]:
    pattern = r"^supported " + rec["axis"] + r": (.*?) / 3 selected code-grounded systems"
    assert ast.literal_eval(re.search(pattern, statistics, re.M).group(1)) == rec["membership_counts"]
table = (cache / "trial-table.md").read_text()
identity_lines = re.findall(r"^- `([^`]+)`: `([0-9a-f]{64})`; exact result `([^`]+)`: `([0-9a-f]{64})`; source `([^`]+)` at `([^`]+)`\.$", table, re.M)
assert len(identity_lines) == 3
expected_table = {(r["review_file"],r["review_sha256"],r["result_file"],r["result_sha256"],r["source_identity"],r["reviewed_revision"]) for r in rows}
assert set(identity_lines) == expected_table
assert set(expected_inputs) == {r["review_file"] for r in rows} | {r["result_file"] for r in rows}
print("PASS: all 21 JSON records reproduced byte-for-byte; every field independently checked from bundled result frontmatter.")
print("PASS: all 42 result-axis records agree with bundled CSV; trial matrix matches bundled matrix bytes.")
print("PASS: statistics has exactly six matching input identities and fourteen matching positive-count records; table has exactly three matching identity tuples.")
print("Q1-Q6 numerators / selected population: " + ", ".join(str(r["numerator"]) + "/3" for r in records[15:]))
```

Verification executable SHA-256: `1c638f14586a7d12c8d55704d44b2bf508b4d4a94efe7635fac095e7eba4a2ae`. Exit code 0; stderr empty. Exact verification output:

```text
PASS: all 21 JSON records reproduced byte-for-byte; every field independently checked from bundled result frontmatter.
PASS: all 42 result-axis records agree with bundled CSV; trial matrix matches bundled matrix bytes.
PASS: statistics has exactly six matching input identities and fourteen matching positive-count records; table has exactly three matching identity tuples.
Q1-Q6 numerators / selected population: 2/3, 2/3, 2/3, 3/3, 2/3, 0/3
```

Retention note: the verification block paths now use this retained bundle and
outputs directory. The repair coordinator reran the adjusted block; query
logic and exact output records are unchanged.

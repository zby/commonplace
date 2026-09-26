# Per-value pilot query ledger

The three-system pilot uses one immutable matrix. Count each source once per
query. Strong value membership accepts known or partial coverage; uncounted
rows are not assumed negative. Conjunctions assert both mechanisms within the
recorded boundary, not necessarily on one route. Complete-profile statistics
require known coverage and strong evidence for every member.

Manifest SHA-256: `101754b023abbd2efd352e11c8cc75a234dc81802829c2c2d15199b05f8b3113`. Matrix SHA-256:
`dc82c6f2e5e9084214147782cf7361c64b20e2940139122e5ded38ad5a4d800d`. Run the following as `python3 - <bundle>/matrix.csv`
with a heredoc. This is a snapshot-specific query; the matrix hash is checked.

```python
import csv
import hashlib
import io
import json
import sys
from collections import Counter
from pathlib import Path

raw = Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'dc82c6f2e5e9084214147782cf7361c64b20e2940139122e5ded38ad5a4d800d'
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

## Exact output

```jsonl
{"population": 3, "source_tiers": {"code-grounded": 3}}
{"axis": "storage_substrate", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02", "AAS-2026-09-26-napkin-03"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-26-napkin-03": "known"}, "membership_counts": {"files": 2, "in-memory": 2, "service-object": 1, "sqlite": 2, "vector": 2}, "selected_code_grounded": 3, "weaker_values": {}}
{"axis": "representational_form", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02", "AAS-2026-09-26-napkin-03"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-26-napkin-03": "known"}, "membership_counts": {"natural-language": 3, "symbolic": 3}, "selected_code_grounded": 3, "weaker_values": {}}
{"axis": "lineage", "complete_strong_profiles": [], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-26-napkin-03": "known"}, "membership_counts": {"authored": 1, "imported": 2, "other-compiled": 2, "trace-extracted": 2}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-dynamic-cheatsheet-02": {"authored": "afforded"}, "AAS-2026-09-26-mem0-02": {"authored": "afforded"}, "AAS-2026-09-26-napkin-03": {"trace-extracted": "afforded"}}}
{"axis": "behavioral_authority", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02", "AAS-2026-09-26-napkin-03"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-26-napkin-03": "known"}, "membership_counts": {"instruction": 1, "knowledge": 3, "ranking": 3, "routing": 2}, "selected_code_grounded": 3, "weaker_values": {}}
{"axis": "write_agency", "complete_strong_profiles": ["AAS-2026-09-26-napkin-03"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-26-napkin-03": "known"}, "membership_counts": {"automatic": 3, "manual": 1}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-dynamic-cheatsheet-02": {"manual": "afforded"}, "AAS-2026-09-26-mem0-02": {"manual": "afforded"}}}
{"axis": "curation_operations", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-26-napkin-03": "known"}, "membership_counts": {"consolidate": 1, "decay": 3, "dedup": 2, "evolve": 3, "invalidate": 2, "promote": 1, "synthesize": 1}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-napkin-03": {"consolidate": "afforded", "dedup": "afforded", "promote": "afforded", "synthesize": "afforded"}}}
{"axis": "read_back_direction", "complete_strong_profiles": ["AAS-2026-09-26-napkin-03"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-26-napkin-03": "known"}, "membership_counts": {"pull": 2, "push": 2}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-mem0-02": {"pull": "afforded"}}}
{"axis": "read_back_signal", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-26-napkin-03": "inapplicable"}, "membership_counts": {"coarse": 1, "identifier": 1, "inferred-embedding": 2, "inferred-judgment": 1}, "selected_code_grounded": 3, "weaker_values": {}}
{"axis": "trace_learning", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-26-napkin-03": "known"}, "membership_counts": {"yes": 2}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-napkin-03": {"yes": "afforded"}}}
{"axis": "trace_source", "complete_strong_profiles": [], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-26-napkin-03": "known"}, "membership_counts": {"session-logs": 1, "tool-traces": 1, "trajectories": 1}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-mem0-02": {"tool-traces": "afforded", "trajectories": "afforded"}, "AAS-2026-09-26-napkin-03": {"session-logs": "afforded"}}}
{"axis": "learning_scope", "complete_strong_profiles": [], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "partial", "AAS-2026-09-26-napkin-03": "known"}, "membership_counts": {"cross-task": 1, "per-task": 1}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-mem0-02": {"per-task": "afforded"}, "AAS-2026-09-26-napkin-03": {"cross-task": "afforded", "per-project": "afforded"}}}
{"axis": "learning_timing", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-26-napkin-03": "known"}, "membership_counts": {"online": 2}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-napkin-03": {"offline": "afforded", "online": "afforded"}}}
{"axis": "distilled_form", "complete_strong_profiles": ["AAS-2026-09-26-mem0-02"], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "partial", "AAS-2026-09-26-mem0-02": "known", "AAS-2026-09-26-napkin-03": "known"}, "membership_counts": {"natural-language": 2, "symbolic": 1}, "selected_code_grounded": 3, "weaker_values": {"AAS-2026-09-26-napkin-03": {"natural-language": "afforded"}}}
{"axis": "faithfulness_tested", "complete_strong_profiles": [], "coverage": {"AAS-2026-09-26-dynamic-cheatsheet-02": "not-determinable", "AAS-2026-09-26-mem0-02": "not-determinable", "AAS-2026-09-26-napkin-03": "not-determinable"}, "membership_counts": {}, "selected_code_grounded": 3, "weaker_values": {}}
{"matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-02", "AAS-2026-09-26-mem0-02"], "numerator": 2, "query": "Q1_trace_writes", "selected_code_grounded": 3, "selected_population": 3, "tests": [["trace_learning", "yes"]], "uncounted_not_assumed_negative": {"AAS-2026-09-26-napkin-03": [{"assessment": "known", "axis": "trace_learning", "evidence": {"basis": "afforded", "note": "The skill specifies automatic session-fed extraction, durable notes and a documented later agent retrieval route. The host that executes the skill is excluded.", "records": ["RTE-3"]}, "tier": "code-grounded", "value": "yes"}]}}
{"matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-02", "AAS-2026-09-26-mem0-02"], "numerator": 2, "query": "Q2_push", "selected_code_grounded": 3, "selected_population": 3, "tests": [["read_back_direction", "push"]], "uncounted_not_assumed_negative": {"AAS-2026-09-26-napkin-03": [{"assessment": "known", "axis": "read_back_direction", "evidence": null, "tier": "code-grounded", "value": "push"}]}}
{"matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-02", "AAS-2026-09-26-mem0-02"], "numerator": 2, "query": "Q3_automatic_and_push", "selected_code_grounded": 3, "selected_population": 3, "tests": [["write_agency", "automatic"], ["read_back_direction", "push"]], "uncounted_not_assumed_negative": {"AAS-2026-09-26-napkin-03": [{"assessment": "known", "axis": "read_back_direction", "evidence": null, "tier": "code-grounded", "value": "push"}]}}
{"matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-02", "AAS-2026-09-26-mem0-02", "AAS-2026-09-26-napkin-03"], "numerator": 3, "query": "Q4_natural_language_and_symbolic", "selected_code_grounded": 3, "selected_population": 3, "tests": [["representational_form", "natural-language"], ["representational_form", "symbolic"]], "uncounted_not_assumed_negative": {}}
{"matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-02", "AAS-2026-09-26-napkin-03"], "numerator": 2, "query": "Q5_files", "selected_code_grounded": 3, "selected_population": 3, "tests": [["storage_substrate", "files"]], "uncounted_not_assumed_negative": {"AAS-2026-09-26-mem0-02": [{"assessment": "known", "axis": "storage_substrate", "evidence": null, "tier": "code-grounded", "value": "files"}]}}
{"matched_runs": [], "numerator": 0, "query": "Q6_no_faithfulness_test_in_boundary", "selected_code_grounded": 3, "selected_population": 3, "tests": [["faithfulness_tested", "no"]], "uncounted_not_assumed_negative": {"AAS-2026-09-26-dynamic-cheatsheet-02": [{"assessment": "not-determinable", "axis": "faithfulness_tested", "evidence": null, "tier": "code-grounded", "value": "no"}], "AAS-2026-09-26-mem0-02": [{"assessment": "not-determinable", "axis": "faithfulness_tested", "evidence": null, "tier": "code-grounded", "value": "no"}], "AAS-2026-09-26-napkin-03": [{"assessment": "not-determinable", "axis": "faithfulness_tested", "evidence": null, "tier": "code-grounded", "value": "no"}]}}
```

# Pilot comparison query ledger

Historical initial pilot, before ADR 093 adopted per-value evidence. The results,
contracts and counts below belong to that frozen first trial.

These queries use only the frozen three-result matrix. Counts are value membership,
not equality of the whole set. Each system contributes at most once per query.
The assessed denominator excludes weaker bases and uncertainty; exclusions remain
visible and are never counted as negatives. An empty denominator yields no proportion.

Run the code below as `python3 - <bundle>/matrix.csv` using a heredoc. The expected
matrix hash makes this a snapshot-specific executable query, not a generic command.

```python
import csv, hashlib, io, json, sys
from collections import Counter
from pathlib import Path

raw = Path(sys.argv[1]).read_bytes()
expected = "d0901f96a8f43605f43e63a97a3f7a1eea21426c74244e96786ca3f17e2a7f95"
assert hashlib.sha256(raw).hexdigest() == expected
rows = list(csv.DictReader(io.StringIO(raw.decode())))
strong = {"wired", "observed", "causally supported"}
axes = [key[:-11] for key in rows[0] if key.endswith("_assessment")]
assert len(rows) == 3 and len(axes) == 14
print(json.dumps({"population": len(rows), "source_tiers": dict(Counter(r["source_tier"] for r in rows))}, sort_keys=True))
for axis in axes:
    eligible = [r for r in rows if r["source_tier"] == "code-grounded" and
                r[axis + "_assessment"] == "known" and r[axis + "_basis"] in strong]
    negatives = [r["analysis_run"] for r in rows if r["source_tier"] == "code-grounded" and
                 r[axis + "_assessment"] == "absent"]
    counts = Counter(v for r in eligible for v in set(json.loads(r[axis])))
    excluded = {r["analysis_run"]: r[axis + "_assessment"] + ":" + r[axis + "_basis"]
                for r in rows if r not in eligible and r["analysis_run"] not in negatives}
    print(json.dumps({"axis": axis, "eligible_known": len(eligible),
        "membership_counts": dict(sorted(counts.items())), "evidenced_absences": negatives,
        "excluded": excluded}, sort_keys=True))
queries = {
    "Q1_trace_writes": [("trace_learning", "yes")],
    "Q2_push": [("read_back_direction", "push")],
    "Q3_automatic_and_push": [("write_agency", "automatic"), ("read_back_direction", "push")],
    "Q4_natural_language_and_symbolic": [("representational_form", "natural-language"),
                                         ("representational_form", "symbolic")],
    "Q5_files": [("storage_substrate", "files")],
    "Q6_no_faithfulness_test_in_boundary": [("faithfulness_tested", "no")],
}
for name, tests in queries.items():
    eligible, matched, excluded = [], [], {}
    for row in rows:
        reasons = [axis + "=" + row[axis + "_assessment"] + ":" + row[axis + "_basis"]
                   for axis, _ in tests if row[axis + "_assessment"] != "known" or
                   row[axis + "_basis"] not in strong]
        if row["source_tier"] != "code-grounded": reasons.append("tier=" + row["source_tier"])
        run = row["analysis_run"]
        if reasons:
            excluded[run] = sorted(set(reasons)); continue
        eligible.append(run)
        if all(value in json.loads(row[axis]) for axis, value in tests): matched.append(run)
    print(json.dumps({"query": name, "test": tests, "total_population": len(rows),
        "numerator": len(matched), "assessed_denominator": len(eligible),
        "matched_runs": matched, "eligible_runs": eligible, "excluded": excluded}, sort_keys=True))
```

## Exact output

```jsonl
{"population": 3, "source_tiers": {"code-grounded": 3}}
{"axis": "storage_substrate", "eligible_known": 3, "evidenced_absences": [], "excluded": {}, "membership_counts": {"files": 2, "in-memory": 2, "sqlite": 1, "vector": 1}}
{"axis": "representational_form", "eligible_known": 3, "evidenced_absences": [], "excluded": {}, "membership_counts": {"natural-language": 3, "parametric": 1, "symbolic": 3}}
{"axis": "lineage", "eligible_known": 0, "evidenced_absences": [], "excluded": {"AAS-2026-09-26-dynamic-cheatsheet-01": "known:afforded", "AAS-2026-09-26-mem0-01": "known:afforded", "AAS-2026-09-26-napkin-01": "known:afforded"}, "membership_counts": {}}
{"axis": "behavioral_authority", "eligible_known": 2, "evidenced_absences": [], "excluded": {"AAS-2026-09-26-napkin-01": "known:afforded"}, "membership_counts": {"knowledge": 2, "learning": 1, "ranking": 2, "routing": 1}}
{"axis": "write_agency", "eligible_known": 0, "evidenced_absences": [], "excluded": {"AAS-2026-09-26-dynamic-cheatsheet-01": "known:afforded", "AAS-2026-09-26-mem0-01": "known:afforded", "AAS-2026-09-26-napkin-01": "known:afforded"}, "membership_counts": {}}
{"axis": "curation_operations", "eligible_known": 1, "evidenced_absences": [], "excluded": {"AAS-2026-09-26-dynamic-cheatsheet-01": "known:claimed", "AAS-2026-09-26-napkin-01": "known:afforded"}, "membership_counts": {"decay": 1, "dedup": 1, "evolve": 1, "invalidate": 1}}
{"axis": "read_back_direction", "eligible_known": 1, "evidenced_absences": [], "excluded": {"AAS-2026-09-26-mem0-01": "known:afforded", "AAS-2026-09-26-napkin-01": "known:afforded"}, "membership_counts": {"push": 1}}
{"axis": "read_back_signal", "eligible_known": 2, "evidenced_absences": [], "excluded": {"AAS-2026-09-26-napkin-01": "inapplicable:"}, "membership_counts": {"coarse": 1, "identifier": 1, "inferred-embedding": 2, "inferred-judgment": 1}}
{"axis": "trace_learning", "eligible_known": 2, "evidenced_absences": [], "excluded": {"AAS-2026-09-26-napkin-01": "known:afforded"}, "membership_counts": {"yes": 2}}
{"axis": "trace_source", "eligible_known": 1, "evidenced_absences": [], "excluded": {"AAS-2026-09-26-mem0-01": "known:afforded", "AAS-2026-09-26-napkin-01": "known:afforded"}, "membership_counts": {"tool-traces": 1, "trajectories": 1}}
{"axis": "learning_scope", "eligible_known": 1, "evidenced_absences": [], "excluded": {"AAS-2026-09-26-mem0-01": "not-determinable:", "AAS-2026-09-26-napkin-01": "known:afforded"}, "membership_counts": {"cross-task": 1, "per-task": 1}}
{"axis": "learning_timing", "eligible_known": 1, "evidenced_absences": [], "excluded": {"AAS-2026-09-26-mem0-01": "not-determinable:", "AAS-2026-09-26-napkin-01": "known:afforded"}, "membership_counts": {"online": 1}}
{"axis": "distilled_form", "eligible_known": 2, "evidenced_absences": [], "excluded": {"AAS-2026-09-26-napkin-01": "known:afforded"}, "membership_counts": {"natural-language": 2, "parametric": 1, "symbolic": 2}}
{"axis": "faithfulness_tested", "eligible_known": 2, "evidenced_absences": [], "excluded": {"AAS-2026-09-26-dynamic-cheatsheet-01": "not-determinable:"}, "membership_counts": {"no": 2}}
{"assessed_denominator": 2, "eligible_runs": ["AAS-2026-09-26-dynamic-cheatsheet-01", "AAS-2026-09-26-mem0-01"], "excluded": {"AAS-2026-09-26-napkin-01": ["trace_learning=known:afforded"]}, "matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-01", "AAS-2026-09-26-mem0-01"], "numerator": 2, "query": "Q1_trace_writes", "test": [["trace_learning", "yes"]], "total_population": 3}
{"assessed_denominator": 1, "eligible_runs": ["AAS-2026-09-26-dynamic-cheatsheet-01"], "excluded": {"AAS-2026-09-26-mem0-01": ["read_back_direction=known:afforded"], "AAS-2026-09-26-napkin-01": ["read_back_direction=known:afforded"]}, "matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-01"], "numerator": 1, "query": "Q2_push", "test": [["read_back_direction", "push"]], "total_population": 3}
{"assessed_denominator": 0, "eligible_runs": [], "excluded": {"AAS-2026-09-26-dynamic-cheatsheet-01": ["write_agency=known:afforded"], "AAS-2026-09-26-mem0-01": ["read_back_direction=known:afforded", "write_agency=known:afforded"], "AAS-2026-09-26-napkin-01": ["read_back_direction=known:afforded", "write_agency=known:afforded"]}, "matched_runs": [], "numerator": 0, "query": "Q3_automatic_and_push", "test": [["write_agency", "automatic"], ["read_back_direction", "push"]], "total_population": 3}
{"assessed_denominator": 3, "eligible_runs": ["AAS-2026-09-26-dynamic-cheatsheet-01", "AAS-2026-09-26-mem0-01", "AAS-2026-09-26-napkin-01"], "excluded": {}, "matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-01", "AAS-2026-09-26-mem0-01", "AAS-2026-09-26-napkin-01"], "numerator": 3, "query": "Q4_natural_language_and_symbolic", "test": [["representational_form", "natural-language"], ["representational_form", "symbolic"]], "total_population": 3}
{"assessed_denominator": 3, "eligible_runs": ["AAS-2026-09-26-dynamic-cheatsheet-01", "AAS-2026-09-26-mem0-01", "AAS-2026-09-26-napkin-01"], "excluded": {}, "matched_runs": ["AAS-2026-09-26-dynamic-cheatsheet-01", "AAS-2026-09-26-napkin-01"], "numerator": 2, "query": "Q5_files", "test": [["storage_substrate", "files"]], "total_population": 3}
{"assessed_denominator": 2, "eligible_runs": ["AAS-2026-09-26-mem0-01", "AAS-2026-09-26-napkin-01"], "excluded": {"AAS-2026-09-26-dynamic-cheatsheet-01": ["faithfulness_tested=not-determinable:"]}, "matched_runs": ["AAS-2026-09-26-mem0-01", "AAS-2026-09-26-napkin-01"], "numerator": 2, "query": "Q6_no_faithfulness_test_in_boundary", "test": [["faithfulness_tested", "no"]], "total_population": 3}
```

"""Fast, read-only statistics from generated agentic analysis report artifacts.

No Commonplace imports, validation, source reads, run stores, Git or network.
Roots are report directories or parents of report directories, not run stores.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[1] / "kb/agentic-system-analyses/retained"
MEMBERS = (
    "boundary", "runtime", "memory", "epistemic", "workflow", "reconciliation",
    "memory-profile", "synthesis", "report-verification", "profile-verification",
    "synthesis-verification", "overview",
)
VERIFIERS = ("report-verification", "profile-verification", "synthesis-verification")
FILENAMES = tuple(f"{name}.md" for name in MEMBERS) + ("report-check.md",)
STATUSES = ("recorded-failure", "blocked", "incomplete", "accepted-with-limits", "clean-accepted", "out-of-scope")


def scalar(text: str, key: str) -> str | None:
    """Read only simple top-level scalar identity fields, not general YAML."""
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return None
    frontmatter = text.split("\n---\n", 1)[0][4:]
    values = re.findall(rf"^{re.escape(key)}:[ \t]*(.*)$", frontmatter, re.MULTILINE)
    if len(values) != 1:
        return None
    value = values[0].strip()
    if value.startswith(('"', "'")):
        if len(value) < 2 or value[-1] != value[0]:
            return None
        value = value[1:-1]
    return value if value and value not in ("null", "~") else None


def section(text: str, heading: str) -> str | None:
    matches = list(re.finditer(rf"^## {re.escape(heading)}[ \t]*$", text, re.MULTILINE))
    if len(matches) != 1:
        return None
    rest = text[matches[0].end():]
    return re.split(r"^#{1,2} ", rest, maxsplit=1, flags=re.MULTILINE)[0].strip()


def findings(body: str | None) -> list[str] | None:
    """The runner's exact none-or-Markdown-list convention; malformed is unknown."""
    if body == "none":
        return []
    if not body:
        return None
    entries: list[str] = []
    for line in body.splitlines():
        if line.startswith("- ") and line[2:].strip():
            entries.append(line[2:].strip())
        elif line.strip():
            if not entries or not line.startswith((" ", "\t")):
                return None
            entries[-1] += "\n" + line
    return entries or None


def inspect_set(directory: Path) -> dict:
    reports = {}
    issues = []
    for filename in FILENAMES:
        path = directory / filename
        # Never follow report symlinks into sources or elsewhere.
        if path.is_symlink():
            issues.append(f"{filename}: symlink not read")
        elif path.is_file():
            try:
                reports[filename] = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                issues.append(f"{filename}: {exc}")
    ids = sorted({value for text in reports.values() if (value := scalar(text, "run-id"))})
    if len(ids) != 1:
        issues.append("missing or conflicting run-id")
    run_id = ids[0] if len(ids) == 1 else None
    for filename, text in reports.items():
        if filename != "report-check.md" and scalar(text, "run-id") != run_id:
            issues.append(f"{filename}: missing or conflicting run-id")
    overview = reports.get("overview.md", "")
    boundary = reports.get("boundary.md", "")
    disposition = scalar(overview, "result-disposition")
    boundary_disposition = scalar(boundary, "result-disposition")
    if disposition and boundary_disposition and disposition != boundary_disposition:
        issues.append("overview and boundary dispositions disagree")
    disposition = disposition or boundary_disposition
    if disposition not in ("complete", "blocked", "out-of-scope"):
        issues.append("missing or unknown result-disposition")
    failures = []
    limits = []
    for name in VERIFIERS:
        if (text := reports.get(f"{name}.md")) is not None:
            for heading, target in (("Blockers", failures), ("Limits", limits)):
                entries = findings(section(text, heading))
                if entries is None:
                    issues.append(f"{name}.md: malformed or missing {heading}")
                else:
                    target.extend({"report": f"{name}.md", "finding": entry} for entry in entries)
    if (text := reports.get("report-check.md")) is not None:
        body = text.removeprefix("# Artifact check\n").strip()
        entries = findings(body) if text.startswith("# Artifact check\n") else None
        if entries is None:
            issues.append("report-check.md: malformed Artifact check")
        else:
            failures.extend({"report": "report-check.md", "finding": entry} for entry in entries)
    required = MEMBERS if disposition not in ("blocked", "out-of-scope") else ("boundary", "overview")
    missing = [f"{name}.md" for name in required if f"{name}.md" not in reports]
    validation = section(overview, "Deterministic validation") or ""
    # These are the exact rows emitted by assemble_analysis, not free prose verdicts.
    checked = set(re.findall(r"^- `([^`]+)`: deterministic snapshot checks passed\.$", validation, re.MULTILINE))
    unchecked = [f"{name}.md" for name in required if f"{name}.md" not in checked]
    if unchecked:
        issues.append("no recorded passing snapshot check: " + ", ".join(unchecked))
    incomplete = bool(missing or issues)
    if failures:
        status = "recorded-failure"
    elif disposition == "blocked":
        status = "blocked"
    elif incomplete:
        status = "incomplete"
    elif disposition == "out-of-scope":
        status = "out-of-scope"
    elif limits:
        status = "accepted-with-limits"
    else:
        status = "clean-accepted"
    return {
        "directory": str(directory), "run_id": run_id, "observed_run_ids": ids,
        "disposition": disposition, "status": status, "report_count": len(reports),
        "failures": failures, "limits": limits, "incomplete": incomplete,
        "missing_reports": missing, "issues": issues,
    }


def report_directories(root: Path) -> list[Path]:
    """Bounded discovery: root and immediate children only; never recurse into stores."""
    directories = [root] + sorted(
        p for p in root.iterdir() if p.is_dir() and not p.is_symlink() and not p.name.startswith(".")
    )
    return [p for p in directories if any((p / name).exists() for name in FILENAMES)]


def collect(roots: list[Path], run_ids: list[str], since: str | None) -> dict:
    sets = []
    errors = []
    seen = set()
    excluded = 0
    reports_read = 0
    for root in roots:
        if root.is_symlink():
            errors.append(f"{root}: symlink root not scanned")
            continue
        try:
            directories = report_directories(root)
        except OSError as exc:
            errors.append(f"{root}: {exc}")
            continue
        for directory in directories:
            canonical = directory.resolve()
            if canonical in seen:
                continue
            seen.add(canonical)
            result = inspect_set(directory)
            reports_read += result["report_count"]
            run_id = result["run_id"]
            run_date = re.match(r"AAS-(\d{4}-\d{2}-\d{2})-", run_id or "")
            if ((run_ids and run_id not in run_ids)
                    or (since and (not run_date or run_date[1] < since))):
                excluded += 1
                continue
            sets.append(result)
    counts = Counter(item["status"] for item in sets)
    return {
        "roots": [str(root) for root in roots], "run_ids": run_ids, "since": since,
        "report_sets": len(sets), "reports_read": reports_read,
        "selected_reports": sum(item["report_count"] for item in sets),
        "excluded_sets": excluded,
        "statuses": {status: counts[status] for status in STATUSES},
        "sets_with_recorded_failures": sum(bool(item["failures"]) for item in sets),
        "recorded_failure_findings": sum(len(item["failures"]) for item in sets),
        "sets_with_limits": sum(bool(item["limits"]) for item in sets),
        "recorded_limit_findings": sum(len(item["limits"]) for item in sets),
        "sets_with_blocked_disposition": sum(item["disposition"] == "blocked" for item in sets),
        "incomplete_sets": sum(item["incomplete"] for item in sets),
        "errors": errors, "sets": sets,
        "caveat": "Report-only snapshot, not rerun completion or runtime success. Missing reports are not success. "
                  "No inventory denominator; roots may include older runs. Limits are warnings, not blockers. "
                  "Accepted means a complete overview with recorded passing checks and blocker-free verifications; "
                  "publication and checks are not independently verified. Separate directories are separate report sets.",
    }


def iso_date(value: str) -> str:
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as exc:
        raise argparse.ArgumentTypeError("expected YYYY-MM-DD") from exc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", action="append", type=Path, help="report directory or parent of report directories; repeatable; replaces default retained root. For in-flight runs supply their artifact/ directory, not the run store. Only root and immediate children are inspected")
    parser.add_argument("--run-id", action="append", default=[], help="include only this exact report run-id; repeatable")
    parser.add_argument("--since", type=iso_date, help="include run-id dates on/after YYYY-MM-DD (not file modification time); unidentified sets excluded")
    parser.add_argument("--json", action="store_true", help="print structured statistics and per-set findings")
    args = parser.parse_args(argv)
    result = collect(args.root or [DEFAULT_ROOT], args.run_id, args.since)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Report sets: {result['report_sets']}; selected reports: {result['selected_reports']}; reports read: {result['reports_read']}; excluded sets: {result['excluded_sets']}")
        print("Scope: " + ", ".join(result["roots"]))
        for status, count in result["statuses"].items():
            print(f"  {status}: {count}")
        print(f"Recorded failures: {result['recorded_failure_findings']}; limits/warnings: {result['recorded_limit_findings']}; incomplete sets: {result['incomplete_sets']}")
        for item in result["sets"]:
            print(f"{item['status']}: {item['run_id'] or 'unidentified'} — {item['directory']}")
            for finding in item["failures"]:
                print(f"  failure: {finding['report']}: {finding['finding']}")
            if item["limits"]:
                print(f"  limits/warnings: {len(item['limits'])} (findings in --json)")
            for issue in item["issues"]:
                print(f"  incomplete: {issue}")
            if item["missing_reports"]:
                print("  missing: " + ", ".join(item["missing_reports"]))
        for error in result["errors"]:
            print(f"Scan error: {error}")
        print(result["caveat"])
    # Findings are data, not validation exit codes. Only scan errors fail the CLI.
    return 2 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

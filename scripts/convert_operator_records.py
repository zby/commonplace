"""One-off: convert the operator records of revise and rewrite runs to kept answers, in place.

Before the review workflows stopped repeating runs, the operator approved an
answers file with `commonplace-review approve`, which stored the answered
text in `<run>/operator/<n>.json` (`name`, `key`, `proposal`, and once
answered `answer` and `answered-at`). The current code reads no such record:
it reads the answers a run kept in `<run>/answers/`
(`decisions.keep_answers()`), and a run's start in `<run>/start.json`.

For every revise and rewrite run under `<root>/kb/reports/state/review/runs/v2/`
this script:

- converts each answered operator record to a kept answers record whose
  `origin` is the answers file `<run>/artifact/<name>`, whose `text` is the
  approved answer and whose `at` is `answered-at`, then deletes the record;
- leaves an unanswered record in place and counts it: it holds no decision;
- writes `start.json` from `artifact/start.md` when the run has none, with
  `brief-sha256` null, since the old runs did not record the brief's hash;
- removes the `operator/` directory when it is empty afterwards.

Full-pass runs are not touched: `decisions` still reads their operator
records. `--dry-run` reports what would change and writes nothing. Run it
once per checkout of the review state, then delete this script.

    python3 scripts/convert_operator_records.py --root PATH [--dry-run]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

RUNS = Path("kb/reports/state/review/runs/v2")
WORKFLOWS = ("revise", "rewrite")


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def kept_path(run_dir: Path, origin: str) -> Path:
    """Where `decisions.keep_answers()` keeps the answers file at the repository path `origin`."""
    return run_dir / "answers" / f"{Path(origin).stem}-{_sha(origin.encode('utf-8'))[:8]}.json"


def _write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def _runs(root: Path) -> list[tuple[str, Path]]:
    """Each revise or rewrite run directory that holds operator records or lacks a start record."""
    found = set()
    for workflow in WORKFLOWS:
        base = root / RUNS / workflow
        if not base.is_dir():
            continue
        found |= {(workflow, path.parent) for path in base.rglob("operator") if path.is_dir()}
        found |= {(workflow, path.parent.parent) for path in base.rglob("artifact/start.md")}
    return sorted(found, key=lambda pair: pair[1])


def convert(root: Path, dry_run: bool = False) -> dict:
    """Convert every run under `root`; return what was, or would be, converted."""
    root = root.resolve()
    report = {"root": str(root), "dry-run": dry_run, "converted": [], "left-unanswered": [], "started": [],
              "problems": []}
    for workflow, run_dir in _runs(root):
        note = run_dir.parent.relative_to(root / RUNS / workflow).as_posix() + ".md"
        start = run_dir / "artifact" / "start.md"
        if start.is_file() and not (run_dir / "start.json").is_file():
            report["started"].append(run_dir.relative_to(root).as_posix())
            if not dry_run:
                _write_json(run_dir / "start.json",
                            {"note": note, "sha256": _sha(start.read_bytes()), "brief-sha256": None})
        records = run_dir / "operator"
        for path in sorted(records.glob("*.json")) if records.is_dir() else []:
            rel = path.relative_to(root).as_posix()
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                name = data["name"]
            except (json.JSONDecodeError, KeyError, TypeError) as error:
                report["problems"].append(f"{rel}: not an operator record: {error!r}")
                continue
            if data.get("answer") is None:
                report["left-unanswered"].append(rel)
                continue
            origin = (run_dir / "artifact" / name).relative_to(root).as_posix()
            text, at = data["answer"], data.get("answered-at")
            if not isinstance(text, str) or not isinstance(at, str):
                report["problems"].append(f"{rel}: the answer or answered-at is not text")
                continue
            target = kept_path(run_dir, origin)
            report["converted"].append({"record": rel, "kept": target.relative_to(root).as_posix(),
                                        "origin": origin})
            if not dry_run:
                _write_json(target, {"origin": origin, "sha256": _sha(text.encode("utf-8")), "at": at,
                                     "text": text})
                path.unlink()
        if not dry_run and records.is_dir() and not any(records.iterdir()):
            records.rmdir()
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, required=True, help="the checkout that holds kb/reports/state/")
    parser.add_argument("--dry-run", action="store_true", help="report what would change; write nothing")
    arguments = parser.parse_args(argv)
    report = convert(arguments.root, arguments.dry_run)
    print(json.dumps(report, indent=2))
    return 1 if report["problems"] else 0


if __name__ == "__main__":
    sys.exit(main())

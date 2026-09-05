"""Render a memory comparison table directly from retained main-review results."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from commonplace.lib.agentic_publication import _atomic_write
from commonplace.lib.systems_matrix import load_results

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT = REPO_ROOT / "kb/agentic-systems/comparisons/memory-systems-table.md"
DISPLAY = {
    "storage_substrate": "Storage",
    "read_back_direction": "Read-back",
    "read_back_signal": "Push selection",
    "trace_learning": "Trace learning",
    "behavioral_authority": "Authority",
}


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def assessment(row: dict[str, str], axis: str) -> str:
    if row[axis + "_assessment"] != "known":
        return row[axis + "_assessment"]
    return ", ".join(json.loads(row[axis])) + " [" + row[axis + "_basis"] + "]"


def render(rows: list[dict[str, str]], output: Path) -> str:
    lines = [
        "---",
        'description: "Generated memory comparisons from retained main-review evidence"',
        "type: kb/types/note.md",
        "traits: [has-comparison]",
        "---",
        "",
        "# Memory mechanisms in agentic systems",
        "",
        "Each row uses one main-review result and its stated memory boundary. Values",
        "carry their evidence basis. Absence, inapplicability, uninspected mechanisms,",
        "and indeterminate classifications remain distinct. This is the selected",
        "population, not the historical memory-review corpus.",
        "",
    ]
    for tier in ("code-grounded", "doc-grounded"):
        selected = [r for r in rows if r["source_tier"] == tier]
        lines.extend([f"## {tier} ({len(selected)})", ""])
        if not selected:
            lines.extend(["No selected results in this tier.", ""])
            continue
        lines.extend(
            [
                "| System | Compared boundary | "
                + " | ".join(DISPLAY.values())
                + " | Evidence |",
                "|---|---|" + "---|" * (len(DISPLAY) + 1),
            ]
        )
        for row in selected:
            public = os.path.relpath(REPO_ROOT / row["review_file"], output.parent)
            evidence = os.path.relpath(REPO_ROOT / row["result_file"], output.parent)
            cells = [
                f"[{cell(row['system_name'])}]({public})",
                cell(row["comparison_scope"]),
            ]
            cells += [cell(assessment(row, key)) for key in DISPLAY]
            cells += [f"[{row['analysis_run']}]({evidence})"]
            lines.append("| " + " | ".join(cells) + " |")
        lines.append("")
    lines.extend(["## Input identities", ""])
    for row in rows:
        lines.extend(
            [
                f"- `{row['review_file']}`: `{row['review_sha256']}`; exact result `{row['result_file']}`: `{row['result_sha256']}`; source `{row['source_identity']}` at `{row['reviewed_revision']}`."
            ]
        )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review", action="append", type=Path)
    parser.add_argument("--output", type=Path, default=OUT)
    args = parser.parse_args(argv)
    try:
        inputs = load_results(REPO_ROOT, args.review)
        content = render(inputs.rows, args.output.resolve())
        inputs.recheck(REPO_ROOT)
        _atomic_write(args.output, content.encode("utf-8"))
    except (OSError, ValueError, KeyError, UnicodeError) as exc:
        print(f"table not written: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {args.output} ({len(inputs.rows)} rows, evidence tiers separated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

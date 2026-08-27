"""Carry assay evidence across exact inspected input changes."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.cli.freshness_io import read_input_payload
from commonplace.review.acknowledgement import ack_pairs, records_from_selector_payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Advance review freshness for exact changed-input observations emitted "
            "by the review target selector."
        ),
        allow_abbrev=False,
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Inspected selector JSON path, or '-' for stdin. Keep only targets authorized for acknowledgement.",
    )
    return parser


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    repo_root = cwd if cwd is not None else Path.cwd()
    try:
        input_path = args.input
        if input_path != "-" and not Path(input_path).is_absolute():
            input_path = str(repo_root / input_path)
        payload = read_input_payload(input_path)
        model, records = records_from_selector_payload(repo_root, payload)
        acked = ack_pairs(repo_root, records, model)
    except (FileNotFoundError, OSError, TypeError, ValueError) as exc:
        parser.error(str(exc))
    for note_path, criterion_id in acked:
        print(f"acked: {note_path} {criterion_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

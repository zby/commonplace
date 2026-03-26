from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from review_metadata import git_blob_sha, last_commit_for_path, run_git


METADATA_PATTERN = re.compile(r"^<!-- GATE-REVIEW\n(.*?)\n-->\n?", re.DOTALL)
MODEL_ENV_VAR = "COMMONPLACE_REVIEW_MODEL"
CSV_COLUMNS = [
    "note_path",
    "gate_id",
    "model",
    "gate_hash",
    "recorded_commit",
    "watched_hash",
    "recorded_at",
]


@dataclass(frozen=True)
class GateReviewRecord:
    note_path: str
    gate_id: str
    model: str
    gate_hash: str
    recorded_commit: str
    watched_hash: str
    recorded_at: str
    review_path: str | None = None


def iso_now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def encode_note_path(note_path: str) -> str:
    return str(Path(note_path).with_suffix("")).replace("/", "__")


def encode_gate_id(gate_id: str) -> str:
    return gate_id.replace("/", "__")


def encode_model(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", model).strip("-").lower()


def require_review_model() -> str:
    model = os.environ.get(MODEL_ENV_VAR, "").strip()
    if not model:
        raise ValueError(f"{MODEL_ENV_VAR} must be set")
    return model


def gate_review_path_for(
    note_path: str,
    gate_id: str,
    model: str,
    reviews_root: Path,
) -> Path:
    return reviews_root / encode_note_path(note_path) / f"{encode_gate_id(gate_id)}.{encode_model(model)}.md"


def gate_review_csv_path(repo_root: Path) -> Path:
    return repo_root / "kb" / "reports" / "review-csv" / "gate_reviews.csv"


def canonical_gate_review_path(
    repo_root: Path,
    *,
    note_path: str,
    gate_id: str,
) -> Path:
    reviews_root = repo_root / "kb" / "reports" / "reviews"
    model = require_review_model()
    return gate_review_path_for(note_path, gate_id, model, reviews_root)


def parse_gate_review_metadata(review_text: str) -> GateReviewRecord | None:
    match = METADATA_PATTERN.match(review_text)
    if match is None:
        return None

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()

    required = [
        "note-path",
        "gate-id",
        "model",
        "gate-hash",
        "recorded-commit",
        "watched-hash",
        "recorded-at",
    ]
    if any(not fields.get(key) for key in required):
        return None

    return GateReviewRecord(
        note_path=fields["note-path"],
        gate_id=fields["gate-id"],
        model=fields["model"],
        gate_hash=fields["gate-hash"],
        recorded_commit=fields["recorded-commit"],
        watched_hash=fields["watched-hash"],
        recorded_at=fields["recorded-at"],
    )


def strip_gate_review_metadata(review_text: str) -> str:
    return METADATA_PATTERN.sub("", review_text, count=1)


def render_gate_review_metadata(record: GateReviewRecord) -> str:
    lines = [
        "<!-- GATE-REVIEW",
        f"note-path: {record.note_path}",
        f"gate-id: {record.gate_id}",
        f"model: {record.model}",
        f"gate-hash: {record.gate_hash}",
        f"recorded-commit: {record.recorded_commit}",
        f"watched-hash: {record.watched_hash}",
        f"recorded-at: {record.recorded_at}",
        "-->",
    ]
    return "\n".join(lines) + "\n"


def load_gate_review_index(csv_path: Path) -> dict[tuple[str, str, str], GateReviewRecord]:
    if not csv_path.is_file():
        return {}

    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        records: dict[tuple[str, str, str], GateReviewRecord] = {}
        for row in reader:
            record = GateReviewRecord(
                note_path=row["note_path"],
                gate_id=row["gate_id"],
                model=row["model"],
                gate_hash=row["gate_hash"],
                recorded_commit=row["recorded_commit"],
                watched_hash=row["watched_hash"],
                recorded_at=row["recorded_at"],
            )
            records[(record.note_path, record.gate_id, record.model)] = record
        return records


def write_gate_review_index(csv_path: Path, records: list[GateReviewRecord]) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for record in sorted(records, key=lambda item: (item.note_path, item.gate_id)):
            writer.writerow(
                {
                    "note_path": record.note_path,
                    "gate_id": record.gate_id,
                    "model": record.model,
                    "gate_hash": record.gate_hash,
                    "recorded_commit": record.recorded_commit,
                    "watched_hash": record.watched_hash,
                    "recorded_at": record.recorded_at,
                }
            )


def rebuild_gate_review_index(
    reviews_root: Path,
    csv_path: Path,
) -> list[GateReviewRecord]:
    records: list[GateReviewRecord] = []
    if reviews_root.is_dir():
        for note_dir in sorted(path for path in reviews_root.iterdir() if path.is_dir()):
            for review_path in sorted(note_dir.glob("*.md")):
                record = parse_gate_review_metadata(review_path.read_text(encoding="utf-8"))
                if record is None:
                    raise ValueError(f"Missing or invalid gate review metadata in {review_path}")
                records.append(
                    GateReviewRecord(
                        note_path=record.note_path,
                        gate_id=record.gate_id,
                        model=record.model,
                        gate_hash=record.gate_hash,
                        recorded_commit=record.recorded_commit,
                        watched_hash=record.watched_hash,
                        recorded_at=record.recorded_at,
                        review_path=review_path.relative_to(reviews_root.parent.parent).as_posix(),
                    )
                )

    write_gate_review_index(csv_path, records)
    return records


def write_recorded_gate_review(
    repo_root: Path,
    *,
    note_path: str,
    gate_id: str,
    model: str,
    gate_hash: str,
    recorded_commit: str,
    watched_hash: str,
    review_body: str,
    recorded_at: str | None = None,
) -> Path:
    reviews_root = repo_root / "kb" / "reports" / "reviews"
    csv_path = gate_review_csv_path(repo_root)
    record = GateReviewRecord(
        note_path=note_path,
        gate_id=gate_id,
        model=model,
        gate_hash=gate_hash,
        recorded_commit=recorded_commit,
        watched_hash=watched_hash,
        recorded_at=recorded_at or iso_now(),
    )
    review_path = gate_review_path_for(note_path, gate_id, model, reviews_root)
    review_path.parent.mkdir(parents=True, exist_ok=True)
    review_path.write_text(
        render_gate_review_metadata(record) + review_body.lstrip("\n"),
        encoding="utf-8",
    )
    rebuild_gate_review_index(reviews_root, csv_path)
    return review_path


def build_current_gate_review_record(
    repo_root: Path,
    *,
    note_path: str,
    gate_id: str,
    recorded_at: str | None = None,
) -> GateReviewRecord:
    from gate_core import compute_watched_hash, load_gate_definition, load_note_regions, non_body_watches

    model = require_review_model()
    gate_def = load_gate_definition(
        repo_root / "kb" / "instructions" / "review-gates",
        gate_id,
    )
    note_file = repo_root / note_path
    note_regions = load_note_regions(note_file, repo_root)
    watched_hash = compute_watched_hash(
        note_regions,
        gate_def.watches if gate_def.staleness.mode == "changed" else non_body_watches(gate_def),
    )

    recorded_commit = last_commit_for_path(repo_root, Path(note_path))
    if recorded_commit is None:
        head = run_git(repo_root, "rev-parse", "HEAD", check=False)
        if head.returncode != 0:
            raise ValueError("Could not determine recorded commit for gate review")
        recorded_commit = head.stdout.strip()

    return GateReviewRecord(
        note_path=note_path,
        gate_id=gate_id,
        model=model,
        gate_hash=git_blob_sha(gate_def.path),
        recorded_commit=recorded_commit,
        watched_hash=watched_hash,
        recorded_at=recorded_at or iso_now(),
    )


def record_gate_review(
    repo_root: Path,
    *,
    note_path: str,
    gate_id: str,
    review_body: str,
    recorded_at: str | None = None,
) -> Path:
    record = build_current_gate_review_record(
        repo_root,
        note_path=note_path,
        gate_id=gate_id,
        recorded_at=recorded_at,
    )
    return write_recorded_gate_review(
        repo_root,
        note_path=record.note_path,
        gate_id=record.gate_id,
        model=record.model,
        gate_hash=record.gate_hash,
        recorded_commit=record.recorded_commit,
        watched_hash=record.watched_hash,
        review_body=review_body,
        recorded_at=record.recorded_at,
    )


def finalize_gate_review(
    repo_root: Path,
    *,
    note_path: str,
    gate_id: str,
    recorded_at: str | None = None,
) -> Path:
    reviews_root = repo_root / "kb" / "reports" / "reviews"
    model = require_review_model()
    review_path = gate_review_path_for(note_path, gate_id, model, reviews_root)
    if not review_path.is_file():
        raise ValueError(f"Gate review file not found: {review_path.relative_to(repo_root)}")

    review_body = strip_gate_review_metadata(
        review_path.read_text(encoding="utf-8")
    ).lstrip("\n")
    if not review_body.strip():
        raise ValueError(f"Gate review body is empty: {review_path.relative_to(repo_root)}")

    record = build_current_gate_review_record(
        repo_root,
        note_path=note_path,
        gate_id=gate_id,
        recorded_at=recorded_at,
    )
    return write_recorded_gate_review(
        repo_root,
        note_path=record.note_path,
        gate_id=record.gate_id,
        model=record.model,
        gate_hash=record.gate_hash,
        recorded_commit=record.recorded_commit,
        watched_hash=record.watched_hash,
        review_body=review_body,
        recorded_at=record.recorded_at,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Gate review storage helpers.",
    )
    subparsers = parser.add_subparsers(dest="command")
    path_parser = subparsers.add_parser(
        "path",
        help="Print the canonical review path for one note and gate under the current review model.",
    )
    path_parser.add_argument(
        "note_path",
        help="Repository-relative note path, for example kb/notes/backlinks.md.",
    )
    path_parser.add_argument(
        "gate_id",
        help="Gate id such as frontmatter/title-composability.",
    )
    subparsers.add_parser(
        "rebuild-csv",
        help="Regenerate kb/reports/review-csv/gate_reviews.csv from stored gate reviews.",
    )
    finalize_parser = subparsers.add_parser(
        "finalize",
        help="Finalize one gate review already written at its canonical path and regenerate the CSV index.",
    )
    finalize_parser.add_argument(
        "note_path",
        help="Repository-relative note path, for example kb/notes/backlinks.md.",
    )
    finalize_parser.add_argument(
        "gate_id",
        help="Gate id such as frontmatter/title-composability.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "path":
        repo_root = Path.cwd()
        print(
            canonical_gate_review_path(
                repo_root,
                note_path=args.note_path,
                gate_id=args.gate_id,
            ).relative_to(repo_root).as_posix()
        )
        return

    if args.command == "rebuild-csv":
        repo_root = Path.cwd()
        rebuild_gate_review_index(
            repo_root / "kb" / "reports" / "reviews",
            gate_review_csv_path(repo_root),
        )
        return

    if args.command == "finalize":
        repo_root = Path.cwd()
        finalize_gate_review(
            repo_root,
            note_path=args.note_path,
            gate_id=args.gate_id,
        )
        return

    if args.command is None:
        parser.print_help(sys.stderr)
        sys.exit(2)
    parser.error(f"unknown command: {args.command}")


if __name__ == "__main__":
    main()

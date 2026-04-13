"""Review-system relocation hook."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from commonplace.lib.relocation import NotePathMove, move_path
from commonplace.review import review_db, review_metadata


@dataclass(frozen=True)
class ReviewExportMove:
    source_dir: Path
    destination_dir: Path
    file_updates: dict[Path, tuple[Path, str]]


@dataclass(frozen=True)
class ReviewRelocationPlan:
    root: Path
    export_moves: list[ReviewExportMove]
    db_path: Path
    db_rekeys: list[tuple[str, str]]
    db_counts: list[Any]


def reviews_root(kb_root: Path) -> Path:
    return kb_root / "reports" / "reviews"


def repo_relative_note_path(note_path: Path, root: Path) -> str:
    return note_path.relative_to(root).as_posix()


def encode_review_export_dir(note_path: str) -> str:
    stem = note_path[:-3] if note_path.endswith(".md") else note_path
    return stem.replace("/", "__")


def review_export_dir_for_note(note_path: Path, *, root: Path, kb_root: Path) -> Path:
    return reviews_root(kb_root) / encode_review_export_dir(
        repo_relative_note_path(note_path, root)
    )


def rewrite_review_export_metadata(
    content: str,
    *,
    old_note_path: str,
    new_note_path: str,
) -> tuple[str, bool]:
    metadata = review_metadata.parse_review_metadata(content)
    if metadata is None or metadata.note_path != old_note_path:
        return content, False
    return (
        review_metadata.inject_review_metadata(
            content,
            replace(metadata, note_path=new_note_path),
        ),
        True,
    )


def collect_review_export_updates(
    source: Path,
    destination: Path,
    *,
    root: Path,
    kb_root: Path,
) -> tuple[Path, Path, dict[Path, tuple[Path, str]]]:
    source_dir = review_export_dir_for_note(source, root=root, kb_root=kb_root)
    destination_dir = review_export_dir_for_note(destination, root=root, kb_root=kb_root)
    if not source_dir.is_dir():
        return source_dir, destination_dir, {}

    old_note_path = repo_relative_note_path(source, root)
    new_note_path = repo_relative_note_path(destination, root)
    updates: dict[Path, tuple[Path, str]] = {}
    for review_file in sorted(source_dir.rglob("*.md")):
        updated, changed = rewrite_review_export_metadata(
            review_file.read_text(encoding="utf-8"),
            old_note_path=old_note_path,
            new_note_path=new_note_path,
        )
        if changed:
            target = destination_dir / review_file.relative_to(source_dir)
            updates[review_file] = (target, updated)
    return source_dir, destination_dir, updates


class ReviewRelocationHook:
    """Relocation hook that moves review exports and rekeys the review DB."""

    def plan(
        self,
        *,
        root: Path,
        moves: Sequence[NotePathMove],
    ) -> ReviewRelocationPlan | None:
        kb_root = root / "kb"
        export_moves: list[ReviewExportMove] = []
        db_rekeys: list[tuple[str, str]] = []
        db_counts: list[Any] = []
        db_path = review_db.resolve_db_path(root)
        has_db = db_path.exists()

        for move in moves:
            source_dir, destination_dir, file_updates = collect_review_export_updates(
                move.old_path,
                move.new_path,
                root=root,
                kb_root=kb_root,
            )
            if source_dir.exists():
                if destination_dir.exists():
                    raise FileExistsError(
                        "Destination review export directory already exists: "
                        f"{destination_dir.relative_to(root)}"
                    )
                export_moves.append(
                    ReviewExportMove(
                        source_dir=source_dir,
                        destination_dir=destination_dir,
                        file_updates=file_updates,
                    )
                )

            if has_db:
                old_note_path = repo_relative_note_path(move.old_path, root)
                new_note_path = repo_relative_note_path(move.new_path, root)
                db_rekeys.append((old_note_path, new_note_path))

        if has_db and db_rekeys:
            with review_db.connect(db_path) as conn:
                db_counts = [
                    review_db.count_note_path_records(conn, note_path=old)
                    for old, _new in db_rekeys
                ]

        if not export_moves and not db_counts:
            return None
        return ReviewRelocationPlan(
            root=root,
            export_moves=export_moves,
            db_path=db_path,
            db_rekeys=db_rekeys,
            db_counts=db_counts,
        )

    def describe(self, plan: object) -> list[str]:
        assert isinstance(plan, ReviewRelocationPlan)
        lines: list[str] = []
        if not plan.export_moves:
            lines.append("Review exports: none")
        elif len(plan.export_moves) == 1:
            move = plan.export_moves[0]
            lines.append(
                "Review exports:"
                f" {move.source_dir.relative_to(plan.root)} -> {move.destination_dir.relative_to(plan.root)}"
            )
            lines.append(
                f"Review export files to rewrite: {len(move.file_updates)}"
            )
        else:
            lines.append(f"Review export directories to move: {len(plan.export_moves)}")

        if not plan.db_counts:
            lines.append("Review DB updates: none")
        else:
            run_sum = sum(count.review_runs for count in plan.db_counts)
            gate_sum = sum(count.gate_reviews for count in plan.db_counts)
            ack_sum = sum(count.acceptance_events for count in plan.db_counts)
            label = (
                "Review DB rekeys"
                if len(plan.db_counts) > 1
                else "Review DB updates"
            )
            lines.append(
                f"{label}: review_runs={run_sum}, gate_reviews={gate_sum}, "
                f"acceptance_events={ack_sum}"
            )
        return lines

    def execute(self, plan: object) -> None:
        assert isinstance(plan, ReviewRelocationPlan)
        for export_move in plan.export_moves:
            move_path(
                export_move.source_dir,
                export_move.destination_dir,
                repo_root=plan.root,
            )
            for _source, (target, content) in export_move.file_updates.items():
                target.write_text(content, encoding="utf-8")

        if plan.db_rekeys:
            with review_db.connect(plan.db_path) as conn:
                for old, new in plan.db_rekeys:
                    review_db.rekey_note_path(conn, old_note_path=old, new_note_path=new)
                conn.commit()

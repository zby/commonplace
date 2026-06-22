"""Review-system relocation hook."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from commonplace.lib.relocation import NotePathMove
from commonplace.review import review_db


@dataclass(frozen=True)
class ReviewRelocationPlan:
    root: Path
    db_path: Path
    db_rekeys: list[tuple[str, str]]
    db_counts: list[Any]


def repo_relative_note_path(note_path: Path, root: Path) -> str:
    return note_path.relative_to(root).as_posix()


class ReviewRelocationHook:
    """Relocation hook that rekeys review DB rows."""

    def plan(
        self,
        *,
        root: Path,
        moves: Sequence[NotePathMove],
    ) -> ReviewRelocationPlan | None:
        db_rekeys: list[tuple[str, str]] = []
        db_counts: list[Any] = []
        db_path = review_db.resolve_db_path(root)
        has_db = db_path.exists()

        for move in moves:
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

        if not db_counts:
            return None
        return ReviewRelocationPlan(
            root=root,
            db_path=db_path,
            db_rekeys=db_rekeys,
            db_counts=db_counts,
        )

    def describe(self, plan: object) -> list[str]:
        assert isinstance(plan, ReviewRelocationPlan)
        lines: list[str] = []
        if not plan.db_counts:
            lines.append("Review DB updates: none")
        else:
            pair_sum = sum(count.review_pairs for count in plan.db_counts)
            ack_sum = sum(count.acceptance_events for count in plan.db_counts)
            label = (
                "Review DB rekeys"
                if len(plan.db_counts) > 1
                else "Review DB updates"
            )
            lines.append(
                f"{label}: review_pairs={pair_sum}, "
                f"acceptance_events={ack_sum}"
            )
        return lines

    def execute(self, plan: object) -> None:
        assert isinstance(plan, ReviewRelocationPlan)
        if plan.db_rekeys:
            with review_db.connect(plan.db_path) as conn:
                for old, new in plan.db_rekeys:
                    review_db.rekey_note_path(conn, old_note_path=old, new_note_path=new)
                conn.commit()

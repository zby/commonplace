from __future__ import annotations

import importlib.util
import csv
import sys
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[2] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


summarize_reviews = load_module(
    "summarize_reviews",
    SCRIPTS_DIR / "summarize_reviews.py",
)


def make_review(note: str, findings: list[tuple[str, str, str]]) -> summarize_reviews.NoteReview:
    review = summarize_reviews.NoteReview(note=note, review_type="semantic-review")
    for level, check, text in findings:
        review.findings.append(
            summarize_reviews.Finding(
                note=note,
                check=check,
                text=text,
                review_type="semantic-review",
                level=level,
            )
        )
    return review


def test_build_tables_orders_rows_for_orchestrator() -> None:
    reviews = [
        make_review(
            "b.md",
            [
                ("WARN", "Completeness", "b warn 1"),
                ("WARN", "Grounding", "b warn 2"),
                ("INFO", "Completeness", "b info"),
            ],
        ),
        make_review(
            "a.md",
            [
                ("WARN", "Completeness", "a warn"),
            ],
        ),
        make_review(
            "c.md",
            [
                ("INFO", "Style", "c info"),
            ],
        ),
    ]

    tables = summarize_reviews.build_tables(reviews)

    assert tables.notes_summary_rows[0] == ["b.md", "2", "1", "0"]
    assert tables.notes_summary_rows[1] == ["a.md", "1", "0", "0"]
    assert tables.checks_summary_rows[0][0] == "Completeness"
    assert tables.checks_low_signal_rows[0][0] == "Style"
    assert tables.findings_rows[0][:6] == [
        "b.md",
        "semantic-review",
        "WARN",
        "2",
        "2",
        "Completeness",
    ]


def test_build_markdown_only_uses_top_five_rows() -> None:
    reviews = []
    for index in range(6):
        reviews.append(
            make_review(
                f"note-{index}.md",
                [("WARN", f"Check-{index}", f"warning {index}")],
            )
        )

    tables = summarize_reviews.build_tables(reviews)
    markdown = summarize_reviews.build_markdown(
        reviews,
        "semantic-review",
        "Semantic Review Sweep",
        tables,
    )

    assert "note-0" in markdown
    assert "note-4" in markdown
    assert "note-5" not in markdown
    assert "Check-5" not in markdown
    assert "## First Findings" not in markdown
    assert "## Low-Yield Checks" in markdown


def test_main_skips_stale_reviews_in_csv_outputs(tmp_path, monkeypatch) -> None:
    reviews_dir = tmp_path / "reviews"
    notes_dir = tmp_path / "kb" / "notes"
    reviews_dir.mkdir(parents=True)
    notes_dir.mkdir(parents=True)

    (notes_dir / "live-note.md").write_text("# Live note\n", encoding="utf-8")

    (reviews_dir / "live-note.semantic-review.md").write_text(
        "=== Semantic Review: live-note.md ===\n"
        "WARN:\n"
        "- [Completeness] live warning\n",
        encoding="utf-8",
    )
    (reviews_dir / "renamed-note.semantic-review.md").write_text(
        "=== Semantic Review: renamed-note.md ===\n"
        "WARN:\n"
        "- [Grounding] stale warning\n",
        encoding="utf-8",
    )

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        sys,
        "argv",
        ["summarize_reviews.py", "semantic-review"],
    )

    summarize_reviews.main()

    notes_by_warnings_path = reviews_dir / "csv" / "semantic-review.notes_by_warnings.csv"
    with notes_by_warnings_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 1
    assert rows[0]["note"] == "live-note.md"

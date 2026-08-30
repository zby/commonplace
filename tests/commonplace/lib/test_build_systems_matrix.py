from __future__ import annotations

from pathlib import Path

from scripts import build_systems_matrix as builder


def test_flags_do_not_replace_the_existing_matrix(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    reviews = tmp_path / "kb" / "agent-memory-systems" / "reviews"
    reviews.mkdir(parents=True)
    (reviews / "incomplete.md").write_text(
        """---
source-tier: code-grounded
---

# Incomplete
""",
        encoding="utf-8",
    )
    matrix = reviews.parent / "systems.csv"
    matrix.write_text("last-complete-matrix\n", encoding="utf-8")

    monkeypatch.setattr(builder, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(builder, "REVIEWS_DIR", reviews)
    monkeypatch.setattr(builder, "SYSTEMS_CSV", matrix)
    monkeypatch.setattr(builder, "RELATED_SYSTEMS", tmp_path / "related-systems")

    assert builder.main() == 1
    assert matrix.read_text(encoding="utf-8") == "last-complete-matrix\n"
    captured = capsys.readouterr()
    assert "flags:" in captured.out
    assert "matrix not written" in captured.err

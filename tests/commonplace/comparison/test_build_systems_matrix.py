from pathlib import Path

import pytest

from scripts import build_systems_matrix as builder
from scripts import render_systems_table as renderer


@pytest.mark.parametrize(
    "module, message",
    [(builder, "matrix not written"), (renderer, "table not written")],
)
def test_incomplete_main_review_preserves_existing_output(
    tmp_path: Path, monkeypatch, capsys, module, message
):
    review = tmp_path / "kb/agentic-systems/reviews/incomplete.md"
    review.parent.mkdir(parents=True)
    review.write_text(
        "---\ngenerated-by: analyse-agentic-system\nanalysis-run: AAS-2026-09-04-incomplete-01\n---\n\n# Incomplete\n"
    )
    output = tmp_path / "incumbent"
    output.write_text("last complete output\n")
    monkeypatch.setattr(module, "REPO_ROOT", tmp_path)
    assert module.main(["--output", str(output)]) == 1
    assert output.read_text() == "last complete output\n"
    assert message in capsys.readouterr().err

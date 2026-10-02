"""Quotation availability at the boundary worker's real scheduling point."""

from pathlib import Path

import pytest

from commonplace.cli.quote import main as quote_main
from commonplace.lib import agentic_publication
from commonplace.workflow import Done, Handout
from tests.commonplace.lib.test_agentic_workflow import Fixture, github_agent

pytestmark = pytest.mark.usefixtures("tmp_library")


@pytest.mark.parametrize("retry", [False, True])
def test_boundary_can_ground_quotes_before_submitting_its_result(
    tmp_path: Path, monkeypatch, capsys, retry: bool,
) -> None:
    monkeypatch.setattr(agentic_publication, "running_package_root", lambda: tmp_path)
    fixture = Fixture(tmp_path)
    fixture.on_github()
    selection = fixture.scratch / "selection.txt"
    selection.write_text("# Frozen source", encoding="utf-8")
    quotations = []

    def boundary(handout: Handout) -> None:
        assert quote_main([
            str(fixture.run_dir / "run-state.md"),
            "--source-path", "README.md", "--text-file", str(selection),
        ], cwd=fixture.root) == 0
        citation = capsys.readouterr().out
        assert "# Frozen source" in citation and fixture.revision in citation
        quotations.append(citation)
        changes = {"analysis-cutoff": None} if retry and handout.attempt == 1 else {}
        handout.output_path.write_text(fixture.boundary(**changes) + "\n" + citation)

    scripted, definition = github_agent(fixture, fixture.revision, boundary=boundary)

    assert isinstance(scripted.run()[-1], Done)
    assert len(quotations) == (2 if retry else 1)
    assert len(set(quotations)) == 1
    assert definition.publications == 1

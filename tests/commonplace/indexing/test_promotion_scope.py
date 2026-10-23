from pathlib import Path

import pytest

from commonplace.cli.promotion_candidates import main
from commonplace.lib.note_parser import find_markdown_links
from commonplace.lib.promotion import write_promotion_candidates_report


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


def test_promotion_reports_are_scoped_and_links_resolve_for_arbitrary_collections(tmp_path: Path):
    reports = []
    for name in ("claims", "teams/claims", "manuals"):
        root = tmp_path / "kb" / name
        write(root / "COLLECTION.md", "---\ntype: types/collection-contract.md\n---\n# Contract\n")
        raw = write(root / "capture.md", "# Capture\n")
        source = write(root / "source.md", "# Source\n\n[Capture](./capture.md)\n")
        write(root / "captured/.commonplace-validation-ignore", "")
        write(root / "captured/pinned.md", "# Not a candidate\n")
        result = write_promotion_candidates_report(tmp_path, name)
        reports.append(result.output)
        assert result.text_count == 2
        report = result.output.read_text()
        assert f"Collection: `kb/{name}`" in report
        assert "**1 links in**" in report
        assert {(result.output.parent / link).resolve() for link in find_markdown_links(report)} == {
            raw, source,
        }
    assert len(set(reports)) == 3
    assert all(path.exists() for path in reports)


def test_invalid_scope_writes_no_promotion_report(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert main(["missing"]) == 1
    assert not (tmp_path / "kb/reports").exists()
    with pytest.raises(SystemExit) as exc:
        main([])
    assert exc.value.code == 2

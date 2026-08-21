from __future__ import annotations

from pathlib import Path

import yaml

from commonplace.cli import validate_notes
from commonplace.lib.validation import validate_redirect_map


def write_config(root: Path, redirect_maps: dict[str, str]) -> None:
    config = {
        "docs_dir": "kb",
        "plugins": [{"redirects": {"redirect_maps": redirect_maps}}],
    }
    (root / "properdocs.yml").write_text(
        yaml.safe_dump(config, sort_keys=False), encoding="utf-8"
    )


def write_page(root: Path, relative_path: str) -> None:
    path = root / "kb" / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# Page\n", encoding="utf-8")


def test_redirect_map_validation_skips_absent_config(tmp_path: Path) -> None:
    results = validate_redirect_map(repo_root=tmp_path)

    assert results.fails == []
    assert results.passes == []
    assert results.infos == [
        "[repository] properdocs.yml: not configured; redirect validation skipped"
    ]


def test_redirect_map_validation_accepts_resolving_flat_map(tmp_path: Path) -> None:
    write_page(tmp_path, "notes/current.md")
    write_config(tmp_path, {"notes/old.md": "notes/current.md"})

    results = validate_redirect_map(repo_root=tmp_path)

    assert results.fails == []
    assert "[repository] redirect targets: all 1 resolve" in results.passes
    assert "[repository] redirect keys: none shadow live pages" in results.passes
    assert "[repository] redirect topology: flat" in results.passes


def test_redirect_map_validation_reports_missing_target(tmp_path: Path) -> None:
    write_config(tmp_path, {"notes/old.md": "notes/missing.md"})

    results = validate_redirect_map(repo_root=tmp_path)

    assert results.fails == [
        "[repository] redirect target does not exist: "
        "notes/old.md -> notes/missing.md"
    ]


def test_redirect_map_validation_reports_live_key_and_chain(tmp_path: Path) -> None:
    write_page(tmp_path, "notes/old.md")
    write_page(tmp_path, "notes/middle.md")
    write_page(tmp_path, "notes/current.md")
    write_config(
        tmp_path,
        {
            "notes/old.md": "notes/middle.md",
            "notes/middle.md": "notes/current.md",
        },
    )

    results = validate_redirect_map(repo_root=tmp_path)

    assert "[repository] redirect key shadows a live page: notes/old.md" in results.fails
    assert "[repository] redirect key shadows a live page: notes/middle.md" in results.fails
    assert (
        "[repository] redirect chain is not flat: notes/old.md -> notes/middle.md"
        in results.fails
    )


def test_redirects_cli_target_reports_repository_validation(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    write_config(tmp_path, {"notes/old.md": "notes/missing.md"})
    monkeypatch.chdir(tmp_path)

    exit_code = validate_notes.main(["redirects"])
    output = capsys.readouterr().out

    assert exit_code == 1
    assert "=== VALIDATION: properdocs.yml ===" in output
    assert "Type: redirect-map" in output
    assert "notes/old.md -> notes/missing.md" in output


def test_redirects_cli_target_skips_absent_config(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    monkeypatch.chdir(tmp_path)

    exit_code = validate_notes.main(["redirects"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "properdocs.yml: not configured; redirect validation skipped" in output
    assert "Overall: PASS (clean)" in output

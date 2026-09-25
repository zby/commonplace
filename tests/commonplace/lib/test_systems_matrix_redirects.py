from __future__ import annotations

from pathlib import Path

from commonplace.lib.systems_matrix import _redirect_sources, _redirected_link


def test_missing_link_to_a_redirected_path_is_accepted(tmp_path: Path) -> None:
    (tmp_path / "properdocs.yml").write_text(
        "docs_dir: kb\nplugins:\n  - redirects:\n      redirect_maps:\n"
        "        'notes/definitions/old.md': 'notes/definitions/new.md'\n",
        encoding="utf-8",
    )
    source = tmp_path / "kb" / "reports" / "retained" / "run" / "result.md"
    _redirect_sources.cache_clear()

    assert _redirected_link(
        "link health: missing target ../../../notes/definitions/old.md", source, tmp_path
    )
    assert not _redirected_link(
        "link health: missing target ../../../notes/definitions/gone.md", source, tmp_path
    )
    assert not _redirected_link("description: too short", source, tmp_path)

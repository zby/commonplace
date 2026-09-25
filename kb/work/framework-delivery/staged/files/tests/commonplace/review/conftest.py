"""Review tests build a repository in tmp_path that is its own Commonplace library.

In the source checkout the library is the repository's kb/; these fixtures
reproduce that layout. Tests build the repository at tmp_path or tmp_path/"repo"
during the test, so the library root is chosen when it is first needed.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib import library


@pytest.fixture(autouse=True)
def _test_repository_is_the_library(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    def root(_override: str | None) -> Path:
        for candidate in (tmp_path / "repo" / "kb", tmp_path / "kb"):
            if candidate.is_dir():
                return candidate.resolve()
        return (tmp_path / "kb").resolve()

    monkeypatch.setattr(library, "_library_root", root)

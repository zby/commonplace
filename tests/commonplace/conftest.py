from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib import library


@pytest.fixture
def tmp_library(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Make tmp_path/kb the library, as a source checkout's kb/ is.

    For tests whose temporary repository carries its own global types: a type
    value such as types/note.md must name one file (ADR 088).
    """
    monkeypatch.setenv(library.LIBRARY_ENV, str(tmp_path / "kb"))

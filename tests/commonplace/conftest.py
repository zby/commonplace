from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib import library
from tests.commonplace.platforms import ANALYSIS_TESTS_SKIPPED

# These modules import the analysis code at load time, so they are ignored, not skipped.
collect_ignore = [
    "agentic_analysis",
    "comparison/test_build_systems_matrix.py",
    "comparison/test_comparison_consumers.py",
] if ANALYSIS_TESTS_SKIPPED else []


@pytest.fixture
def tmp_library(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Make tmp_path/kb the library, as a source checkout's kb/ is.

    For tests whose temporary repository carries its own global types: a type
    value such as types/note.md must name one file (ADR 088).
    """
    monkeypatch.setenv(library.LIBRARY_ENV, str(tmp_path / "kb"))

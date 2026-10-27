from __future__ import annotations

import sys

import pytest

# The agentic-system-analyses collection is this repository's own; it is built
# and read on Linux only, because its code locks files with fcntl. Windows skips
# the tests that build or read it.
ANALYSIS_TESTS_SKIPPED = sys.platform == "win32"

analysis_linux_only = pytest.mark.skipif(
    ANALYSIS_TESTS_SKIPPED, reason="agentic-system-analyses is built and read on Linux only"
)

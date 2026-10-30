from __future__ import annotations

import sys

# Agentic analysis runs on Linux only: its sandbox, publication lock and
# worktrees are Linux-bound. Windows ignores the tests that build or publish
# analyses; tests that only read analysis artifacts run everywhere.
ANALYSIS_TESTS_SKIPPED = sys.platform == "win32"

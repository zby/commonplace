"""Scan explicit Claude Code traces using the same scanner as the analysis workflow.

This source-checkout wrapper needs only Python's standard library.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from commonplace.lib.agentic_analysis.claude_code_tool_failures import main

if __name__ == "__main__":
    raise SystemExit(main())

"""Revise notes with headless workers: `commonplace-revise`, the only review and editing command that writes a note.

The parsers and the handlers live in `commonplace.cli.review_workflows`, which
documents both commands; this module is the entry point.
"""

from __future__ import annotations

import sys

from commonplace.cli.review_workflows import revise_main as main

__all__ = ["main"]

if __name__ == "__main__":
    sys.exit(main())

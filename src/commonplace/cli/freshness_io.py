"""Shared helpers for freshness CLI commands."""

from __future__ import annotations

import sys
from pathlib import Path

from commonplace.freshness.transitions import load_json_input


def read_input_payload(path: str) -> dict[str, object]:
    if path == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path).read_text(encoding="utf-8")
    return load_json_input(raw)
"""Time helpers for review state."""

from __future__ import annotations

from datetime import datetime


def iso_now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")

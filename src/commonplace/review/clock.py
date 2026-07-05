"""Time helpers for review state.

All review-state timestamps come from this one clock and are UTC. Stored
timestamps are compared lexically (latest-review selection, warn selection),
which is only chronological when every value shares one fixed offset.
"""

from __future__ import annotations

from datetime import UTC, datetime


def iso_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")

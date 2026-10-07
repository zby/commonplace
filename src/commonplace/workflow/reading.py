"""Reading batches: bounded reads a hand-out suggests to its worker."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

READ_BATCH_BYTES = 24 * 1024
"""Shared byte budget for input batches and line ranges.

Keep below the harness's tool-result delivery limit, leaving room for wrappers.
Change this constant to tune both grouping and range hints together. Workers
must still recover actual truncation; the budget is not a delivery guarantee.
"""


def reading_batches(paths: Sequence[str]) -> list[list[str]]:
    """Suggest bounded reads without copying files or changing dependencies.

    Oversized or not-yet-produced inputs are read separately, in ranges.
    """
    batches: list[list[str]] = []
    batch: list[str] = []
    size = 0
    for path in paths:
        file = Path(path)
        count = file.stat().st_size if file.is_file() else READ_BATCH_BYTES + 1
        if batch and size + count > READ_BATCH_BYTES:
            batches.append(batch)
            batch, size = [], 0
        if count > READ_BATCH_BYTES:
            batches.append([f"{path} — read in bounded ranges"])
        else:
            batch.append(path)
            size += count
    if batch:
        batches.append(batch)
    return batches


def reading_ranges(path: Path) -> list[tuple[int, int]]:
    """Line ranges fitting the read budget; an oversized line stands alone."""
    ranges = []
    start = 1
    size = 0
    end = 0
    with path.open("rb") as source:
        for end, line in enumerate(source, 1):
            if size and size + len(line) > READ_BATCH_BYTES:
                ranges.append((start, end - 1))
                start, size = end, 0
            size += len(line)
    if end:
        ranges.append((start, end))
    return ranges

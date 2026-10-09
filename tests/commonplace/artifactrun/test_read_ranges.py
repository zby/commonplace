"""Oversized-input hints cover the file without overflowing ordinary ranges."""

from pathlib import Path

import pytest

from commonplace.lib.reading_batches import READ_BATCH_BYTES, reading_ranges


@pytest.mark.parametrize(("content", "expected"), [
    (b"", None),
    (b"one line", None),
    (("Unicode: \u0105\u00f3\u017c\n" * 1400).encode(), None),
    (b"a" * (READ_BATCH_BYTES + 20) + b"\nsmall\n", None),
    (b"a\r\n" * 5000, None),
    (b"Contract line\n" * 1000, [(1, 1000)]),  # moderate input stays one call
])
def test_read_ranges_preserve_all_lines_and_bound_multiple_line_reads(
    tmp_path: Path, content: bytes, expected: list | None,
) -> None:
    path = tmp_path / "input.md"
    path.write_bytes(content)
    lines = content.splitlines(keepends=True)
    ranges = reading_ranges(path)

    assert [number for start, end in ranges for number in range(start, end + 1)] == (
        list(range(1, len(lines) + 1))
    )
    for start, end in ranges:
        assert sum(len(line) for line in lines[start - 1:end]) <= READ_BATCH_BYTES or start == end
    if expected is not None:
        assert ranges == expected

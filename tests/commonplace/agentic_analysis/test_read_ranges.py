"""Reading hints over content known before the files exist: batches and ranges."""

import pytest

from commonplace.lib.agentic_analysis.workflow import READ_BATCH_BYTES, batches, ranges


@pytest.mark.parametrize(("content", "expected"), [
    (b"", None),
    (b"one line", None),
    (("Unicode: ąóż\n" * 1400).encode(), None),
    (b"a" * (READ_BATCH_BYTES + 20) + b"\nsmall\n", None),
    (b"a\r\n" * 5000, None),
    (b"Contract line\n" * 1000, [(1, 1000)]),  # moderate input stays one call
])
def test_ranges_preserve_all_lines_and_bound_multiple_line_reads(content: bytes, expected: list | None) -> None:
    lines = content.splitlines(keepends=True)
    result = ranges(content)

    assert [number for start, end in result for number in range(start, end + 1)] == (
        list(range(1, len(lines) + 1))
    )
    for start, end in result:
        assert sum(len(line) for line in lines[start - 1:end]) <= READ_BATCH_BYTES or start == end
    if expected is not None:
        assert result == expected


def test_batches_keep_order_bound_each_batch_and_isolate_oversized_inputs() -> None:
    half = b"x" * (READ_BATCH_BYTES // 2)
    sized = [("a.md", half), ("b.md", half), ("c.md", b"y"),
             ("big.md", b"z" * (READ_BATCH_BYTES + 1)), ("d.md", b"w")]
    assert batches(sized) == [["a.md", "b.md"], ["c.md"], ["big.md — read in bounded ranges"], ["d.md"]]
    assert batches([]) == []

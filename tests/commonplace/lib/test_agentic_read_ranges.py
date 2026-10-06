"""Oversized-input hints cover the file without overflowing ordinary ranges."""

from pathlib import Path

import pytest

from commonplace.lib.agentic_workflow import (
    READ_BATCH_BYTES,
    AnalyseAgenticSystem,
    reading_ranges,
)


@pytest.mark.parametrize("content", [
    b"",
    b"one line",
    ("Unicode: \u0105\u00f3\u017c\n" * 1400).encode(),
    b"a" * (READ_BATCH_BYTES + 20) + b"\nsmall\n",
    b"a\r\n" * 5000,
])
def test_read_ranges_preserve_all_lines_and_bound_multiple_line_reads(
    tmp_path: Path, content: bytes,
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


def test_read_ranges_keep_a_moderate_input_in_one_call(tmp_path: Path) -> None:
    path = tmp_path / "input.md"
    content = b"Contract line\n" * 1000
    assert 6 * 1024 < len(content) < READ_BATCH_BYTES
    path.write_bytes(content)

    assert reading_ranges(path) == [(1, 1000)]


def test_invocation_names_ranges_for_oversized_method_and_task_inputs(tmp_path: Path) -> None:
    instruction = tmp_path / "runtime.md"
    instruction.write_text("Follow the worker rules.\n")
    rules = tmp_path / "worker-rules.md"
    rules.write_text("Method\n" * (READ_BATCH_BYTES // 7 + 1))
    task = tmp_path / "boundary.md"
    task.write_text("Input\n" * (READ_BATCH_BYTES // 6 + 1))
    definition = AnalyseAgenticSystem({
        "system": "Example", "source": "capture", "source-identity": "capture",
        "model": "fixture-model",
    })
    definition.jobs_dir = tmp_path

    job = definition.job(tmp_path, "runtime", "result.md", reads={"boundary": "boundary.md"})

    for path in (rules, task):
        spans = "; ".join(f"{start}-{end}" for start, end in reading_ranges(path))
        assert f"- {path}: lines {spans}" in job.prompt
    assert "Read each range in a separate tool call" in job.prompt
    assert str(instruction) in job.inputs
    assert str(rules) in job.inputs
    assert str(task) in job.inputs

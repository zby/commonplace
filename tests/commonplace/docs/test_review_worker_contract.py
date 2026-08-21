"""Keep reviewer dispatch at the one-prompt architecture boundary."""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]


def test_review_worker_dispatch_contains_only_the_prompt_path() -> None:
    instruction = (REPO_ROOT / "kb/instructions/run-review-batches.md").read_text(
        encoding="utf-8"
    )
    delegate_section = instruction.split("## Delegate jobs", 1)[1].split(
        "## Finalize completed jobs", 1
    )[0]

    task_blocks = re.findall(r"```text\n(.*?)\n```", delegate_section, re.DOTALL)

    assert task_blocks == ["Read {prompt_path} and follow it exactly."]


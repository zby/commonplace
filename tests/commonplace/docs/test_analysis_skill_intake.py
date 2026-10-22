"""Keep the coordinator's lightweight target check ahead of run preparation."""
from __future__ import annotations

import re
from pathlib import Path

import pytest

SKILL = Path(__file__).resolve().parents[3] / (
    "kb/agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md"
)


def intake() -> str:
    text = SKILL.read_text()
    return text.split("## Confirm the target\n", 1)[1].split("## Isolated run setup\n", 1)[0]


def test_missing_target_requires_an_answer_before_preparation():
    text = intake()
    assert "Which system" in text
    assert "Stop\nand wait for the answer." in text
    assert "Do not select a system from prior analyses" in text
    assert "Do not run\n`git ls-remote`, clone, fetch or test credentials during intake." in text
    assert "local checkout" in text and "snapshot, bundle or documents" in text


def test_profile_defaults_to_pi_sol_but_resumes_keep_their_profile():
    text = intake()
    assert "Use **`pi-sol`** (`gpt-6.1-sol`, medium effort)" in text
    assert "An explicit profile overrides the default." in text
    assert "A resumed run always keeps its\nrecorded profile" in text
    assert "ask which profile" not in text


def test_preparation_label_correction_is_not_general_setup_recovery():
    text = " ".join(SKILL.read_text().split("## Isolated run setup\n", 1)[1].split("## 1. Run the analysis", 1)[0].split())
    assert "only lowercase letters, digits and hyphens" in text
    assert "starting with a letter or digit (`[a-z0-9][a-z0-9-]*`)" in text
    assert 'use `--name ace` here and `--system "ACE"`' in text
    assert "For a label-only rejection, you may correct only `--name` and retry without operator escalation" in text
    assert "only before any worktree or run has been created" in text
    assert "with the target, source and scope unchanged" in text
    assert "For every other preparation failure, stop" in text
    assert "do not retry automatically" in text
    assert "Do not start a run in the originating checkout" in text
    assert "If preparation fails, stop" not in text


@pytest.mark.parametrize("locator,accepted", [
    ("https://github.com/owner/repo", True),
    ("https://github.com/owner/repo.git/", True),
    ("git@github.com:owner/repo.git", True),
    ("ssh://git@example.org/owner/repo.git", True),
    ("", False),
    ("system-name", False),
    ("https://github.com/owner", False),
    ("https://github.com/owner/repo/issues/1", False),
    ("https://github.com/owner/repo/blob/main/README.md", False),
    ("https://github.com/owner/repo?tab=readme", False),
    ("https://github.com/owner/repo#readme", False),
    ("https://github.com/owner/repo name", False),
])
def test_remote_repository_shape_check(locator, accepted):
    pattern = re.search(r"```regex\n([^\n]+)\n```", intake()).group(1)
    assert bool(re.fullmatch(pattern, locator)) is accepted

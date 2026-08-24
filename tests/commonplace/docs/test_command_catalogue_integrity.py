"""Keep published Commonplace commands discoverable and their live help safe."""

from __future__ import annotations

import re
import subprocess
import sys
import tomllib
from collections import Counter
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
COMMAND_HEADING_RE = re.compile(r"^### (commonplace-[a-z0-9-]+)\s*$", re.MULTILINE)


def published_commands() -> dict[str, str]:
    with (REPO_ROOT / "pyproject.toml").open("rb") as file:
        configuration = tomllib.load(file)
    return {
        name: target
        for name, target in configuration["project"]["scripts"].items()
        if name.startswith("commonplace-")
    }


PUBLISHED_COMMANDS = published_commands()


def test_every_published_command_has_one_reference_section() -> None:
    headings = COMMAND_HEADING_RE.findall(
        (REPO_ROOT / "kb/reference/commands.md").read_text(encoding="utf-8")
    )
    duplicates = sorted(
        name for name, count in Counter(headings).items() if count > 1
    )

    assert duplicates == [], f"duplicate command headings: {duplicates}"

    documented = set(headings)
    published = set(PUBLISHED_COMMANDS)
    assert documented == published, (
        "command catalogue drift: "
        f"undocumented={sorted(published - documented)}, "
        f"not published={sorted(documented - published)}"
    )


@pytest.mark.parametrize(
    ("command", "entry_point"),
    sorted(PUBLISHED_COMMANDS.items()),
)
def test_every_published_command_has_side_effect_free_help(
    tmp_path: Path,
    command: str,
    entry_point: str,
) -> None:
    module, separator, function = entry_point.partition(":")
    assert (separator, function) == (":", "main")

    result = subprocess.run(
        [sys.executable, "-m", module, "--help"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, (
        f"{command} --help failed:\nstdout={result.stdout}\nstderr={result.stderr}"
    )
    assert "usage:" in result.stdout.lower(), f"{command} has no help usage"
    assert list(tmp_path.iterdir()) == [], f"{command} --help changed the filesystem"

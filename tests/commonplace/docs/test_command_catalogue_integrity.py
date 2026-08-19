"""Keep published Commonplace commands and their reference catalogue aligned."""

from __future__ import annotations

import re
import tomllib
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
COMMAND_HEADING_RE = re.compile(r"^### (commonplace-[a-z0-9-]+)\s*$", re.MULTILINE)


def test_every_published_command_has_one_reference_section() -> None:
    with (REPO_ROOT / "pyproject.toml").open("rb") as file:
        configuration = tomllib.load(file)

    published = {
        name
        for name in configuration["project"]["scripts"]
        if name.startswith("commonplace-")
    }
    headings = COMMAND_HEADING_RE.findall(
        (REPO_ROOT / "kb/reference/commands.md").read_text(encoding="utf-8")
    )
    duplicates = sorted(
        name for name, count in Counter(headings).items() if count > 1
    )

    assert duplicates == [], f"duplicate command headings: {duplicates}"

    documented = set(headings)
    assert documented == published, (
        "command catalogue drift: "
        f"undocumented={sorted(published - documented)}, "
        f"not published={sorted(documented - published)}"
    )

"""Parse markdown frontmatter with a thin YAML wrapper.

Frontmatter sits between ``---`` delimiters at the start of a markdown
file. Delimiter handling stays local; the contents are parsed with
``yaml.safe_load``.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

import yaml


@dataclass
class FrontmatterResult:
    """Parsed frontmatter with optional diagnostics."""

    data: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


_FM_RE = re.compile(r"^---\n(.*?)\n---(?:\n|$)", re.DOTALL)


def parse(content: str) -> FrontmatterResult:
    match = _FM_RE.match(content)
    if match is None:
        if content.startswith("---\n"):
            return FrontmatterResult(errors=["frontmatter: missing closing delimiter"])
        return FrontmatterResult()

    raw = match.group(1)
    result = FrontmatterResult()
    try:
        loaded = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        result.errors.append(str(exc))
        return result

    if loaded is None:
        return result
    if not isinstance(loaded, dict):
        result.errors.append("frontmatter must parse to a mapping")
        return result

    result.data = loaded

    return result


def strip(content: str) -> str:
    match = _FM_RE.match(content)
    if match is None:
        return content
    return content[match.end() :]

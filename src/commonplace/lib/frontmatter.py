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


# CRLF-tolerant: a note saved with Windows line endings must parse as
# frontmatter, not silently fall through to the untyped-text path.
_FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?(?:\n|$)", re.DOTALL)
_FM_OPEN_RE = re.compile(r"^---\r?\n")


def opens_frontmatter(content: str) -> bool:
    """True when content starts with a frontmatter opening delimiter."""
    return _FM_OPEN_RE.match(content) is not None


def parse(content: str) -> FrontmatterResult:
    match = _FM_RE.match(content)
    if match is None:
        if opens_frontmatter(content):
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

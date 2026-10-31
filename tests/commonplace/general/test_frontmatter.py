from __future__ import annotations

import pytest
import yaml

from commonplace.lib import frontmatter


@pytest.mark.parametrize("python_loader", [False, True])
def test_safe_loaders_reject_python_object_tags(monkeypatch, python_loader) -> None:
    if python_loader:
        monkeypatch.delattr(yaml, "CSafeLoader", raising=False)
    result = frontmatter.parse("---\nvalue: !!python/tuple [one, two]\n---\n")

    assert not result.ok
    assert result.data == {}


def test_parse_requires_frontmatter_to_be_mapping() -> None:
    result = frontmatter.parse("---\n- not\n- a\n- mapping\n---\n")

    assert result.errors == ["frontmatter must parse to a mapping"]


def test_parse_accepts_crlf_line_endings() -> None:
    result = frontmatter.parse(
        "---\r\n"
        "description: Windows note\r\n"
        "type: kb/types/note.md\r\n"
        "---\r\n"
        "# Title\r\n"
    )

    assert result.data == {
        "description": "Windows note",
        "type": "kb/types/note.md",
    }


def test_strip_removes_crlf_frontmatter_block() -> None:
    content = "---\r\ntype: kb/types/note.md\r\n---\r\n# Title\r\nBody."

    assert frontmatter.strip(content) == "# Title\r\nBody."

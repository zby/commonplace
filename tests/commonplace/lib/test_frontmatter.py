from __future__ import annotations

from commonplace.lib import frontmatter


def test_parse_extracts_mapping_between_delimiters() -> None:
    result = frontmatter.parse(
        "---\n"
        "description: Some description here\n"
        "type: kb/types/note.md\n"
        "---\n"
        "# Title\n"
    )

    assert result.ok
    assert result.data == {
        "description": "Some description here",
        "type": "kb/types/note.md",
    }


def test_parse_without_frontmatter_returns_empty_result() -> None:
    result = frontmatter.parse("# Just a heading\nSome text.\n")

    assert result.ok
    assert result.data == {}


def test_parse_empty_frontmatter_returns_empty_result() -> None:
    result = frontmatter.parse("---\n\n---\n# Title\n")

    assert result.ok
    assert result.data == {}


def test_parse_closing_delimiter_without_trailing_newline() -> None:
    result = frontmatter.parse("---\ndescription: test\n---")

    assert result.ok
    assert result.data == {"description": "test"}


def test_parse_reports_missing_closing_delimiter() -> None:
    result = frontmatter.parse("---\ndescription: test\n# Title\n")

    assert not result.ok
    assert result.data == {}
    assert result.errors == ["frontmatter: missing closing delimiter"]


def test_parse_reports_yaml_errors() -> None:
    result = frontmatter.parse("---\nnot a valid line\ntype: kb/types/note.md\n---\n")

    assert not result.ok
    assert result.data == {}
    assert result.errors


def test_parse_requires_frontmatter_to_be_mapping() -> None:
    result = frontmatter.parse("---\n- not\n- a\n- mapping\n---\n")

    assert not result.ok
    assert result.data == {}
    assert result.errors == ["frontmatter must parse to a mapping"]


def test_parse_accepts_crlf_line_endings() -> None:
    result = frontmatter.parse(
        "---\r\n"
        "description: Windows note\r\n"
        "type: kb/types/note.md\r\n"
        "---\r\n"
        "# Title\r\n"
    )

    assert result.ok
    assert result.data == {
        "description": "Windows note",
        "type": "kb/types/note.md",
    }


def test_strip_removes_crlf_frontmatter_block() -> None:
    content = "---\r\ntype: kb/types/note.md\r\n---\r\n# Title\r\nBody."

    assert frontmatter.strip(content) == "# Title\r\nBody."


def test_strip_removes_frontmatter_block() -> None:
    content = "---\ntype: kb/types/note.md\n---\n# Title\nBody."

    assert frontmatter.strip(content) == "# Title\nBody."


def test_strip_without_frontmatter_is_noop() -> None:
    content = "# Title\nBody."

    assert frontmatter.strip(content) == content

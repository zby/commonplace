from __future__ import annotations

import pytest

from commonplace.lib.note_parser import (
    find_markdown_links_with_text,
    parse_document,
)


def test_parse_document_extracts_headings_and_excludes_fenced_code() -> None:
    document, error = parse_document(
        """---
description: Example
type: types/note.md
---

# Title

## Kept

```md
## Ignored
```
"""
    )

    assert error is None
    assert document is not None
    assert document.headings == ("# Title", "## Kept")


def test_parse_document_extracts_links_and_body_dates() -> None:
    document, error = parse_document(
        """---
description: Example
type: types/note.md
---

# Title

Reference [one](./one.md)

Date: 2026-04-09
"""
    )

    assert error is None
    assert document is not None
    assert document.links == ("./one.md",)
    assert document.body_dates == ("2026-04-09",)


def test_parse_document_excludes_dates_in_code_regions() -> None:
    document, error = parse_document(
        """# Title

Prose date: 2026-04-09
Inline example: `released: 2026-04-10`

```yaml
released: 2026-04-11
```

Repeated prose date: 2026-04-09
"""
    )

    assert error is None
    assert document is not None
    assert document.body_dates == ("2026-04-09",)


def test_parse_document_excludes_date_shaped_tails_of_longer_tokens() -> None:
    document, error = parse_document(
        """# Title

Cited as https://doi.org/10.1186/1471-2288-13-91 in the bibliography.
See [the record](./records/run-2026-04-10.md) and https://example.org/2026-04-11/post.
Reviewed on 2026-04-09. Range (2026-04-12) ends: 2026-04-13, as planned.
Run AAS-2026-04-14-example-01 covered the deletions of 2026-04-15/16.
"""
    )

    assert error is None
    assert document is not None
    assert document.body_dates == (
        "2026-04-09",
        "2026-04-12",
        "2026-04-13",
        "2026-04-15",
    )


def test_find_markdown_links_with_text_keeps_code_formatted_link_text() -> None:
    links = find_markdown_links_with_text(
        "Reference [`examples/`](../examples/) and `[ignored](./ignored.md)`."
    )

    assert links == (("`examples/`", "../examples/"),)


def test_parse_document_keeps_plain_text_as_no_frontmatter() -> None:
    document, error = parse_document(
        """# Title

Body.
"""
    )

    assert error is None
    assert document is not None
    assert document.frontmatter is None
    assert document.body == "# Title\n\nBody.\n"


def test_parse_document_reports_unclosed_frontmatter() -> None:
    document, error = parse_document(
        """---
description: Example
# Title
"""
    )

    assert document is None
    assert error == "frontmatter: missing closing delimiter"


@pytest.mark.parametrize("opening,inside,closing", [
    ("```md", "``` trailing text\n", "```"),
    ("````md", "```\n", "`````"),
    ("~~~md", "```\n~~~ trailing text\n", "~~~~"),
    ("  ```md", "", "   ```\t"),
])
def test_quote_parsers_share_fences_and_keep_source_lines(opening, inside, closing):
    from commonplace.lib.note_parser import blank_fenced_code_blocks
    from commonplace.lib.quote_matching import parse_blockquotes
    from commonplace.lib.quote_verification import parse_prose_citations

    example = '> hidden\n> --- `doc.md` @ `abc`\n\n"hidden" ([source](doc.md), verbatim).\n'
    prefix = opening + '\n' + inside + example + closing + '\n'
    visible = '> real\n> --- `doc.md` @ `abc`\n\n"real" ([source](doc.md), verbatim).\n'
    content = prefix + visible
    cleaned = blank_fenced_code_blocks(content)
    assert len(cleaned) == len(content)
    assert cleaned.count('\n') == content.count('\n')
    assert cleaned[len(prefix):] == visible
    blocks = parse_blockquotes(content)
    assert [c.quote for c in blocks] == ['real']
    assert blocks[0].line == prefix.count('\n') + 2
    assert [c.quote for c in parse_prose_citations(content)] == ['real']


@pytest.mark.parametrize("prefix", ["```example```\n", "    ```\n"])
def test_non_fence_prefix_does_not_hide_prose(prefix):
    from commonplace.lib.note_parser import blank_fenced_code_blocks

    content = prefix + "Keep this paragraph.\n"
    assert blank_fenced_code_blocks(content) == content


def test_unclosed_fence_hides_examples_through_end_of_document():
    from commonplace.lib.note_parser import blank_fenced_code_blocks
    from commonplace.lib.quote_matching import parse_blockquotes
    from commonplace.lib.quote_verification import parse_prose_citations

    content = '~~~md\n> example\n> --- `doc.md` @ `abc`\n\n"example" ([source](doc.md), verbatim).\n'
    assert not blank_fenced_code_blocks(content).strip()
    assert not parse_blockquotes(content)
    assert not parse_prose_citations(content)

from __future__ import annotations

import sys
from pathlib import Path

SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.lib.note_parser import (
    find_markdown_links_with_text,
    parse_document,
)


def test_parse_document_extracts_headings_and_excludes_fenced_code() -> None:
    document, error = parse_document(
        """---
description: Example
type: kb/types/note.md
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
type: kb/types/note.md
---

# Title

Reference [one](./one.md)
Code-formatted link text: [`examples/`](../examples/)
`[ignored](./ignored.md)`

Date: 2026-04-09
"""
    )

    assert error is None
    assert document is not None
    assert document.links == ("./one.md", "../examples/")
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

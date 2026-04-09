from __future__ import annotations

import sys
from pathlib import Path


SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.lib.note_parser import parse_document


def test_parse_document_extracts_headings_and_excludes_fenced_code() -> None:
    document, error = parse_document(
        """---
description: Example
type: note
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
type: review
---

# Title

Reference [one](./one.md)
`[ignored](./ignored.md)`

Date: 2026-04-09
"""
    )

    assert error is None
    assert document is not None
    assert document.links == ("./one.md",)
    assert document.body_dates == ("2026-04-09",)


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

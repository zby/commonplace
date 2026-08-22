"""Extract the canonical external URL for a source file (snapshot or ingest)."""

from __future__ import annotations

import re
from pathlib import Path

from commonplace.lib import frontmatter

_URL_RE = re.compile(r"https?://\S+")
_SOURCE_LINE_RE = re.compile(r"^\*{0,2}(?:Source|source|From|from):\*{0,2}\s*(.+)$")
_BODY_SCAN_LIMIT = 40


def _strip_url_punctuation(url: str) -> str:
    return url.rstrip(".,);")


def extract_url(source_path: Path) -> str | None:
    """Find the external URL for a source file.

    Resolution order:

    1. Frontmatter ``source: <URL>`` (ingests and local snapshots)
    2. Body lines beginning with ``Source:`` or ``From:`` in the first 40 lines
       (markdown link or bare URL)
    3. First ``http(s)://`` URL in the first 40 lines

    Returns ``None`` if no URL can be derived. The retired
    ``source_snapshot`` pointer is not followed; tracked ingests carry their
    canonical URL directly.
    """
    source_path = source_path.resolve()
    if not source_path.is_file():
        return None

    text = source_path.read_text(encoding="utf-8", errors="replace")
    parsed = frontmatter.parse(text)
    fm = parsed.data if parsed.ok else {}

    # 1. Direct source: URL
    direct = fm.get("source")
    if isinstance(direct, str) and direct.strip().startswith("http"):
        return _strip_url_punctuation(direct.strip())

    # 2 & 3. Body scan
    body = frontmatter.strip(text)
    body_lines = body.splitlines()[:_BODY_SCAN_LIMIT]

    # Pass 1: explicit Source:/From: lines
    for line in body_lines:
        m = _SOURCE_LINE_RE.match(line.strip())
        if m:
            rest = m.group(1)
            paren = re.search(r"\((https?://[^)]+)\)", rest)
            if paren:
                return _strip_url_punctuation(paren.group(1))
            url = _URL_RE.search(rest)
            if url:
                return _strip_url_punctuation(url.group(0))

    # Pass 2: any URL in body
    for line in body_lines:
        m = _URL_RE.search(line)
        if m:
            return _strip_url_punctuation(m.group(0))

    return None

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


def extract_url(
    source_path: Path,
    *,
    repo_root: Path | None = None,
    _seen: set[Path] | None = None,
) -> str | None:
    """Find the external URL for a source file.

    Resolution order:

    1. Frontmatter ``source: <URL>`` (snapshot files)
    2. Follow frontmatter ``source_snapshot: <path>`` to the snapshot, recurse
    3. Body lines beginning with ``Source:`` or ``From:`` in the first 40 lines
       (markdown link or bare URL)
    4. First ``http(s)://`` URL in the first 40 lines

    Returns ``None`` if no URL can be derived. Cycles in
    ``source_snapshot:`` chains are guarded.

    ``repo_root`` is used to resolve ``kb/...``-absolute snapshot pointers;
    if ``None``, only relative pointers are followed.
    """
    if _seen is None:
        _seen = set()
    source_path = source_path.resolve()
    if not source_path.is_file() or source_path in _seen:
        return None
    _seen.add(source_path)

    text = source_path.read_text(encoding="utf-8", errors="replace")
    parsed = frontmatter.parse(text)
    fm = parsed.data if parsed.ok else {}

    # 1. Direct source: URL
    direct = fm.get("source")
    if isinstance(direct, str) and direct.strip().startswith("http"):
        return _strip_url_punctuation(direct.strip())

    # 2. Follow source_snapshot pointer
    snap = fm.get("source_snapshot")
    if isinstance(snap, str):
        snap = snap.strip()
        if snap.startswith("kb/") and repo_root is not None:
            snap_path = repo_root / snap
        else:
            snap_path = source_path.parent / snap
        result = extract_url(snap_path, repo_root=repo_root, _seen=_seen)
        if result:
            return result

    # 3 & 4. Body scan
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

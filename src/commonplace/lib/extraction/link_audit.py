"""Find markdown links across a KB tree, optionally filtered by URL pattern."""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path


_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


@dataclass(frozen=True)
class LinkOccurrence:
    """A markdown link found in a file."""

    file: Path
    line: int  # 1-based
    text: str  # display text
    url: str  # raw URL string


def _is_inside_backticks(line: str, pos: int) -> bool:
    """True if ``pos`` in ``line`` falls inside a backtick code span on the same line.

    Crude heuristic — counts backticks before ``pos``; odd count means
    we're inside a span. Misses multi-line code blocks; that's acceptable
    for the typical case (KB notes, where ``[label](url)`` patterns inside
    fenced blocks are rare).
    """
    return line[:pos].count("`") % 2 == 1


def find_links(
    *,
    roots: Iterable[Path],
    url_pattern: str | re.Pattern[str] | None = None,
    glob: str = "*.md",
    include_backtick_matches: bool = False,
) -> list[LinkOccurrence]:
    """Find markdown links across ``roots``, optionally filtered by URL pattern.

    ``url_pattern`` may be:
      - ``None`` — return all links
      - a string — substring match against the URL
      - a compiled regex — ``re.search`` match against the URL

    By default, links inside backtick code spans on the same line (e.g.
    inline examples like \\`[label](url)\\`) are skipped. Set
    ``include_backtick_matches=True`` to include them.

    Symlinks are skipped.
    """
    if url_pattern is None:
        def matches(url: str) -> bool:
            return True
    elif isinstance(url_pattern, str):
        substr = url_pattern
        def matches(url: str) -> bool:
            return substr in url
    else:
        compiled = url_pattern
        def matches(url: str) -> bool:
            return compiled.search(url) is not None

    out: list[LinkOccurrence] = []
    for root in roots:
        for md in sorted(Path(root).rglob(glob)):
            if md.is_symlink() or not md.is_file():
                continue
            text = md.read_text(encoding="utf-8", errors="replace")
            for lineno, line in enumerate(text.splitlines(), start=1):
                for m in _LINK_RE.finditer(line):
                    if not matches(m.group(2)):
                        continue
                    if not include_backtick_matches and _is_inside_backticks(line, m.start()):
                        continue
                    out.append(
                        LinkOccurrence(
                            file=md,
                            line=lineno,
                            text=m.group(1),
                            url=m.group(2),
                        )
                    )
    return out

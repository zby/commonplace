"""Shared quotation records, attributed-block parsing, and occurrence matching.

Resolvers choose normalization and eligible source regions.
"""

from __future__ import annotations

import html
import re
import unicodedata
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal
from urllib.parse import unquote, urlsplit

Normalization = Literal["prose", "code"]
ATTRIBUTION_RE = re.compile(r"^\s*>\s*---\s*(?P<attribution>.*\S)?\s*$")
LOCAL_SOURCE_RE = re.compile(
    r"`(?P<path>[^`\n]+?)"
    r"(?::(?P<ranges>[0-9]+(?:-[0-9]+)?(?:,[0-9]+(?:-[0-9]+)?)*)?)?`"
    r"\s*@\s*`(?P<version>[^`]+)`"
)
URL_RE = re.compile(r"https?://[^\s<>()`\"']+")


@dataclass(frozen=True)
class Citation:
    quote: str
    source: str | None
    version: str | None = None
    ranges: tuple[tuple[int, int], ...] = ()
    line: int = 1
    attribution: str = ""
    error: str | None = None


def parse_line_ranges(value: str) -> tuple[tuple[int, int], ...]:
    ranges = []
    for item in value.split(","):
        start, separator, end = item.partition("-")
        ranges.append((int(start), int(end) if separator else int(start)))
    return tuple(ranges)


def _attributed_citation(quote: str, attribution: str, line: int) -> Citation:
    local = LOCAL_SOURCE_RE.search(attribution)
    if local:
        return Citation(
            quote,
            local["path"],
            local["version"],
            parse_line_ranges(local["ranges"]) if local["ranges"] else (),
            line,
            attribution,
        )
    url_match = URL_RE.search(attribution)
    if url_match:
        url = url_match[0].rstrip(".,;")
        parsed = urlsplit(url)
        parts = parsed.path.split("/")
        if parsed.hostname == "github.com" and len(parts) > 3 and parts[3] == "blob":
            if len(parts) < 6 or not parts[5]:
                return Citation(
                    quote, url, line=line, error="incomplete GitHub blob path"
                )
            ranges = ()
            if parsed.fragment:
                anchor = re.fullmatch(r"L([0-9]+)(?:-L([0-9]+))?", parsed.fragment)
                if anchor is None:
                    return Citation(
                        quote, url, line=line, error="invalid GitHub line anchor"
                    )
                ranges = ((int(anchor[1]), int(anchor[2] or anchor[1])),)
            return Citation(quote, url, parts[4], ranges, line, attribution)
        return Citation(quote, url, line=line, attribution=attribution)
    return Citation(
        quote,
        None,
        line=line,
        attribution=attribution,
        error="expected a pinned source path or source URL",
    )


def parse_blockquotes(content: str) -> tuple[Citation, ...]:
    """Read attributed blocks, excluding fenced examples and attribution bytes."""
    citations = []
    lines = content.splitlines()
    fence: str | None = None
    for index, line in enumerate(lines):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if marker:
            if fence is None:
                fence = marker[1]
            elif marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue
        match = ATTRIBUTION_RE.fullmatch(line)
        if match is None:
            continue
        quote_lines = []
        cursor = index - 1
        while cursor >= 0 and re.match(r"^\s*>", lines[cursor]):
            if ATTRIBUTION_RE.fullmatch(lines[cursor]):
                break
            quote_lines.append(re.sub(r"^\s*> ?", "", lines[cursor], count=1))
            cursor -= 1
        citations.append(
            _attributed_citation(
                "\n".join(reversed(quote_lines)),
                (match["attribution"] or "").strip(),
                index + 1,
            )
        )
    return tuple(citations)


def git_citation_path(citation: Citation) -> tuple[str, str | None]:
    """Return commit-relative path and optional repository from a parsed citation."""
    source = citation.source or ""
    if source.startswith(("http://", "https://")):
        parsed = urlsplit(source)
        parts = parsed.path.split("/")
        if parsed.hostname != "github.com" or len(parts) < 6 or parts[3] != "blob":
            raise ValueError("expected a commit-pinned GitHub blob URL")
        return unquote("/".join(parts[5:])), f"https://github.com/{parts[1]}/{parts[2]}"
    return source, None


def normalize_text(text: str, kind: Normalization = "prose") -> str:
    if kind == "prose":
        text = html.unescape(unicodedata.normalize("NFKC", text))
        text = text.translate(
            str.maketrans(
                {
                    "‘": "'",
                    "’": "'",
                    "‚": "'",
                    "‛": "'",
                    "“": '"',
                    "”": '"',
                    "„": '"',
                    "‟": '"',
                    "…": "...",
                    "\u00ad": "",
                }
            )
        )
        text = re.sub(r"(?<!\\)(?:\*\*|__)", "", text)
    return " ".join(text.split())


@dataclass(frozen=True)
class QuoteMatch:
    count: int
    error: str | None = None

    @property
    def matched(self) -> bool:
        return self.error is None and self.count == 1


def match_quote(
    quote: str,
    source: str | Sequence[str],
    *,
    kind: Normalization,
    ranges: tuple[tuple[int, int], ...] = (),
) -> QuoteMatch:
    """Require one occurrence, slicing original lines before normalization.

    Separate retained extracts and disjoint ranges remain separate regions:
    concatenation would fabricate passages across their boundaries. Overlapping
    ranges are merged so they cannot count the same occurrence twice.
    """
    regions = [source] if isinstance(source, str) else list(source)
    if ranges:
        if not isinstance(source, str):
            return QuoteMatch(0, "line ranges require one original source")
        lines = source.splitlines()
        if any(start < 1 or end < start or end > len(lines) for start, end in ranges):
            return QuoteMatch(
                0, f"line range is outside source's 1-{len(lines)} lines"
            )
        merged: list[tuple[int, int]] = []
        for start, end in sorted(ranges):
            if merged and start <= merged[-1][1] + 1:
                merged[-1] = (merged[-1][0], max(end, merged[-1][1]))
            else:
                merged.append((start, end))
        regions = ["\n".join(lines[start - 1 : end]) for start, end in merged]
    needle = normalize_text(quote, kind)
    if not needle:
        return QuoteMatch(0, "quote body is empty after normalization")
    count = 0
    for region in regions:
        haystack = normalize_text(region, kind)
        offset = haystack.find(needle)
        while offset >= 0:
            count += 1
            offset = haystack.find(needle, offset + 1)
    location = "the cited line range" if ranges else "the source region"
    if count == 0:
        return QuoteMatch(count, f"quote does not occur in {location}")
    if count > 1:
        return QuoteMatch(
            count,
            f"quote occurs {count} times in {location}; "
            "quote more context or supply a range containing one occurrence",
        )
    return QuoteMatch(count)

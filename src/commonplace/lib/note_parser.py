"""Parse markdown notes into a schema-friendly document model."""

from __future__ import annotations

import re
from collections.abc import Callable, Iterator
from copy import deepcopy
from dataclasses import dataclass, replace
from functools import lru_cache
from typing import Any

from commonplace.lib import frontmatter as fm_mod

_BODY_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
_FENCE_LINE_RE = re.compile(r" {0,3}(`{3,}|~{3,})(.*)")
_INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
# A date stands alone: not the tail of a longer hyphenated, slashed, or dotted
# token such as the DOI 10.1186/1471-2288-13-91.
_DATE_RE = re.compile(r"(?<![\w/.-])\d{4}-\d{2}-\d{2}(?![\w-])")


@dataclass(frozen=True)
class ParsedDocument:
    frontmatter: dict[str, Any] | None
    body: str
    headings: tuple[str, ...]
    links: tuple[str, ...]
    body_dates: tuple[str, ...]
    title: str

    def to_validation_object(self) -> dict[str, Any]:
        return {
            "frontmatter": self.frontmatter if self.frontmatter is not None else None,
            "body": self.body,
            "headings": list(self.headings),
            "links": list(self.links),
            "body_dates": list(self.body_dates),
        }


def strip_frontmatter(content: str) -> str:
    return fm_mod.strip(content)


def _fenced_code_spans(text: str) -> Iterator[tuple[int, int]]:
    """Locate top-level fences; inline backticks cannot open or close one."""
    fence: str | None = None
    start = offset = 0
    for line in text.splitlines(keepends=True):
        marker = _FENCE_LINE_RE.fullmatch(line.rstrip("\r\n"))
        if marker:
            run, tail = marker.groups()
            if fence is None:
                # Backtick fence info strings cannot contain backticks.
                if run[0] != "`" or "`" not in tail:
                    fence, start = run, offset
            elif run[0] == fence[0] and len(run) >= len(fence) and not tail.strip(" \t"):
                yield start, offset + len(line)
                fence = None
        offset += len(line)
    if fence is not None:
        yield start, len(text)


def _replace_fenced_code(text: str, *, blank: bool) -> str:
    parts = []
    previous = 0
    for start, end in _fenced_code_spans(text):
        parts.append(text[previous:start])
        if blank:
            parts.append("".join(char if char in "\r\n" else " " for char in text[start:end]))
        previous = end
    parts.append(text[previous:])
    return "".join(parts)


def blank_fenced_code_blocks(text: str) -> str:
    """Neutralize fenced code while preserving every offset and line number.

    Code fences are not note content: a fence demonstrating a convention is
    showing it, not asserting it. Body-content checks must therefore agree on
    what counts as code — see the checks that consume this.

    Blanking rather than deleting is what lets a check report a line number.
    Callers that only need the *set* of matches (link health) are indifferent,
    since a blanked span cannot match a link; callers that pair elements by
    proximity (verbatim-quote resolution) require the offsets to survive. One
    primitive serves both, so the two checks cannot disagree about code.
    """
    return _replace_fenced_code(text, blank=True)


def remove_fenced_code_blocks(text: str) -> str:
    return _replace_fenced_code(text, blank=False)


def remove_code_regions(text: str) -> str:
    text = remove_fenced_code_blocks(text)
    return _INLINE_CODE_RE.sub("", text)


def extract_title(body: str) -> str:
    match = re.search(r"^#\s+(.+)$", body, flags=re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def extract_headings(body: str) -> tuple[str, ...]:
    cleaned = remove_fenced_code_blocks(body)
    headings: list[str] = []
    for match in _BODY_HEADING_RE.finditer(cleaned):
        hashes = match.group(1)
        title = match.group(2).strip()
        headings.append(f"{hashes} {title}")
    return tuple(headings)


def _is_inside_span(start: int, end: int, spans: tuple[tuple[int, int], ...]) -> bool:
    return any(span_start <= start and end <= span_end for span_start, span_end in spans)


def _iter_markdown_link_matches(body: str) -> tuple[re.Match[str], ...]:
    # Import at call time: quotation parsing itself uses the fence lexer here.
    from commonplace.lib.quote_matching import blank_quote_bodies

    cleaned = blank_quote_bodies(blank_fenced_code_blocks(body))
    inline_code_spans = tuple(match.span() for match in _INLINE_CODE_RE.finditer(cleaned))
    return tuple(
        match
        for match in _LINK_RE.finditer(cleaned)
        if not _is_inside_span(match.start(), match.end(), inline_code_spans)
    )


def find_markdown_links(body: str) -> tuple[str, ...]:
    return tuple(match.group(2) for match in _iter_markdown_link_matches(body))


def replace_markdown_links(body: str, replace: Callable[[str], str]) -> str:
    """The body with each link target that `find_markdown_links` finds
    replaced by ``replace(target)``; everything else unchanged."""
    pieces: list[str] = []
    end = 0
    for match in _iter_markdown_link_matches(body):
        start, stop = match.span(2)
        pieces += [body[end:start], replace(body[start:stop])]
        end = stop
    return "".join(pieces) + body[end:]


def find_markdown_links_with_text(body: str) -> tuple[tuple[str, str], ...]:
    return tuple(
        (match.group(1), match.group(2).strip())
        for match in _iter_markdown_link_matches(body)
    )


def extract_body_dates(body: str) -> tuple[str, ...]:
    return tuple(dict.fromkeys(_DATE_RE.findall(remove_code_regions(body))))


def parse_document(content: str) -> tuple[ParsedDocument | None, str | None]:
    """Reuse parsing for unchanged text, without sharing mutable frontmatter.

    Workflow replay validates the same documents repeatedly. Keying by text
    keeps edits visible; the bounded cache does not retain every run's inputs.
    """
    document, error = _parse_document(content)
    if document is not None and document.frontmatter is not None:
        document = replace(document, frontmatter=deepcopy(document.frontmatter))
    return document, error


@lru_cache(maxsize=256)
def _parse_document(content: str) -> tuple[ParsedDocument | None, str | None]:
    frontmatter: dict[str, Any] | None = None
    if fm_mod.opens_frontmatter(content):
        result = fm_mod.parse(content)
        if result.errors:
            return None, "; ".join(result.errors)
        frontmatter = result.data

    body = strip_frontmatter(content)
    return (
        ParsedDocument(
            frontmatter=frontmatter,
            body=body,
            headings=extract_headings(body),
            links=find_markdown_links(body),
            body_dates=extract_body_dates(body),
            title=extract_title(body),
        ),
        None,
    )


def section(body: str, title: str) -> str:
    """The text under one level-two heading, or empty when the heading is absent."""
    match = re.search(rf"(?ms)^## {re.escape(title)}[ \t]*\n(.*?)(?=^## |\Z)", body)
    return match[1] if match else ""

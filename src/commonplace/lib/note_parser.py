"""Parse markdown notes into a schema-friendly document model."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from commonplace.lib import frontmatter as fm_mod


_BODY_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
_FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")


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


def _blank(match: re.Match[str]) -> str:
    """Replace a matched span with same-shaped whitespace, preserving newlines."""
    return "".join("\n" if char == "\n" else " " for char in match.group(0))


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
    return _FENCED_CODE_RE.sub(_blank, text)


def remove_fenced_code_blocks(text: str) -> str:
    return _FENCED_CODE_RE.sub("", text)


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
    cleaned = blank_fenced_code_blocks(body)
    inline_code_spans = tuple(match.span() for match in _INLINE_CODE_RE.finditer(cleaned))
    return tuple(
        match
        for match in _LINK_RE.finditer(cleaned)
        if not _is_inside_span(match.start(), match.end(), inline_code_spans)
    )


def find_markdown_links(body: str) -> tuple[str, ...]:
    return tuple(match.group(2) for match in _iter_markdown_link_matches(body))


def find_markdown_links_with_text(body: str) -> tuple[tuple[str, str], ...]:
    return tuple(
        (match.group(1), match.group(2).strip())
        for match in _iter_markdown_link_matches(body)
    )


def extract_body_dates(body: str) -> tuple[str, ...]:
    return tuple(dict.fromkeys(_DATE_RE.findall(body)))


def parse_document(content: str) -> tuple[ParsedDocument | None, str | None]:
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

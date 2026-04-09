"""Parse markdown notes into a schema-friendly document model."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from commonplace.lib import frontmatter as fm_mod


_BODY_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
_FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
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


def parse_frontmatter(content: str) -> tuple[dict[str, Any] | None, str | None]:
    if not content.startswith("---\n"):
        return None, None

    result = fm_mod.parse(content)
    if result.errors:
        return None, "; ".join(result.errors)
    return result.data, None


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


def find_markdown_links(body: str) -> tuple[str, ...]:
    cleaned = remove_code_regions(body)
    return tuple(_LINK_RE.findall(cleaned))


def extract_body_dates(body: str) -> tuple[str, ...]:
    return tuple(dict.fromkeys(_DATE_RE.findall(body)))


def parse_document(content: str) -> tuple[ParsedDocument | None, str | None]:
    frontmatter, fm_error = parse_frontmatter(content)
    if fm_error:
        return None, fm_error

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

"""Verifier for ``verbatim``-marked Markdown quotations.

A ``verbatim`` citation asserts that a quoted span is copied exactly from a
linked source retained in the KB. That assertion is mechanically decidable —
does string X occur in file Y — so it is a Level A deterministic check, and
leaving it hand-trusted is the state the derived-copy rule forbids.

The checker targets the prose convention used by dialectical/evidential
collections: a quoted span, a ``verbatim`` marker, and a Markdown link to the
source, in one paragraph. It discovers quoted spans near a marker, associates
each with the nearest linked Markdown source, and checks normalized substring
containment. Unclear pairings are reported as ``unresolved`` rather than
guessed, so parser coverage gaps stay visible instead of passing silently.

Three outcomes per candidate:

``match``
    the quote occurs in the linked source
``mismatch``
    the quote does not occur — the ``verbatim`` claim is false
``unresolved``
    no quote could be confidently paired with the citation

``commonplace-validate`` consumes this via :func:`verify_note`; the
``commonplace-verify-quotes`` command reports over a corpus.
"""

from __future__ import annotations

import html
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Sequence

from commonplace.lib.note_parser import blank_fenced_code_blocks


LINK_RE = re.compile(r"\[([^]]*)\]\(([^)]+\.md)(?:#[^)]*)?\)")
VERBATIM_RE = re.compile(r"\bverbatim\b", re.IGNORECASE)
NEGATED_VERBATIM_RE = re.compile(
    r"(?:does\s+not|do\s+not|not|no)\s+(?:\w+\s+){0,3}verbatim"
    r"|verbatim\s+(?:passage|text|detail|quotation|quote)\s+"
    r"(?:was|is|were|are)\s+not",
    re.IGNORECASE,
)
DOUBLE_QUOTE_RE = re.compile(r'"([^"\n]+)"|“([^”\n]+)”')


@dataclass(frozen=True)
class QuoteResult:
    status: str
    note: Path
    line: int
    quote: str | None
    source: Path | None
    detail: str


@dataclass(frozen=True)
class _Link:
    start: int
    end: int
    target: str


@dataclass(frozen=True)
class _Quote:
    start: int
    end: int
    text: str


def normalize_text(text: str) -> str:
    """Normalize capture-level typography without weakening word matching."""

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
    # Markdown emphasis is presentation, not part of a quoted source span.
    text = re.sub(r"(?<!\\)(?:\*\*|__)", "", text)
    return " ".join(text.split())


def _paragraphs(text: str) -> Iterable[tuple[int, str]]:
    raw = [
        (text.count("\n", 0, match.start(1)) + 1, match.group(1))
        for match in re.finditer(
            r"(?:\A|\n\s*\n)(.*?)(?=\n\s*\n|\Z)", text, re.DOTALL
        )
        if match.group(1).strip()
    ]
    index = 0
    while index < len(raw):
        line, paragraph = raw[index]
        if (
            paragraph.lstrip().startswith(">")
            and index + 1 < len(raw)
            and raw[index + 1][1].lstrip().startswith("(")
            and LINK_RE.search(raw[index + 1][1])
        ):
            paragraph = f"{paragraph}\n\n{raw[index + 1][1]}"
            index += 1
        yield line, paragraph
        index += 1


def _links(paragraph: str) -> list[_Link]:
    return [
        _Link(match.start(), match.end(), match.group(2))
        for match in LINK_RE.finditer(paragraph)
    ]


def _citation_ranges(paragraph: str, links: Sequence[_Link]) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    for link in links:
        start = paragraph.rfind("(", 0, link.start)
        end = paragraph.find(")", link.end)
        if start >= 0 and end >= 0:
            ranges.append((start, end + 1))
    return ranges


def _quotes(paragraph: str, links: Sequence[_Link]) -> list[_Quote]:
    found: list[_Quote] = []
    excluded = [(link.start, link.end) for link in links] + _citation_ranges(paragraph, links)
    for match in DOUBLE_QUOTE_RE.finditer(paragraph):
        if any(start <= match.start() < end for start, end in excluded):
            continue
        # Quoted titles commonly occur inside bold lead-ins before the actual
        # evidence quotation; they are labels, not verbatim source spans.
        if paragraph.count("**", 0, match.start()) % 2 == 1:
            continue
        text = match.group(1) if match.group(1) is not None else match.group(2)
        if text and text.strip():
            found.append(_Quote(match.start(), match.end(), text.strip()))
    return found


def _nearest_link(quote: _Quote, links: Sequence[_Link]) -> tuple[_Link | None, bool]:
    if not links:
        return None, False

    def distance(link: _Link) -> int:
        if link.start >= quote.end:
            return link.start - quote.end
        return quote.start - link.end

    # Citations conventionally follow their quotation. Prefer that direction
    # so a quote at the start of the next list item is not captured by the
    # preceding item's nearby citation.
    following = [link for link in links if link.start >= quote.end]
    ordered = sorted(following or list(links), key=distance)
    ambiguous = len(ordered) > 1 and distance(ordered[0]) == distance(ordered[1])
    return ordered[0], ambiguous


def _marker_is_confident(paragraph: str, quote: _Quote, link: _Link) -> bool:
    """Return whether local prose explicitly marks this quote as verbatim."""

    def positive_marker(text: str) -> bool:
        return bool(VERBATIM_RE.search(text) and not NEGATED_VERBATIM_RE.search(text))

    # Support ``verbatim: "quote"`` and ``states, verbatim, that ...`` without
    # borrowing a marker from an earlier sentence in the same paragraph.
    before = paragraph[max(0, quote.start - 120) : quote.start]
    before = re.split(r"[.!?]\s+", before)[-1]
    if positive_marker(before):
        return True

    if quote.end <= link.start:
        between = paragraph[quote.end : link.start]
        # A later sentence's citation belongs to that later quotation, not this
        # one. Multiple quotations joined inside one sentence remain supported.
        another_quote = DOUBLE_QUOTE_RE.search(between)
        if re.search(r"[.!?]\s+", between) or (
            another_quote and quote.text.rstrip().endswith((".", "!", "?"))
        ):
            return False
        citation_tail = paragraph[link.end : min(len(paragraph), link.end + 120)]
        for start, end in _citation_ranges(paragraph, [link]):
            if start <= link.start < end:
                citation_tail = paragraph[link.end:end]
                break
        return positive_marker(between + citation_tail)

    # Less common prefix form: ``verbatim in [source]: "quote"``.
    between = paragraph[link.end : quote.start]
    if re.search(r"[.!?]\s+", between):
        return False
    return positive_marker(paragraph[max(0, link.start - 80) : quote.start])


def verify_content(
    content: str,
    note: Path,
    *,
    load_source: Callable[[Path], str] | None = None,
) -> list[QuoteResult]:
    """Verify verbatim quotations in already-read note content.

    Code fences are neutralized through the shared parser primitive, so this
    check and link health agree on what counts as code: a fence *demonstrating*
    the citation convention is showing it, not asserting it, and scanning one
    would report a false mismatch against whatever source the example links.
    """
    if load_source is None:

        def load_source(path: Path) -> str:
            return path.read_text(encoding="utf-8")

    text = blank_fenced_code_blocks(content)
    results: list[QuoteResult] = []

    for start_line, paragraph in _paragraphs(text):
        if not VERBATIM_RE.search(paragraph):
            continue
        links = _links(paragraph)
        quotes = _quotes(paragraph, links)
        if not links:
            continue

        paired_links: set[_Link] = set()
        for quote in quotes:
            link, ambiguous = _nearest_link(quote, links)
            if link is None or not _marker_is_confident(paragraph, quote, link):
                continue
            paired_links.add(link)
            line = start_line + paragraph.count("\n", 0, quote.start)
            source = (note.parent / link.target).resolve()
            if ambiguous:
                results.append(
                    QuoteResult(
                        "unresolved",
                        note,
                        line,
                        quote.text,
                        source,
                        "quotation is equally close to multiple source links",
                    )
                )
            elif not source.is_file():
                results.append(
                    QuoteResult(
                        "unresolved",
                        note,
                        line,
                        quote.text,
                        source,
                        "linked source is missing or is not a file",
                    )
                )
            elif normalize_text(quote.text) in normalize_text(load_source(source)):
                results.append(QuoteResult("match", note, line, quote.text, source, ""))
            else:
                results.append(
                    QuoteResult(
                        "mismatch",
                        note,
                        line,
                        quote.text,
                        source,
                        "normalized quotation does not occur in linked source",
                    )
                )

        # An explicit citation-level marker is a candidate even when quote
        # extraction fails. Surface that coverage gap instead of silently
        # treating the paragraph as checked.
        for link in links:
            if link in paired_links:
                continue
            citation = next(
                (
                    paragraph[start:end]
                    for start, end in _citation_ranges(paragraph, [link])
                    if start <= link.start < end
                ),
                "",
            )
            if VERBATIM_RE.search(citation) and not NEGATED_VERBATIM_RE.search(citation):
                line = start_line + paragraph.count("\n", 0, link.start)
                results.append(
                    QuoteResult(
                        "unresolved",
                        note,
                        line,
                        None,
                        (note.parent / link.target).resolve(),
                        "verbatim citation has no confidently paired quotation",
                    )
                )

    return results


def verify_note(note: Path) -> list[QuoteResult]:
    return verify_content(note.read_text(encoding="utf-8"), note)


def markdown_files(paths: Sequence[Path]) -> list[Path]:
    files: set[Path] = set()
    for path in paths:
        if path.is_dir():
            files.update(
                candidate
                for candidate in path.rglob("*.md")
                if candidate.name != "COLLECTION.md"
            )
        elif path.suffix.lower() == ".md":
            files.add(path)
    return sorted(files)


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(Path.cwd()))
    except ValueError:
        return str(path)

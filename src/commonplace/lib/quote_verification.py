"""Verifier for ``verbatim``-marked Markdown quotations.

A ``verbatim`` citation asserts that a quoted span is copied exactly from a
linked source retained in the KB. That assertion is mechanically decidable —
does string X occur in file Y — so it is a Level A deterministic check, and
leaving it hand-trusted is the state the derived-copy rule forbids.

The checker targets the prose convention used by dialectical/evidential
collections: a quoted span, a ``verbatim`` marker, and a Markdown link to the
source, in one paragraph. It discovers quoted spans near a marker, associates
each with the nearest linked Markdown source, and checks normalized occurrence
uniqueness. Unclear pairings are reported as ``unresolved`` rather than
guessed, so parser coverage gaps stay visible instead of passing silently.

Three outcomes per candidate:

``match``
    the quote occurs exactly once in the linked source
``mismatch``
    the quote is absent or ambiguous in the linked source
``unresolved``
    no quote could be confidently paired with the citation

``commonplace-validate`` consumes this via :func:`verify_note`; the
``commonplace-verify-quotes`` command reports over a corpus.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib.note_parser import blank_fenced_code_blocks
from commonplace.lib.quote_matching import Citation, match_quote, parse_blockquotes

LINK_RE = re.compile(r"\[([^]]*)\]\(([^)]+\.md)(?:#[^)]*)?\)")
VERBATIM_RE = re.compile(r"\bverbatim\b", re.IGNORECASE)
NEGATED_VERBATIM_RE = re.compile(
    r"(?:does\s+not|do\s+not|not|no)\s+(?:\w+\s+){0,3}verbatim"
    r"|verbatim\s+(?:passage|text|detail|quotation|quote)\s+"
    r"(?:was|is|were|are)\s+not",
    re.IGNORECASE,
)
# A quotation may wrap across source lines inside one paragraph; paragraphs
# are already split on blank lines, so the span cannot cross one.
DOUBLE_QUOTE_RE = re.compile(r'"([^"]+)"|“([^”]+)”')
INGEST_QUOTES_HEADING_RE = re.compile(r"^## Quotes[ \t]*$", re.MULTILINE)
NEXT_H2_RE = re.compile(r"^##[ \t]+", re.MULTILINE)


def ingest_quotes_section(content: str) -> str:
    """Return the body of an ingest's ``## Quotes`` section, or "" if absent.

    The section runs from the end of the ``## Quotes`` heading line to the start
    of the next ``## `` heading, or the end of the file.
    """
    heading = INGEST_QUOTES_HEADING_RE.search(content)
    if heading is None:
        return ""
    next_heading = NEXT_H2_RE.search(content, heading.end())
    end = next_heading.start() if next_heading is not None else len(content)
    return content[heading.end() : end]


def _source_support_text(source: Path, content: str) -> str | list[str]:
    """Return the span of a source that can support a verbatim quotation.

    An ingest's own analysis prose is not source support (ADR 073): only the
    passages retained under ``## Quotes`` are copied from the pinned snapshot,
    so a quote satisfied by analytical text would assert support the ingest
    never carries. Other sources are searched whole.
    """
    if source.name.endswith(".ingest.md"):
        return [c.quote for c in parse_blockquotes(ingest_quotes_section(content))]
    return content


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


def _mask_link_targets(paragraph: str, links: Sequence[_Link]) -> str:
    """Blank every link target so a marker word inside a path is not prose.

    Offsets are preserved: the returned text has the same length as
    ``paragraph`` and is used only for marker searches, never for pairing.
    """
    chars = list(paragraph)
    for link in links:
        target_start = paragraph.index("](", link.start, link.end) + 2
        for index in range(target_start, link.end - 1):
            chars[index] = " "
    return "".join(chars)


def _citation_ranges(paragraph: str, links: Sequence[_Link]) -> list[tuple[int, int]]:
    """Find balanced parentheses enclosing links, ignoring link and quote text."""
    # Inspect every link even when the caller requests just one citation.
    # Markdown destinations and parentheses quoted from a source are not
    # citation delimiters.
    masked = list(paragraph)
    for match in (*LINK_RE.finditer(paragraph), *DOUBLE_QUOTE_RE.finditer(paragraph)):
        masked[match.start() : match.end()] = " " * (match.end() - match.start())

    openings: list[int] = []
    pairs: list[tuple[int, int]] = []
    for index, char in enumerate(masked):
        if char == "(":
            openings.append(index)
        elif char == ")" and openings:
            pairs.append((openings.pop(), index + 1))

    ranges: list[tuple[int, int]] = []
    for link in links:
        enclosing = [pair for pair in pairs if pair[0] < link.start < link.end < pair[1]]
        if enclosing:
            ranges.append(max(enclosing, key=lambda pair: pair[0]))
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


def _nearest_link(quote: _Quote, links: Sequence[_Link]) -> tuple[_Link, bool]:
    """Choose among the paragraph's nonempty source links."""
    def distance(link: _Link) -> int:
        if link.start >= quote.end:
            return link.start - quote.end
        return quote.start - link.end

    # Citations conventionally follow their quotation. Prefer that direction
    # so a quote at the start of the next list item is not captured by the
    # preceding item's nearby citation.
    following = [link for link in links if link.start >= quote.end]
    ordered = sorted(following or links, key=distance)
    ambiguous = len(ordered) > 1 and distance(ordered[0]) == distance(ordered[1])
    return ordered[0], ambiguous


def _marker_is_confident(
    paragraph: str, quote: _Quote, link: _Link, prose: str
) -> bool:
    """Return whether local prose explicitly marks this quote as verbatim.

    ``prose`` is ``paragraph`` with link targets blanked (same offsets); marker
    words are searched there so a path such as ``046-verbatim-quotes.md``
    never counts as a citation marker. Structure is still read from
    ``paragraph``.
    """
    def positive_marker(text: str) -> bool:
        return bool(VERBATIM_RE.search(text) and not NEGATED_VERBATIM_RE.search(text))

    # Support ``verbatim: "quote"`` and ``states, verbatim, that ...`` without
    # borrowing a marker from an earlier sentence in the same paragraph.
    before = prose[max(0, quote.start - 120) : quote.start]
    before = re.split(r"[.!?]\s+", before)[-1]
    if positive_marker(before):
        return True

    if quote.end <= link.start:
        between = prose[quote.end : link.start]
        # A later sentence's citation belongs to that later quotation, not this
        # one. Multiple quotations joined inside one sentence remain supported.
        another_quote = DOUBLE_QUOTE_RE.search(between)
        if re.search(r"[.!?]\s+", between) or (
            another_quote and quote.text.rstrip().endswith((".", "!", "?"))
        ):
            return False
        citation_tail = prose[link.end : min(len(prose), link.end + 120)]
        for start, end in _citation_ranges(paragraph, [link]):
            if start <= link.start < end:
                citation_tail = prose[link.end:end]
                break
        return positive_marker(between + citation_tail)

    # Less common prefix form: ``verbatim in [source]: "quote"``.
    between = prose[link.end : quote.start]
    if re.search(r"[.!?]\s+", between):
        return False
    return positive_marker(prose[max(0, link.start - 80) : quote.start])


def parse_prose_citations(content: str) -> list[Citation]:
    """Pair prose quotations and links without reading or resolving a source."""
    text = blank_fenced_code_blocks(content)
    citations: list[Citation] = []
    for start_line, paragraph in _paragraphs(text):
        if not VERBATIM_RE.search(paragraph):
            continue
        links = _links(paragraph)
        quotes = _quotes(paragraph, links)
        if not links:
            continue
        prose = _mask_link_targets(paragraph, links)
        if not VERBATIM_RE.search(prose):
            continue
        paired_links: set[_Link] = set()
        for quote in quotes:
            link, ambiguous = _nearest_link(quote, links)
            if not _marker_is_confident(paragraph, quote, link, prose):
                continue
            paired_links.add(link)
            citations.append(Citation(
                quote.text, link.target,
                line=start_line + paragraph.count("\n", 0, quote.start),
                error="quotation is equally close to multiple source links" if ambiguous else None,
            ))
        for link in links:
            if link in paired_links:
                continue
            citation = next((prose[start:end] for start, end in _citation_ranges(paragraph, [link])
                             if start <= link.start < end), "")
            if VERBATIM_RE.search(citation) and not NEGATED_VERBATIM_RE.search(citation):
                citations.append(Citation(
                    "", link.target, line=start_line + paragraph.count("\n", 0, link.start),
                    error="verbatim citation has no confidently paired quotation",
                ))
    return citations


def verify_content(
    content: str, note: Path, *, load_source: Callable[[Path], str] | None = None,
) -> list[QuoteResult]:
    """Resolve parsed prose citations against current KB source bytes."""
    if load_source is None:
        def load_source(path: Path) -> str:
            return path.read_text(encoding="utf-8")
    results = []
    for citation in parse_prose_citations(content):
        source = (note.parent / citation.source).resolve() if citation.source else None
        error = citation.error
        status = "unresolved"
        if error is None:
            if source is None or not source.is_file():
                error = "source error: linked source is missing or is not a file"
            else:
                try:
                    region = _source_support_text(source, load_source(source))
                except (OSError, UnicodeError) as exc:
                    error = f"source error: cannot read linked source: {exc}"
                else:
                    matched = match_quote(citation.quote, region, kind="prose")
                    status = "match" if matched.matched else "mismatch"
                    error = matched.error
                    if error and source.name.endswith(".ingest.md"):
                        error += " (linked ingest's Quotes section)"
        results.append(QuoteResult(status, note, citation.line, citation.quote or None, source, error or ""))
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

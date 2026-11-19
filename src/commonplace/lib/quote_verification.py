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
from urllib.parse import urlsplit

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import blank_fenced_code_blocks
from commonplace.lib.quote_matching import (
    Citation,
    Normalization,
    match_quote,
    parse_blockquotes,
)

LINK_RE = re.compile(r"\[([^]]*)\]\(([^)]+\.md)(?:#[^)]*)?\)")
VERBATIM_RE = re.compile(r"\bverbatim\b", re.IGNORECASE)
NEGATED_VERBATIM_RE = re.compile(
    r"(?:does\s+not|do\s+not|not|no)\s+(?:\w+\s+){0,3}verbatim"
    r"|verbatim\s+(?:passage|text|detail|quotation|quote)\s+"
    r"(?:was|is|were|are)\s+not"
    # Hedged forms such as "near-verbatim" claim resemblance, not copying.
    r"|(?:near(?:ly)?|almost|quasi|roughly|close\s+to)[\s-]*verbatim",
    re.IGNORECASE,
)
# A quotation may wrap across source lines inside one paragraph; paragraphs
# are already split on blank lines, so the span cannot cross one.
DOUBLE_QUOTE_RE = re.compile(r'"([^"]+)"|“([^”]+)”')
LIST_ITEM_SPLIT_RE = re.compile(r"\n(?=[ \t]*(?:[-*+]|\d+[.)])[ \t]+)")
STANDALONE_TRAILING_MARKER_RE = re.compile(
    r"^[ \t]*(?:\([^()\[\]]*\bverbatim\b[^()\[\]]*\)|,[ \t]*verbatim\b)",
    re.IGNORECASE,
)
INGEST_QUOTES_HEADING_RE = re.compile(r"^## Quotes[ \t]*$", re.MULTILINE)
NEXT_H2_RE = re.compile(r"^##[ \t]+", re.MULTILINE)


def ingest_normalization(content: str) -> Normalization:
    """Use the same source-kind rule for snapshots and their retained extracts."""
    metadata = frontmatter.parse(content).data
    source = metadata.get("source")
    try:
        host = urlsplit(source).hostname if isinstance(source, str) and source.startswith(("http://", "https://")) else None
    except ValueError:
        host = None
    return "code" if metadata.get("genre") == "code-repository" or host in {
        "github.com", "raw.githubusercontent.com", "gist.github.com",
        "gitlab.com", "bitbucket.org",
    } else "prose"


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


def _split_tight_list_items(start_line: int, paragraph: str) -> Iterable[tuple[int, str]]:
    """Split a tight Markdown list into per-item blocks with exact line numbers."""
    if paragraph.lstrip().startswith(">") or not LIST_ITEM_SPLIT_RE.search(paragraph):
        yield start_line, paragraph
        return
    offset = 0
    for boundary in LIST_ITEM_SPLIT_RE.finditer(paragraph):
        segment = paragraph[offset : boundary.start()]
        if segment.strip():
            yield start_line + paragraph.count("\n", 0, offset), segment
        offset = boundary.end()
    tail = paragraph[offset:]
    if tail.strip():
        yield start_line + paragraph.count("\n", 0, offset), tail


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
        yield from _split_tight_list_items(line, paragraph)
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


def _positive_marker(text: str) -> bool:
    return bool(VERBATIM_RE.search(text) and not NEGATED_VERBATIM_RE.search(text))


def _has_standalone_trailing_marker(prose: str, quote: _Quote) -> bool:
    match = STANDALONE_TRAILING_MARKER_RE.match(prose[quote.end :])
    return bool(match and _positive_marker(match.group(0)))


def _same_sentence(prose: str, quote: _Quote, link: _Link) -> bool:
    between = (
        prose[quote.end : link.start]
        if quote.end <= link.start
        else prose[link.end : quote.start]
    )
    return not bool(re.search(r"[.!?]\s+", between))


def _link_citation_has_verbatim(paragraph: str, link: _Link, prose: str) -> bool:
    for start, end in _citation_ranges(paragraph, [link]):
        if start <= link.start < end:
            return _positive_marker(prose[start:end])
    return False


def _nearest_link(
    paragraph: str, quote: _Quote, links: Sequence[_Link], prose: str
) -> tuple[_Link, bool]:
    """Choose among the paragraph's nonempty source links."""
    def distance(link: _Link) -> int:
        if link.start >= quote.end:
            return link.start - quote.end
        return quote.start - link.end

    same_sentence = [link for link in links if _same_sentence(prose, quote, link)]
    standalone_trailing = _has_standalone_trailing_marker(prose, quote)

    candidates: list[_Link] = []
    if not standalone_trailing:
        candidates = [
            link
            for link in same_sentence
            if link.start >= quote.end
            and _link_citation_has_verbatim(paragraph, link, prose)
        ]
    if not candidates and standalone_trailing:
        candidates = [link for link in same_sentence if link.end <= quote.start]
    if not candidates:
        following = [link for link in same_sentence if link.start >= quote.end]
        if not following:
            following = [link for link in links if link.start >= quote.end]
        candidates = following or same_sentence or list(links)

    ordered = sorted(candidates, key=distance)
    ambiguous = len(ordered) > 1 and distance(ordered[0]) == distance(ordered[1])
    return ordered[0], ambiguous


def _marker_is_confident(
    paragraph: str,
    quote: _Quote,
    link: _Link,
    prose: str,
    *,
    prev_quote_end: int | None = None,
) -> bool:
    """Return whether local prose explicitly marks this quote as verbatim.

    ``prose`` is ``paragraph`` with link targets blanked (same offsets); marker
    words are searched there so a path such as ``046-verbatim-quotes.md``
    never counts as a citation marker. Structure is still read from
    ``paragraph``.
    """
    before_start = max(0, quote.start - 120)
    if prev_quote_end is not None and prev_quote_end >= before_start:
        # Do not borrow a standalone trailing marker such as ``(verbatim)`` from
        # an earlier quotation in the same sentence, while preserving shared
        # prefix forms such as ``read, verbatim, as "q1" and "q2"``.
        trail = STANDALONE_TRAILING_MARKER_RE.match(prose[prev_quote_end : quote.start])
        if trail is not None:
            before_start = prev_quote_end + trail.end()
    before = prose[before_start : quote.start]
    before = re.split(r"[.!?]\s+", before)[-1]
    if _positive_marker(before):
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
        if _has_standalone_trailing_marker(prose, quote):
            trail = STANDALONE_TRAILING_MARKER_RE.match(between)
            remainder = between[trail.end() :] if trail else between
            if re.search(r"\w", remainder) and not _positive_marker(citation_tail):
                return False
        return _positive_marker(between + citation_tail)

    # Prefix link form: ``verbatim in [source]: "quote"`` or
    # ``[source] writes "quote" (verbatim)``.
    between = prose[link.end : quote.start]
    if re.search(r"[.!?]\s+", between):
        return False
    prefix_start = max(0, link.start - 80)
    prefix = prose[prefix_start : quote.start]
    if prev_quote_end is not None and prefix_start <= prev_quote_end <= quote.start:
        trail = STANDALONE_TRAILING_MARKER_RE.match(prose[prev_quote_end : quote.start])
        if trail is not None:
            cut = prev_quote_end - prefix_start
            prefix = prefix[:cut] + prefix[cut + trail.end() :]
    return _has_standalone_trailing_marker(prose, quote) or _positive_marker(prefix)


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
        prev_quote_end: int | None = None
        for quote in quotes:
            link, ambiguous = _nearest_link(paragraph, quote, links, prose)
            confident = _marker_is_confident(
                paragraph, quote, link, prose, prev_quote_end=prev_quote_end
            )
            prev_quote_end = quote.end
            if not confident:
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
                    source_content = load_source(source)
                    region = _source_support_text(source, source_content)
                except (OSError, UnicodeError) as exc:
                    error = f"source error: cannot read linked source: {exc}"
                else:
                    kind = ingest_normalization(source_content) if source.name.endswith(".ingest.md") else "prose"
                    matched = match_quote(citation.quote, region, kind=kind)
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

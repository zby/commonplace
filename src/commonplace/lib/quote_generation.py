"""Locate bounded quotation occurrences for frozen-source diagnostics."""

from __future__ import annotations

import re
from bisect import bisect_right
from dataclasses import dataclass

from commonplace.lib.quote_matching import normalize_text

MAX_QUOTE_OCCURRENCES = 10


@dataclass(frozen=True)
class QuoteOccurrence:
    text: str
    start_line: int
    end_line: int
    start_offset: int
    end_offset: int


def quote_occurrences(quote: str, source: str) -> tuple[QuoteOccurrence, ...]:
    """Locate every whitespace-normalized occurrence in original source text.

    Return exact source text and derived line bounds, never caller-provided
    endpoints. Offsets are zero-based character offsets with an exclusive end.
    Never expand the requested passage. Context for a diagnostic is separate
    from the occurrence: its range must be checked against the unchanged quote.
    Reject more than ten so the analyst can choose a longer passage.
    """
    needle = normalize_text(quote, "code")
    if not needle:
        raise ValueError("quote text is empty after whitespace normalization")
    normalized = normalize_text(source, "code")
    positions = []
    position = normalized.find(needle)
    while position >= 0:
        positions.append(position)
        if len(positions) > MAX_QUOTE_OCCURRENCES:
            raise ValueError(
                f"requested text has more than {MAX_QUOTE_OCCURRENCES} occurrences; "
                "choose a longer quote"
            )
        position = normalized.find(needle, position + 1)
    if not positions:
        return ()

    # Build the source-coordinate map only for a bounded, nonempty match set.
    offsets: list[int] = []
    for token in re.finditer(r"\S+", source):
        if offsets:
            offsets.append(token.start() - 1)
        offsets.extend(range(token.start(), token.end()))
    line_starts = [0]
    for line in source.splitlines(keepends=True):
        line_starts.append(line_starts[-1] + len(line))

    occurrences = []
    for position in positions:
        left, right = position, position + len(needle)
        start, end = offsets[left], offsets[right - 1] + 1
        start_line = bisect_right(line_starts, start)
        end_line = bisect_right(line_starts, end - 1)
        text = source[start:end]
        occurrences.append(QuoteOccurrence(text, start_line, end_line, start, end))
    return tuple(occurrences)

"""Construct citations from selected text and a frozen analysis source."""

from __future__ import annotations

import re
from bisect import bisect_right
from dataclasses import dataclass
from hashlib import sha256

from commonplace.lib.agentic_analysis import SourceIdentity, git_blob_text
from commonplace.lib.quote_matching import ATTRIBUTION_RE, normalize_text

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
    Where occurrences share a line, expand each excerpt with source
    context until it is unique within its range. Keep one result per original
    occurrence, including overlapping occurrences. Reject more than ten before
    constructing excerpts so the author can choose a more specific passage.
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
        while True:
            start, end = offsets[left], offsets[right - 1] + 1
            start_line = bisect_right(line_starts, start)
            end_line = bisect_right(line_starts, end - 1)
            text = source[start:end]
            region = normalize_text(
                source[line_starts[start_line - 1] : line_starts[end_line]], "code"
            )
            excerpt = normalized[left:right]
            first = region.find(excerpt)
            if region.find(excerpt, first + 1) < 0:
                break
            # Expansion remains contiguous and includes the requested match.
            # Skip intervening whitespace so each iteration adds real context.
            if left:
                left -= 1
                while left and normalized[left].isspace():
                    left -= 1
            if right < len(normalized):
                right += 1
                while right < len(normalized) and normalized[right - 1].isspace():
                    right += 1
        occurrences.append(QuoteOccurrence(text, start_line, end_line, start, end))
    return tuple(occurrences)


def render_quote(occurrence: QuoteOccurrence, *, path: str, version: str) -> str:
    """Render one already located occurrence in the shared attributed form."""
    if any(character in path + version for character in "`\r\n"):
        raise ValueError(
            "source identity cannot be represented in a citation code span"
        )
    # Trailing whitespace would fail whitespace checks; matching ignores it.
    lines = [("> " + line).rstrip() for line in occurrence.text.splitlines()]
    if any(ATTRIBUTION_RE.fullmatch(line) for line in lines):
        raise ValueError(
            "source passage cannot be represented as one attributed blockquote"
        )
    lines.append(
        f"> --- `{path}:{occurrence.start_line}-{occurrence.end_line}` @ `{version}`"
    )
    return "\n".join(lines) + "\n"


def _frozen_source_text(
    source: SourceIdentity, source_path: str | None
) -> tuple[str, str, str]:
    """Return the frozen text plus the path and version its citations carry."""
    if source.kind == "git":
        if not source_path:
            raise ValueError("Git quotation generation requires --source-path")
        content, error = git_blob_text(
            source_root=source.path,
            revision=source.revision,
            source_path=source_path,
        )
        if error or content is None:
            raise ValueError(f"cannot read frozen source: {error}")
        return content, source_path, source.revision
    if source.kind == "capture":
        if source_path is not None:
            raise ValueError(
                "capture quotation generation uses the run's capture; omit --source-path"
            )
        raw = source.path.read_bytes()
        if sha256(raw).hexdigest() != source.expected_sha256:
            raise ValueError("frozen capture SHA-256 mismatch")
        return (
            raw.decode("utf-8"),
            source.path.as_posix(),
            f"sha256:{source.expected_sha256}",
        )
    raise ValueError(f"unsupported source kind: {source.kind}")


def _quote_payload(
    text: str, *, content: str, path: str, version: str
) -> str | dict[str, object]:
    occurrences = quote_occurrences(text, content)
    if not occurrences:
        raise ValueError("requested text does not occur in the frozen source")
    if len(occurrences) == 1:
        return render_quote(occurrences[0], path=path, version=version)
    return {
        "occurrences": [
            {
                "occurrence": index,
                "start_line": occurrence.start_line,
                "end_line": occurrence.end_line,
                "start_offset": occurrence.start_offset,
                "end_offset": occurrence.end_offset,
                "citation": render_quote(occurrence, path=path, version=version),
            }
            for index, occurrence in enumerate(occurrences, 1)
        ],
    }


def generate_quotes(
    text: str,
    *,
    source: SourceIdentity,
    source_path: str | None = None,
) -> str | dict[str, object]:
    """Emit a citation, or selection metadata for two to ten occurrences.

    This constructs citations; it does not validate a document or accept an
    author-supplied citation. The regular validator owns document verification.
    """
    content, path, version = _frozen_source_text(source, source_path)
    return _quote_payload(text, content=content, path=path, version=version)


def generate_quote_batch(
    selections: object, *, source: SourceIdentity
) -> dict[str, dict[str, object]]:
    """Resolve many selections against one frozen source in one call.

    ``selections`` is a JSON list of objects with a unique nonempty ``key``,
    the selected ``text``, and ``source_path`` (a commit-relative Git path;
    omitted or null for a capture). Each key maps to one of:
    ``{"status": "citation", "citation": ...}`` for a unique occurrence,
    ``{"status": "candidates", "occurrences": [...]}`` for two to ten, or
    ``{"status": "error", "error": ...}`` when the selection cannot be
    resolved. A malformed list is rejected as a whole; a bad entry only
    fails its own key.
    """
    if not isinstance(selections, list) or not selections:
        raise ValueError("selections must be a nonempty JSON list")
    results: dict[str, dict[str, object]] = {}
    sources: dict[str | None, tuple[str, str, str] | str] = {}
    for index, entry in enumerate(selections, 1):
        if not isinstance(entry, dict):
            raise ValueError(f"selection {index} is not a JSON object")  # noqa: TRY004
        key = entry.get("key")
        if not isinstance(key, str) or not key.strip():
            raise ValueError(f"selection {index} has no nonempty string key")
        if key in results:
            raise ValueError(f"selection key {key!r} is not unique")
        text = entry.get("text")
        source_path = entry.get("source_path")
        if not isinstance(text, str):
            results[key] = {"status": "error", "error": "text must be a string"}
            continue
        if source_path is not None and not isinstance(source_path, str):
            results[key] = {
                "status": "error", "error": "source_path must be a string or null",
            }
            continue
        if source_path not in sources:
            try:
                sources[source_path] = _frozen_source_text(source, source_path)
            except (OSError, ValueError, UnicodeDecodeError) as exc:
                sources[source_path] = str(exc)
        loaded = sources[source_path]
        if isinstance(loaded, str):
            results[key] = {"status": "error", "error": loaded}
            continue
        content, path, version = loaded
        try:
            payload = _quote_payload(
                text, content=content, path=path, version=version
            )
        except ValueError as exc:
            results[key] = {"status": "error", "error": str(exc)}
            continue
        if isinstance(payload, str):
            results[key] = {"status": "citation", "citation": payload}
        else:
            results[key] = {"status": "candidates", **payload}
    return results

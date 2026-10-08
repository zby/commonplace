"""Resolve quote-anchored citations against a pinned source.

One mechanism serves source grounding and analysis evidence. A citation is a
blockquote with a ``> ---`` attribution; a declaring document pins the bytes it
may quote: an ingest's ``snapshot_sha256``, or an analysis boundary's frozen
``source`` (a Git revision or a capture digest). The pinned bytes are local to
the machine that took them (ADR 072), so a citation resolves to one of three
outcomes:

``match``
    the attribution names the pinned source and the quote occurs once in it
``mismatch``
    the attribution or the quote is wrong for the pinned source
``unverified``
    the pinned bytes are not available here, so the quote cannot be checked

Standing validation reports ``unverified`` as information; a caller that holds
the source, such as an analysis run, treats it as a failure.
"""

from __future__ import annotations

import subprocess
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from hashlib import sha256
from pathlib import Path
from typing import Any, Literal, Protocol

from commonplace.lib.agentic_analysis.sets import is_normalized_relative
from commonplace.lib.quote_generation import MAX_QUOTE_OCCURRENCES, quote_occurrences
from commonplace.lib.quote_matching import (
    Citation,
    Normalization,
    git_citation_path,
    match_quote,
)
from commonplace.lib.source_identity import normalize_source_identity

Status = Literal["match", "mismatch", "unverified"]


@dataclass(frozen=True)
class Resolution:
    citation: Citation
    status: Status
    detail: str


@dataclass(frozen=True)
class SourceText:
    """The pinned text a citation addresses, or why there is none: ``missing``
    when the pinned bytes are not here, ``error`` when the citation addresses
    nothing in bytes that are."""

    text: str | None = None
    path: str = ""
    location: str = ""
    missing: str | None = None
    error: str | None = None


class PinnedSource(Protocol):
    def attribution_error(self, citation: Citation) -> str | None: ...

    def read(self, citation: Citation) -> SourceText: ...


@dataclass
class SnapshotPin:
    """An ingest's name-paired snapshot, pinned by ``snapshot_sha256``."""

    attribution_path: str
    checksum: str
    file: Path
    _text: SourceText | None = field(default=None, init=False)

    def attribution_error(self, citation: Citation) -> str | None:
        if citation.source != self.attribution_path:
            return f"attribution must name {self.attribution_path}"
        if citation.version != "sha256:" + self.checksum:
            return "attribution checksum differs from snapshot_sha256"
        return None

    def read(self, citation: Citation) -> SourceText:
        if self._text is None:
            location = "the checksum-verified snapshot"
            try:
                content = self.file.read_bytes()
            except OSError:
                content = None
            if content is None or sha256(content).hexdigest() != self.checksum:
                self._text = SourceText(missing="pinned snapshot unavailable or checksum differs")
            else:
                try:
                    self._text = SourceText(content.decode("utf-8"), self.attribution_path, location)
                except UnicodeError as exc:
                    self._text = SourceText(missing=f"cannot read pinned snapshot: {exc}")
        return self._text


@dataclass
class GitPin:
    """A checkout frozen at one commit; a citation names a path in it.

    Files are read from the checkout itself. That is only evidence of the
    commit while the checkout is exactly that commit's files, which freezing
    establishes; this is confirmed once, and a checkout that is absent, at
    another commit or locally changed leaves every citation unverified.
    """

    identity: str
    revision: str
    root: Path
    _missing: str | None | bool = field(default=False, init=False)

    def attribution_error(self, citation: Citation) -> str | None:
        try:
            _, repository = git_citation_path(citation)
        except ValueError as exc:
            return str(exc)
        if repository and repository.casefold() != normalize_source_identity(self.identity).casefold():
            return f"attribution uses repository {repository}, expected {self.identity}"
        if citation.version is not None and citation.version != self.revision:
            return f"attribution uses revision {citation.version}, expected {self.revision}"
        return None

    def missing(self) -> str | None:
        """Why the pinned bytes are not here, or None when they are."""
        if self._missing is False:
            self._missing = checkout_not_at(self.root, self.revision)
        return self._missing  # type: ignore[return-value]

    def file(self, path: str) -> tuple[Path | None, str | None]:
        """The checkout file a commit-relative path names, or why it names none."""
        if not is_normalized_relative(path):
            return None, "expected a normalized commit-relative path"
        file = self.root / path
        if not file.is_file() or not file.resolve().is_relative_to(self.root.resolve()):
            return None, "path does not name a file at the recorded commit"
        return file, None

    def read(self, citation: Citation) -> SourceText:
        missing = self.missing()
        if missing is not None:
            return SourceText(missing=missing)
        path, _ = git_citation_path(citation)
        file, error = self.file(path)
        if file is None:
            return SourceText(path=path, error=error)
        try:
            text = file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return SourceText(path=path, error="cited file is not UTF-8 text")
        return SourceText(text, path, f"{path} at the recorded commit")


@dataclass
class CapturePin:
    """A frozen capture file pinned by its digest."""

    identity: str
    label: str
    file: Path
    checksum: str
    _text: SourceText | None = field(default=None, init=False)

    def attribution_error(self, citation: Citation) -> str | None:
        if citation.source and citation.source.startswith(("http://", "https://")):
            if citation.source != self.identity:
                return (f"attribution URL does not match registered capture identity; "
                        f"expected {self.identity}, or cite {self.file.as_posix()}")
            if citation.ranges:
                return "a blob line range cannot address the full capture; cite a capture range"
            return None
        if citation.version is not None and citation.version != f"sha256:{self.checksum}":
            return f"attribution checksum does not match frozen capture; expected sha256:{self.checksum}"
        source = Path(citation.source or "").as_posix()
        if source != self.file.as_posix() and not self.file.as_posix().endswith("/" + (citation.source or "")):
            return f"attribution path does not identify frozen capture; expected {self.file.as_posix()}"
        return None

    def missing(self) -> str | None:
        """Why the pinned bytes are not here, or None when they are."""
        return self._load().missing

    def read(self, citation: Citation) -> SourceText:
        return self._load()

    def _load(self) -> SourceText:
        if self._text is None:
            try:
                content = self.file.read_bytes()
            except OSError as exc:
                self._text = SourceText(missing=f"cannot read frozen capture {self.file}: {exc}")
            else:
                actual = sha256(content).hexdigest()
                if actual != self.checksum:
                    self._text = SourceText(missing=(
                        f"frozen capture SHA-256 mismatch; expected {self.checksum}, got {actual}"))
                else:
                    try:
                        self._text = SourceText(content.decode("utf-8"), self.file.as_posix(),
                                                f"frozen capture {self.label}")
                    except UnicodeError as exc:
                        self._text = SourceText(missing=f"cannot read frozen capture as UTF-8 text: {exc}")
        return self._text


def frozen_source_pin(source: Mapping[str, Any]) -> GitPin | CapturePin:
    """The pin an analysis boundary's ``source`` declares."""
    if source.get("kind") == "capture":
        return CapturePin(str(source["identity"]), str(source["revision"]), Path(str(source["path"])),
                          str(source.get("sha256") or ""))
    return GitPin(str(source["identity"]), str(source["revision"]), Path(str(source["path"])))


def resolve_citations(
    citations: Iterable[Citation], source: PinnedSource, *, kind: Normalization,
) -> list[Resolution]:
    """Resolve each citation against the pinned source, in order."""
    resolutions = []
    for citation in citations:
        def result(status: Status, detail: str, citation: Citation = citation) -> None:
            resolutions.append(Resolution(citation, status, detail))

        if not citation.quote.strip():
            result("mismatch", "quote body is empty")
            continue
        error = citation.error or source.attribution_error(citation)
        if error:
            result("mismatch", f"source error: {error}")
            continue
        found = source.read(citation)
        if found.missing is not None:
            result("unverified", f"source unavailable: {found.missing}")
            continue
        if found.error is not None or found.text is None:
            result("mismatch", f"source error: {found.error}")
            continue
        matched = match_quote(citation.quote, found.text, kind=kind, ranges=citation.ranges)
        if matched.matched:
            result("match", f"quote resolves in {found.location}")
        elif matched.count > 1:
            advice = quote_ambiguity_advice(citation, found.text, path=found.path)
            result("mismatch", f"quotation ambiguous: {matched.error} ({found.location}); {advice}")
        elif matched.count == 0 and (matched.error or "").startswith("quote does not occur"):
            result("mismatch", f"quotation not found: {matched.error} ({found.location}); "
                               "reread the source and recheck the claim this quotation supports")
        else:
            result("mismatch", f"{matched.error} ({found.location}); "
                               "check the passage and range against the pinned source")
    return resolutions


def quote_ambiguity_advice(citation: Citation, source_text: str, *, path: str) -> str:
    """Offer checked ranges; context cannot silently replace the quoted text."""
    lines = source_text.splitlines(keepends=True)
    regions: list[tuple[int, int]] = []
    for start, end in sorted(citation.ranges or ((1, len(lines)),)):
        if regions and start <= regions[-1][1] + 1:
            regions[-1] = (regions[-1][0], max(end, regions[-1][1]))
        else:
            regions.append((start, end))
    candidates = []
    try:
        for start, end in regions:
            region = "".join(lines[start - 1:end])
            region_offset = sum(map(len, lines[:start - 1]))
            for occurrence in quote_occurrences(citation.quote, region):
                first = start + occurrence.start_line - 1
                last = start + occurrence.end_line - 1
                candidates.append((first, occurrence.start_offset + region_offset, last))
        if len(candidates) > MAX_QUOTE_OCCURRENCES:
            raise ValueError(f"more than {MAX_QUOTE_OCCURRENCES} occurrences")
    except ValueError as error:
        return f"{error}; expand the quotation to make it less ambiguous; no candidates proposed"
    proposals = []
    for number, (first, offset, last) in enumerate(candidates, 1):
        unique = match_quote(citation.quote, source_text, kind="code", ranges=((first, last),)).matched
        attribution = f"> --- `{path}:{first}-{last}`"
        if citation.version is not None:
            attribution += f" @ `{citation.version}`"
        context = "".join(lines[max(0, first - 2):min(len(lines), last + 1)]).rstrip()
        column = offset - sum(map(len, lines[:first - 1])) + 1
        repair = f"paste attribution: {attribution}" if unique else "no attribution can separate this occurrence; lengthen the quotation using its context"
        proposals.append(f"candidate {number}, source line {first}, column {column}: {repair}\nsource context:\n{context}")
    return "choose the occurrence whose context supports the finding, or lengthen the quotation:\n" + "\n".join(proposals)


def checkout_not_at(root: Path, revision: str) -> str | None:
    """Why ``root`` is not exactly the files of ``revision``, or None when it is."""
    if not root.is_dir():
        return f"source checkout: directory does not exist: {root}"

    def git(*args: str) -> str | None:
        try:
            done = subprocess.run(["git", "-C", str(root), *args], check=False, capture_output=True, text=True)
        except OSError:
            return None
        return done.stdout.strip() if done.returncode == 0 else None

    head = git("rev-parse", "HEAD")
    if head is None:
        return f"source checkout: not a readable Git checkout: {root}"
    if head != revision:
        return f"source checkout: at {head}, not the frozen revision {revision}"
    if git("status", "--porcelain"):
        return "source checkout: has local changes, so its files are not the frozen revision's"
    return None

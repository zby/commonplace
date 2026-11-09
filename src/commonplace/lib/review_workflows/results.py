"""Review result files and their freshness.

A result is one reviewer's judgment of one note against one criterion, kept
at `kb/reports/state/review/results/<note-path>/<criterion-id>.md`. Its
frontmatter names both inputs with the SHA-256 of the text the judgment was
produced from, the outcome and the executor; its body is the reviewer's text.
A pair is fresh when both hashes match the current files, so freshness needs
no store and no Git history.

The note hash covers only the parts the criterion declares in `watches:`
(title, description, body), so an edit outside them leaves the pair fresh;
a criterion without a valid declaration watches the whole note. The note
hash is computed under the criterion's current `watches:`: a criterion edit
that changes the declaration stales its pairs on the criterion and may report
the note changed as well.

A criterion is named by its artifact identity: a repository path, or
`commonplace:<path>` for a library file outside the repository. Its text is
read through the library resolution, so a project that reads the installed
library and this checkout, whose library is its own kb/, keep results the same
way.

Everything here is a pure function of the files under `root` and the library.
"""

from __future__ import annotations

import hashlib
import json
import re
import uuid
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

from commonplace.lib import frontmatter
from commonplace.lib.library import (
    LIBRARY_IDENTITY_PREFIX,
    artifact_file,
    artifact_identity,
    is_library_identity,
)
from commonplace.lib.review_workflows.criteria import gates_dir

RESULTS = Path("kb/reports/state/review/results")
LIBRARY_ID_PREFIX = "commonplace/"
"""Where a library criterion outside the gate catalog keeps its results; repository criteria live under kb/."""
WATCHABLE = {"title", "description", "body"}
OUTCOMES = ("pass", "warn", "fail", "report")
PARTS_DOMAIN = "commonplace-review-watched-parts/1\n"
"""Prefix of a watched-parts hash input, so it never equals a whole note's text by design."""


@dataclass(frozen=True)
class Result:
    note: str                         # repository-relative POSIX path
    note_sha256: str                  # over the parts the criterion watches, see `note_sha256()`
    criterion: str                    # artifact identity: repository path or `commonplace:<path>`
    criterion_sha256: str
    outcome: str                      # one of OUTCOMES
    profile: dict[str, Any]           # harness, launch-model, effort
    model: str | None                 # the model the harness recorded
    run: str
    launch: str
    completed_at: str
    body: str                         # the reviewer's text, unchanged


@dataclass(frozen=True)
class Freshness:
    state: str                        # "fresh", "missing" or "stale"
    changed: tuple[str, ...] = ()     # when stale: "note", "criterion" or both, in that order


@dataclass(frozen=True)
class Row:
    note: str
    criterion: str
    freshness: Freshness
    outcome: str | None = None        # None when the result is missing
    profile: dict[str, Any] | None = None
    model: str | None = None
    path: Path | None = None          # the result file, None when the result is missing


@dataclass(frozen=True)
class Summary:
    results: int = 0
    fresh: int = 0
    stale: int = 0
    orphaned: int = 0
    warn: int = 0                     # fresh results whose outcome is warn
    fail: int = 0                     # fresh results whose outcome is fail


_KEYS = {"note": "note", "note-sha256": "note_sha256", "criterion": "criterion",
         "criterion-sha256": "criterion_sha256", "outcome": "outcome", "profile": "profile",
         "model": "model", "run": "run", "launch": "launch", "completed-at": "completed_at"}


def _posix(path: str | Path, *, label: str) -> str:
    """A repository-relative path in POSIX form; absolute paths and `..` are refused."""
    native = Path(path)
    text = native.as_posix()
    pure = PurePosixPath(text)
    if text in ("", ".") or native.drive or native.is_absolute() or pure.is_absolute() or ".." in pure.parts:
        raise ValueError(f"{label} must be a repository-relative path: {path}")
    return text


def _identity(criterion: str | Path) -> str:
    """A criterion identity: a repository-relative path, or a library identity whose path stays in the library."""
    text = str(criterion)
    if is_library_identity(text):
        _posix(text[len(LIBRARY_IDENTITY_PREFIX):], label="library criterion")
        return text
    return _posix(criterion, label="criterion")


def criterion_id(root: Path, criterion: str | Path) -> str:
    """The criterion's short name, which keys its result file under the note.

    A catalog gate is `<lens>/<name>` (`prose/source-residue`) in both
    layouts. Any other repository criterion is its path without `.md`
    (`kb/types/note`); any other library criterion is `commonplace/` and its
    library path without `.md` (`commonplace/types/note`).
    """
    identity = _identity(criterion)
    gates = artifact_identity(root, gates_dir()) + "/"
    if identity.startswith(gates):
        name = identity[len(gates):]
    elif is_library_identity(identity):
        name = LIBRARY_ID_PREFIX + identity[len(LIBRARY_IDENTITY_PREFIX):]
    else:
        name = identity
    return name.removesuffix(".md")


def criterion_file(root: Path, criterion: str | Path) -> Path:
    """The file a criterion identity names, in the repository or in the library."""
    return artifact_file(root, _identity(criterion))


_TITLE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def _normalize_markdown(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.splitlines() if line.strip())


def _normalize_scalar(value: Any) -> Any:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        return tuple(_normalize_scalar(item) for item in value)
    return value


def note_parts(note_text: str) -> dict[str, Any] | None:
    """The watchable parts of a note, normalized; None when its frontmatter does not parse.

    The title is the first `# ` heading; the body is the text after it with
    blank lines and trailing spaces dropped, so a whitespace-only edit changes
    no part.
    """
    parsed = frontmatter.parse(note_text)
    if not parsed.ok:
        return None
    body = frontmatter.strip(note_text)
    title = _TITLE.search(body)
    return {"title": title.group(1).strip() if title else "",
            "description": _normalize_scalar(parsed.data.get("description", "")),
            "body": _normalize_markdown(body[title.end():] if title else body)}


def watches(criterion_text: str) -> set[str] | None:
    """The note parts the criterion declares in `watches:`; None without a valid declaration."""
    parsed = frontmatter.parse(criterion_text)
    raw = parsed.data.get("watches") if parsed.ok else None
    if not isinstance(raw, list) or not raw or not all(isinstance(item, str) for item in raw):
        return None
    return set(raw) if set(raw) <= WATCHABLE else None


def note_sha256(note_text: str, criterion_text: str) -> str:
    """SHA-256 over the note parts the criterion watches, or over the whole note.

    The whole note is hashed when the criterion declares no valid `watches:`
    or the note's frontmatter does not parse. The parts are JSON-encoded, so
    part content cannot forge a part boundary.
    """
    watched = watches(criterion_text)
    parts = note_parts(note_text) if watched is not None else None
    if parts is None:
        data = note_text
    else:
        data = PARTS_DOMAIN + json.dumps([[key, parts[key]] for key in sorted(watched)],
                                         ensure_ascii=False, default=repr)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def criterion_sha256(criterion_text: str) -> str:
    return hashlib.sha256(criterion_text.encode("utf-8")).hexdigest()


def result_path(root: Path, note: str | Path, criterion_id: str) -> Path:
    """Where the result for a pair lives; a path resolving outside the results root is refused."""
    results = (root / RESULTS).resolve()
    rel = PurePosixPath(_posix(note, label="note")) / f"{_posix(criterion_id, label='criterion id')}.md"
    target = (results / rel).resolve()
    if not target.is_relative_to(results) or target == results:
        raise ValueError(f"result for {note} and {criterion_id} is outside {RESULTS.as_posix()}")
    return target


def _read(path: Path) -> str:
    # Universal newlines: a CRLF checkout hashes as the LF text does.
    return path.read_text(encoding="utf-8")


def make_result(note: str | Path, note_text: str, criterion: str | Path, criterion_text: str, *, outcome: str,
                profile: dict[str, Any], model: str | None, run: str, launch: str, completed_at: str,
                body: str) -> Result:
    """A result hashing the note and criterion texts the reviewer was given."""
    return Result(note=_posix(note, label="note"), note_sha256=note_sha256(note_text, criterion_text),
                  criterion=_identity(criterion), criterion_sha256=criterion_sha256(criterion_text),
                  outcome=outcome, profile=dict(profile), model=model, run=run, launch=launch,
                  completed_at=completed_at, body=body)


def write_result(root: Path, result: Result) -> Path:
    """Write the result file atomically: readers see the old bytes or the new ones."""
    if result.outcome not in OUTCOMES:
        raise ValueError(f"outcome must be one of {', '.join(OUTCOMES)}: {result.outcome}")
    target = result_path(root, result.note, criterion_id(root, result.criterion))
    data = {key: getattr(result, field) for key, field in _KEYS.items()}
    text = "---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True) + "---\n" + result.body
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_name(f".{target.name}.{uuid.uuid4().hex[:6]}.tmp")
    with tmp.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    tmp.replace(target)
    return target


def read_result(path: Path) -> Result:
    """Parse a result file; a file that is not a valid result raises ValueError naming it."""
    with path.open(encoding="utf-8", newline="") as handle:
        text = handle.read()
    parsed = frontmatter.parse(text)
    problems = list(parsed.errors)
    if not problems and not frontmatter.opens_frontmatter(text):
        problems.append("no frontmatter")
    data = parsed.data
    if not problems:
        missing = [key for key in _KEYS if key not in data]
        if missing:
            problems.append(f"missing {', '.join(missing)}")
        for key in ("note", "note-sha256", "criterion", "criterion-sha256", "run", "launch", "completed-at"):
            if key in data and not isinstance(data[key], str):
                problems.append(f"{key} must be a string")
        if data.get("outcome") not in OUTCOMES:
            problems.append(f"outcome must be one of {', '.join(OUTCOMES)}")
        if "profile" in data and not isinstance(data["profile"], dict):
            problems.append("profile must be a mapping")
        if data.get("model") is not None and not isinstance(data["model"], str):
            problems.append("model must be a string or null")
    if problems:
        raise ValueError(f"unreadable review result {path}: {'; '.join(problems)}")
    return Result(**{field: data[key] for key, field in _KEYS.items()}, body=frontmatter.strip(text))


def _check(root: Path, note: str | Path, criterion: str | Path) -> tuple[Freshness, Result | None, Path]:
    note, criterion = _posix(note, label="note"), _identity(criterion)
    path = result_path(root, note, criterion_id(root, criterion))
    if not path.is_file():
        return Freshness("missing"), None, path
    result = read_result(path)
    if (result.note, result.criterion) != (note, criterion):
        raise ValueError(f"review result {path} records {result.note} and {result.criterion}, "
                         f"not {note} and {criterion}")
    return _freshness(root, result, {}), result, path


def _freshness(root: Path, result: Result, texts: dict[Path, str]) -> Freshness:
    """Compare the result's hashes with the current files; `texts` caches file texts across results."""
    def text(path: Path) -> str:
        if path not in texts:
            texts[path] = _read(path)
        return texts[path]
    criterion_text = text(criterion_file(root, result.criterion))
    changed = tuple(name for name, same in (
        ("note", note_sha256(text(root / result.note), criterion_text) == result.note_sha256),
        ("criterion", criterion_sha256(criterion_text) == result.criterion_sha256)) if not same)
    return Freshness("stale", changed) if changed else Freshness("fresh")


def freshness(root: Path, note: str | Path, criterion: str | Path) -> Freshness:
    """Whether the stored result for the pair still matches the note and the criterion."""
    return _check(root, note, criterion)[0]


def _row(result: Result, state: Freshness, path: Path) -> Row:
    return Row(result.note, result.criterion, state, result.outcome, result.profile, result.model, path)


def status(root: Path, pairs: Iterable[tuple[str | Path, str | Path]]) -> list[Row]:
    """One row per (note, criterion) pair, with the stored outcome and executor when there is a result."""
    rows = []
    for note, criterion in pairs:
        state, result, path = _check(root, note, criterion)
        rows.append(_row(result, state, path) if result is not None
                    else Row(_posix(note, label="note"), _identity(criterion), state))
    return rows


def _stored_files(root: Path) -> Iterator[tuple[Path, Result]]:
    results = root / RESULTS
    if not results.is_dir():
        return
    for path in sorted(path for path in results.rglob("*.md") if path.is_file()):  # note dirs end in .md
        yield path, read_result(path)


def _is_orphan(root: Path, result: Result) -> bool:
    try:
        return not (root / result.note).is_file() or not criterion_file(root, result.criterion).is_file()
    except ValueError:                    # an identity that no longer resolves in this library
        return True


def orphaned(root: Path) -> list[Path]:
    """Stored result files whose note or criterion file no longer exists; removing one is deleting it."""
    return [path for path, result in _stored_files(root) if _is_orphan(root, result)]


def stored(root: Path) -> tuple[list[Row], list[Path]]:
    """Every stored result once: rows for those whose inputs exist, and the orphaned result files.

    Each note and criterion file is read once however many results name it.
    """
    rows, orphans, texts = [], [], {}
    for path, result in _stored_files(root):
        if _is_orphan(root, result):
            orphans.append(path)
        else:
            rows.append(_row(result, _freshness(root, result, texts), path))
    return rows, orphans


def summarize(root: Path) -> Summary:
    """Counts over every stored result: fresh, stale and orphaned, and the fresh warn and fail outcomes."""
    rows, orphans = stored(root)
    fresh = [row for row in rows if row.freshness.state == "fresh"]
    return Summary(results=len(rows) + len(orphans), fresh=len(fresh), stale=len(rows) - len(fresh),
                   orphaned=len(orphans), warn=sum(row.outcome == "warn" for row in fresh),
                   fail=sum(row.outcome == "fail" for row in fresh))

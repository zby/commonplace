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

Everything here is a pure function of the files under `root`.
"""

from __future__ import annotations

import hashlib
import json
import uuid
from collections.abc import Iterable
from dataclasses import dataclass, replace
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

from commonplace.lib import frontmatter
from commonplace.review.ack_trivial_note_changes import gate_watches, note_parts
from commonplace.review.paths import GATES_REL

RESULTS = Path("kb/reports/state/review/results")
GATES = PurePosixPath("kb") / GATES_REL
OUTCOMES = ("pass", "warn", "fail", "report")
PARTS_DOMAIN = "commonplace-review-watched-parts/1\n"
"""Prefix of a watched-parts hash input, so it never equals a whole note's text by design."""


@dataclass(frozen=True)
class Result:
    note: str                         # repository-relative POSIX path
    note_sha256: str                  # over the parts the criterion watches, see `note_sha256()`
    criterion: str                    # repository-relative POSIX path
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


def criterion_id(root: Path, criterion_path: str | Path) -> str:
    """The catalog gate id (`prose/source-residue`) for a gate; else the repository path without `.md`."""
    path = PurePosixPath(_posix(criterion_path, label="criterion"))
    if path.is_relative_to(GATES):
        path = path.relative_to(GATES)
    return path.with_suffix("").as_posix() if path.suffix == ".md" else path.as_posix()


def note_sha256(note_text: str, criterion_text: str) -> str:
    """SHA-256 over the note parts the criterion watches, or over the whole note.

    The whole note is hashed when the criterion declares no valid `watches:`
    or the note's frontmatter does not parse. The parts are JSON-encoded, so
    part content cannot forge a part boundary.
    """
    watches = gate_watches(criterion_text)
    parts = note_parts(note_text) if watches is not None else None
    if parts is None:
        data = note_text
    else:
        data = PARTS_DOMAIN + json.dumps([[key, parts[key]] for key in sorted(watches)],
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
                  criterion=_posix(criterion, label="criterion"), criterion_sha256=criterion_sha256(criterion_text),
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


def _check(root: Path, note: str | Path, criterion: str | Path) -> tuple[Freshness, Result | None]:
    note, criterion = _posix(note, label="note"), _posix(criterion, label="criterion")
    path = result_path(root, note, criterion_id(root, criterion))
    if not path.is_file():
        return Freshness("missing"), None
    result = read_result(path)
    if (result.note, result.criterion) != (note, criterion):
        raise ValueError(f"review result {path} records {result.note} and {result.criterion}, "
                         f"not {note} and {criterion}")
    criterion_text = _read(root / criterion)
    changed = tuple(name for name, same in (
        ("note", note_sha256(_read(root / note), criterion_text) == result.note_sha256),
        ("criterion", criterion_sha256(criterion_text) == result.criterion_sha256)) if not same)
    return Freshness("stale", changed) if changed else Freshness("fresh"), result


def freshness(root: Path, note: str | Path, criterion: str | Path) -> Freshness:
    """Whether the stored result for the pair still matches the note and the criterion."""
    return _check(root, note, criterion)[0]


def status(root: Path, pairs: Iterable[tuple[str | Path, str | Path]]) -> list[Row]:
    """One row per (note, criterion) pair, with the stored outcome and executor when there is a result."""
    rows = []
    for note, criterion in pairs:
        state, result = _check(root, note, criterion)
        row = Row(_posix(note, label="note"), _posix(criterion, label="criterion"), state)
        if result is not None:
            row = replace(row, outcome=result.outcome, profile=result.profile, model=result.model)
        rows.append(row)
    return rows


def orphaned(root: Path) -> list[Path]:
    """Stored result files whose note or criterion file no longer exists; removing one is deleting it."""
    results = root / RESULTS
    if not results.is_dir():
        return []
    found = []
    for path in sorted(path for path in results.rglob("*.md") if path.is_file()):  # note dirs end in .md
        result = read_result(path)
        if not (root / result.note).is_file() or not (root / result.criterion).is_file():
            found.append(path)
    return found

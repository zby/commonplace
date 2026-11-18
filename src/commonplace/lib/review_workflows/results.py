"""Review result files and their freshness.

A result is one reviewer's judgment of one note against one criterion, kept
at `kb/reports/state/review/results/<note-path>/<criterion-id>.md`. Its
frontmatter names both inputs with the SHA-256 of the text the judgment was
produced from, the outcome and the executor; its body is the reviewer's text.
A pair is fresh when its normalized input hashes and output-contract fingerprint
match the current files. When the operator rejected a finding of the pair at
a triage, the criterion hash also covers those finding decisions, which the
reviewer receives as an input; a new rejection therefore stales that pair
alone, and status names it as a changed criterion. Freshness requires no Git history; exact evidence
hashes remain distinct.

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
from functools import cached_property
from pathlib import Path, PurePosixPath
from typing import Any

from commonplace.lib import frontmatter
from commonplace.lib.library import (
    LIBRARY_IDENTITY_PREFIX,
    artifact_file,
    artifact_identity,
    is_library_identity,
)
from commonplace.lib.review_workflows import result_contract
from commonplace.lib.review_workflows.criteria import gates_dir

RESULTS = Path("kb/reports/state/review/results")
LIBRARY_ID_PREFIX = "commonplace/"
"""Where a library criterion outside the gate catalog keeps its results; repository criteria live under kb/."""
WATCHABLE = {"title", "description", "body"}
OUTCOMES = ("pass", "warn", "fail", "report")
PARTS_DOMAIN = "commonplace-review-watched-parts/1\n"
"""Prefix of a watched-parts hash input, so it never equals a whole note's text by design."""
DECISIONS_DOMAIN = "commonplace-review-finding-decisions/1\n"
"""Prefix of a criterion hash input that includes the operator's finding decisions on the pair."""


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
    body: str                         # report prose; raw worker frontmatter remains in the launch
    findings: list[dict]
    contract: str
    target_sha256: str
    target_capture: str
    observation: str
    contract_sha256: str
    raw_output: str
    raw_output_sha256: str
    attack_outcome: str | None = None


@dataclass(frozen=True)
class Freshness:
    state: str                        # "fresh", "missing" or "stale"
    changed: tuple[str, ...] = ()     # stale inputs: note, criterion, output-contract


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
         "model": "model", "run": "run", "launch": "launch", "completed-at": "completed_at",
         "findings": "findings", "contract": "contract", "target-sha256": "target_sha256",
         "target-capture": "target_capture", "observation": "observation", "contract-sha256": "contract_sha256",
         "raw-output": "raw_output", "raw-output-sha256": "raw_output_sha256"}


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
    note_text = note_text.replace("\r\n", "\n").replace("\r", "\n")
    watched = watches(criterion_text)
    parts = note_parts(note_text) if watched is not None else None
    if parts is None:
        data = note_text
    else:
        data = PARTS_DOMAIN + json.dumps([[key, parts[key]] for key in sorted(watched)],
                                         ensure_ascii=False, default=repr)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def criterion_sha256(criterion_text: str, finding_decisions: str | None = None) -> str:
    """SHA-256 of the criterion text, or, for a pair with finding decisions, of the text and those decisions.

    `finding_decisions` is the review input of the operator's rejected
    findings of the pair (`decisions.review_inputs()`). Without it the hash
    is the plain hash of the criterion text, as it always was, so a pair the
    operator rejected nothing on keeps its stored hash. With it, the inputs
    are JSON-encoded behind a domain prefix, so the hash never equals a plain
    criterion hash by design.
    """
    text = criterion_text.replace("\r\n", "\n").replace("\r", "\n")
    if finding_decisions is None:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()
    data = DECISIONS_DOMAIN + json.dumps([text, finding_decisions.replace("\r\n", "\n")], ensure_ascii=False)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


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
                body: str, findings: list[dict], evidence: dict[str, str],
                contract: str = "verdict", attack_outcome: str | None = None) -> Result:
    """Build one result; callers supply retained evidence, never synthesized provenance."""
    return Result(note=_posix(note, label="note"), note_sha256=note_sha256(note_text, criterion_text),
                  criterion=_identity(criterion), criterion_sha256=criterion_sha256(criterion_text),
                  outcome=outcome, profile=dict(profile), model=model, run=run, launch=launch,
                  completed_at=completed_at, body=body, findings=findings, contract=contract,
                  attack_outcome=attack_outcome, **evidence)


def result_text(result: Result) -> str:
    data = {"type": result_contract.TYPE, "format": result_contract.FORMAT,
            "description": f"Retained {result.contract} review of {result.note} against {result.criterion}",
            **{key: getattr(result, field) for key, field in _KEYS.items()}}
    if result.attack_outcome is not None:
        data["attack-outcome"] = result.attack_outcome
    return result_contract.render(data, result.body)


def from_candidate(candidate: result_contract.Candidate) -> Result:
    return Result(**{field: candidate.data[key] for key, field in _KEYS.items()},
                  attack_outcome=candidate.data.get("attack-outcome"), body=candidate.body)


def write_result(root: Path, result: Result) -> Path:
    """Validate and atomically publish the current view of a retained result."""
    target = result_path(root, result.note, criterion_id(root, result.criterion))
    text = result_text(result)
    result_contract.validate_saved(root, target, text)
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_name(f".{target.name}.{uuid.uuid4().hex[:6]}.tmp")
    tmp.write_bytes(text.encode("utf-8"))
    tmp.replace(target)
    return target


def read_result(path: Path, *, context: result_contract.ValidationContext | None = None) -> Result:
    """Read the single supported result format; old state must be archived."""
    text = path.read_bytes().decode("utf-8")
    resolved = path.resolve()
    root = context.root if context is not None else next(
        (parent for parent in resolved.parents if resolved.is_relative_to(parent / RESULTS)), None)
    if root is None or not resolved.is_relative_to(root / RESULTS):
        raise ValueError(f"review result is outside the current result tree: {path}")
    try:
        result_contract.validate_saved(root, path, text, context=context)
        data = frontmatter.parse(text).data
        return Result(**{field: data[key] for key, field in _KEYS.items()},
                      attack_outcome=data.get("attack-outcome"), body=frontmatter.strip(text))
    except ValueError as error:
        raise ValueError(f"unreadable review result {path}: {error}") from error


def parse_result(text: str) -> Result:
    """The result a retained copy of a result file holds, such as a rewrite's `review-<n>.md`, without validation.

    `write_result()` validates it before it is stored.
    """
    data = frontmatter.parse(text).data
    return Result(**{field: data[key] for key, field in _KEYS.items()}, attack_outcome=data.get("attack-outcome"),
                  body=frontmatter.strip(text))


class _ReadContext:
    """Scan-local inputs; creating an empty/missing-result scan does no schema work."""

    def __init__(self, root: Path):
        self.root = root
        self.texts: dict[Path, str] = {}
        self.decided: dict[str, dict[str, str]] = {}

    @cached_property
    def validation(self) -> result_contract.ValidationContext:
        return result_contract.ValidationContext(self.root)

    def finding_decisions(self, note: str, criterion: str) -> str | None:
        """The pair's review input of the operator's rejected findings; None without a rejection."""
        if note not in self.decided:
            # decisions reads answers files through edits, which imports this module.
            from commonplace.lib.review_workflows import decisions
            self.decided[note] = decisions.review_inputs(self.root, note)
        return self.decided[note].get(criterion)


def _check(root: Path, note: str | Path, criterion: str | Path,
           context: _ReadContext) -> tuple[Freshness, Result | None, Path]:
    note, criterion = _posix(note, label="note"), _identity(criterion)
    path = result_path(root, note, criterion_id(root, criterion))
    if not path.is_file():
        return Freshness("missing"), None, path
    result = read_result(path, context=context.validation)
    if (result.note, result.criterion) != (note, criterion):
        raise ValueError(f"review result {path} records {result.note} and {result.criterion}, "
                         f"not {note} and {criterion}")
    return _freshness(root, result, context), result, path


def _freshness(root: Path, result: Result, context: _ReadContext) -> Freshness:
    """Compare against this scan's inputs and already validated contract."""
    texts = context.texts
    def text(path: Path) -> str:
        if path not in texts:
            texts[path] = _read(path)
        return texts[path]
    criterion_text = text(criterion_file(root, result.criterion))
    changed = tuple(name for name, same in (
        ("note", note_sha256(text(root / result.note), criterion_text) == result.note_sha256),
        ("criterion", criterion_sha256(criterion_text, context.finding_decisions(result.note, result.criterion))
         == result.criterion_sha256),
        ("output-contract", result.contract_sha256 == context.validation.fingerprint)) if not same)
    return Freshness("stale", changed) if changed else Freshness("fresh")


def freshness(root: Path, note: str | Path, criterion: str | Path) -> Freshness:
    """Whether the stored result for the pair still matches the note and the criterion."""
    return _check(root, note, criterion, _ReadContext(root))[0]


def _row(result: Result, state: Freshness, path: Path) -> Row:
    return Row(result.note, result.criterion, state, result.outcome, result.profile, result.model, path)


def status(root: Path, pairs: Iterable[tuple[str | Path, str | Path]]) -> list[Row]:
    """One row per (note, criterion) pair, with the stored outcome and executor when there is a result."""
    rows = []
    context = _ReadContext(root)
    for note, criterion in pairs:
        state, result, path = _check(root, note, criterion, context)
        rows.append(_row(result, state, path) if result is not None
                    else Row(_posix(note, label="note"), _identity(criterion), state))
    return rows


def _stored_files(root: Path, context: _ReadContext) -> Iterator[tuple[Path, Result]]:
    results = root / RESULTS
    if not results.is_dir():
        return
    for path in sorted(path for path in results.rglob("*.md") if path.is_file()):  # note dirs end in .md
        yield path, read_result(path, context=context.validation)


def _is_orphan(root: Path, result: Result) -> bool:
    try:
        return not (root / result.note).is_file() or not criterion_file(root, result.criterion).is_file()
    except ValueError:                    # an identity that no longer resolves in this library
        return True


def orphaned(root: Path) -> list[Path]:
    """Stored result files whose note or criterion file no longer exists; removing one is deleting it."""
    return [path for path, result in _stored_files(root, _ReadContext(root)) if _is_orphan(root, result)]


def stored(root: Path) -> tuple[list[Row], list[Path]]:
    """Every stored result once: rows for those whose inputs exist, and the orphaned result files.

    Each note and criterion file is read once however many results name it.
    """
    rows, orphans = [], []
    context = _ReadContext(root)
    for path, result in _stored_files(root, context):
        if _is_orphan(root, result):
            orphans.append(path)
        else:
            rows.append(_row(result, _freshness(root, result, context), path))
    return rows, orphans


def note_rows(root: Path, note: str | Path) -> list[Row]:
    """A row for each stored result of one note whose criterion still exists, read from the note's result directory."""
    note = _posix(note, label="note")
    base = root / RESULTS / note
    if not base.is_dir():
        return []
    rows = []
    context = _ReadContext(root)
    for path in sorted(path for path in base.rglob("*.md") if path.is_file()):
        result = read_result(path, context=context.validation)
        if result.note == note and not _is_orphan(root, result):
            rows.append(_row(result, _freshness(root, result, context), path))
    return rows


def summarize(root: Path) -> Summary:
    """Counts over every stored result: fresh, stale and orphaned, and the fresh warn and fail outcomes."""
    rows, orphans = stored(root)
    fresh = [row for row in rows if row.freshness.state == "fresh"]
    return Summary(results=len(rows) + len(orphans), fresh=len(fresh), stale=len(rows) - len(fresh),
                   orphaned=len(orphans), warn=sum(row.outcome == "warn" for row in fresh),
                   fail=sum(row.outcome == "fail" for row in fresh))

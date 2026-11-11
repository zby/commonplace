"""Draft one ingest report as a candidate and publish it when it is accepted.

The ingest skill hands drafting to a fresh worker. The worker writes a
candidate in an ignored working directory; the ingest in ``kb/sources/`` is not
touched until the candidate passes every deterministic check. ``prepare_handoff``
guards the target and writes the handoff record, which keeps the facts of the
run that a report does not carry: the snapshot checksum at dispatch, the
incumbent's hash, the occasion that was supplied. ``verify_handoff`` checks the
candidate against the record and the incumbent. ``publish_handoff`` copies an
accepted candidate to its destination; ``close_handoff`` ends a run without
publishing.

The working directory outlives the run. Its record keeps every handoff check
and how the run ended, so the directories are the operational record of
ingest drafting. ``prune_published`` deletes old published runs.

Keeping finished runs is provisional. The records exist to decide whether the
ingest skill keeps its repair round; the end condition is in
kb/work/decision-lifecycle-evidence/ingest-working-directory.md.

Rules that hold for an ingest at any time are ordinary validation
(``validate_ingest_contract``). A handoff treats their warnings, and dead
links, as failures.
"""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import yaml

from commonplace.lib import frontmatter
from commonplace.lib.candidate import (
    PublicationRefused,
    exact_sha256,
    publish_candidate,
    validate_at_destination,
)
from commonplace.lib.quote_verification import INGEST_QUOTES_HEADING_RE, NEXT_H2_RE
from commonplace.lib.snapshot import snapshot_sha256
from commonplace.lib.validation import (
    EMPTY_INGEST_QUOTES_SENTENCE,
    INGEST_CONTRACT_LABEL,
    name_paired_snapshot,
    run_validation,
)

RECORD_SCHEMA = "commonplace.ingest-handoff.v2"
RECORD_NAME = "handoff.yaml"
CANDIDATE_NAME = "candidate.md"
RETAINED_QUOTES_NAME = "retained-quotes.md"
# Local, ignored and owned by this workflow (see kb/reports/COLLECTION.md).
WORKING_ROOT = Path("kb/reports/state/ingest")
CANONICAL_EMPTY_QUOTES = f"## Quotes\n\n{EMPTY_INGEST_QUOTES_SENTENCE}\n\n"
RETIRED_FIELDS = ("source_snapshot", "code_revisions")
# Validation warnings that refuse a handoff: a published ingest must not carry them.
BLOCKING_WARNING_LABELS = (f"{INGEST_CONTRACT_LABEL}:", "link health:")

_CODE_GROUNDING_HEADING_RE = re.compile(r"^## Code Grounding[ \t]*$", re.MULTILINE)
_LABEL_PREFIX_RE = re.compile(r"^\[[^\]]+\]\s*")


class HandoffError(Exception):
    """The handoff cannot start or finish; the ingest was left as it was."""


@dataclass(frozen=True)
class HandoffRecord:
    """Facts of one drafting run that the candidate is checked against."""

    path: Path
    ingest: Path
    snapshot_sha256: str
    incumbent_sha256: str | None = None
    occasion: str | None = None
    code_grounded: bool = False
    created_snapshot: bool = False
    # None while the run is open, then "published" or "closed".
    outcome: str | None = None
    ended: datetime | None = None

    @property
    def candidate(self) -> Path:
        return self.path.parent / CANDIDATE_NAME

    @property
    def retained_quotes_path(self) -> Path:
        return self.path.parent / RETAINED_QUOTES_NAME


@dataclass
class HandoffResult:
    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    snapshot_sha256: str | None = None


def read_exact(path: Path) -> str:
    """Decode a file without newline translation, so text equality is byte equality."""
    return path.read_bytes().decode("utf-8")


def quotes_blocks(content: str) -> list[str]:
    """Return every Quotes block: its heading through the byte before the next H2."""
    blocks = []
    for heading in INGEST_QUOTES_HEADING_RE.finditer(content):
        following = NEXT_H2_RE.search(content, heading.end())
        end = following.start() if following is not None else len(content)
        blocks.append(content[heading.start() : end])
    return blocks


def retained_quotes_from_incumbent(content: str) -> str:
    """Return the Quotes block a refresh must keep; an absent block is the empty one."""
    blocks = quotes_blocks(content)
    if len(blocks) > 1:
        raise HandoffError(f"incumbent has {len(blocks)} Quotes blocks; expected zero or one")
    return blocks[0] if blocks else CANONICAL_EMPTY_QUOTES


def _retained_quotes(ingest: Path) -> str:
    return retained_quotes_from_incumbent(read_exact(ingest)) if ingest.is_file() else CANONICAL_EMPTY_QUOTES


def working_directory(ingest: Path, *, repo_root: Path) -> Path:
    return repo_root / WORKING_ROOT / ingest.name[: -len(".ingest.md")]


def prepare_handoff(
    ingest: Path,
    *,
    repo_root: Path,
    occasion: str | None = None,
    code_grounded: bool = False,
    created_snapshot: bool = False,
) -> HandoffRecord:
    """Guard an ingest target and open its working directory.

    Every guard runs before anything is written, and the ingest is never
    written here.
    """
    ingest = ingest.resolve()
    repo_root = repo_root.resolve()
    if not ingest.name.endswith(".ingest.md"):
        raise HandoffError(f"{ingest.name} is not an .ingest.md path")
    if not ingest.is_relative_to(repo_root):
        raise HandoffError(f"{ingest} is outside {repo_root}")
    snapshot = name_paired_snapshot(ingest)
    if not snapshot.is_file():
        raise HandoffError(
            f"snapshot not available on this machine: expected {snapshot}. "
            "Do not recapture; a new capture cannot reproduce the pinned bytes."
        )
    checksum = snapshot_sha256(snapshot)

    retained = CANONICAL_EMPTY_QUOTES
    if ingest.is_file():
        content = read_exact(ingest)
        metadata = frontmatter.parse(content).data
        retired = [name for name in RETIRED_FIELDS if name in metadata]
        if retired:
            raise HandoffError(f"incumbent carries retired fields: {', '.join(retired)}")
        snapshot_source = frontmatter.parse(read_exact(snapshot)).data.get("source")
        if (
            isinstance(snapshot_source, str)
            and snapshot_source.startswith(("http://", "https://"))
            and metadata.get("source") != snapshot_source
        ):
            raise HandoffError(
                f"incumbent source {metadata.get('source')!r} differs from the "
                f"snapshot's source {snapshot_source!r}"
            )
        recorded = metadata.get("snapshot_sha256")
        if recorded != checksum:
            raise HandoffError(
                f"snapshot checksum {checksum} differs from the incumbent's "
                f"snapshot_sha256 {recorded} ({snapshot} against {ingest}). An ingest's "
                "snapshot_sha256 is immutable; a changed observation is a new ingest. "
                "Read and execute the Commonplace library instruction re-ingest "
                f"with Target: {ingest}."
            )
        retained = retained_quotes_from_incumbent(content)

    directory = working_directory(ingest, repo_root=repo_root)
    if directory.exists():
        if _is_open(directory, repo_root=repo_root):
            raise HandoffError(
                f"an unfinished ingest run exists at {directory}. Inspect it, then end it with "
                f"`commonplace-ingest-handoff close {directory / RECORD_NAME}` before starting again."
            )
        # Only the last run of an ingest is kept.
        shutil.rmtree(directory)
    directory.mkdir(parents=True)
    fields: dict[str, Any] = {
        "schema": RECORD_SCHEMA,
        "ingest": ingest.relative_to(repo_root).as_posix(),
        "snapshot_sha256": checksum,
        "incumbent_sha256": exact_sha256(ingest),
        "code_grounded": code_grounded,
        "created_snapshot": created_snapshot,
        "opened": _now(),
    }
    if occasion is not None:
        fields["occasion"] = occasion
    # A convenience copy for the worker; verification reads the incumbent itself.
    (directory / RETAINED_QUOTES_NAME).write_bytes(retained.encode("utf-8"))
    record = directory / RECORD_NAME
    record.write_text(yaml.safe_dump(fields, sort_keys=False, allow_unicode=True), encoding="utf-8")
    return load_record(record, repo_root=repo_root)


def _now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def _read_fields(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        raise HandoffError(f"cannot read handoff record {path}: {error}") from error
    if not isinstance(data, dict) or data.get("schema") != RECORD_SCHEMA:
        raise HandoffError(f"{path} is not a {RECORD_SCHEMA} record")
    return data


def _write_fields(path: Path, data: dict[str, Any]) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def _is_open(directory: Path, *, repo_root: Path) -> bool:
    """A directory without a readable finished record counts as an open run."""
    try:
        return load_record(directory / RECORD_NAME, repo_root=repo_root).outcome is None
    except HandoffError:
        return True


def load_record(path: Path, *, repo_root: Path) -> HandoffRecord:
    path = path.resolve()
    data = _read_fields(path)
    try:
        ended = data.get("ended")
        return HandoffRecord(
            path=path,
            ingest=(repo_root.resolve() / data["ingest"]).resolve(),
            snapshot_sha256=data["snapshot_sha256"],
            incumbent_sha256=data.get("incumbent_sha256"),
            occasion=data.get("occasion"),
            code_grounded=bool(data.get("code_grounded", False)),
            created_snapshot=bool(data.get("created_snapshot", False)),
            outcome=data.get("outcome"),
            ended=datetime.fromisoformat(ended) if ended else None,
        )
    except (KeyError, ValueError) as error:
        raise HandoffError(f"handoff record {path} is incomplete: missing {error}") from error


def _first_difference(expected: str, actual: str) -> str:
    left, right = expected.encode("utf-8"), actual.encode("utf-8")
    offset = next(
        (i for i, (a, b) in enumerate(zip(left, right)) if a != b),
        min(len(left), len(right)),
    )
    return (
        f"first difference at byte {offset} of the block "
        f"(retained {len(left)} bytes, candidate {len(right)} bytes)"
    )


def _collapse(text: str) -> str:
    return " ".join(text.split())


def verify_handoff(record: HandoffRecord, *, repo_root: Path) -> HandoffResult:
    """Run every deterministic acceptance check on the record's candidate."""
    result = HandoffResult()
    candidate, ingest = record.candidate, record.ingest
    if not candidate.is_file() or candidate.stat().st_size == 0:
        result.failures.append(f"candidate: {candidate} is missing or empty")
        return result

    if exact_sha256(ingest) != record.incumbent_sha256:
        result.failures.append(
            f"incumbent: {ingest.name} changed since the handoff opened; "
            "the candidate was drafted against other bytes"
        )
        return result

    content = read_exact(candidate)
    metadata = frontmatter.parse(content).data

    snapshot = name_paired_snapshot(ingest)
    if not snapshot.is_file():
        result.failures.append(f"snapshot: name-paired .snapshots/{snapshot.name} is missing")
    else:
        actual = snapshot_sha256(snapshot)
        result.snapshot_sha256 = actual
        if actual != record.snapshot_sha256:
            result.failures.append(
                "snapshot: bytes changed since dispatch; "
                f"expected {record.snapshot_sha256}, found {actual}"
            )
        recorded = metadata.get("snapshot_sha256")
        if recorded != record.snapshot_sha256:
            result.failures.append(
                f"snapshot: candidate snapshot_sha256 is {recorded}, "
                f"but the handoff pinned {record.snapshot_sha256}"
            )

    retained = _retained_quotes(ingest)
    blocks = quotes_blocks(content)
    if len(blocks) != 1:
        result.failures.append(f"quotes: expected exactly one Quotes block, found {len(blocks)}")
    elif blocks[0] != retained:
        result.failures.append(
            "quotes: the block does not equal the retained Quotes; "
            f"{_first_difference(retained, blocks[0])}"
        )

    recorded_occasion = metadata.get("occasion")
    if record.occasion is None:
        if "occasion" in metadata:
            result.failures.append("occasion: field is present, but no occasion was supplied")
    elif not isinstance(recorded_occasion, str) or _collapse(recorded_occasion) != _collapse(
        record.occasion
    ):
        result.failures.append("occasion: field does not equal the supplied occasion")

    has_secondary = "secondary_sources" in metadata
    has_section = _CODE_GROUNDING_HEADING_RE.search(content) is not None
    if record.code_grounded:
        if not has_secondary:
            result.failures.append("code grounding: secondary_sources is missing")
        if not has_section:
            result.failures.append("code grounding: '## Code Grounding' section is missing")
    else:
        if has_secondary:
            result.failures.append("code grounding: secondary_sources is present without code grounding")
        if has_section:
            result.failures.append("code grounding: '## Code Grounding' is present without code grounding")

    outcomes = [("validation", validate_at_destination(candidate.read_bytes(), ingest, repo_root=repo_root))]
    if record.created_snapshot and snapshot.is_file():
        resolved = snapshot.resolve()
        outcomes.append((
            f"validation ({snapshot.name})",
            run_validation((resolved,), repo_root=repo_root).results.get(resolved),
        ))
    for label, outcome in outcomes:
        if outcome is None:
            result.failures.append(f"{label}: not analysed")
            continue
        result.failures.extend(f"{label}: {message}" for message in outcome.fails)
        for message in outcome.warns:
            blocking = _LABEL_PREFIX_RE.sub("", message).startswith(BLOCKING_WARNING_LABELS)
            (result.failures if blocking else result.warnings).append(f"{label}: {message}")
    return result


def shown_path(path: Path, repo_root: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except ValueError:
        return str(path)


def print_handoff_result(record: HandoffRecord, result: HandoffResult, *, repo_root: Path) -> None:
    """Print the verdict; the failure lines are what a repair worker receives."""
    checksum = f" (snapshot_sha256 {result.snapshot_sha256})" if result.snapshot_sha256 else ""
    verdict = "HANDOFF FAILED" if result.failures else "HANDOFF CLEAN"
    print(
        f"{verdict}: {shown_path(record.candidate, repo_root)} "
        f"for {shown_path(record.ingest, repo_root)}{checksum}"
    )
    for failure in result.failures:
        print(f"- {failure}")
    if result.warnings:
        print("WARNINGS (not handoff failures):")
        for warning in result.warnings:
            print(f"- {warning}")


def _require_open(record: HandoffRecord) -> None:
    if record.outcome is not None:
        raise HandoffError(f"the run at {record.path.parent} already ended ({record.outcome})")


def check_handoff(record: HandoffRecord, *, repo_root: Path) -> HandoffResult:
    """Verify the candidate and append the verdict to the record's ``checks``."""
    _require_open(record)
    result = verify_handoff(record, repo_root=repo_root)
    data = _read_fields(record.path)
    data.setdefault("checks", []).append({"at": _now(), "failures": list(result.failures)})
    _write_fields(record.path, data)
    return result


def _end(record: HandoffRecord, outcome: str) -> None:
    data = _read_fields(record.path)
    data["outcome"] = outcome
    data["ended"] = _now()
    _write_fields(record.path, data)


def close_handoff(record: HandoffRecord) -> None:
    """End the run without publishing; the candidate stays for inspection."""
    _require_open(record)
    _end(record, "closed")


def publish_handoff(record: HandoffRecord, *, repo_root: Path) -> HandoffResult:
    """Publish the candidate if it is clean and end the run.

    The check runs again here, so only bytes that pass it reach the library.
    A candidate with failures is left in place for repair. A published
    candidate is deleted: it equals the ingest byte for byte.
    """
    result = check_handoff(record, repo_root=repo_root)
    if result.failures:
        return result
    try:
        publish_candidate(
            record.candidate, record.ingest, expected_incumbent_sha256=record.incumbent_sha256
        )
    except (PublicationRefused, OSError) as error:
        raise HandoffError(f"publication refused: {error}") from error
    _end(record, "published")
    record.candidate.unlink()
    return result


def prune_published(*, repo_root: Path, older_than_days: int) -> list[Path]:
    """Delete working directories of runs published at least that many days ago."""
    root = repo_root.resolve() / WORKING_ROOT
    cutoff = datetime.now().astimezone() - timedelta(days=older_than_days)
    removed = []
    for record_path in sorted(root.glob(f"*/{RECORD_NAME}")):
        try:
            record = load_record(record_path, repo_root=repo_root)
        except HandoffError:
            continue
        if record.outcome == "published" and record.ended is not None and record.ended <= cutoff:
            shutil.rmtree(record_path.parent)
            removed.append(record_path.parent)
    return removed

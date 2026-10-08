"""Pinned new-engine assembly and publication; never manufacture legacy state.

Whole-set validation uses closed criterion and member snapshots and refuses
missing dependencies. Effect recovery
is independent of engine attempt commits and never infers success from an overview
alone. Only complete dispositions replace a public set.
"""
from __future__ import annotations

import json
import os
import re
import shutil
from collections.abc import Mapping
from hashlib import sha256
from pathlib import Path

import yaml

from commonplace.lib.agentic_analysis.boundary import boundary_refusals
from commonplace.lib.agentic_analysis.guards import (
    atomic_write,
    inspect_destination,
    publication_lock,
)
from commonplace.lib.agentic_analysis.handlers import (
    _locate,
    _opened_environment,
    _require_opened_method,
)
from commonplace.lib.agentic_analysis.records import amendment_index
from commonplace.lib.agentic_analysis.sets import (
    ARCHIVE_ROOT,
    RETAINED_ROOT,
    SET_TYPE,
    source_slug,
)
from commonplace.lib.agentic_analysis.validation import criterion_bytes
from commonplace.lib.directory_artifact import MANIFEST_NAME, UniqueKeyLoader
from commonplace.lib.note_parser import parse_document
from commonplace.lib.validation import validate_pinned_analysis_set
from commonplace.workflow import CodeAttempt, UncertainEffectError

JOURNAL = "effects/publish.json"
PRODUCERS = {
    "boundary": ("boundary", "boundary"), "runtime": ("runtime", "report"),
    "memory": ("memory", "report"), "epistemic": ("epistemic", "report"),
    "reconciliation": ("reconcile", "reconciliation"),
    "record-verification": ("verify", "verification"),
    "memory-profile": ("profile", "profile"),
    "profile-verification": ("verify-profile", "verification"),
    "synthesis": ("synthesize", "synthesis"),
    "synthesis-verification": ("verify-synthesis", "verification"),
}
IDENTITY_FIELDS = (
    "run-id", "result-disposition", "target-class", "boundary-kind",
    "reviewed-boundary", "analysis-cutoff", "evidence-tier",
)


def _digest(data: bytes) -> str:
    return sha256(data).hexdigest()


def _json(data: bytes | None, label: str) -> dict:
    if data is None:
        raise ValueError(f"{label} requires a declared present input")
    value = json.loads(data)
    if not isinstance(value, dict):
        raise TypeError(f"{label} must be an object")
    return value


def _document(data: bytes):
    document, error = parse_document(data.decode("utf-8"))
    if error or document is None or document.frontmatter is None:
        raise ValueError(f"unparseable typed member: {error}")
    return document


def _accepted(data: bytes | None, version: str, relation: str | None = None,
              other_version: str | None = None) -> bool:
    # The judgment address resolves only holding acceptances of current members.
    # Its canonical claim carries versions, not the private judgment record.
    if data is None:
        return False
    claim = _json(data, "acceptance")
    return (claim.get("outcome") == "accepted" and claim.get("subject") == version
            and (relation is None or [relation, other_version] in claim.get("scope", [])))


def _snapshot(attempt: CodeAttempt, *, overview: bool):
    layout, relations = attempt.layout, attempt.relations
    members = {}
    documents = {}
    for role in layout.roles:
        if role == "overview" and not overview:
            continue
        data = attempt.read(role)
        if data is not None:
            members[role] = data
            documents[layout.path(role)] = _document(data)
    required, permitted = layout.requirement(documents)
    if not overview:
        required -= {"overview"}
    if not required <= members.keys() or (permitted is not None and not members.keys() <= permitted):
        raise ValueError("disposition-dependent membership is incomplete or forbidden")
    boundary = documents.get(layout.path("boundary"))
    if boundary is None or boundary.frontmatter.get("result-disposition") not in (
            "complete", "blocked", "out-of-scope"):
        raise ValueError("a classified boundary is required")
    for role, data in members.items():
        if not _accepted(attempt.read(f"{role}-accepted"), _digest(data)):
            raise ValueError(f"{role} lacks a holding acceptance of its pinned member")
    for origin, partner, relation in relations:
        if origin not in members or partner not in members:
            continue
        if not any(_accepted(
            attempt.read(f"coverage-{relation.replace(':', '-')}-{end}"),
            _digest(members[end]), relation, _digest(members[other]),
        ) for end, other in ((origin, partner), (partner, origin))):
            raise ValueError(f"uncovered relation: {relation}")
    return layout, relations, members, boundary


def _provenance(attempt: CodeAttempt, members: Mapping[str, bytes]) -> dict:
    """Require completed producer records, including the memory analyst's identity.

    No metadata parameter or mutable run scan may substitute for coordinator-
    reported worker identity. The retained type currently allows one worker only.
    """
    workers = []
    for role, data in members.items():
        if role == "overview":
            continue  # Code-written, never a model worker.
        record = _json(attempt.read(f"{role}-attempt"), f"{role} producer attempt")
        producer, primary = PRODUCERS[role]
        # The member can be older than the producer's latest completed output,
        # so the digest ties the worker identity to the member actually published.
        if (record.get("kind") != "model"
                or record.get("job") != producer
                or record.get("outputs", {}).get(primary) != _digest(data)):
            raise ValueError(f"{role} provenance does not identify its completed output")
        model = record.get("model")
        effort = record.get("effort")
        if not isinstance(model, str) or not model.strip():
            raise ValueError(f"{role} provenance requires the coordinator-reported model")
        if effort is not None and (not isinstance(effort, str) or not effort.strip()):
            raise ValueError(f"{role} provenance has invalid effort")
        workers.append({"model": model, **({"effort": effort} if effort is not None else {})})
    if not workers or any(worker != workers[0] for worker in workers):
        raise ValueError("the retained manifest requires one identical worker identity across the run")
    return workers[0]


def validate_pinned_set(attempt: CodeAttempt, *, repo: Path, members: Mapping[str, bytes],
                        manifest: bytes) -> None:
    """Validate all exact member, manifest and criterion bytes; never forge legacy state."""
    boundary = _document(members["boundary.md"])
    result = validate_pinned_analysis_set(
        repo=repo, intended_set_path=attempt.run_dir / "set", members=members,
        manifest=manifest, criteria=criterion_bytes(attempt),
        frozen_source=boundary.frontmatter.get("source"),
    )
    if result.fails:
        raise ValueError("pinned set validation failed: " + "; ".join(result.fails))
    # Assembly's current receipt cannot faithfully retain per-member warnings.
    # Refuse rather than claim that a warning-bearing set passed unqualified.
    if result.warns:
        raise ValueError("pinned set validation warnings require review: " + "; ".join(result.warns))


def _manifest(layout, members: Mapping[str, bytes], worker: dict) -> bytes:
    return yaml.safe_dump({
        "type": SET_TYPE,
        "members": {layout.path(role): {"sha256": _digest(data)} for role, data in members.items()},
        "worker": worker,
    }, sort_keys=False).encode("utf-8")


def _environment(attempt: CodeAttempt, boundary, *, job: str, guard: bool = False):
    metadata, repo = (_opened_environment(attempt, attempt.read("metadata"), job=job) if guard
                      else _locate(attempt))
    source_bytes = attempt.read("source")
    if source_bytes is None:
        raise ValueError(f"{job} requires the pinned acquisition result")
    frozen = json.loads(source_bytes)
    if frozen is not None and (not isinstance(frozen, dict) or frozen.get("kind") != "git"):
        raise ValueError("acquisition result must be a Git source object or explicit JSON null")
    if boundary.frontmatter.get("result-disposition") == "complete" and not isinstance(
            boundary.frontmatter.get("source"), dict):
        raise ValueError("complete publication requires a frozen boundary source")
    reasons = boundary_refusals(
        attempt.read("boundary"), repo_root=repo, run_id=metadata["run-id"],
        identity=metadata["source-identity"], frozen=frozen,
        capture_directory=Path(metadata["capture-directory"]),
    )
    if reasons:
        raise ValueError("source/opening identity: " + "; ".join(reasons))
    if boundary.frontmatter.get("run-id") != metadata["run-id"]:
        raise ValueError("boundary must name the opened run")
    return metadata, repo


def assemble_analysis(attempt: CodeAttempt) -> dict[str, bytes]:
    """Assemble an entry and exact-byte manifest from declared members only."""
    layout, relations, members, boundary = _snapshot(attempt, overview=False)
    metadata, repo = _environment(attempt, boundary, job="assembly")
    worker = _provenance(attempt, members)
    fields = boundary.frontmatter
    disposition = fields["result-disposition"]
    description = (str(_document(members["synthesis"]).frontmatter["description"])
                   if disposition == "complete" else
                   f"Analysis of {metadata['system']} at {fields.get('reviewed-boundary') or 'no established boundary'}, "
                   f"with {disposition} disposition")
    frontmatter = {
        "type": layout.roles["overview"].type, "description": " ".join(description.split()),
        **{name: fields.get(name) for name in IDENTITY_FIELDS},
        "system": metadata["system"], "run-date": metadata["run-date"],
        "inputs-commit": metadata["inputs-commit"],
    }
    index = (amendment_index(_document(members["reconciliation"]).body) if "reconciliation" in members
             else "Amended or superseded records: none. Reconciliation was not reached.")
    links = "\n".join(f"- [{role}](./{layout.path(role)})" for role in members)
    targets = "\n".join(f"- `{layout.path(role)}`: deterministic snapshot checks passed."
                        for role in (*members, "overview"))
    body = (f"# {metadata['system']} agentic-system analysis\n\n## Members\n\n"
            f"Disposition: `{disposition}`. See the boundary for its stopping condition.\n\n{links}\n\n"
            f"## Amendment index\n\n{index}\n\n## Deterministic validation\n\n{targets}\n\n"
            "The exact manifest and cross-member checks passed; publication rechecks them. "
            "These are deterministic checks, not semantic certification.\n")
    overview = ("---\n" + yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True)
                + "---\n\n" + body).encode("utf-8")
    complete = {**members, "overview": overview}
    manifest = _manifest(layout, complete, worker)
    validate_pinned_set(attempt, repo=repo,
                        members={layout.path(r): b for r, b in complete.items()}, manifest=manifest)
    scope = tuple(relation for origin, partner, relation in relations
                  if "overview" in (origin, partner)
                  and (partner if origin == "overview" else origin) in members)
    attempt.judge("overview", outcome="accepted", scope=scope)
    return {"overview": overview, "manifest": manifest}


def _tree(path: Path) -> dict[str, bytes] | None:
    if not os.path.lexists(path):
        return None
    if path.resolve() != path or not path.is_dir():
        raise UncertainEffectError(f"publication tree redirects or is not a directory: {path}")
    result = {}
    for file in path.iterdir():
        if not file.is_file() or file.is_symlink():
            raise UncertainEffectError(f"unexpected publication tree entry: {file}")
        result[file.name] = file.read_bytes()
    return result


def _hashes(tree: Mapping[str, bytes] | None):
    return None if tree is None else {name: _digest(data) for name, data in sorted(tree.items())}


def _safe(path: Path) -> Path:
    if path.resolve() != path:
        raise UncertainEffectError(f"publication path must not traverse symlinks: {path}")
    return path


def _write_record(path: Path, record: dict) -> None:
    atomic_write(path, (json.dumps(record, sort_keys=True, indent=2) + "\n").encode())


def _publish_effect(*, run_dir: Path, destination: Path, archive_root: Path,
                    files: Mapping[str, bytes], expected: str, identity: str,
                    inspect_incumbent) -> dict:
    """Install exact bytes or recognize a journaled result; partial effects Stop.

    Caller holds publication_lock after any per-run engine lock, through journal
    recognition, incumbent inspection, mutation and rollback. Byte guards preserve
    detected unexpected writes, but cannot prevent TOCTOU from non-cooperating
    writers: those still require authority-level exclusivity.
    """
    destination, archive_root = _safe(destination), _safe(archive_root)
    journal = _safe(run_dir / JOURNAL)
    intent = {"version": 1, "run-id": run_dir.name, "destination": str(destination),
              "source-identity": identity, "expected": expected, "new": _hashes(files)}
    if journal.exists():
        try:
            record = json.loads(journal.read_bytes())
            if (not isinstance(record, dict) or any(record.get(k) != v for k, v in intent.items())
                    or set(record) != {*intent, "old", "archive", "state"}
                    or record["state"] not in ("started", "completed", "rolled-back")):
                raise ValueError("journal input identity or structure differs")
            old = record["old"]
            if old is not None and (not isinstance(old, dict) or "overview.md" not in old
                    or any(Path(name).name != name or not re.fullmatch(r"[0-9a-f]{64}", str(value))
                           for name, value in old.items())):
                raise ValueError("invalid old tree identity")
            if ("absent" if old is None else old["overview.md"]) != expected:
                raise ValueError("old tree differs from opened incumbent")
            if (old is None) != (record["archive"] is None):
                raise ValueError("archive and old tree disagree")
            archive = Path(record["archive"]) if record["archive"] else None
            if archive is not None and (archive.parent != archive_root or archive.name in ("", ".", "..")):
                raise ValueError("invalid archive path")
            now = _hashes(_tree(destination))
            archived = _hashes(_tree(_safe(archive))) if archive else None
            if now == intent["new"] and (old is None or archived == old):
                _write_record(journal, {**record, "state": "completed"})
                return {"state": "published", "destination": str(destination), "members": intent["new"]}
            if record["state"] == "completed":
                raise ValueError("completed publication no longer has its exact bytes")
            if now != old or archived is not None:
                raise ValueError("interrupted publication is not its exact old or completed state")
        except (OSError, ValueError, TypeError, KeyError) as error:
            raise UncertainEffectError(f"cannot establish publication outcome: {error}") from error
    else:
        record = None
    # Full incumbent validation and source ownership precede any effect.
    inspect_incumbent()
    old_tree = _tree(destination)
    actual = "absent" if old_tree is None else _digest(old_tree.get("overview.md", b""))
    if actual != expected:
        raise ValueError("publication destination changed since opening inspection")
    archive = None
    if old_tree is not None:
        old_id = _document(old_tree["overview.md"]).frontmatter.get("run-id")
        if not isinstance(old_id, str) or not re.fullmatch(r"AAS-[a-zA-Z0-9-]+", old_id) or old_id == run_dir.name:
            raise ValueError("replacement requires a different valid incumbent run ID")
        archive = _safe(archive_root / old_id)
        if os.path.lexists(archive):
            raise ValueError("archive destination already exists")
    if record is not None and (record["old"] != _hashes(old_tree)
                               or record["archive"] != (str(archive) if archive else None)):
        raise UncertainEffectError("incumbent differs from journaled starting bytes")
    record = {**intent, "old": _hashes(old_tree), "archive": str(archive) if archive else None, "state": "started"}
    _write_record(journal, record)
    moved = created = False
    try:
        if _tree(destination) != old_tree:
            raise ValueError("incumbent changed before mutation")
        if archive:
            archive.parent.mkdir(parents=True, exist_ok=True)
            destination.rename(archive)
            moved = True
        destination.mkdir(parents=True, exist_ok=False)
        created = True
        for name, data in files.items():
            if Path(name).name != name or name in (".", ".."):
                raise ValueError("publication members must be direct files")
            atomic_write(destination / name, data)
        if _tree(destination) != dict(files):
            raise UncertainEffectError("installed publication bytes differ")
        _write_record(journal, {**record, "state": "completed"})
    except Exception as error:
        try:
            if created:
                partial = _tree(destination)
                if partial is None or any(name not in files or data != files[name] for name, data in partial.items()):
                    raise ValueError("new tree has unexpected bytes; preserve it")
                shutil.rmtree(destination)
            if moved:
                if _hashes(_tree(archive)) != record["old"]:
                    raise ValueError("archive changed; preserve it")
                if os.path.lexists(destination):
                    raise ValueError("destination reappeared; preserve it and the archive")
                archive.rename(destination)
            if _tree(destination) != old_tree:
                raise ValueError("old state was not restored")
            _write_record(journal, {**record, "state": "rolled-back"})
        except Exception as rollback:  # noqa: BLE001 - any rollback failure leaves an uncertain effect
            raise UncertainEffectError(f"publication failed ({error}); rollback uncertain ({rollback})") from error
        raise
    return {"state": "published", "destination": str(destination), "members": intent["new"]}


def _prepare_publication(attempt: CodeAttempt):
    """Check pinned inputs and environment before journal reconciliation or mutation."""
    layout, _, members, boundary = _snapshot(attempt, overview=True)
    metadata, repo = _environment(attempt, boundary, job="publication", guard=True)
    worker = _provenance(attempt, members)
    manifest = attempt.read("manifest")
    if manifest is None:
        raise ValueError("publication requires assembly's pinned manifest")
    supplied = yaml.load(manifest, Loader=UniqueKeyLoader)
    if supplied != yaml.safe_load(_manifest(layout, members, worker)):
        raise ValueError("assembly manifest does not pin these exact members and provenance")
    files = {layout.path(role): data for role, data in members.items()}
    validate_pinned_set(attempt, repo=repo, members=files, manifest=manifest)
    _require_opened_method(repo, metadata, job="publication")
    if boundary.frontmatter["result-disposition"] != "complete":
        if os.path.lexists(attempt.run_dir / JOURNAL):
            raise UncertainEffectError("non-complete set has a publication effect journal")
        return None  # Accepted set remains local; no retained or archive output.
    destination = repo / RETAINED_ROOT / source_slug(metadata["source-identity"], metadata["system"])
    if metadata["review-path"] != (destination / layout.path("overview")).relative_to(repo).as_posix():
        raise ValueError("opened publication destination differs from the canonical source path")

    return metadata, repo, destination, {MANIFEST_NAME: manifest, **files}


def publish_analysis(attempt: CodeAttempt) -> dict[str, bytes]:
    """Publish a pinned complete set, or close a non-complete set without public mutation."""
    try:
        prepared = _prepare_publication(attempt)
    except UncertainEffectError:
        raise
    except Exception as error:
        # A guard can fail because an earlier attempt moved tracked files. Until
        # exact-tree reconciliation runs, even a rolled-back journal's label is
        # not proof of the current outcome. Preserve all evidence and the guard.
        if os.path.lexists(attempt.run_dir / JOURNAL):
            raise UncertainEffectError(
                f"cannot establish publication outcome: preliminary checks failed: {error}"
            ) from error
        raise
    if prepared is None:
        return {}
    metadata, repo, destination, files = prepared

    def inspect_incumbent():
        decision = inspect_destination(repo_root=repo, generated_destination=metadata["review-path"],
                                       source_identity=metadata["source-identity"])
        if decision["expected_incumbent_sha256"] != metadata["expected-incumbent-sha256"]:
            raise ValueError("publication destination changed since opening inspection")

    # The engine already holds the per-run lock. Never take it inside this lock.
    with publication_lock(repo):
        _publish_effect(run_dir=attempt.run_dir, destination=destination, archive_root=repo / ARCHIVE_ROOT,
                        files=files, identity=metadata["source-identity"],
                        expected=metadata["expected-incumbent-sha256"], inspect_incumbent=inspect_incumbent)
    return {}

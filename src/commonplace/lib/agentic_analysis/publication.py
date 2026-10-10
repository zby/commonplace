"""Pinned assembly and publication.

Whole-artifact validation uses closed criterion and member snapshots and refuses
missing dependencies. Effect recovery
is independent of engine attempt commits and never infers success from an overview
alone. Only complete dispositions replace a public artifact.
"""
from __future__ import annotations

import json
import os
import re
from collections.abc import Mapping
from hashlib import sha256
from pathlib import Path

import yaml

from commonplace.artifactrun import CodeAttempt, UncertainEffectError
from commonplace.artifactrun.checks import criterion_bytes
from commonplace.artifactrun.effects import hashes, install_tree
from commonplace.artifactrun.worktree import (
    preparation_for,
    require_run_code,
    require_running_package_unchanged,
    run_command,
    source_checkout,
)
from commonplace.lib.agentic_analysis.analyses import (
    ARCHIVE_ROOT,
    RETAINED_ROOT,
    source_slug,
)
from commonplace.lib.agentic_analysis.boundary import boundary_refusals
from commonplace.lib.agentic_analysis.guards import (
    inspect_destination,
    publication_lock,
    require_publishable_worktree,
)
from commonplace.lib.agentic_analysis.opening import locate
from commonplace.lib.agentic_analysis.records import amendment_index
from commonplace.lib.agentic_analysis.worktree import STATE_ROOT
from commonplace.lib.directory_artifact import MANIFEST_NAME, UniqueKeyLoader
from commonplace.lib.note_parser import parse_document
from commonplace.lib.validation import validate_pinned_artifact_snapshot

JOURNAL = "effects/publish.json"
PRODUCERS = {
    "boundary": ("boundary", "boundary"), "runtime": ("runtime", "report"),
    "memory": ("memory", "report"), "epistemic": ("epistemic", "report"),
    "reconciliation": ("reconciliation", "reconciliation"),
    "report-verification": ("report-verification", "verification"),
    "memory-profile": ("memory-profile", "profile"),
    "profile-verification": ("profile-verification", "verification"),
    "synthesis": ("synthesis", "synthesis"),
    "synthesis-verification": ("synthesis-verification", "verification"),
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


def _require_opened_method(repo: Path, metadata: dict, *, job: str) -> None:
    preparation = preparation_for(repo)
    if metadata["run-id"].rsplit("-", 2)[-2:-1] != [preparation["token"]]:
        raise ValueError(f"{job} preparation token differs from the opened run")
    commit = metadata.get("inputs-commit")
    if run_command(["git", "rev-parse", "HEAD"], cwd=repo) != commit or preparation.get("commit") != commit:
        raise ValueError(f"{job} worktree differs from the opened preparation commit")
    require_publishable_worktree(repo)
    require_running_package_unchanged(commit)


def _opened_environment(attempt: CodeAttempt, metadata_bytes: bytes | None, *, job: str) -> tuple[dict, Path]:
    if metadata_bytes is None:
        raise ValueError(f"{job} requires the opening metadata")
    metadata = json.loads(metadata_bytes)
    if not isinstance(metadata, dict) or metadata.get("run-id") != attempt.run_dir.name:
        raise ValueError(f"{job} opening metadata must name this run")
    repo = source_checkout(attempt.run_dir)
    if repo is None or attempt.run_dir.parent != repo / STATE_ROOT or attempt.library != repo / "kb":
        raise ValueError(f"{job} must use this run's analysis checkout and recorded library")
    require_run_code(attempt.run_dir, cwd=Path.cwd())
    _require_opened_method(repo, metadata, job=job)
    return metadata, repo


def _snapshot(attempt: CodeAttempt, *, overview: bool):
    # The required coverage input gates this job: the engine has established
    # that every required member is present, accepted and related as declared.
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
    boundary = documents.get(layout.path("boundary"))
    if boundary is None or boundary.frontmatter.get("result-disposition") not in (
            "complete", "blocked", "out-of-scope"):
        raise ValueError("a classified boundary is required")
    return layout, relations, members, boundary


def _provenance(attempt: CodeAttempt, members: Mapping[str, bytes], metadata: dict) -> dict:
    """The run's worker profile and the exact model its workers report.

    Opening resolved the profile the run started with; every worker uses it.
    A producer record that a coordinator reported with a model or effort must
    agree with it. Every producer must report the same model from its
    environment, which may be `not stated`. Reported effective effort must
    match the profile when available; unavailable effort remains explicit in
    the attempt record.
    """
    worker = metadata.get("worker")
    if not isinstance(worker, dict) or not all(
            isinstance(worker.get(field), str) and worker[field].strip()
            for field in ("profile", "harness", "launch-model", "effort")):
        raise ValueError("the opening metadata records no worker profile")
    reported = set()
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
        for field, profiled in (("model", "launch-model"), ("effort", "effort")):
            if record.get(field) is not None and record[field] != worker[profiled]:
                raise ValueError(f"{role} was reported with {field} {record[field]!r}, "
                                 f"not the run profile's {worker[profiled]!r}")
        effective_effort = record.get("worker_effort")
        if effective_effort not in (worker["effort"], "not stated"):
            raise ValueError(f"{role} reported worker effort {effective_effort!r}, "
                             f"not the run profile's {worker['effort']!r}")
        reported.add(record.get("worker_model"))
    if len(reported) != 1 or not all(isinstance(model, str) and model for model in reported):
        raise ValueError("every worker must report the same model; reported: "
                         + ", ".join(sorted(map(str, reported))))
    return {**worker, "model": reported.pop()}


def validate_pinned_artifact(attempt: CodeAttempt, *, repo: Path, members: Mapping[str, bytes],
                        manifest: bytes) -> None:
    """Validate all exact member, manifest and criterion bytes."""
    boundary = _document(members["boundary.md"])
    result = validate_pinned_artifact_snapshot(
        repo=repo, artifact_type=attempt.type_spec, intended_artifact_path=attempt.run_dir / "artifact", members=members,
        manifest=manifest, criteria=criterion_bytes(attempt),
        frozen_source=boundary.frontmatter.get("source"),
    )
    if result.fails:
        raise ValueError("pinned artifact validation failed: " + "; ".join(result.fails))
    # Assembly's current receipt cannot faithfully retain per-member warnings.
    # Refuse rather than claim that a warning-bearing artifact passed unqualified.
    if result.warns:
        raise ValueError("pinned artifact validation warnings require review: " + "; ".join(result.warns))


def _manifest(attempt: CodeAttempt, members: Mapping[str, bytes], worker: dict) -> bytes:
    layout = attempt.layout
    return yaml.safe_dump({
        "type": attempt.type_spec,
        "members": {layout.path(role): {"sha256": _digest(data)} for role, data in members.items()},
        "worker": worker,
    }, sort_keys=False).encode("utf-8")


def _environment(attempt: CodeAttempt, boundary, *, job: str, guard: bool = False):
    metadata, repo = (_opened_environment(attempt, attempt.read("metadata"), job=job) if guard
                      else locate(attempt))
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
    worker = _provenance(attempt, members, metadata)
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
    manifest = _manifest(attempt, complete, worker)
    validate_pinned_artifact(attempt, repo=repo,
                        members={layout.path(r): b for r, b in complete.items()}, manifest=manifest)
    scope = tuple(relation for origin, partner, relation in relations
                  if "overview" in (origin, partner)
                  and (partner if origin == "overview" else origin) in members)
    attempt.judge("overview", outcome="accepted", scope=scope)
    return {"overview": overview, "manifest": manifest}


def _archive_name(incumbent: Mapping[str, bytes], run_id: str) -> str:
    """An incumbent artifact is archived under its own run ID, never this run's."""
    old_id = _document(incumbent["overview.md"]).frontmatter.get("run-id")
    if not isinstance(old_id, str) or not re.fullmatch(r"AAS-[a-zA-Z0-9-]+", old_id) or old_id == run_id:
        raise ValueError("replacement requires a different valid incumbent run ID")
    return old_id


def _prepare_publication(attempt: CodeAttempt):
    """Check pinned inputs and environment before journal reconciliation or mutation."""
    layout, _, members, boundary = _snapshot(attempt, overview=True)
    metadata, repo = _environment(attempt, boundary, job="publication", guard=True)
    worker = _provenance(attempt, members, metadata)
    manifest = attempt.read("manifest")
    if manifest is None:
        raise ValueError("publication requires assembly's pinned manifest")
    supplied = yaml.load(manifest, Loader=UniqueKeyLoader)
    if supplied != yaml.safe_load(_manifest(attempt, members, worker)):
        raise ValueError("assembly manifest does not pin these exact members and provenance")
    files = {layout.path(role): data for role, data in members.items()}
    validate_pinned_artifact(attempt, repo=repo, members=files, manifest=manifest)
    _require_opened_method(repo, metadata, job="publication")
    if boundary.frontmatter["result-disposition"] != "complete":
        if os.path.lexists(attempt.run_dir / JOURNAL):
            raise UncertainEffectError("non-complete artifact has a publication effect journal")
        return None  # Accepted artifact remains local; no retained or archive output.
    destination = repo / RETAINED_ROOT / source_slug(metadata["source-identity"], metadata["system"])
    if metadata["review-path"] != (destination / layout.path("overview")).relative_to(repo).as_posix():
        raise ValueError("opened publication destination differs from the canonical source path")

    return metadata, repo, destination, {MANIFEST_NAME: manifest, **files}


def publish_analysis(attempt: CodeAttempt) -> dict[str, bytes]:
    """Publish a pinned complete artifact, or close a non-complete artifact without public mutation."""
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
        return {"receipt": _receipt(published=False)}
    metadata, repo, destination, files = prepared

    def inspect_incumbent():
        decision = inspect_destination(repo_root=repo, generated_destination=metadata["review-path"],
                                       source_identity=metadata["source-identity"])
        if decision["expected_incumbent_sha256"] != metadata["expected-incumbent-sha256"]:
            raise ValueError("publication destination changed since opening inspection")

    # The engine already holds the per-run lock. Never take it inside this lock.
    with publication_lock(repo):
        install_tree(journal=attempt.run_dir / JOURNAL, destination=destination,
                     archive_root=repo / ARCHIVE_ROOT, files=files, anchor="overview.md",
                     expected=metadata["expected-incumbent-sha256"],
                     identity={"run-id": attempt.run_dir.name, "source-identity": metadata["source-identity"]},
                     archive_name=lambda old: _archive_name(old, attempt.run_dir.name),
                     inspect_incumbent=inspect_incumbent)
    return {"receipt": _receipt(published=True, destination=str(destination), members=hashes(files),
                                **{name: metadata.get(name) for name in RECEIPT_PINS})}


RECEIPT_PINS = ("run-id", "inputs-commit", "system", "source-identity", "source", "source-revision",
                "expected-incumbent-sha256")


def _receipt(**fields) -> bytes:
    """What publication did, for consumers that read the job's current completion."""
    return (json.dumps(fields, sort_keys=True) + "\n").encode("utf-8")

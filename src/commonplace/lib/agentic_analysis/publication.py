"""Pinned assembly and publication.

Whole-artifact validation uses closed criterion and member snapshots and refuses
missing dependencies. Effect recovery
is independent of engine attempt commits and never infers success from an overview
alone. Only complete dispositions replace a public artifact.

Assembly and publication take plain values; the engine adapters live in
``handlers``. The publication reset hook reads engine run records directly.
"""
from __future__ import annotations

import json
import os
from collections.abc import Mapping
from contextlib import contextmanager
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

import yaml

from commonplace.artifactrun import UncertainEffectError
from commonplace.artifactrun.effects import hashes, install_tree, safe, tree
from commonplace.artifactrun.worktree import (
    preparation_for,
)
from commonplace.lib.agentic_analysis import run_ids
from commonplace.lib.agentic_analysis.analyses import (
    ARCHIVE_ROOT,
    CAPTURE_DIRECTORY,
    RETAINED_ROOT,
    publication_slug,
)
from commonplace.lib.agentic_analysis.boundary import acquired_source, boundary_refusals
from commonplace.lib.agentic_analysis.guards import (
    checkout,
    inspect_destination,
    publication_lock,
    require_prepared_method,
    run_checkout,
)
from commonplace.lib.agentic_analysis.records import amendment_index
from commonplace.lib.directory_artifact import MANIFEST_NAME, UniqueKeyLoader
from commonplace.lib.directory_layout import Layout
from commonplace.lib.note_parser import parse_document
from commonplace.lib.validation import validate_pinned_artifact_snapshot

JOURNAL = "effects/publish.json"


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
    if run_ids.run_token(metadata["run-id"]) != preparation["token"]:
        raise ValueError(f"{job} preparation token differs from the opened run")
    require_prepared_method(repo, metadata.get("inputs-commit"), preparation, job=job)


def _opened_environment(metadata: bytes | None, run_dir: Path, library: Path, *, job: str) -> tuple[dict, Path]:
    if metadata is None:
        raise ValueError(f"{job} requires the opening metadata")
    record = json.loads(metadata)
    if not isinstance(record, dict) or record.get("run-id") != run_dir.name:
        raise ValueError(f"{job} opening metadata must name this run")
    repo = run_checkout(run_dir, library, job=job)
    _require_opened_method(repo, record, job=job)
    return record, repo


def _classified_boundary(members: Mapping[str, bytes]):
    """The boundary member's document, which must carry a classified disposition.

    Every member must parse. The required coverage input gates the job: the
    engine has established that every required member is present, accepted
    and related as declared.
    """
    documents = {role: _document(data) for role, data in members.items()}
    boundary = documents.get("boundary")
    if boundary is None or boundary.frontmatter.get("result-disposition") not in (
            "complete", "blocked", "out-of-scope"):
        raise ValueError("a classified boundary is required")
    return boundary


@dataclass(frozen=True)
class Provenance:
    """The model that produced a role's published output, and that output's digest.

    `model` is the model actually used, as the harness records it (None when
    nothing recorded one). Until the artifact-run engine is retired, its adapter
    supplies the worker-reported model here. `output_sha256` is the digest of
    the completed primary output the record pins.
    """
    model: str | None
    output_sha256: str


def _provenance(members: Mapping[str, bytes], provenance: Mapping[str, Provenance], metadata: dict) -> dict:
    """The run's worker profile and the exact model its workers used.

    Opening resolved the worker profile the run started with; every worker is
    launched with its model and effort. Every producer record must name the same
    model actually used, as the harness records it (the engine adapter supplies
    the worker-reported model until the engine is retired).
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
        record = provenance.get(role)
        # The member can be older than the producer's latest completed output,
        # so the digest ties the model to the member actually published.
        if record is None or record.output_sha256 != _digest(data):
            raise ValueError(f"{role} provenance does not identify its completed output")
        reported.add(record.model)
    if len(reported) != 1 or not all(isinstance(model, str) and model for model in reported):
        raise ValueError("every worker must report the same model; reported: "
                         + ", ".join(sorted(map(str, reported))))
    return {**worker, "model": reported.pop()}


def validate_pinned_artifact(*, repo: Path, members: Mapping[str, bytes], manifest: bytes, layout: Layout,
                             type_spec: str, criteria: Mapping[str, bytes], run_dir: Path) -> None:
    """Validate all exact member, manifest and criterion bytes; members are keyed by path."""
    boundary = _document(members[layout.path("boundary")])
    result = validate_pinned_artifact_snapshot(
        repo=repo, artifact_type=type_spec, intended_artifact_path=run_dir / "artifact", members=members,
        manifest=manifest, criteria=criteria,
        frozen_source=boundary.frontmatter.get("source"),
    )
    if result.fails:
        raise ValueError("pinned artifact validation failed: " + "; ".join(result.fails))
    # Assembly's current receipt cannot faithfully retain per-member warnings.
    # Refuse rather than claim that a warning-bearing artifact passed unqualified.
    if result.warns:
        raise ValueError("pinned artifact validation warnings require review: " + "; ".join(result.warns))


def _manifest(layout: Layout, type_spec: str, members: Mapping[str, bytes], worker: dict) -> bytes:
    return yaml.safe_dump({
        "type": type_spec,
        "members": {layout.path(role): {"sha256": _digest(data)} for role, data in members.items()},
        "worker": worker,
    }, sort_keys=False).encode("utf-8")


def _environment(metadata: dict, repo: Path, boundary: bytes, source: bytes | None, run_dir: Path,
                 *, job: str) -> None:
    """Bind the boundary's source to the opened identity and the acquisition result."""
    frozen = acquired_source(source, job=job)
    fields = _document(boundary).frontmatter
    if fields.get("result-disposition") == "complete" and not isinstance(fields.get("source"), dict):
        raise ValueError("complete publication requires a frozen boundary source")
    reasons = boundary_refusals(
        boundary, repo_root=repo, identity=metadata["source-identity"], frozen=frozen,
        capture_directory=run_dir / CAPTURE_DIRECTORY,
    )
    if reasons:
        raise ValueError("source/opening identity: " + "; ".join(reasons))


def assemble_analysis(members: Mapping[str, bytes], *, metadata: bytes, source: bytes | None,
                      provenance: Mapping[str, Provenance], layout: Layout, type_spec: str,
                      criteria: Mapping[str, bytes], run_dir: Path) -> tuple[bytes, bytes]:
    """Assemble an overview and exact-byte manifest from the present role members only.

    ``members`` are by role, without the overview. Returns (overview, manifest).
    """
    boundary = _classified_boundary(members)
    opened, repo = json.loads(metadata), checkout(run_dir)
    _environment(opened, repo, members["boundary"], source, run_dir, job="assembly")
    worker = _provenance(members, provenance, opened)
    fields = boundary.frontmatter
    disposition = fields["result-disposition"]
    description = (str(_document(members["synthesis"]).frontmatter["description"])
                   if disposition == "complete" else
                   f"Analysis of {opened['system']} at {fields.get('reviewed-boundary') or 'no established boundary'}, "
                   f"with {disposition} disposition")
    frontmatter = {
        "type": layout.roles["overview"].type, "description": " ".join(description.split()),
        **{name: fields.get(name) for source in layout.roles["overview"].identity for name in source.fields},
        "system": opened["system"], "run-date": opened["run-date"],
        "inputs-commit": opened["inputs-commit"],
    }
    index = (amendment_index(_document(members["reconciliation"]).body) if "reconciliation" in members
             else "Amended or superseded records: none. Reconciliation was not reached.")
    links = "\n".join(f"- [{role}](./{layout.path(role)})" for role in members)
    targets = "\n".join(f"- `{layout.path(role)}`: deterministic snapshot checks passed."
                        for role in (*members, "overview"))
    body = (f"# {opened['system']} agentic-system analysis\n\n## Members\n\n"
            f"Disposition: `{disposition}`. See the boundary for its stopping condition.\n\n{links}\n\n"
            f"## Amendment index\n\n{index}\n\n## Deterministic validation\n\n{targets}\n\n"
            "The exact manifest and cross-member checks passed; publication rechecks them. "
            "These are deterministic checks, not semantic certification.\n")
    overview = ("---\n" + yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True)
                + "---\n\n" + body).encode("utf-8")
    complete = {**members, "overview": overview}
    manifest = _manifest(layout, type_spec, complete, worker)
    validate_pinned_artifact(repo=repo, members={layout.path(r): b for r, b in complete.items()},
                             manifest=manifest, layout=layout, type_spec=type_spec, criteria=criteria,
                             run_dir=run_dir)
    return overview, manifest


def _archive_name(incumbent: Mapping[str, bytes], run_id: str, overview: str) -> str:
    """An incumbent artifact is archived under its own run ID, never this run's."""
    old_id = _document(incumbent[overview]).frontmatter.get("run-id")
    if not run_ids.is_archived_run_id(old_id) or old_id == run_id:
        raise ValueError("replacement requires a different valid incumbent run ID")
    return old_id


@contextmanager
def preliminary_checks(run_dir: Path):
    """Checks before journal reconciliation: once a journal exists, their failure is uncertain.

    A guard can fail because an earlier attempt moved tracked files. Until
    exact-tree reconciliation runs, even a rolled-back journal's label is
    not proof of the current outcome. Preserve all evidence and the guard.
    """
    try:
        yield
    except UncertainEffectError:
        raise
    except Exception as error:
        if os.path.lexists(run_dir / JOURNAL):
            raise UncertainEffectError(
                f"cannot establish publication outcome: preliminary checks failed: {error}"
            ) from error
        raise


def _prepare_publication(members: Mapping[str, bytes], *, metadata: bytes | None, source: bytes | None,
                         provenance: Mapping[str, Provenance], manifest: bytes | None, layout: Layout,
                         type_spec: str, criteria: Mapping[str, bytes], run_dir: Path, library: Path):
    """Check pinned inputs and environment before journal reconciliation or mutation."""
    boundary = _classified_boundary(members)
    opened, repo = _opened_environment(metadata, run_dir, library, job="publication")
    _environment(opened, repo, members["boundary"], source, run_dir, job="publication")
    worker = _provenance(members, provenance, opened)
    if manifest is None:
        raise ValueError("publication requires assembly's pinned manifest")
    supplied = yaml.load(manifest, Loader=UniqueKeyLoader)
    if supplied != yaml.safe_load(_manifest(layout, type_spec, members, worker)):
        raise ValueError("assembly manifest does not pin these exact members and provenance")
    files = {layout.path(role): data for role, data in members.items()}
    validate_pinned_artifact(repo=repo, members=files, manifest=manifest, layout=layout,
                             type_spec=type_spec, criteria=criteria, run_dir=run_dir)
    _require_opened_method(repo, opened, job="publication")
    if boundary.frontmatter["result-disposition"] != "complete":
        if os.path.lexists(run_dir / JOURNAL):
            raise UncertainEffectError("non-complete artifact has a publication effect journal")
        return None  # Accepted artifact remains local; no retained or archive output.
    destination = repo / RETAINED_ROOT / publication_slug(opened["source-identity"], opened["system"])
    if opened["review-path"] != (destination / layout.path("overview")).relative_to(repo).as_posix():
        raise ValueError("opened publication destination differs from the canonical source path")

    return opened, repo, destination, {MANIFEST_NAME: manifest, **files}


def publish_analysis(members: Mapping[str, bytes], *, metadata: bytes | None, source: bytes | None,
                     provenance: Mapping[str, Provenance], manifest: bytes | None, layout: Layout,
                     type_spec: str, criteria: Mapping[str, bytes], run_dir: Path, library: Path) -> bytes:
    """Publish a pinned complete artifact, or close a non-complete artifact without public mutation.

    ``members`` are by role, including the overview. Returns the receipt.
    """
    with preliminary_checks(run_dir):
        prepared = _prepare_publication(
            members, metadata=metadata, source=source, provenance=provenance, manifest=manifest,
            layout=layout, type_spec=type_spec, criteria=criteria, run_dir=run_dir, library=library)
    if prepared is None:
        return _receipt(published=False)
    opened, repo, destination, files = prepared

    def inspect_incumbent():
        decision = inspect_destination(repo_root=repo, generated_destination=opened["review-path"],
                                       source_identity=opened["source-identity"])
        if decision["expected_incumbent_sha256"] != opened["expected-incumbent-sha256"]:
            raise ValueError("publication destination changed since opening inspection")

    # The engine already holds the per-run lock. Never take it inside this lock.
    with publication_lock(repo):
        install_tree(journal=run_dir / JOURNAL, destination=destination,
                     archive_root=repo / ARCHIVE_ROOT, files=files, anchor=layout.path("overview"),
                     expected=opened["expected-incumbent-sha256"],
                     identity={"run-id": run_dir.name, "source-identity": opened["source-identity"]},
                     archive_name=lambda old: _archive_name(old, run_dir.name, layout.path("overview")),
                     inspect_incumbent=inspect_incumbent)
    return _receipt(published=True, destination=str(destination), members=hashes(files),
                    **{name: opened.get(name) for name in RECEIPT_PINS})


def _unreleased_publication(run_dir: Path, repo: Path, metadata: dict, anchor: str
                            ) -> tuple[Path, Path | None, Path, str, dict | None]:
    """This run's unreleased worktree publication: destination, archive, journal, its state and record.

    The state is ``none`` (no journal; the destination holds the opening
    incumbent), ``rolled-back`` (the journal says so and the destination holds
    the incumbent) or ``established`` (the destination holds the published
    bytes and the archive the exact incumbent). A withdrawal interrupted
    after it marked the journal ``withdrawing`` is ``established`` while the
    archive still holds the incumbent (the destination may already be moved
    away) and ``rolled-back`` once the incumbent is back. Anything else, and
    an already integrated result, raises. Caller holds the publication lock.
    """
    overview = safe(repo / metadata["review-path"])
    destination = overview.parent
    if destination.parent != repo / RETAINED_ROOT or overview.name != anchor:
        raise ValueError("publication reset destination is not a retained analysis")
    preparation = preparation_for(repo)
    origin = Path(str(preparation["origin"]))
    if origin == repo:
        raise ValueError("publication reset only replaces an unreleased worktree result")
    for published in [*(origin / RETAINED_ROOT).glob("*/overview.md"),
                      origin / ARCHIVE_ROOT / run_dir.name / "overview.md"]:
        if published.is_file() and _document(published.read_bytes()).frontmatter.get("run-id") == run_dir.name:
            raise ValueError("publication is already integrated; reset only supports unreleased results")
    journal = safe(run_dir / JOURNAL)
    expected = metadata["expected-incumbent-sha256"]
    if not journal.exists():
        incumbent = tree(destination)
        actual = "absent" if incumbent is None else hashes(incumbent).get(anchor)
        if actual != expected:
            raise ValueError("publication reset has no journal establishing the changed destination")
        return destination, None, journal, "none", None
    record = json.loads(journal.read_bytes())
    if (record.get("run-id") != run_dir.name or record.get("destination") != str(destination)
            or record.get("source-identity") != metadata["source-identity"]
            or record.get("expected") != expected):
        raise ValueError("publication reset journal differs from opening identity")
    old, new = record.get("old"), record.get("new")
    if not isinstance(new, dict) or (old is not None and not isinstance(old, dict)):
        raise ValueError("invalid publication reset byte maps")
    if ("absent" if old is None else old.get(anchor)) != expected:
        raise ValueError("publication reset incumbent differs from opening")
    archive = safe(Path(record["archive"])) if record.get("archive") else None
    if (old is None) != (archive is None) or (archive and archive.parent != repo / ARCHIVE_ROOT):
        raise ValueError("invalid publication reset archive")
    now = hashes(tree(destination))
    archived = hashes(tree(archive)) if archive else None
    if record.get("state") in ("rolled-back", "withdrawing") and now == old and archived is None:
        return destination, None, journal, "rolled-back", record
    if record.get("state") == "withdrawing" and now in (None, new) and archived == old:
        return destination, archive, journal, "established", record
    if record.get("state") not in ("started", "completed") or now != new or archived != old:
        raise ValueError("publication reset requires exact established publication bytes")
    return destination, archive, journal, "established", record


@contextmanager
def reset_publish_analysis(run_dir: Path, job):
    """Lock publication, then prepare withdrawal of an engine run's unreleased effect.

    Restore the opening incumbent (if any), so ordinary publication can run again
    with its unchanged opening metadata. The debugging snapshot retains withdrawn
    bytes and journals. Already integrated results are not reset by this hook.
    """
    from commonplace.artifactrun.reset import Replacement
    from commonplace.artifactrun.run import Run
    from commonplace.artifactrun.store import RunStore

    # Acquisition of the same lock also works while a reset is pending; do not
    # read active records until the returned preparation callable is invoked.
    from commonplace.artifactrun.worktree import source_checkout

    repo = source_checkout(run_dir)
    if repo is None:
        raise ValueError("publication reset requires an analysis worktree")

    def prepare():
        run = Run(RunStore(run_dir))
        opened = run.latest_completed("opening")
        if opened is None:
            raise ValueError("publication reset requires opening metadata")
        metadata = _json(run.store.get(opened["outputs"]["metadata"]), "opening metadata")
        destination, archive, journal, state, _ = _unreleased_publication(
            run_dir, repo, metadata, run.layout.path("overview"))
        if state == "none":
            return []
        if state == "rolled-back":
            return [Replacement(journal)]
        replacements = [Replacement(destination, archive), Replacement(journal)]
        if archive is not None:
            replacements.append(Replacement(archive))
        return replacements

    with publication_lock(repo):
        yield prepare


def withdraw_publication(run_dir: Path, metadata: dict, *, anchor: str) -> dict:
    """Withdraw a workflow run's unreleased worktree publication and restore the opening incumbent.

    Requires the publication journal: with nothing published, there is
    nothing to withdraw. The withdrawn destination and journal are kept under
    the run's ``withdrawn/<time>/`` as evidence; the archive, when there was
    an incumbent, moves back to the destination unchanged. The journal is
    marked ``withdrawing`` before the moves, so a withdrawal interrupted
    between them is finished by calling again, and a `run` meanwhile stops on
    the unrecognised journal. Afterwards the unchanged opening metadata
    supports an ordinary publication again. Caller holds the run lock; an
    already integrated result is refused.
    """
    import datetime
    import shutil
    import uuid

    from commonplace.artifactrun.effects import write_json
    from commonplace.artifactrun.worktree import source_checkout

    repo = source_checkout(run_dir)
    if repo is None:
        raise ValueError("publication reset requires an analysis worktree")
    with publication_lock(repo):
        destination, archive, journal, state, record = _unreleased_publication(run_dir, repo, metadata, anchor)
        if state == "none":
            raise ValueError("nothing to withdraw: no publication journal, and the destination holds the "
                             "opening incumbent")
        stamp = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%SZ")
        evidence = run_dir / "withdrawn" / f"{stamp}-{uuid.uuid4().hex[:6]}"
        evidence.mkdir(parents=True)
        if state == "established":
            write_json(journal, {**record, "state": "withdrawing"})
            if destination.exists():
                shutil.move(destination, evidence / destination.name)
            if archive is not None:
                shutil.move(archive, destination)
        shutil.move(journal, evidence / journal.name)
        return {"state": state, "destination": str(destination), "evidence": str(evidence)}


RECEIPT_PINS = ("run-id", "inputs-commit", "system", "source-identity", "source", "source-revision",
                "expected-incumbent-sha256")


def _receipt(**fields) -> bytes:
    """What publication did, for consumers that read the job's current completion."""
    return (json.dumps(fields, sort_keys=True) + "\n").encode("utf-8")

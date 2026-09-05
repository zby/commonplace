"""Prepare and publish one agentic-analysis projection bundle."""

from __future__ import annotations

import os
import re
import subprocess
import tempfile
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path, PurePosixPath

import yaml

from commonplace.lib import validation
from commonplace.lib.agentic_analysis import (
    AgenticAnalysisRunState,
    parse_agentic_analysis_run_state,
    verify_agentic_analysis_run_state,
)
from commonplace.lib.note_parser import ParsedDocument, parse_document
from commonplace.review.batch import PreparedBatch, prepare_grouped_review_job
from commonplace.review.paths import criterion_path_for_id, review_gates_dir
from commonplace.review.resolve_criteria import (
    applicable_criterion_ids_for_frontmatter,
    resolve_to_criterion_ids,
)
from commonplace.review.review_db import prepare_review_db
from commonplace.review.review_model import normalize_model_partition


@dataclass(frozen=True)
class PublicationSpec:
    repo_root: Path
    run_state_path: Path
    generated_candidate_path: Path
    generated_destination: str
    legacy_candidate_path: Path | None = None
    legacy_destination: str | None = None
    legacy_model_partition: str | None = None


@dataclass(frozen=True)
class PreparedPublication:
    review_batch: PreparedBatch | None


@dataclass(frozen=True)
class PublishedPublication:
    generated_path: str
    legacy_path: str | None
    cleanup_warnings: tuple[str, ...]


@dataclass(frozen=True)
class _CheckedBundle:
    spec: PublicationSpec
    running_state: AgenticAnalysisRunState
    final_state: AgenticAnalysisRunState
    final_state_text: str
    generated_text: str
    generated_bytes: bytes
    legacy_text: str | None
    legacy_bytes: bytes | None


class PublicationUncertainError(RuntimeError):
    """A publication failure whose rollback did not fully restore old bytes."""


def _repo_path(repo_root: Path, raw: Path) -> Path:
    path = raw if raw.is_absolute() else repo_root / raw
    resolved = path.resolve()
    try:
        resolved.relative_to(repo_root)
    except ValueError as exc:
        raise ValueError(f"path is outside the repository: {raw}") from exc
    return resolved


def _destination_path(repo_root: Path, raw: str, *, legacy: bool) -> Path:
    pure = PurePosixPath(raw)
    valid = (
        not pure.is_absolute()
        and raw == pure.as_posix()
        and ".." not in pure.parts
        and pure.suffix == ".md"
        and (
            (
                legacy
                and len(pure.parts) == 4
                and pure.parts[:2] == ("kb", "agent-memory-systems")
                and pure.parts[2] in {"reviews", "lightweight"}
            )
            or (
                not legacy
                and len(pure.parts) == 4
                and pure.parts[:3] == ("kb", "agentic-systems", "reviews")
            )
        )
    )
    if not valid:
        expected = (
            "kb/agent-memory-systems/{reviews|lightweight}/<name>.md"
            if legacy
            else "kb/agentic-systems/reviews/<name>.md"
        )
        raise ValueError(f"publication destination must be {expected}: {raw}")
    return repo_root.joinpath(*pure.parts)


def _read_utf8(path: Path, *, label: str) -> tuple[bytes, str]:
    try:
        content = path.read_bytes()
        return content, content.decode("utf-8")
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"cannot read {label} {path}: {exc}") from exc


def _parse(content: str, *, label: str) -> ParsedDocument:
    document, error = parse_document(content)
    if error is not None or document is None or document.frontmatter is None:
        raise ValueError(f"{label} is not a parseable typed Markdown artifact")
    return document


def _clean_validation(content: str, *, path: Path, repo_root: Path, label: str) -> None:
    results = validation.validate_note_text_at_path(
        content,
        path=path,
        repo_root=repo_root,
    )
    diagnostics = [*results.warns, *results.fails]
    if diagnostics:
        raise ValueError(f"{label} validation failed: " + "; ".join(diagnostics))


def _load_running_state(path: Path, *, repo_root: Path) -> tuple[AgenticAnalysisRunState, ParsedDocument]:
    if not path.is_file():
        raise ValueError(f"run state does not exist: {path}")
    results = validation.validate_note(path, repo_root=repo_root)
    diagnostics = [*results.warns, *results.fails]
    if diagnostics:
        raise ValueError("running run-state validation failed: " + "; ".join(diagnostics))
    _, content = _read_utf8(path, label="run state")
    document = _parse(content, label="run state")
    state = parse_agentic_analysis_run_state(path, document, repo_root=repo_root)
    if state.status != "running":
        raise ValueError("publication requires a running run state")
    if state.source is None:
        raise ValueError("publication requires a frozen source in the run state")
    return state, document


def _require_candidate_in_run(candidate: Path, state: AgenticAnalysisRunState) -> None:
    try:
        relative = candidate.relative_to(state.run_dir)
    except ValueError as exc:
        raise ValueError(f"candidate must be inside {state.run_dir}: {candidate}") from exc
    if not relative.parts or candidate == state.path or candidate.name == "result.md":
        raise ValueError(f"candidate path is reserved: {candidate}")


def _check_incumbent(
    *,
    path: Path,
    repo_root: Path,
    source_identity: str,
    generated: bool,
) -> None:
    if not path.exists():
        return
    if not path.is_file():
        raise ValueError(f"publication destination is not a file: {path}")
    relative = path.relative_to(repo_root).as_posix()
    try:
        status = subprocess.run(
            ["git", "status", "--short", "--untracked-files=all", "--", relative],
            cwd=repo_root,
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise ValueError(f"cannot inspect destination Git status: {exc}") from exc
    if status.returncode != 0:
        raise ValueError(f"cannot inspect destination Git status: {status.stderr.strip()}")
    if status.stdout.strip():
        raise ValueError(f"publication destination has local changes: {relative}")

    _, content = _read_utf8(path, label="publication incumbent")
    document = _parse(content, label="publication incumbent")
    frontmatter = document.frontmatter or {}
    if generated:
        same_source = (
            frontmatter.get("generated-by") == "analyse-agentic-system"
            and frontmatter.get("source-identity") == source_identity
        )
    else:
        accepted_types = {
            "kb/agent-memory-systems/types/agent-memory-system-review.md",
            "../types/agent-memory-system-review.md",
        }
        identity_header = content.split("\n## ", maxsplit=1)[0]
        same_source = (
            frontmatter.get("type") in accepted_types
            and (
                frontmatter.get("source-identity") == source_identity
                or source_identity in identity_header
            )
        )
    if not same_source:
        raise ValueError(
            "publication destination is not a generated review of the same source: "
            f"{relative}"
        )


def _render_final_state(
    *,
    state: AgenticAnalysisRunState,
    document: ParsedDocument,
    result_bytes: bytes,
    generated_bytes: bytes,
    generated_destination: str,
    legacy_bytes: bytes | None,
    legacy_destination: str | None,
    legacy_model_partition: str | None,
) -> str:
    frontmatter = dict(document.frontmatter or {})
    result_path = state.run_dir / "result.md"
    frontmatter.update(
        {
            "run-status": "complete",
            "result-disposition": "complete",
            "result": {
                "path": result_path.relative_to(state.repo_root).as_posix(),
                "sha256": sha256(result_bytes).hexdigest(),
            },
            "generated-review": {
                "path": generated_destination,
                "sha256": sha256(generated_bytes).hexdigest(),
            },
            "memory-review-required": legacy_bytes is not None,
            "legacy-review": (
                {
                    "path": legacy_destination,
                    "sha256": sha256(legacy_bytes).hexdigest(),
                }
                if legacy_bytes is not None
                else None
            ),
            "legacy-review-model-partition": legacy_model_partition,
            "failure": None,
        }
    )
    body = re.sub(
        r"(?ms)^## Outcome\s*$.*\Z",
        "## Outcome\n\nPublication completed for the exact result and declared review projections.\n",
        document.body.rstrip() + "\n",
    )
    serialized = yaml.safe_dump(
        frontmatter,
        sort_keys=False,
        allow_unicode=True,
        width=1000,
    )
    return f"---\n{serialized}---\n{body.lstrip()}"


def _check_bundle(spec: PublicationSpec, *, require_semantic: bool) -> _CheckedBundle:
    repo_root = spec.repo_root.resolve()
    state_path = _repo_path(repo_root, spec.run_state_path)
    generated_candidate = _repo_path(repo_root, spec.generated_candidate_path)
    generated_path = _destination_path(
        repo_root, spec.generated_destination, legacy=False
    )
    has_legacy = any(
        value is not None
        for value in (
            spec.legacy_candidate_path,
            spec.legacy_destination,
            spec.legacy_model_partition,
        )
    )
    if has_legacy and not all(
        value is not None
        for value in (
            spec.legacy_candidate_path,
            spec.legacy_destination,
            spec.legacy_model_partition,
        )
    ):
        raise ValueError(
            "legacy candidate, destination, and model partition are required together"
        )
    legacy_candidate = (
        _repo_path(repo_root, spec.legacy_candidate_path)
        if spec.legacy_candidate_path is not None
        else None
    )
    legacy_path = (
        _destination_path(repo_root, spec.legacy_destination, legacy=True)
        if spec.legacy_destination is not None
        else None
    )
    model_partition = (
        normalize_model_partition(spec.legacy_model_partition)
        if spec.legacy_model_partition is not None
        else None
    )

    running_state, state_document = _load_running_state(
        state_path, repo_root=repo_root
    )
    _require_candidate_in_run(generated_candidate, running_state)
    if legacy_candidate is not None:
        _require_candidate_in_run(legacy_candidate, running_state)
    if legacy_candidate == generated_candidate:
        raise ValueError("generated and legacy candidates must be different files")
    if legacy_path == generated_path:
        raise ValueError("generated and legacy destinations must be different files")

    result_path = running_state.run_dir / "result.md"
    result_bytes, result_text = _read_utf8(result_path, label="exact result")
    result_document = _parse(result_text, label="exact result")
    if result_document.frontmatter.get("result-disposition") != "complete":
        raise ValueError("publication requires a complete exact result")
    _clean_validation(
        result_text,
        path=result_path,
        repo_root=repo_root,
        label="exact result",
    )

    generated_bytes, generated_text = _read_utf8(
        generated_candidate, label="generated candidate"
    )
    legacy_bytes: bytes | None = None
    legacy_text: str | None = None
    if legacy_candidate is not None:
        legacy_bytes, legacy_text = _read_utf8(
            legacy_candidate, label="legacy candidate"
        )

    final_state_text = _render_final_state(
        state=running_state,
        document=state_document,
        result_bytes=result_bytes,
        generated_bytes=generated_bytes,
        generated_destination=spec.generated_destination,
        legacy_bytes=legacy_bytes,
        legacy_destination=spec.legacy_destination,
        legacy_model_partition=model_partition,
    )
    final_document = _parse(final_state_text, label="prospective run state")
    final_state = parse_agentic_analysis_run_state(
        state_path, final_document, repo_root=repo_root
    )
    overrides = {generated_path: generated_text}
    if legacy_path is not None and legacy_text is not None:
        overrides[legacy_path] = legacy_text
    if require_semantic:
        results = validation.validate_note_text_at_path(
            final_state_text,
            path=state_path,
            repo_root=repo_root,
            content_overrides=overrides,
        )
        diagnostics = [*results.warns, *results.fails]
        if diagnostics:
            raise ValueError(
                "publication bundle verification failed: " + "; ".join(diagnostics)
            )
    else:
        _, failures = verify_agentic_analysis_run_state(
            final_state,
            content_overrides=overrides,
            require_legacy_semantic_baselines=False,
        )
        if failures:
            raise ValueError(
                "publication bundle verification failed: " + "; ".join(failures)
            )

    source_identity = running_state.source.identity
    _check_incumbent(
        path=generated_path,
        repo_root=repo_root,
        source_identity=source_identity,
        generated=True,
    )
    if legacy_path is not None:
        _check_incumbent(
            path=legacy_path,
            repo_root=repo_root,
            source_identity=source_identity,
            generated=False,
        )

    return _CheckedBundle(
        spec=PublicationSpec(
            repo_root=repo_root,
            run_state_path=state_path,
            generated_candidate_path=generated_candidate,
            generated_destination=spec.generated_destination,
            legacy_candidate_path=legacy_candidate,
            legacy_destination=spec.legacy_destination,
            legacy_model_partition=model_partition,
        ),
        running_state=running_state,
        final_state=final_state,
        final_state_text=final_state_text,
        generated_text=generated_text,
        generated_bytes=generated_bytes,
        legacy_text=legacy_text,
        legacy_bytes=legacy_bytes,
    )


def prepare_publication(spec: PublicationSpec) -> PreparedPublication:
    """Validate a candidate bundle and create its one semantic review job."""
    bundle = _check_bundle(spec, require_semantic=False)
    if bundle.legacy_text is None or bundle.spec.legacy_destination is None:
        return PreparedPublication(review_batch=None)

    document = _parse(bundle.legacy_text, label="legacy candidate")
    gates_dir = review_gates_dir(bundle.spec.repo_root)
    criterion_ids = applicable_criterion_ids_for_frontmatter(
        document.frontmatter or {},
        resolve_to_criterion_ids(["semantic"], gates_dir),
        gates_dir,
    )
    pairs = [
        (
            bundle.spec.legacy_destination,
            criterion_path_for_id(bundle.spec.repo_root, criterion_id),
            "verdict",
        )
        for criterion_id in criterion_ids
    ]
    db_path = prepare_review_db(bundle.spec.repo_root)
    review_batch = prepare_grouped_review_job(
        repo_root=bundle.spec.repo_root,
        db_path=db_path,
        pairs=pairs,
        grouping="note",
        runner=None,
        model_partition=bundle.spec.legacy_model_partition or "",
        note_text_overrides={
            bundle.spec.legacy_destination: bundle.legacy_text,
        },
    )
    return PreparedPublication(review_batch=review_batch)


def _atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary_path = Path(temporary)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
    except Exception:
        temporary_path.unlink(missing_ok=True)
        raise


def _restore(path: Path, content: bytes | None) -> None:
    if content is None:
        path.unlink(missing_ok=True)
    else:
        _atomic_write(path, content)


def publish_publication(spec: PublicationSpec) -> PublishedPublication:
    """Publish an already-reviewed bundle, rolling back ordinary failures."""
    bundle = _check_bundle(spec, require_semantic=True)
    repo_root = bundle.spec.repo_root
    generated_path = repo_root / bundle.spec.generated_destination
    legacy_path = (
        repo_root / bundle.spec.legacy_destination
        if bundle.spec.legacy_destination is not None
        else None
    )
    state_path = bundle.spec.run_state_path
    targets: list[tuple[Path, bytes]] = [
        (generated_path, bundle.generated_bytes),
    ]
    if legacy_path is not None and bundle.legacy_bytes is not None:
        targets.append((legacy_path, bundle.legacy_bytes))
    targets.append((state_path, bundle.final_state_text.encode("utf-8")))
    old_bytes = {
        path: path.read_bytes() if path.exists() else None for path, _ in targets
    }
    written: list[Path] = []
    try:
        for path, content in targets:
            _atomic_write(path, content)
            written.append(path)
        results = validation.validate_note(state_path, repo_root=repo_root)
        diagnostics = [*results.warns, *results.fails]
        if diagnostics:
            raise ValueError(
                "published run-state validation failed: " + "; ".join(diagnostics)
            )
    except Exception as publication_error:
        rollback_errors: list[str] = []
        for path in reversed(written):
            try:
                _restore(path, old_bytes[path])
            except OSError as exc:
                rollback_errors.append(f"{path}: {exc}")
        if rollback_errors:
            raise PublicationUncertainError(
                f"publication failed ({publication_error}); rollback also failed: "
                + "; ".join(rollback_errors)
            ) from publication_error
        raise

    cleanup_warnings: list[str] = []
    for candidate in (
        bundle.spec.generated_candidate_path,
        bundle.spec.legacy_candidate_path,
    ):
        if candidate is None:
            continue
        try:
            candidate.unlink(missing_ok=True)
        except OSError as exc:
            cleanup_warnings.append(f"could not remove candidate {candidate}: {exc}")
    return PublishedPublication(
        generated_path=bundle.spec.generated_destination,
        legacy_path=bundle.spec.legacy_destination,
        cleanup_warnings=tuple(cleanup_warnings),
    )

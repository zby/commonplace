"""Filesystem paths used by the review subsystem."""

from __future__ import annotations

from pathlib import Path

from commonplace.lib.library import (
    LIBRARY_IDENTITY_PREFIX,
    artifact_file,
    artifact_identity,
    is_library_identity,
    library_root,
)
from commonplace.review.collection_conformance import (
    collection_criterion_id_for_path,
    is_collection_conformance_request,
    is_collection_md_criterion_path,
    resolve_collection_criterion_id,
)
from commonplace.review.critique import (
    CRITIQUE_LENS,
    critique_criterion_path,
    is_critique_criterion_path,
    is_critique_request,
)
from commonplace.review.type_conformance import (
    is_type_conformance_request,
    is_type_spec_criterion_path,
    resolve_type_criterion_id,
    type_criterion_id_for_path,
)

GATES_REL = "instructions/review-gates"
# Prefixes a stored gate identity may carry: the source checkout's repo path,
# the library identity, and the kb/commonplace/ copy of releases before ADR 086.
STORED_GATE_PREFIXES = (
    f"kb/{GATES_REL}/",
    f"{LIBRARY_IDENTITY_PREFIX}{GATES_REL}/",
    f"kb/commonplace/{GATES_REL}/",
)


def reject_unsafe_relative(raw: str, *, kind: str) -> None:
    path = Path(raw)
    if path.is_absolute() or raw in {"", "."} or ".." in path.parts:
        raise ValueError(f"{kind} must be relative and stay inside the review gate catalog: {raw}")


def normalize_repo_relative_path(raw: str, *, label: str) -> str:
    """Validate a repo-relative path string and return its POSIX form."""
    path = Path(raw)
    normalized = path.as_posix()
    if path.is_absolute() or normalized == "." or ".." in path.parts:
        raise ValueError(f"{label} must be repo-relative: {raw}")
    return normalized


def review_gates_dir(repo_root: Path) -> Path:
    """Return the gate catalog directory: the installed library's review gates.

    In the source checkout the library is the repository's own kb/, so this is
    kb/instructions/review-gates. `repo_root` is kept for call-site symmetry.
    """
    return library_root() / GATES_REL


def criterion_path_for_id(repo_root: Path, criterion_id: str) -> str:
    """Resolve a criterion shorthand to its repo-relative markdown path."""
    normalized = criterion_id.strip().removesuffix(".md")
    reject_unsafe_relative(normalized, kind="criterion id")
    if is_type_conformance_request(normalized):
        return resolve_type_criterion_id(repo_root, normalized)
    if is_collection_conformance_request(normalized):
        return resolve_collection_criterion_id(repo_root, normalized)
    if is_critique_request(normalized):
        return critique_criterion_path(repo_root)
    gates_dir = review_gates_dir(repo_root)
    criterion_abs = (gates_dir / f"{normalized}.md").resolve()
    gates_dir_resolved = gates_dir.resolve()
    if not criterion_abs.is_relative_to(gates_dir_resolved):
        raise ValueError(f"criterion id is outside the review gate catalog: {criterion_id}")
    if not criterion_abs.is_file():
        raise FileNotFoundError(f"criterion not found: {criterion_id}")
    return artifact_identity(repo_root, criterion_abs)


def criterion_id_for_path(repo_root: Path, criterion_path: str) -> str:
    """Derive the human-facing criterion shorthand from a criterion identity."""
    reject_unsafe_relative(criterion_path, kind="criterion path")
    if is_type_spec_criterion_path(criterion_path):
        if not artifact_file(repo_root, criterion_path).is_file():
            raise FileNotFoundError(f"criterion not found: {criterion_path}")
        return type_criterion_id_for_path(criterion_path)
    if is_collection_md_criterion_path(Path(criterion_path).as_posix()):
        if not (repo_root / criterion_path).is_file():
            raise FileNotFoundError(f"criterion not found: {criterion_path}")
        return collection_criterion_id_for_path(criterion_path)
    if is_critique_criterion_path(criterion_path):
        if not artifact_file(repo_root, criterion_path).is_file():
            raise FileNotFoundError(f"criterion not found: {criterion_path}")
        return CRITIQUE_LENS
    criterion_abs = artifact_file(repo_root, criterion_path).resolve()
    gates_dir = review_gates_dir(repo_root).resolve()
    try:
        rel = criterion_abs.relative_to(gates_dir)
    except ValueError as exc:
        raise ValueError(f"criterion path is outside the review gate catalog: {criterion_path}") from exc
    return rel.with_suffix("").as_posix()


def criterion_id_from_stored_path(criterion_path: str) -> str:
    """Best-effort shorthand for a stored criterion identity."""
    if is_type_spec_criterion_path(criterion_path):
        return type_criterion_id_for_path(criterion_path)
    if is_collection_md_criterion_path(Path(criterion_path).as_posix()):
        return collection_criterion_id_for_path(criterion_path)
    if is_critique_criterion_path(criterion_path):
        return CRITIQUE_LENS
    normalized = criterion_path.removesuffix(".md")
    for prefix in STORED_GATE_PREFIXES:
        if normalized.startswith(prefix):
            return normalized[len(prefix) :]
    return normalized


def normalize_criterion_path(repo_root: Path, criterion: str) -> str:
    """Accept a criterion identity, path, or shorthand and return the identity."""
    raw = criterion.strip()
    if not raw:
        raise ValueError("criterion must not be empty")
    reject_unsafe_relative(raw, kind="criterion path")
    if is_library_identity(raw):
        path = artifact_file(repo_root, raw)
        if not path.is_file():
            raise FileNotFoundError(f"criterion not found: {criterion}")
        return raw
    candidate = Path(raw)
    if not raw.endswith(".md") and not raw.startswith("kb/"):
        return criterion_path_for_id(repo_root, raw)

    criterion_abs = (repo_root / candidate).resolve()
    if (
        is_type_spec_criterion_path(candidate.as_posix())
        or is_collection_md_criterion_path(candidate.as_posix())
        or is_critique_criterion_path(candidate.as_posix())
    ):
        if not criterion_abs.is_file():
            raise FileNotFoundError(f"criterion not found: {criterion}")
        return artifact_identity(repo_root, criterion_abs)

    if criterion_abs.is_file() or raw.startswith("kb/"):
        gates_dir = review_gates_dir(repo_root).resolve()
        if not criterion_abs.is_relative_to(gates_dir):
            raise ValueError(f"criterion path is outside the review gate catalog: {criterion}")
        if not criterion_abs.is_file():
            raise FileNotFoundError(f"criterion not found: {criterion}")
        return artifact_identity(repo_root, criterion_abs)
    # A `.md` name outside kb/ that resolves to no file is a shorthand with an
    # extension; criterion_path_for_id strips it and searches the catalog.
    return criterion_path_for_id(repo_root, raw)

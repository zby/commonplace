"""Filesystem paths used by the review subsystem."""

from __future__ import annotations

from pathlib import Path

from commonplace.review.collection_conformance import (
    collection_criterion_id_for_path,
    is_collection_gate_request,
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
    is_type_gate_request,
    is_type_spec_criterion_path,
    resolve_type_criterion_id,
    type_criterion_id_for_path,
)


SOURCE_GATES_ROOT = Path("kb/instructions/review-gates")
INSTALLED_GATES_ROOT = Path("kb/commonplace/instructions/review-gates")


def _reject_unsafe_relative(raw: str, *, kind: str) -> None:
    path = Path(raw)
    if path.is_absolute() or raw in {"", "."} or ".." in path.parts:
        raise ValueError(f"{kind} must be relative and stay inside the review gate catalog: {raw}")


def review_gates_dir(repo_root: Path) -> Path:
    """Return the gate catalog directory for this project layout.

    Source checkouts author gates at kb/instructions/review-gates. Installed
    projects receive the shipped gate catalog under kb/commonplace/instructions.
    Prefer the installed location when present so user-owned instructions do not
    shadow the framework gate catalog by accident.
    """
    installed = repo_root / INSTALLED_GATES_ROOT
    if installed.is_dir():
        return installed
    return repo_root / SOURCE_GATES_ROOT


def criterion_path_for_id(repo_root: Path, criterion_id: str) -> str:
    """Resolve a criterion shorthand to its repo-relative markdown path."""
    normalized = criterion_id.strip().removesuffix(".md")
    _reject_unsafe_relative(normalized, kind="criterion id")
    if is_type_gate_request(normalized):
        return resolve_type_criterion_id(repo_root, normalized)
    if is_collection_gate_request(normalized):
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
    return criterion_abs.relative_to(repo_root.resolve()).as_posix()


def criterion_id_for_path(repo_root: Path, criterion_path: str) -> str:
    """Derive the human-facing criterion shorthand from a repo-relative criterion path."""
    _reject_unsafe_relative(criterion_path, kind="criterion path")
    if is_type_spec_criterion_path(Path(criterion_path).as_posix()):
        if not (repo_root / criterion_path).is_file():
            raise FileNotFoundError(f"criterion not found: {criterion_path}")
        return type_criterion_id_for_path(criterion_path)
    if is_collection_md_criterion_path(Path(criterion_path).as_posix()):
        if not (repo_root / criterion_path).is_file():
            raise FileNotFoundError(f"criterion not found: {criterion_path}")
        return collection_criterion_id_for_path(criterion_path)
    if is_critique_criterion_path(criterion_path):
        if not (repo_root / criterion_path).is_file():
            raise FileNotFoundError(f"criterion not found: {criterion_path}")
        return CRITIQUE_LENS
    criterion_abs = (repo_root / criterion_path).resolve()
    gates_dir = review_gates_dir(repo_root).resolve()
    try:
        rel = criterion_abs.relative_to(gates_dir)
    except ValueError as exc:
        raise ValueError(f"criterion path is outside the review gate catalog: {criterion_path}") from exc
    return rel.with_suffix("").as_posix()


def criterion_id_from_stored_path(criterion_path: str) -> str:
    """Best-effort shorthand for a stored repo-relative criterion path."""
    if is_type_spec_criterion_path(Path(criterion_path).as_posix()):
        return type_criterion_id_for_path(criterion_path)
    if is_collection_md_criterion_path(Path(criterion_path).as_posix()):
        return collection_criterion_id_for_path(criterion_path)
    if is_critique_criterion_path(criterion_path):
        return CRITIQUE_LENS
    normalized = Path(criterion_path).with_suffix("").as_posix()
    prefixes = (
        SOURCE_GATES_ROOT.as_posix() + "/",
        INSTALLED_GATES_ROOT.as_posix() + "/",
    )
    for prefix in prefixes:
        if normalized.startswith(prefix):
            return normalized[len(prefix) :]
    return normalized


def normalize_criterion_path(repo_root: Path, criterion: str) -> str:
    """Accept a criterion path or shorthand and return the repo-relative path."""
    raw = criterion.strip()
    if not raw:
        raise ValueError("criterion must not be empty")
    _reject_unsafe_relative(raw, kind="criterion path")
    candidate = Path(raw)
    if candidate.is_absolute():
        raise ValueError(f"criterion path must be repo-relative: {criterion}")
    if raw.endswith(".md") or raw.startswith("kb/"):
        if (
            is_type_spec_criterion_path(candidate.as_posix())
            or is_collection_md_criterion_path(candidate.as_posix())
            or is_critique_criterion_path(candidate.as_posix())
        ):
            criterion_abs = (repo_root / candidate).resolve()
            if not criterion_abs.is_file():
                raise FileNotFoundError(f"criterion not found: {criterion}")
            return criterion_abs.relative_to(repo_root.resolve()).as_posix()
        criterion_abs = (repo_root / candidate).resolve()
        if criterion_abs.is_file():
            gates_dir = review_gates_dir(repo_root).resolve()
            if not criterion_abs.is_relative_to(gates_dir):
                raise ValueError(f"criterion path is outside the review gate catalog: {criterion}")
            return criterion_abs.relative_to(repo_root.resolve()).as_posix()
        if raw.startswith("kb/"):
            gates_dir = review_gates_dir(repo_root).resolve()
            if not criterion_abs.is_relative_to(gates_dir):
                raise ValueError(f"criterion path is outside the review gate catalog: {criterion}")
            raise FileNotFoundError(f"criterion not found: {criterion}")
    return criterion_path_for_id(repo_root, raw)

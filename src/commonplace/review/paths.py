"""Filesystem paths used by the review subsystem."""

from __future__ import annotations

from pathlib import Path


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


def gate_path_for_id(repo_root: Path, gate_id: str) -> str:
    """Resolve a gate shorthand to the repo-relative gate markdown path."""
    normalized = gate_id.strip().removesuffix(".md")
    _reject_unsafe_relative(normalized, kind="gate id")
    gates_dir = review_gates_dir(repo_root)
    gate_abs = (gates_dir / f"{normalized}.md").resolve()
    gates_dir_resolved = gates_dir.resolve()
    if not gate_abs.is_relative_to(gates_dir_resolved):
        raise ValueError(f"gate id is outside the review gate catalog: {gate_id}")
    if not gate_abs.is_file():
        raise FileNotFoundError(f"gate not found: {gate_id}")
    return gate_abs.relative_to(repo_root.resolve()).as_posix()


def gate_id_for_path(repo_root: Path, gate_path: str) -> str:
    """Derive the human-facing gate shorthand from a repo-relative gate path."""
    _reject_unsafe_relative(gate_path, kind="gate path")
    gate_abs = (repo_root / gate_path).resolve()
    gates_dir = review_gates_dir(repo_root).resolve()
    try:
        rel = gate_abs.relative_to(gates_dir)
    except ValueError as exc:
        raise ValueError(f"gate path is outside the review gate catalog: {gate_path}") from exc
    return rel.with_suffix("").as_posix()


def gate_id_from_stored_path(gate_path: str) -> str:
    """Best-effort shorthand for a stored repo-relative gate path."""
    normalized = Path(gate_path).with_suffix("").as_posix()
    prefixes = (
        SOURCE_GATES_ROOT.as_posix() + "/",
        INSTALLED_GATES_ROOT.as_posix() + "/",
    )
    for prefix in prefixes:
        if normalized.startswith(prefix):
            return normalized[len(prefix) :]
    return normalized


def normalize_gate_path(repo_root: Path, gate: str) -> str:
    """Accept a gate path or shorthand and return the repo-relative path."""
    raw = gate.strip()
    if not raw:
        raise ValueError("gate must not be empty")
    _reject_unsafe_relative(raw, kind="gate path")
    candidate = Path(raw)
    if candidate.is_absolute():
        raise ValueError(f"gate path must be repo-relative: {gate}")
    if raw.endswith(".md") or raw.startswith("kb/"):
        gate_abs = (repo_root / candidate).resolve()
        if gate_abs.is_file():
            gates_dir = review_gates_dir(repo_root).resolve()
            if not gate_abs.is_relative_to(gates_dir):
                raise ValueError(f"gate path is outside the review gate catalog: {gate}")
            return gate_abs.relative_to(repo_root.resolve()).as_posix()
        if raw.startswith("kb/"):
            gates_dir = review_gates_dir(repo_root).resolve()
            if not gate_abs.is_relative_to(gates_dir):
                raise ValueError(f"gate path is outside the review gate catalog: {gate}")
            raise FileNotFoundError(f"gate not found: {gate}")
    return gate_path_for_id(repo_root, raw)

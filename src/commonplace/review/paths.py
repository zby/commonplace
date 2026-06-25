"""Filesystem paths used by the review subsystem."""

from __future__ import annotations

from pathlib import Path


SOURCE_GATES_ROOT = Path("kb/instructions/review-gates")
INSTALLED_GATES_ROOT = Path("kb/commonplace/instructions/review-gates")

# Backward-compatible name for source-checkout callers. Runtime code should use
# review_gates_dir() so installed projects resolve the shipped library location.
GATES_ROOT = SOURCE_GATES_ROOT


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
    gates_dir = review_gates_dir(repo_root)
    gate_abs = gates_dir / f"{normalized}.md"
    if not gate_abs.is_file():
        raise FileNotFoundError(f"gate not found: {gate_id}")
    return gate_abs.relative_to(repo_root).as_posix()


def gate_id_for_path(repo_root: Path, gate_path: str) -> str:
    """Derive the human-facing gate shorthand from a repo-relative gate path."""
    gate_abs = repo_root / gate_path
    try:
        rel = gate_abs.relative_to(review_gates_dir(repo_root))
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
    candidate = Path(raw)
    if candidate.is_absolute():
        raise ValueError(f"gate path must be repo-relative: {gate}")
    if raw.endswith(".md") or raw.startswith("kb/"):
        gate_abs = repo_root / candidate
        if gate_abs.is_file():
            return candidate.as_posix()
        if raw.startswith("kb/"):
            raise FileNotFoundError(f"gate not found: {gate}")
    return gate_path_for_id(repo_root, raw)

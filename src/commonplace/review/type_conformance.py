"""Type-conformance review pairs: the note's type spec is the gate.

A type-conformance pair reviews one note against the type spec named by its
frontmatter `type:`. The pair is ordinary review state — its gate path just
lives under a kb `types/` directory instead of the review-gate catalog — so
snapshots, freshness, acceptance, and acknowledgement apply unchanged: editing
a type spec flips `gate-changed` for exactly the notes of that type.

Pairs are derived from note frontmatter, not from catalog listing plus
`requires-type` filtering. The human-facing gate id is the virtual
`type/{name}` lens; the persisted gate identity is the type-spec repo path.
"""

from __future__ import annotations

from pathlib import Path, PurePosixPath

from commonplace.lib import frontmatter
from commonplace.lib.project_paths import kb_root
from commonplace.lib.type_resolver import validate_type_path

TYPE_GATE_LENS = "type"


def is_type_gate_request(arg: str) -> bool:
    """True when a requested gate id names the virtual type-conformance lens."""
    arg = arg.strip()
    return arg == TYPE_GATE_LENS or arg.startswith(f"{TYPE_GATE_LENS}/")


def is_type_spec_gate_path(gate_path: str) -> bool:
    """True when a repo-relative gate path points into a kb `types/` directory."""
    path = PurePosixPath(gate_path)
    if path.suffix != ".md" or not path.parts or path.parts[0] != "kb":
        return False
    if "review-gates" in path.parts:
        return False
    return path.parent.name == "types"


def type_gate_id_for_path(gate_path: str) -> str:
    """Virtual `type/{name}` shorthand for a type-spec gate path."""
    return f"{TYPE_GATE_LENS}/{PurePosixPath(gate_path).stem}"


def resolve_type_gate_id(repo_root: Path, gate_id: str) -> str:
    """Resolve a `type/{name}` gate id to the repo-relative type-spec path.

    Prefers the global `kb/types/{name}.md`; otherwise the name must match
    exactly one collection-local `kb/**/types/{name}.md`.
    """
    name = gate_id.strip().removeprefix(f"{TYPE_GATE_LENS}/")
    name = name.removesuffix(".md")
    if not name or name == TYPE_GATE_LENS or "/" in name or name in {".", ".."}:
        raise ValueError(f"invalid type gate id: {gate_id}")
    boundary = kb_root(repo_root)
    global_spec = boundary / "types" / f"{name}.md"
    if global_spec.is_file():
        return global_spec.relative_to(repo_root).as_posix()
    candidates = sorted(
        path
        for path in boundary.glob(f"**/types/{name}.md")
        if path.is_file() and is_type_spec_gate_path(path.relative_to(repo_root).as_posix())
    )
    if not candidates:
        raise FileNotFoundError(f"type spec not found for gate id: {gate_id}")
    if len(candidates) > 1:
        rendered = ", ".join(path.relative_to(repo_root).as_posix() for path in candidates)
        raise ValueError(f"type gate id is ambiguous across collections: {gate_id} ({rendered})")
    return candidates[0].relative_to(repo_root).as_posix()


def note_type_spec_path(repo_root: Path, note_abs: Path) -> str | None:
    """Canonical repo-relative type-spec path for a note, or None without a valid binding.

    Malformed frontmatter or a malformed `type:` value yields None — rejecting
    those is the deterministic validator's job, and a note without a valid
    type binding has no conformance pair. A well-formed path whose file is
    missing raises, matching catalog gate resolution.
    """
    try:
        parsed = frontmatter.parse(note_abs.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError):
        return None
    if not parsed.ok or "type" not in parsed.data or not isinstance(parsed.data["type"], str):
        return None
    try:
        canonical, resolved = validate_type_path(
            parsed.data["type"],
            repo_root=repo_root,
            source_file=note_abs,
        )
    except ValueError:
        return None
    if not resolved.is_file():
        raise FileNotFoundError(f"type spec not found: {canonical} (declared by {note_abs.name})")
    return canonical

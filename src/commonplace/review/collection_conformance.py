"""Collection-conformance review pairs: the note's COLLECTION.md is the gate.

A collection-conformance pair reviews one note against the authoring contract
of the collection it lives in — the nearest `COLLECTION.md` above it. The
pair is ordinary review state — its gate path is a collection contract file
instead of a review-gate catalog entry — so snapshots, freshness, acceptance,
and acknowledgement apply unchanged: editing a COLLECTION.md flips
`gate-changed` for exactly the notes in that collection.

Pairs are derived from note location, not from catalog listing. The
human-facing gate id is the virtual `collection/{path}` lens, where `{path}`
is the collection directory relative to `kb/`; the persisted gate identity is
the COLLECTION.md repo path.
"""

from __future__ import annotations

from pathlib import Path, PurePosixPath

from commonplace.lib.project_paths import collection_for_path, kb_root

COLLECTION_GATE_LENS = "collection"


def is_collection_gate_request(arg: str) -> bool:
    """True when a requested gate id names the virtual collection-conformance lens."""
    arg = arg.strip()
    return arg == COLLECTION_GATE_LENS or arg.startswith(f"{COLLECTION_GATE_LENS}/")


def is_collection_md_gate_path(gate_path: str) -> bool:
    """True when a repo-relative gate path is a kb collection's COLLECTION.md.

    `kb/COLLECTION.md` itself is excluded (the kb root is a boundary, not a
    collection), as is any COLLECTION.md under a `types/` directory, matching
    `collection_dirs`.
    """
    path = PurePosixPath(gate_path)
    if path.name != "COLLECTION.md" or not path.parts or path.parts[0] != "kb":
        return False
    if len(path.parts) < 3:
        return False
    return "types" not in path.parent.parts


def collection_gate_id_for_path(gate_path: str) -> str:
    """Virtual `collection/{path}` shorthand for a COLLECTION.md gate path."""
    parent = PurePosixPath(gate_path).parent
    rel = PurePosixPath(*parent.parts[1:]).as_posix()
    return f"{COLLECTION_GATE_LENS}/{rel}"


def resolve_collection_gate_id(repo_root: Path, gate_id: str) -> str:
    """Resolve a `collection/{path}` gate id to the repo-relative COLLECTION.md path.

    `{path}` is the collection directory relative to `kb/`, so collections
    under a non-collection namespace stay unambiguous: `collection/notes`
    names `kb/notes/COLLECTION.md`, `collection/commonplace/notes` names
    `kb/commonplace/notes/COLLECTION.md`.
    """
    rel = gate_id.strip().removeprefix(f"{COLLECTION_GATE_LENS}/").strip("/")
    parts = PurePosixPath(rel).parts
    if (
        not rel
        or rel == COLLECTION_GATE_LENS
        or PurePosixPath(rel).is_absolute()
        or any(part in {".", ".."} for part in parts)
    ):
        raise ValueError(f"invalid collection gate id: {gate_id}")
    gate_abs = kb_root(repo_root) / rel / "COLLECTION.md"
    repo_rel = gate_abs.relative_to(repo_root).as_posix()
    if not is_collection_md_gate_path(repo_rel):
        raise ValueError(f"invalid collection gate id: {gate_id}")
    if not gate_abs.is_file():
        raise FileNotFoundError(f"collection contract not found for gate id: {gate_id}")
    return repo_rel


def note_collection_md_path(repo_root: Path, note_abs: Path) -> str | None:
    """Repo-relative COLLECTION.md path for the note's collection, or None.

    A note outside any collection has no conformance pair. A COLLECTION.md is
    a collection's contract rather than collection content and never pairs
    with itself.
    """
    if note_abs.name == "COLLECTION.md":
        return None
    try:
        collection = collection_for_path(note_abs, repo_root)
    except ValueError:
        return None
    return (collection / "COLLECTION.md").relative_to(repo_root.resolve()).as_posix()

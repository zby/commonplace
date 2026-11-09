"""Criterion requests and the (note, criterion) pairs they select.

A criterion is a markdown file named by its artifact identity: a repository
path for a file in the project, or `commonplace:<path>` for a library file
outside it (see `commonplace.lib.library`). In a Commonplace checkout the
library is the repository's kb/, so every criterion is a repository path; in
an installed project the gate catalog, the global types and the critique
instruction are library identities, and type specs of project collections and
`COLLECTION.md` contracts are repository paths.

A request is one of:

- a catalog gate id (`prose/source-residue`) or a bundle name (`prose`),
  resolved against the library's `instructions/review-gates/` and filtered per
  note by the gate's `requires_type` and `requires_trait`;
- the virtual `type` lens, or `type/<name>` for one type: the note's type
  spec, resolved from its frontmatter `type:`;
- the virtual `collection` lens, or `collection/<path>` (the collection
  directory relative to kb/): the `COLLECTION.md` of the note's collection;
- `critique`: the library's critique instruction, the one report criterion.

Everything here reads files and nothing writes.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

from commonplace.lib import frontmatter
from commonplace.lib.library import artifact_identity, library_root
from commonplace.lib.project_paths import collection_for_path, kb_root
from commonplace.lib.type_resolver import TypeCollisionError, validate_type_path

GATES_REL = "instructions/review-gates"
CRITIQUE_REL = "instructions/critique-note.md"
TYPE = "type"
COLLECTION = "collection"
CRITIQUE = "critique"
KINDS = ("gate", TYPE, COLLECTION, CRITIQUE)
STALENESS = "changed"
"""The only `staleness:` a catalog gate may declare."""


@dataclass(frozen=True)
class Criterion:
    identity: str      # repository path, or `commonplace:<path>` for a library file
    kind: str          # one of KINDS

    @property
    def contract(self) -> str:
        """`report` for the critique instruction, `verdict` (PASS, WARN or FAIL) otherwise."""
        return "report" if self.kind == CRITIQUE else "verdict"


def gates_dir() -> Path:
    """The gate catalog: the library's review gates (kb/instructions/review-gates in a checkout)."""
    return library_root() / GATES_REL


def _reject_unsafe(raw: str, *, kind: str) -> None:
    path = PurePosixPath(raw)
    if raw in {"", "."} or path.is_absolute() or Path(raw).is_absolute() or ".." in path.parts:
        raise ValueError(f"{kind} must be relative and stay inside the review gate catalog: {raw}")


def _is_type_request(request: str) -> bool:
    return request == TYPE or request.startswith(f"{TYPE}/")


def _is_collection_request(request: str) -> bool:
    return request == COLLECTION or request.startswith(f"{COLLECTION}/")


# --- Catalog gates ---------------------------------------------------------------

def _frontmatter(path: Path) -> dict[str, Any]:
    try:
        parsed = frontmatter.parse(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError):
        return {}
    return parsed.data if parsed.ok else {}


def _gate_metadata(path: Path) -> dict[str, Any]:
    metadata = _frontmatter(path)
    if metadata.get("staleness") != STALENESS:
        raise ValueError(f"unsupported staleness declaration in review gate {path}: "
                         f"{metadata.get('staleness')!r}; expected {STALENESS!r}")
    return metadata


def _catalog_ids(requests: list[str], gates: Path) -> list[str]:
    """Gate ids for gate ids and bundle names; a bundle is every gate in its directory."""
    found: list[str] = []
    for request in requests:
        _reject_unsafe(request, kind="criterion id or bundle")
        bundle = gates / request
        if bundle.is_dir():
            for gate in sorted(bundle.glob("*.md")):
                _gate_metadata(gate)
                found.append(f"{request}/{gate.stem}")
            continue
        gate = gates / f"{request.removesuffix('.md')}.md"
        if not gate.is_file():
            raise FileNotFoundError(f"gate not found: {request}")
        _gate_metadata(gate)
        found.append(request.removesuffix(".md"))
    return found


def resolve_requests(requests: list[str] | None) -> list[str]:
    """Catalog gate ids for the catalog requests, followed by the lens requests unchanged.

    None means all gates: every bundle plus `type` and `collection`; the
    critique stays opt-in.
    """
    gates = gates_dir()
    if requests is None:
        bundles = sorted(entry.name for entry in gates.iterdir() if entry.is_dir())
        return _catalog_ids(bundles, gates) + [TYPE, COLLECTION]
    requests = [request.strip() for request in requests]
    lenses = [request for request in requests
              if _is_type_request(request) or _is_collection_request(request) or request == CRITIQUE]
    return _catalog_ids([request for request in requests if request not in lenses], gates) + lenses


def _matches(actual: set[str], required: Any) -> bool:
    if required is None or required == "":
        return True
    if isinstance(required, str):
        return required in actual
    if isinstance(required, list):
        wanted = {item for item in required if isinstance(item, str)}
        return not required or bool(actual & wanted)
    return False


def applicable_gates(note_meta: dict[str, Any], gate_ids: list[str]) -> list[str]:
    """The gate ids whose `requires_type` and `requires_trait` the note's frontmatter satisfies."""
    note_type = note_meta.get("type")
    types = {note_type} if isinstance(note_type, str) else set()
    traits = note_meta.get("traits", [])
    traits = set(traits) if isinstance(traits, list) else set()
    gates = gates_dir()
    applicable = []
    for gate_id in gate_ids:
        metadata = _gate_metadata(gates / f"{gate_id}.md")
        if _matches(traits, metadata.get("requires_trait")) and _matches(types, metadata.get("requires_type")):
            applicable.append(gate_id)
    return applicable


# --- The type lens ---------------------------------------------------------------

def _is_type_spec_path(rel: str) -> bool:
    path = PurePosixPath(rel)
    return (path.suffix == ".md" and path.parts[:1] == ("kb",) and "review-gates" not in path.parts
            and path.parent.name == "types")


def resolve_type_request(root: Path, request: str) -> str:
    """The identity of the type spec `type/<name>` names.

    The library's global type `<name>` wins; otherwise the name must match
    exactly one collection-local `kb/**/types/<name>.md`.
    """
    name = request.strip().removeprefix(f"{TYPE}/").removesuffix(".md")
    if not name or name == TYPE or "/" in name or name in {".", ".."}:
        raise ValueError(f"invalid type gate id: {request}")
    global_spec = library_root() / "types" / f"{name}.md"
    if global_spec.is_file():
        return artifact_identity(root, global_spec)
    candidates = sorted(path for path in kb_root(root).glob(f"**/types/{name}.md")
                        if path.is_file() and _is_type_spec_path(path.relative_to(root).as_posix()))
    if not candidates:
        raise FileNotFoundError(f"type spec not found for gate id: {request}")
    if len(candidates) > 1:
        rendered = ", ".join(path.relative_to(root).as_posix() for path in candidates)
        raise ValueError(f"type gate id is ambiguous across collections: {request} ({rendered})")
    return candidates[0].relative_to(root).as_posix()


def note_type_spec(root: Path, note: Path) -> str | None:
    """The identity of the note's type spec, or None without a valid `type:` binding.

    Malformed frontmatter or a malformed `type:` value yields None: rejecting
    those is the validator's job. A type collision and a well-formed binding
    to a missing file raise.
    """
    try:
        parsed = frontmatter.parse(note.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError):
        return None
    if not parsed.ok or not isinstance(parsed.data.get("type"), str):
        return None
    try:
        canonical, resolved = validate_type_path(parsed.data["type"], repo_root=root, source_file=note)
    except TypeCollisionError:                # a binding error, not a malformed value
        raise
    except ValueError:
        return None
    if not resolved.is_file():
        raise FileNotFoundError(f"type spec not found: {canonical} (declared by {note.name})")
    return artifact_identity(root, resolved)


# --- The collection lens ---------------------------------------------------------

def resolve_collection_request(root: Path, request: str) -> str:
    """The repository path of the `COLLECTION.md` that `collection/<path>` names."""
    rel = request.strip().removeprefix(f"{COLLECTION}/").strip("/")
    parts = PurePosixPath(rel).parts
    if (not rel or rel == COLLECTION or PurePosixPath(rel).is_absolute() or any(part in {".", ".."} for part in parts)
            or "types" in parts[1:]):
        raise ValueError(f"invalid collection gate id: {request}")
    contract = kb_root(root) / rel / "COLLECTION.md"
    if not contract.is_file():
        raise FileNotFoundError(f"collection contract not found for gate id: {request}")
    return contract.relative_to(root).as_posix()


def note_collection_contract(root: Path, note: Path) -> str | None:
    """The repository path of the note's collection contract; None outside a collection or for a contract."""
    if note.name == "COLLECTION.md":
        return None
    try:
        collection = collection_for_path(note, root)
    except ValueError:
        return None
    return (collection / "COLLECTION.md").relative_to(root.resolve()).as_posix()


# --- Selection -------------------------------------------------------------------

def critique_identity(root: Path) -> str:
    path = library_root() / CRITIQUE_REL
    if not path.is_file():
        raise FileNotFoundError(f"critique instruction not found: {path}")
    return artifact_identity(root, path)


def select(root: Path, notes: list[str], requests: list[str] | None = None) -> list[tuple[str, Criterion]]:
    """The applicable (note, criterion) pairs for repository-relative notes, in request order per note."""
    root = root.resolve()
    resolved = resolve_requests(requests)
    lenses = {TYPE: [r for r in resolved if _is_type_request(r)],
              COLLECTION: [r for r in resolved if _is_collection_request(r)]}
    catalog = [r for r in resolved if r not in lenses[TYPE] and r not in lenses[COLLECTION] and r != CRITIQUE]
    gates = gates_dir()
    gate_identities = {gate_id: artifact_identity(root, gates / f"{gate_id}.md") for gate_id in catalog}
    type_specs = {resolve_type_request(root, r) for r in lenses[TYPE] if r != TYPE}
    contracts = {resolve_collection_request(root, r) for r in lenses[COLLECTION] if r != COLLECTION}
    critique = critique_identity(root) if CRITIQUE in resolved else None

    found: list[tuple[str, Criterion]] = []
    for note in notes:
        note_abs = root / note
        chosen = [Criterion(gate_identities[gate_id], "gate")
                  for gate_id in applicable_gates(_frontmatter(note_abs), catalog)]
        if lenses[TYPE]:
            spec = note_type_spec(root, note_abs)
            if spec is not None and (TYPE in lenses[TYPE] or spec in type_specs):
                chosen.append(Criterion(spec, TYPE))
        if lenses[COLLECTION]:
            contract = note_collection_contract(root, note_abs)
            if contract is not None and (COLLECTION in lenses[COLLECTION] or contract in contracts):
                chosen.append(Criterion(contract, COLLECTION))
        if critique is not None:
            chosen.append(Criterion(critique, CRITIQUE))
        seen: set[str] = set()
        for criterion in chosen:
            if criterion.identity not in seen:
                seen.add(criterion.identity)
                found.append((note, criterion))
    return found

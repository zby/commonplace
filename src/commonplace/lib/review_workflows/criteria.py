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
- `compression/<check>`: one of the library's compression checks under
  `instructions/compression-bundle/`, a verdict criterion. Each check is
  requested by its own id; there is no compression bundle request;
- `critique`, `friction`, `premises`, `compression-synthesis` and `role`:
  the library's critique, composition-friction, premise-decomposition,
  compression-synthesis and role-in-the-kb instructions, the report criteria.

The compression checks and the report criteria stay out of the default set.
The compression synthesis and the role report judge operational inputs
(`SUPPLIED`), so each runs alone and publishes no current result.

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
COMPRESSION_REL = "instructions/compression-bundle"
TYPE = "type"
COLLECTION = "collection"
CRITIQUE = "critique"
COMPRESSION = "compression"
FRICTION = "friction"
PREMISES = "premises"
SYNTHESIS = "compression-synthesis"
ROLE = "role"
REPORTS = {CRITIQUE: CRITIQUE_REL,
           FRICTION: "instructions/composition-friction-gate.md",
           PREMISES: "instructions/premise-decomposition-gate.md",
           SYNTHESIS: f"{COMPRESSION_REL}/high-impact-simplification-synthesis.md",
           ROLE: "instructions/role-in-the-kb-gate.md"}
"""Each report criterion's selector and library instruction."""
SUPPLIED = {SYNTHESIS: None, ROLE: "inbound"}
"""The report criteria that judge operational inputs, each with the input role it requires (None: any roles).

No freshness hash covers those inputs, so each runs alone, on one note,
always asked, and publishes no current result; `status` refuses it.
"""
KINDS = ("gate", TYPE, COLLECTION, CRITIQUE, "draft", COMPRESSION, FRICTION, PREMISES, SYNTHESIS, ROLE)
STALENESS = "changed"
"""The only `staleness:` a catalog gate may declare."""


@dataclass(frozen=True)
class Criterion:
    identity: str      # repository path, or `commonplace:<path>` for a library file
    kind: str          # one of KINDS

    @property
    def contract(self) -> str:
        """`report` for a report instruction, `verdict` (PASS, WARN or FAIL) otherwise."""
        return "report" if self.kind in REPORTS else "verdict"


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


def _is_compression_request(request: str) -> bool:
    return request.startswith(f"{COMPRESSION}/")


def _is_lens_request(request: str) -> bool:
    """A request resolved outside the gate catalog."""
    return (_is_type_request(request) or _is_collection_request(request) or _is_compression_request(request)
            or request in REPORTS)


# --- Catalog gates ---------------------------------------------------------------

def _frontmatter(path: Path, text: str | None = None) -> dict[str, Any]:
    """The frontmatter of `text`, or of the file at `path` when `text` is None; empty when it does not parse."""
    try:
        parsed = frontmatter.parse(path.read_text(encoding="utf-8") if text is None else text)
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
    if COMPRESSION in requests:
        raise ValueError("compression checks are requested one at a time as compression/<check>, "
                         "for example compression/detail-overhang")
    lenses = [request for request in requests if _is_lens_request(request)]
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


def _applies(note_meta: dict[str, Any], gate_meta: dict[str, Any]) -> bool:
    """Whether the note's frontmatter satisfies a gate's `requires_type` and `requires_trait`."""
    note_type = note_meta.get("type")
    types = {note_type} if isinstance(note_type, str) else set()
    traits = note_meta.get("traits", [])
    traits = set(traits) if isinstance(traits, list) else set()
    return _matches(traits, gate_meta.get("requires_trait")) and _matches(types, gate_meta.get("requires_type"))


def applicable_gates(note_meta: dict[str, Any], gate_ids: list[str]) -> list[str]:
    """The gate ids whose `requires_type` and `requires_trait` the note's frontmatter satisfies."""
    gates = gates_dir()
    return [gate_id for gate_id in gate_ids if _applies(note_meta, _gate_metadata(gates / f"{gate_id}.md"))]


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


def note_type_spec(root: Path, note: Path, text: str | None = None) -> str | None:
    """The identity of the note's type spec, or None without a valid `type:` binding.

    `text` is the note's text in place of the file's.

    Malformed frontmatter or a malformed `type:` value yields None: rejecting
    those is the validator's job. A type collision and a well-formed binding
    to a missing file raise.
    """
    declared = _frontmatter(note, text).get("type")
    if not isinstance(declared, str):
        return None
    try:
        canonical, resolved = validate_type_path(declared, repo_root=root, source_file=note)
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

def draft(root: Path, notes: list[str], filename: str) -> list[tuple[str, Criterion]]:
    """An explicit untracked/local gate, never silently registered in the catalog."""
    from commonplace.lib.validation import ValidationRun

    path = root / filename
    if (Path(filename).is_absolute() or ".." in Path(filename).parts
            or path.is_symlink() or not path.resolve().is_relative_to(root.resolve())):
        raise ValueError("draft criterion must be a confined repository-local file")
    text = path.read_bytes().decode("utf-8")
    parsed = frontmatter.parse(text)
    if not parsed.ok or parsed.data.get("type") != "types/review-gate.md":
        raise ValueError("draft must declare type: types/review-gate.md")
    if parsed.data.get("reading-scope") != "linked-files":
        raise ValueError("draft must declare supported reading-scope: linked-files; broader reading is not supported")
    problems = ValidationRun(repo_root=root, paths=(path,)).validate(path).fails
    if problems:
        raise ValueError("; ".join(problems))
    identity = path.relative_to(root).as_posix()
    return [(note, Criterion(identity, "draft")) for note in notes
            if _matches(set(_frontmatter(root / note).get("traits", [])), parsed.data.get("requires_trait"))
            and _matches({_frontmatter(root / note).get("type")}, parsed.data.get("requires_type"))]


def report_identity(root: Path, selector: str) -> str:
    """The identity of the library instruction a report selector names."""
    path = library_root() / REPORTS[selector]
    if not path.is_file():
        raise FileNotFoundError(f"{selector} instruction not found: {path}")
    return artifact_identity(root, path)


def compression_check(request: str) -> tuple[Path, dict[str, Any]]:
    """The file and frontmatter of the compression check `compression/<check>` names.

    The file must be a review gate whose `gate_id` is the request.
    """
    name = request.strip().removeprefix(f"{COMPRESSION}/").removesuffix(".md")
    if not name or "/" in name or name in {".", ".."}:
        raise ValueError(f"invalid compression check id: {request}")
    path = library_root() / COMPRESSION_REL / f"{name}.md"
    if not path.is_file():
        raise FileNotFoundError(f"compression check not found: {request}")
    metadata = _frontmatter(path)
    if metadata.get("type") != "types/review-gate.md" or metadata.get("gate_id") != f"{COMPRESSION}/{name}":
        raise ValueError(f"not a compression check: {request}")
    return path, _gate_metadata(path)


def compression_checks() -> list[str]:
    """The id of each compression check in the library, such as `compression/detail-overhang`."""
    found = []
    for path in sorted((library_root() / COMPRESSION_REL).glob("*.md")):
        metadata = _frontmatter(path)
        if metadata.get("type") == "types/review-gate.md" and metadata.get("gate_id") == f"{COMPRESSION}/{path.stem}":
            found.append(metadata["gate_id"])
    return found


def select(root: Path, notes: list[str], requests: list[str] | None = None,
           texts: dict[str, str] | None = None) -> list[tuple[str, Criterion]]:
    """The applicable (note, criterion) pairs for repository-relative notes, in request order per note.

    `texts` gives a note's text by path in place of the file's, so a
    workflow selects for the text it reviews.
    """
    root = root.resolve()
    resolved = resolve_requests(requests)
    lenses = {TYPE: [r for r in resolved if _is_type_request(r)],
              COLLECTION: [r for r in resolved if _is_collection_request(r)]}
    catalog = [r for r in resolved if not _is_lens_request(r)]
    gates = gates_dir()
    gate_identities = {gate_id: artifact_identity(root, gates / f"{gate_id}.md") for gate_id in catalog}
    type_specs = {resolve_type_request(root, r) for r in lenses[TYPE] if r != TYPE}
    contracts = {resolve_collection_request(root, r) for r in lenses[COLLECTION] if r != COLLECTION}
    checks = [(artifact_identity(root, path), metadata) for path, metadata in
              (compression_check(r) for r in dict.fromkeys(r for r in resolved if _is_compression_request(r)))]
    reports = [(selector, report_identity(root, selector)) for selector in REPORTS if selector in resolved]

    found: list[tuple[str, Criterion]] = []
    for note in notes:
        note_abs, text = root / note, (texts or {}).get(note)
        chosen = [Criterion(gate_identities[gate_id], "gate")
                  for gate_id in applicable_gates(_frontmatter(note_abs, text), catalog)]
        if lenses[TYPE]:
            spec = note_type_spec(root, note_abs, text)
            if spec is not None and (TYPE in lenses[TYPE] or spec in type_specs):
                chosen.append(Criterion(spec, TYPE))
        if lenses[COLLECTION]:
            contract = note_collection_contract(root, note_abs)
            if contract is not None and (COLLECTION in lenses[COLLECTION] or contract in contracts):
                chosen.append(Criterion(contract, COLLECTION))
        chosen += [Criterion(identity, COMPRESSION) for identity, metadata in checks
                   if _applies(_frontmatter(note_abs, text), metadata)]
        chosen += [Criterion(identity, selector) for selector, identity in reports]
        seen: set[str] = set()
        for criterion in chosen:
            if criterion.identity not in seen:
                seen.add(criterion.identity)
                found.append((note, criterion))
    return found

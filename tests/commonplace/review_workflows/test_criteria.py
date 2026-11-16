"""Which (note, criterion) pairs a request selects, in a checkout and in an installed project.

A wrong selection is silent: a sweep asks a reviewer for a pair that does not
apply, or never asks for one that does. These tests pin the selection rules
the gate sweep and `status` share.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib import library
from commonplace.lib.review_workflows import criteria
from commonplace.lib.review_workflows.criteria import select


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def note(path: Path, *, note_type: str = "types/note.md", traits: str = "[]") -> Path:
    return write(path, f"---\ndescription: d\ntype: {note_type}\ntraits: {traits}\n---\n\n# {path.stem}\n\nBody.\n")


def gate(path: Path, extra: str = "", staleness: str = "changed") -> Path:
    return write(path, f"---\nwatches: [body]\nstaleness: {staleness}\n{extra}---\n\n## Failure mode\n\nx\n")


def spec(path: Path) -> Path:
    return write(path, f"# {path.stem}\n\n## Authoring Instructions\n\nOne claim.\n")


@pytest.fixture
def checkout(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """A Commonplace checkout: the library is the repository's kb/."""
    monkeypatch.setattr(library, "_library_root", lambda _override: (tmp_path / "kb").resolve())
    gates = tmp_path / "kb/instructions/review-gates"
    gate(gates / "prose/residue.md")
    gate(gates / "prose/hedging.md", "requires_trait: [has-comparison, has-external-sources]\n")
    gate(gates / "structural/adr-shape.md", "requires_type: types/adr.md\n")
    write(tmp_path / "kb/instructions/critique-note.md", "# Critique\n")
    spec(tmp_path / "kb/types/note.md")
    spec(tmp_path / "kb/types/definition.md")
    write(tmp_path / "kb/notes/COLLECTION.md", "# Notes\n")
    note(tmp_path / "kb/notes/plain.md")
    note(tmp_path / "kb/notes/compared.md", traits="[has-comparison]")
    note(tmp_path / "kb/notes/term.md", note_type="types/definition.md")
    return tmp_path


def chosen(root: Path, notes: list[str], requests: list[str] | None) -> list[tuple[str, str, str]]:
    return [(n, c.identity, c.kind) for n, c in select(root, notes, requests)]


def test_bundle_requests_apply_trait_and_type_requirements(checkout: Path) -> None:
    gates = "kb/instructions/review-gates"
    write(checkout / "kb/types/adr.md", "# ADR\n")
    note(checkout / "kb/notes/decision.md", note_type="types/adr.md")
    pairs = chosen(checkout, ["kb/notes/plain.md", "kb/notes/compared.md", "kb/notes/decision.md"],
                   ["prose", "structural"])
    assert pairs == [
        ("kb/notes/plain.md", f"{gates}/prose/residue.md", "gate"),
        ("kb/notes/compared.md", f"{gates}/prose/hedging.md", "gate"),
        ("kb/notes/compared.md", f"{gates}/prose/residue.md", "gate"),
        ("kb/notes/decision.md", f"{gates}/prose/residue.md", "gate"),
        ("kb/notes/decision.md", f"{gates}/structural/adr-shape.md", "gate"),
    ]


@pytest.mark.parametrize(("request_", "error"), [
    ("prose/missing", FileNotFoundError),
    ("../outside", ValueError),
])
def test_unknown_or_escaping_gate_requests_are_refused(checkout: Path, request_: str, error: type) -> None:
    with pytest.raises(error):
        select(checkout, ["kb/notes/plain.md"], [request_])


def test_gate_with_unsupported_staleness_is_refused(checkout: Path) -> None:
    gate(checkout / "kb/instructions/review-gates/prose/odd.md", staleness="always")
    with pytest.raises(ValueError, match="unsupported staleness"):
        select(checkout, ["kb/notes/plain.md"], ["prose"])


def test_type_lens_pairs_each_note_with_its_type_spec(checkout: Path) -> None:
    notes = ["kb/notes/plain.md", "kb/notes/term.md"]
    assert chosen(checkout, notes, ["type"]) == [
        ("kb/notes/plain.md", "kb/types/note.md", "type"), ("kb/notes/term.md", "kb/types/definition.md", "type")]
    assert chosen(checkout, notes, ["type/definition"]) == [("kb/notes/term.md", "kb/types/definition.md", "type")]
    note(checkout / "kb/notes/broken.md", note_type="Not A Type!")
    assert chosen(checkout, ["kb/notes/broken.md"], ["type"]) == []


def test_collection_lens_pairs_each_note_with_its_nearest_contract(checkout: Path) -> None:
    write(checkout / "kb/notes/deep/COLLECTION.md", "# Deep\n")
    note(checkout / "kb/notes/deep/inner.md")
    note(checkout / "kb/loose/stray.md")
    notes = ["kb/notes/plain.md", "kb/notes/deep/inner.md", "kb/notes/COLLECTION.md", "kb/loose/stray.md"]
    assert chosen(checkout, notes, ["collection"]) == [
        ("kb/notes/plain.md", "kb/notes/COLLECTION.md", "collection"),
        ("kb/notes/deep/inner.md", "kb/notes/deep/COLLECTION.md", "collection")]
    assert chosen(checkout, notes, ["collection/notes/deep"]) == [
        ("kb/notes/deep/inner.md", "kb/notes/deep/COLLECTION.md", "collection")]
    for bad in ("collection/../notes", "collection/notes/types/x"):
        with pytest.raises(ValueError, match="invalid collection gate id"):
            criteria.resolve_collection_request(checkout, bad)
    with pytest.raises(FileNotFoundError):
        criteria.resolve_collection_request(checkout, "collection/missing")


def test_installed_library_files_are_library_identities(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    root, lib = tmp_path / "project", tmp_path / "share/commonplace"
    gate(lib / "instructions/review-gates/prose/residue.md")
    write(lib / "instructions/critique-note.md", "# Critique\n")
    spec(lib / "types/note.md")
    write(root / "kb/notes/COLLECTION.md", "# Notes\n")
    spec(root / "kb/notes/types/claim.md")
    note(root / "kb/notes/plain.md")
    note(root / "kb/notes/claim.md", note_type="notes/types/claim.md")
    monkeypatch.setattr(library, "_library_root", lambda _override: lib.resolve())
    assert chosen(root, ["kb/notes/plain.md", "kb/notes/claim.md"], ["prose", "type", "collection", "critique"]) == [
        ("kb/notes/plain.md", "commonplace:instructions/review-gates/prose/residue.md", "gate"),
        ("kb/notes/plain.md", "commonplace:types/note.md", "type"),
        ("kb/notes/plain.md", "kb/notes/COLLECTION.md", "collection"),
        ("kb/notes/plain.md", "commonplace:instructions/critique-note.md", "critique"),
        ("kb/notes/claim.md", "commonplace:instructions/review-gates/prose/residue.md", "gate"),
        ("kb/notes/claim.md", "kb/notes/types/claim.md", "type"),
        ("kb/notes/claim.md", "kb/notes/COLLECTION.md", "collection"),
        ("kb/notes/claim.md", "commonplace:instructions/critique-note.md", "critique"),
    ]
    assert criteria.resolve_type_request(root, "type/note") == "commonplace:types/note.md"

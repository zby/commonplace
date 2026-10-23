"""Pinned criteria include the collection policies consumed while validating types."""

from pathlib import Path
from types import SimpleNamespace

from commonplace.lib.agentic_analysis.workflow import Method


def write(library: Path, path: str, text: str) -> None:
    target = library / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def method_fixture(tmp_path: Path) -> Method:
    library = tmp_path / "kb"
    for name in ("type-spec", "collection-contract"):
        write(library, f"types/{name}.md", (
            f"---\ntype: types/type-spec.md\nname: {name}\ndescription: Fixture\n"
            "schema: null\n---\n# Type\n"
        ))
    write(library, "types/COLLECTION.md", (
        "---\ntype: types/collection-contract.md\n---\n# Global types\n"
    ))
    write(library, "teams/claims/COLLECTION.md", (
        "---\ntype: types/collection-contract.md\nunquoted-source-limit: 2\n---\n# Claims\n"
    ))
    write(library, "teams/claims/types/result.md", (
        "---\ntype: types/type-spec.md\nname: result\ndescription: Fixture\n"
        "schema: ./result.schema.yaml\n---\n# Result\n"
    ))
    write(library, "teams/claims/types/result.schema.yaml", "type: object\n")
    # Isolate criteria capture from plan parsing and directory-layout construction.
    method = object.__new__(Method)
    method.library = library
    method.groups = {"fixture": {"result": "teams/claims/types/result.md"}}
    method.type_spec = "teams/claims/types/result.md"
    method.layout = SimpleNamespace(roles={})
    return method


def test_criteria_capture_governing_contracts_and_their_type_closure(tmp_path: Path):
    method = method_fixture(tmp_path)
    pinned = method.criteria()
    assert {
        "teams/claims/types/result.md",
        "teams/claims/types/result.schema.yaml",
        "teams/claims/COLLECTION.md",
        "types/type-spec.md",
        "types/collection-contract.md",
        "types/COLLECTION.md",
    } <= pinned.keys()
    assert all(data == (method.library / path).read_bytes() for path, data in pinned.items())


def test_captured_collection_policy_does_not_follow_later_disk_edits(tmp_path: Path):
    method = method_fixture(tmp_path)
    pinned = method.criteria()
    contract = "teams/claims/COLLECTION.md"
    original = (method.library / contract).read_bytes()
    (method.library / contract).write_bytes(original.replace(b"limit: 2", b"limit: 9"))
    assert pinned[contract] == original
    assert method.criteria()[contract] != original


def test_criteria_do_not_capture_unrelated_collection_policies(tmp_path: Path):
    method = method_fixture(tmp_path)
    write(method.library, "elsewhere/COLLECTION.md", "# Unrelated collection\n")
    pinned = method.criteria()
    assert "elsewhere/COLLECTION.md" not in pinned

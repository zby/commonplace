from hashlib import sha256

import pytest
import yaml

from commonplace.lib.project_paths import list_directory_validation_paths
from commonplace.lib.validation import ValidationRun

pytestmark = pytest.mark.usefixtures("tmp_library")


def make_artifact(root, *, closed=False, required=("main.md",)):
    types = root / "kb/reports/types"
    types.mkdir(parents=True)
    (root / "kb/reports/COLLECTION.md").write_text("# Reports\n")
    (types / "set.md").write_text("---\ntype: types/type-spec.md\nname: set\ndescription: Example set\nschema: ./set.schema.yaml\n---\n# Set\n")
    schema = {"type": "object", "properties": {"members": {
        "type": "object", "required": list(required),
        "properties": {"main.md": {}, "optional.md": {}},
        "additionalProperties": not closed,
    }}}
    (types / "set.schema.yaml").write_text(yaml.safe_dump(schema))
    directory = root / "kb/reports/retained/example"
    directory.mkdir(parents=True)
    (directory / "main.md").write_text("# Main\n")
    (directory / "ARTIFACT.yaml").write_text("type: reports/types/set.md\n")
    return directory


def run(root, directory):
    return ValidationRun(root, (directory,)).validate(directory)


def test_open_and_closed_membership(tmp_path):
    directory = make_artifact(tmp_path)
    (directory / "extra.md").write_text("# Extra\n")
    assert not run(tmp_path, directory).fails
    schema_path = tmp_path / "kb/reports/types/set.schema.yaml"
    schema = yaml.safe_load(schema_path.read_text())
    schema["properties"]["members"]["additionalProperties"] = False
    schema_path.write_text(yaml.safe_dump(schema))
    from commonplace.lib.type_resolver import (
        _load_schema_with_library,
        _validator_for_path_with_library,
    )
    _load_schema_with_library.cache_clear()
    _validator_for_path_with_library.cache_clear()
    assert run(tmp_path, directory).fails
    (directory / "extra.md").unlink()
    (directory / "optional.md").write_text("# Optional\n")
    assert not run(tmp_path, directory).fails
    (directory / "main.md").unlink()
    assert run(tmp_path, directory).fails


@pytest.mark.parametrize("manifest", ["[bad", "type: reports/types/set.md\ntype: reports/types/set.md\n"])
def test_invalid_manifest_keeps_member_errors(tmp_path, manifest):
    directory = make_artifact(tmp_path)
    (directory / "ARTIFACT.yaml").write_text(manifest)
    (directory / "main.md").write_text("---\ntype: types/missing.md\n---\n# Main\n")
    errors = run(tmp_path, directory).fails
    assert any("member main.md" in error for error in errors)
    assert any("artifact:" in error for error in errors)


def test_hashes_are_optional_but_checked_against_exact_bytes(tmp_path):
    directory = make_artifact(tmp_path)
    content = b"# Main\r\n"
    (directory / "main.md").write_bytes(content)
    manifest = {"type": "reports/types/set.md", "members": {"main.md": {"sha256": sha256(content).hexdigest()}}}
    (directory / "ARTIFACT.yaml").write_text(yaml.safe_dump(manifest))
    assert not run(tmp_path, directory).fails
    (directory / "main.md").write_bytes(b"# Main\n")
    assert any("SHA-256 mismatch" in error for error in run(tmp_path, directory).fails)


def test_traversal_groups_members_and_keeps_descendants(tmp_path):
    directory = make_artifact(tmp_path, closed=True)
    (directory / "other.txt").write_text("outside membership")
    (directory / "subdir").mkdir()
    child = directory / "subdir/child.md"
    child.write_text("---\ntype: types/missing.md\n---\n# Child\n")
    paths = tuple(list_directory_validation_paths(directory))
    outcome = ValidationRun(tmp_path, paths).evaluate()
    assert set(outcome.results) == {directory, child}
    assert not outcome.results[directory].fails
    assert outcome.results[child].fails


def test_file_validation_does_not_load_siblings(tmp_path):
    directory = make_artifact(tmp_path)
    (directory / "ARTIFACT.yaml").write_text("[bad")
    member = directory / "main.md"
    assert not ValidationRun(tmp_path, (member,)).validate(member).fails


def test_candidate_overlay_is_validated_instead_of_disk(tmp_path):
    directory = make_artifact(tmp_path)
    member = directory / "main.md"
    member.write_text("---\ntype: types/missing.md\n---\n# Main\n")
    assert run(tmp_path, directory).fails
    context = ValidationRun(tmp_path, (directory,), content_overrides={member: b"# Candidate\r\n"})
    assert not context.validate(directory).fails


def test_symlink_member_fails(tmp_path):
    directory = make_artifact(tmp_path)
    outside = tmp_path / "outside.md"
    outside.write_text("# Outside\n")
    (directory / "optional.md").symlink_to(outside)
    assert any("symlink" in error for error in run(tmp_path, directory).fails)


def test_collection_sweep_reports_invalid_undeclared_member(tmp_path):
    directory = make_artifact(tmp_path)
    member = directory / "extra.md"
    member.write_bytes(b"\xff")
    paths = tuple(list_directory_validation_paths(directory.parent))
    outcome = ValidationRun(tmp_path, paths, collection=directory.parent).evaluate()
    assert tuple(outcome.results) == (directory,)
    assert any("member extra.md" in error for error in outcome.results[directory].fails)


def test_cli_json_counts_artifact_once_and_locates_member_failure(tmp_path, capsys, monkeypatch):
    import json

    from commonplace.cli.validate_notes import main

    directory = make_artifact(tmp_path)
    (directory / "optional.md").write_text("---\ntype: types/missing.md\n---\n# Invalid\n")
    monkeypatch.chdir(tmp_path)
    assert main([str(directory), "--json"]) == 1
    report = json.loads(capsys.readouterr().out)
    assert report["summary"]["files_analysed"] == 1
    assert len(report["analysed_artifacts"]) == 1
    artifact = report["analysed_artifacts"][0]
    assert artifact["path"] == directory.relative_to(tmp_path).as_posix()
    assert artifact["type"] == "reports/types/set.md"
    assert any(d["subject"].endswith("/optional.md") for d in report["diagnostics"])


def test_artifact_size_diagnostic_does_not_dump_member_bodies(tmp_path):
    directory = make_artifact(tmp_path)
    schema_path = tmp_path / "kb/reports/types/set.schema.yaml"
    schema = yaml.safe_load(schema_path.read_text())
    schema["properties"]["members"]["maxProperties"] = 0
    schema_path.write_text(yaml.safe_dump(schema))
    (directory / "main.md").write_text("DO-NOT-DUMP-CONTENT\n" * 200)
    errors = run(tmp_path, directory).fails
    assert any("maxProperties" in error for error in errors)
    assert all("DO-NOT-DUMP-CONTENT" not in error for error in errors)

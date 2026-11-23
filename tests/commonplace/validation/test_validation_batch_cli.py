import json
import shlex

import pytest

from commonplace.cli import validate_notes


def test_batch_matches_single_file_checks(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    types = tmp_path / "kb/theory/types"
    types.mkdir(parents=True)
    (types / "example.md").write_text("---\ntype: types/type-spec.md\nname: example\ndescription: Example type\nschema: null\n---\n")
    theory = tmp_path / "kb/theory"
    (theory / "COLLECTION.md").write_text("# Theory\n")
    inputs = {
        "kb/notes/clean.md": "# Clean\n",
        "kb/theory/with space.md": "---\ntype: theory/types/example.md\n---\n# Example\n[broken](./missing.md)\n",
        "kb/notes/bad.md": "---\ntype: [\n---\n",
    }
    singles = []
    for name, content in inputs.items():
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        validate_notes.main(["--json", name])
        singles.append(json.loads(capsys.readouterr().out))
    assert [s["status"] for s in singles] == ["success", "warning", "failed"]

    args = [*inputs, "./kb/notes/clean.md"]
    assert validate_notes.main(["--json", "--output", "receipt.json", *args]) == 1
    stdout = capsys.readouterr().out
    assert (tmp_path / "receipt.json").read_text() == stdout
    report = json.loads(stdout)
    assert report["schema"] == "commonplace.validation.batch.v1"
    assert report["targets"] == args
    assert report["summary"]["files_analysed"] == 3
    for field in ("diagnostics", "analysed_artifacts"):
        assert report[field] == [item for s in singles for item in s[field]]
    command, *full_args = shlex.split(report["details_command"])
    assert command == "commonplace-validate"
    assert validate_notes.main(full_args) == 1
    assert capsys.readouterr().out.count("=== VALIDATION:") == 3
    assert validate_notes.main(args[:2]) == 0  # Warnings alone are not failures.


@pytest.mark.parametrize("other", ["all", "kb", "types", "ARTIFACT.yaml", "--role x a.md",
                                   "--handoff record a.md", "--collection notes a.md"])
def test_batch_rejects_non_file_modes(tmp_path, monkeypatch, other):
    monkeypatch.chdir(tmp_path)
    with pytest.raises(SystemExit) as exc:
        validate_notes.main(["a.md", *other.split()])
    assert exc.value.code == 2


def test_batch_preflights_all_paths_before_checking_or_writing(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "exists.md").touch()
    (tmp_path / "receipt").write_text("old receipt")
    monkeypatch.setattr(validate_notes, "run_validation", lambda *a, **kw: pytest.fail("ran"))
    assert validate_notes.main(["--json", "--output", "receipt", "exists.md", "missing.md"]) == 1
    assert (tmp_path / "receipt").read_text() == "old receipt"

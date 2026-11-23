"""A state-directory ignore marker must not bypass explicit typed validation."""

import json

import pytest

from commonplace.cli.validate_notes import main, resolve_validation_target
from commonplace.lib import library
from commonplace.lib.validation import ValidationRun
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, copy_repo_files


@pytest.mark.parametrize("in_memory", [False, True])
def test_explicit_state_artifacts_are_validated_despite_ignore_marker(tmp_path, monkeypatch, capsys, in_memory):
    root = tmp_path / "repo"
    copy_repo_files(root, *NOTE_TYPE_SPECS, "kb/types/connect-report.md", "kb/types/connect-report.schema.yaml")
    monkeypatch.setattr(library, "_library_root", lambda *_args, **_kwargs: root / "kb")
    monkeypatch.chdir(root)
    state = root / "kb/workflow-state/data/current"
    state.mkdir(parents=True)
    (state / ".commonplace-validation-ignore").touch()
    path = state / "invalid-report.md"
    text = ("---\ntype: types/connect-report.md\ndescription: A deliberately malformed report "
            "to probe explicit validation\n---\n\n# Report\n")
    if not in_memory:
        path.write_text(text)
        assert resolve_validation_target(str(path), repo_root=root).paths == (path,)
        assert main([str(path), "--json"]) == 1
        payload = json.loads(capsys.readouterr().out)
        assert payload["summary"]["files_analysed"] == 1
        assert payload["summary"]["failures"] > 0
    run = ValidationRun(repo_root=root, paths=(path,), content_overrides={path: text} if in_memory else {})
    result = run.validate(path)
    assert any("'source' is a required property" in failure for failure in result.fails), result.fails
    assert path.exists() != in_memory

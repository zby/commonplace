"""Static fixture reuse must not share mutable state or hide changed inputs."""
from __future__ import annotations

import yaml

from commonplace.lib.agentic_analysis.plan import PLAN
from tests.commonplace.agentic_analysis import execution_fixtures
from tests.commonplace.agentic_analysis.execution_fixtures import git, method_snapshot
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared,  # noqa: PLC0414 - fixture registration
)
from tests.commonplace.agentic_analysis.fixtures import expanded


def test_prepared_checkout_has_independent_files_and_git_state(prepared, prepared_template):
    source = "src/commonplace/artifactrun/engine.py"
    baseline = (prepared_template.repo / source).read_bytes()
    (prepared.repo / source).write_text("# Changed in this test only.\n")
    git(prepared.repo, "config", "fixture.isolation", "local")
    git(prepared.repo, "add", source)
    git(prepared.repo, "commit", "--quiet", "-m", "Change isolated checkout")
    assert (prepared_template.repo / source).read_bytes() == baseline
    assert git(prepared_template.repo, "rev-parse", "HEAD") == prepared_template.commit
    assert git(prepared.repo, "rev-parse", "HEAD") != prepared_template.commit
    assert "fixture.isolation=local" not in git(prepared_template.repo, "config", "--local", "--list")
    assert prepared.preparation.parent == prepared.repo.parent


def test_cached_plan_returns_independent_nested_data(prepared):
    first = prepared.plan()
    expected = expanded(prepared.repo / "kb")
    assert first == expected
    first["jobs"][0]["handler"] = "changed"
    first["jobs"][0]["inputs"].clear()
    assert prepared.plan() == expected


def test_unchanged_method_and_generated_state_reuse_baseline(prepared, monkeypatch):
    def unexpected_expansion(_library):
        raise AssertionError("Unchanged method should reuse the baseline")

    monkeypatch.setattr(execution_fixtures, "expanded", unexpected_expansion)
    expected = prepared.plan()
    output = prepared.repo / "kb/agentic-system-analyses/state/test-run/artifact/report.md"
    output.parent.mkdir(parents=True)
    output.write_text("Generated state is not a method input.\n")
    assert prepared.plan() == expected


def test_changed_plan_is_really_expanded(prepared):
    library = prepared.repo / "kb"
    path = library / PLAN
    compact = yaml.safe_load(path.read_text())
    compact["jobs"][2]["max-attempts"] = 7
    path.write_text(yaml.safe_dump(compact))
    actual = prepared.plan()
    boundary = next(job for job in actual["jobs"] if job["name"] == "boundary")
    assert boundary["max-attempts"] == 7
    assert actual == expanded(library)
    assert method_snapshot(library) != prepared.template.inputs


def test_added_input_invalidates_baseline(prepared, monkeypatch):
    library = prepared.repo / "kb"
    (library / "types/extra.md").write_text("New method input.\n")
    calls = []
    monkeypatch.setattr(execution_fixtures, "expanded", lambda path: calls.append(path) or {"fresh": True})
    assert prepared.plan() == {"fresh": True}
    assert calls == [library]


def test_removed_input_invalidates_baseline(prepared, monkeypatch):
    library = prepared.repo / "kb"
    (library / "types/note.md").unlink()
    calls = []
    monkeypatch.setattr(execution_fixtures, "expanded", lambda path: calls.append(path) or {"fresh": True})
    assert prepared.plan() == {"fresh": True}
    assert calls == [library]

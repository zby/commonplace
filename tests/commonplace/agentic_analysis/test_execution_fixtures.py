"""Static fixture reuse must not share mutable state."""
from __future__ import annotations

from commonplace.lib.agentic_analysis.preparation import RUNTIME_MARKER
from tests.commonplace.agentic_analysis.execution_fixtures import git, method_snapshot
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared,  # noqa: PLC0414 - fixture registration
)


def test_prepared_checkout_has_independent_files_and_git_state(prepared, prepared_template):
    baseline = (prepared_template.repo / RUNTIME_MARKER).read_bytes()
    (prepared.repo / RUNTIME_MARKER).write_text("# Changed in this test only.\n")
    git(prepared.repo, "config", "fixture.isolation", "local")
    git(prepared.repo, "add", RUNTIME_MARKER)
    git(prepared.repo, "commit", "--quiet", "-m", "Change isolated checkout")
    assert (prepared_template.repo / RUNTIME_MARKER).read_bytes() == baseline
    assert git(prepared_template.repo, "rev-parse", "HEAD") == prepared_template.commit
    assert git(prepared.repo, "rev-parse", "HEAD") != prepared_template.commit
    assert "fixture.isolation=local" not in git(prepared_template.repo, "config", "--local", "--list")
    assert prepared.preparation.parent == prepared.repo.parent


def test_generated_state_is_not_a_method_input(prepared):
    library = prepared.repo / "kb"
    output = library / "agentic-system-analyses/state/test-run/artifact/report.md"
    output.parent.mkdir(parents=True)
    output.write_text("Generated state is not a method input.\n")
    assert method_snapshot(library) == prepared.template.inputs
    (library / "types/extra.md").write_text("New method input.\n")
    assert method_snapshot(library) != prepared.template.inputs

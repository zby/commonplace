"""Reject the status defects that previously consumed semantic correction rounds."""

import pytest

from commonplace.lib.agentic_analysis.records import (
    conclusion_status_errors,
)
from commonplace.lib.validation import validate_draft_in_role
from tests.commonplace.agentic_analysis.fixtures import member_fixture

pytestmark = pytest.mark.usefixtures("tmp_library")


def test_member_validator_rejects_and_accepts_corrected_status(tmp_path):
    directory = member_fixture(tmp_path) / "artifact"
    runtime = directory / "runtime.md"
    valid = runtime.read_text()
    runtime.write_text(valid.replace(
        "- implementation conclusion status: wired",
        "- operation conclusion status: unobserved",
    ))
    findings = validate_draft_in_role(directory, "runtime", runtime, repo_root=tmp_path)
    assert any("conclusion status" in finding.message for finding in findings if not finding.info)
    runtime.write_text(valid)
    findings = validate_draft_in_role(directory, "runtime", runtime, repo_root=tmp_path)
    assert not [finding for finding in findings if not finding.info and not finding.warn]


def route(fields: str, prefix: str = "RT-") -> str:
    return f"## Shared records\n\n### Routes\n\n#### {prefix}RTE-model-call\n\nLabel: Recall\n\n{fields}\n"


@pytest.mark.parametrize("other", [
    "> - implementation conclusion status: wired\n",
    "```markdown\n- implementation conclusion status: wired\n```\n",
    "#### On [RT-RTE-model-call](runtime.md#rt-rte-model-call)\n- implementation conclusion status: wired\n",
    "#### MEM-RTE-memory-update\n\nLabel: Another route\n- implementation conclusion status: wired\n",
])
def test_excerpts_and_other_records_cannot_supply_a_route_status(other: str) -> None:
    errors = conclusion_status_errors(route(other))
    assert any("RTE-model-call: missing labelled field" in error for error in errors)

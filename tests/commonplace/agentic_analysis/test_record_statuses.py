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


def test_unlabelled_route_statuses_do_not_satisfy_the_contract() -> None:
    prefix = "MEM-"
    errors = conclusion_status_errors(route("The route is wired; operation unobserved.", prefix))
    assert len(errors) == 1
    assert prefix + "RTE-model-call" in errors[0] and "missing labelled field" in errors[0]


@pytest.mark.parametrize("value", ["", "unobserved", "wired; observed", "wired — code inspected"])
def test_invalid_or_combined_values_are_rejected(value: str) -> None:
    errors = conclusion_status_errors(route(f"- implementation conclusion status: {value}"))
    assert len(errors) == 1 and "invalid value" in errors[0]


def test_a_repeated_invalid_value_is_one_finding_naming_each_record() -> None:
    body = (route("- implementation conclusion status: wired\n- operation conclusion status: uninspected.")
            + "\n#### RT-RTE-resume\n\nLabel: Resume\n\n- implementation conclusion status: wired\n"
            "- operation conclusion status: uninspected.\n")
    (error,) = conclusion_status_errors(body)
    assert "invalid value 'uninspected.' in RT-RTE-model-call, RT-RTE-resume (2 fields)" in error


def test_layers_remain_separate_and_ordinary_unobserved_prose_is_allowed() -> None:
    fields = ("- implementation conclusion status: `wired`\n"
              "- operation conclusion status: uninspected\n"
              "Host behavior remains unobserved.")
    assert conclusion_status_errors(route(fields)) == []
    duplicate = fields + "\n- Operation conclusion status: observed"
    assert any("duplicate operation conclusion status" in error
               for error in conclusion_status_errors(route(duplicate)))


@pytest.mark.parametrize("other", [
    "> - implementation conclusion status: wired\n",
    "```markdown\n- implementation conclusion status: wired\n```\n",
    "#### On [RT-RTE-model-call](runtime.md#rt-rte-model-call)\n- implementation conclusion status: wired\n",
    "#### MEM-RTE-memory-update\n\nLabel: Another route\n- implementation conclusion status: wired\n",
])
def test_excerpts_and_other_records_cannot_supply_a_route_status(other: str) -> None:
    errors = conclusion_status_errors(route(other))
    assert any("RTE-model-call: missing labelled field" in error for error in errors)

"""Reject the status defects that previously consumed semantic correction rounds."""

import re
from pathlib import Path

import pytest

from commonplace.lib import agentic_publication
from commonplace.lib.agentic_records import (
    conclusion_status_errors,
)
from commonplace.workflow import Done, Handout
from tests.commonplace.lib.test_agentic_analysis import runtime_text
from tests.commonplace.lib.test_agentic_workflow import (
    Fixture,
    agent,
    drive_to,
    prompt_of,
)

pytestmark = pytest.mark.usefixtures("tmp_library")


def route(fields: str, prefix: str = "RT-") -> str:
    return f"## Shared records\n\n### Routes\n\n#### {prefix}RTE-model-call — Recall\n\n{fields}\n"


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
            + "\n#### RT-RTE-resume — Resume\n\n- implementation conclusion status: wired\n"
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
    "#### On RT-RTE-model-call — Annotation\n- implementation conclusion status: wired\n",
    "#### MEM-RTE-memory-update — Another route\n- implementation conclusion status: wired\n",
])
def test_excerpts_and_other_records_cannot_supply_a_route_status(other: str) -> None:
    errors = conclusion_status_errors(route(other))
    assert any("RTE-model-call: missing labelled field" in error for error in errors)


@pytest.mark.slow
def test_status_defects_are_repaired_before_reconciliation(
    tmp_path: Path, monkeypatch,
) -> None:
    defect = "- operation conclusion status: unobserved"
    monkeypatch.setattr(agentic_publication, "running_package_root", lambda: tmp_path)
    fixture = Fixture(tmp_path)
    valid = runtime_text(fixture.revision)
    invalid = valid.replace("- implementation conclusion status: wired", defect)

    def runtime(handout: Handout) -> None:
        if handout.attempt == 1:
            text = invalid
        else:
            prompt = handout.prompt_path.read_text(encoding="utf-8")
            preserved = Path(re.search(r"^previous-output = (.+)$", prompt, re.MULTILINE)[1])
            text = preserved.read_text(encoding="utf-8")
            assert text == invalid
            text = text.replace(defect, "- implementation conclusion status: wired")
            assert text == valid
        handout.output_path.write_text(text, encoding="utf-8")

    scripted, definition = agent(fixture, **{"runtime-0": runtime})
    drive_to(scripted, "runtime-0")
    attempt, prompt = prompt_of(scripted.round(), "runtime-0")
    assert attempt == 2 and "conclusion status:" in prompt
    assert isinstance(scripted.run()[-1], Done)
    assert scripted.launched.count("runtime-0") == 2
    assert scripted.launched.count("reconcile-0") == 1
    assert definition.publications == 1

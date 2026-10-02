"""Reject the status defects that previously consumed semantic correction rounds."""

import re
from pathlib import Path

import pytest

from commonplace.lib import agentic_publication, validation
from commonplace.lib.agentic_records import (
    CONCLUSION_STATUSES,
    conclusion_status_errors,
)
from commonplace.workflow import Done, Handout
from tests.commonplace.lib.test_agentic_analysis import member_fixture, runtime_text
from tests.commonplace.lib.test_agentic_workflow import (
    Fixture,
    agent,
    drive_to,
    prompt_of,
)

pytestmark = pytest.mark.usefixtures("tmp_library")


def route(fields: str, prefix: str = "") -> str:
    return f"## Shared records\n\n### Routes\n\n#### {prefix}RTE-1 — Recall\n\n{fields}\n"


@pytest.mark.parametrize("status", sorted(CONCLUSION_STATUSES))
def test_accepts_each_controlled_status(status: str) -> None:
    assert conclusion_status_errors(route(f"- implementation conclusion status: {status}")) == []


@pytest.mark.parametrize("prefix", ["", "MEM-", "EPI-"])
def test_unlabelled_route_statuses_do_not_satisfy_the_contract(prefix: str) -> None:
    errors = conclusion_status_errors(route("The route is wired; operation unobserved.", prefix))
    assert len(errors) == 1
    assert prefix + "RTE-1" in errors[0] and "missing labelled field" in errors[0]


@pytest.mark.parametrize("value", ["", "unobserved", "wired; observed", "wired — code inspected"])
def test_invalid_or_combined_values_are_rejected(value: str) -> None:
    errors = conclusion_status_errors(route(f"- implementation conclusion status: {value}"))
    assert len(errors) == 1 and "invalid value" in errors[0]


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
    "#### On RTE-1 — Annotation\n- implementation conclusion status: wired\n",
    "#### MEM-RTE-2 — Another route\n- implementation conclusion status: wired\n",
])
def test_excerpts_and_other_records_cannot_supply_a_route_status(other: str) -> None:
    errors = conclusion_status_errors(route(other))
    assert any("RTE-1: missing labelled field" in error for error in errors)


def test_current_member_validation_rejects_the_old_final_blocker(tmp_path: Path) -> None:
    runtime = member_fixture(tmp_path) / "output/runtime.md"
    text = runtime.read_text()
    assert validation.validate_note(runtime, repo_root=tmp_path).fails == []
    runtime.write_text(text.replace(
        "- implementation conclusion status: wired",
        "- implementation conclusion status: wired\n- operation conclusion status: unobserved",
    ))
    assert any("invalid value 'unobserved'" in error
               for error in validation.validate_note(runtime, repo_root=tmp_path).fails)


@pytest.mark.parametrize("defect", [
    "The route is wired; operation unobserved.",
    "- operation conclusion status: unobserved",
])
def test_status_defects_are_amended_before_reconciliation(
    tmp_path: Path, monkeypatch, defect: str,
) -> None:
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

    scripted, definition = agent(fixture, runtime=runtime)
    drive_to(scripted, "runtime")
    attempt, prompt = prompt_of(scripted.round(), "runtime")
    assert attempt == 2 and "conclusion status:" in prompt
    assert isinstance(scripted.run()[-1], Done)
    assert scripted.launched.count("runtime") == 2
    assert scripted.launched.count("reconcile-0") == 1
    assert definition.publications == 1

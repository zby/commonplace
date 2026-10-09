"""A plan-named hand-out template fills one section of the engine's prompt frame."""

from __future__ import annotations

import pytest
import yaml

from commonplace.artifactrun import PlanError, start_run
from tests.commonplace.artifactrun.support import Coordinator, record_calls, toy_library

pytestmark = pytest.mark.usefixtures("tmp_library")

TEMPLATE = """---
type: types/text.md
---
You write the {role} member, typed {member-type}, of a {set-type} artifact
about {param:subject}. Write it to {output}.

[answers]
Answer every blocker of a refusal in {answers}.

Validate it at {validation-role}.
"""


def templated_run(tmp_path, monkeypatch, template: str = TEMPLATE) -> Coordinator:
    declaration, method = toy_library(tmp_path, compact=True)
    (method / "handout.md").write_text(template, encoding="utf-8")
    data = yaml.safe_load(declaration.read_text())
    data["handout"] = "handout.md"
    declaration.write_text(yaml.safe_dump(data, sort_keys=False))
    record_calls(monkeypatch)
    start_run(tmp_path / "run", declaration, parameters={"subject": "toy"})
    c = Coordinator(tmp_path / "run", method, tmp_path / "handlers.log")
    c.advance()
    return c


def section(c: Coordinator, job: str) -> str:
    """The template's section: after the input lines, before the reading batches."""
    prompt = c.handout(job).prompt.read_text(encoding="utf-8")
    head, _, _ = prompt.partition("## Input reading batches")
    return head.split("\n\n", 1)[1]


def test_the_template_fills_one_section_of_the_frame(tmp_path, monkeypatch):
    c = templated_run(tmp_path, monkeypatch)
    c.through_brief()
    text = section(c, "report")
    assert text.startswith("You write the report member, typed types/toy-report.md, of a types/toy-set.md artifact\n"
                           "about toy. Write it to report.")
    assert "Answer every blocker of a refusal in answers." in text and "[answers]" not in text
    assert "Validate it at report." in text and "type: types/text.md" not in text
    prompt = c.handout("report").prompt.read_text(encoding="utf-8")
    assert "handout =" not in prompt and str(c.method / "handout.md") not in prompt, \
        "the template is rendered into the frame, not handed as an input"


def test_the_answers_paragraph_is_only_for_jobs_writing_answers(tmp_path, monkeypatch):
    c = templated_run(tmp_path, monkeypatch)
    c.through_brief()
    assert "Answer every blocker" not in section(c, "other")
    assert "Validate it at other." in section(c, "other")


def test_an_unknown_placeholder_fails_the_plan_at_start(tmp_path, monkeypatch):
    with pytest.raises(PlanError, match=r"job brief has no value for \{reviewer\}"):
        templated_run(tmp_path, monkeypatch, TEMPLATE + "\nAsk {reviewer}.\n")


def test_editing_the_template_hands_out_the_job_again(tmp_path, monkeypatch):
    c = templated_run(tmp_path, monkeypatch)
    c.through_brief()
    assert "brief" not in c.handed()
    (c.method / "handout.md").write_text(TEMPLATE + "\nWrite carefully.\n", encoding="utf-8")
    c.advance()
    assert "brief" in c.handed(), "the template is a pinned input like the instruction"

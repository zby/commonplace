"""A plan-named prompt section fills one part of the engine's prompt frame from its own lines."""

from __future__ import annotations

import pytest
import yaml

from commonplace.artifactrun import PlanError, start_run
from tests.commonplace.artifactrun.support import (
    Coordinator,
    blocking,
    record_calls,
    toy_library,
)

pytestmark = pytest.mark.usefixtures("tmp_library")

SECTION = """---
type: types/text.md
---
You write the {role} member, typed {member-type}, of run {run-id}.
Write it to {output}.

[output-answers]
Answer every blocker of a refusal in {output-answers}.

[refusal]
Repair {refusal}.

Validate it in {artifact}.
"""


def sectioned_run(tmp_path, monkeypatch, section_text: str = SECTION) -> Coordinator:
    declaration, method = toy_library(tmp_path, compact=True)
    (method / "section.md").write_text(section_text, encoding="utf-8")
    data = yaml.safe_load(declaration.read_text())
    data["prompt-section"] = "section.md"
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


def test_the_section_fills_its_slots_from_the_frame_lines(tmp_path, monkeypatch):
    c = sectioned_run(tmp_path, monkeypatch)
    c.through_brief()
    handout = c.handout("report")
    text = section(c, "report")
    member = c.method.parents[1] / "types" / "toy-report.md"
    assert text.startswith(f"You write the report member, typed {member}, of run {c.run_dir.name}.\n"
                           f"Write it to {handout.outputs['report']}.")
    assert f"Answer every blocker of a refusal in {handout.outputs['answers']}." in text
    assert "[output-answers]" not in text and f"Validate it in {c.run_dir / 'artifact'}." in text
    assert "Repair" not in text, "the refusal line reads absent, so its paragraph is dropped"
    prompt = handout.prompt.read_text(encoding="utf-8")
    assert "role = report" in prompt, "the frame prints the role line the section uses"
    assert "prompt-section =" not in prompt and str(c.method / "section.md") not in prompt, \
        "the section is rendered into the frame, not handed as an input"


def test_a_conditioned_paragraph_needs_its_line(tmp_path, monkeypatch):
    c = sectioned_run(tmp_path, monkeypatch)
    c.through_brief()
    assert "Answer every blocker" not in section(c, "other"), "other prints no output-answers line"
    c.complete("report", "report A\n", answers="")
    c.complete("other", "other O1\n")
    c.complete("summary", "summary S1\n")
    c.complete("verification", blocking("report: r1"))
    assert f"Repair {c.handout('report').prompt.parent / 'inputs' / 'refusal.md'}." in section(c, "report")


def test_an_unknown_placeholder_fails_the_plan_at_start(tmp_path, monkeypatch):
    with pytest.raises(PlanError, match="job brief binds no variable reviewer"):
        sectioned_run(tmp_path, monkeypatch, SECTION + "\nAsk {reviewer}.\n")


def test_run_parameters_reach_the_section_only_as_plan_parameter_lines(tmp_path, monkeypatch):
    with pytest.raises(PlanError, match="job brief binds no variable param:subject"):
        sectioned_run(tmp_path, monkeypatch, SECTION + "\nAbout {param:subject}.\n")


def test_editing_the_section_hands_out_the_job_again(tmp_path, monkeypatch):
    c = sectioned_run(tmp_path, monkeypatch)
    c.through_brief()
    assert "brief" not in c.handed()
    (c.method / "section.md").write_text(SECTION + "\nWrite carefully.\n", encoding="utf-8")
    c.advance()
    assert "brief" in c.handed(), "the section is a pinned input like the instruction"


def test_workers_read_the_types_of_what_they_write_and_read_but_not_the_set_type(tmp_path, monkeypatch):
    c = sectioned_run(tmp_path, monkeypatch)
    types = c.method.parents[1] / "types"
    c.through_brief()
    prompt = c.handout("other").prompt.read_text(encoding="utf-8")
    values = dict(line.split(" = ", 1) for line in prompt.splitlines() if " = " in line)
    assert values["member-type"] == str(types / "toy-member.md")
    assert values["brief-type"] == str(types / "toy-member.md"), "the type of each member it reads"
    assert "set-type" not in values and str(types / "toy-set.md") not in prompt

def test_a_condition_no_job_prints_fails_the_plan_at_start(tmp_path, monkeypatch):
    with pytest.raises(PlanError, match="binds no variable refusla"):
        sectioned_run(tmp_path, monkeypatch, SECTION + "\n[refusla]\nTypo.\n")


def test_the_frame_prints_the_layout_facts_of_the_role(tmp_path, monkeypatch):
    c = sectioned_run(tmp_path, monkeypatch, SECTION + "\nRepeat {identity}; cite in {cites}.\n\n[verifies]\nYou verify {verifies}.\n")
    c.through_brief()
    assert "Repeat none; cite in brief." in section(c, "report")
    assert "Repeat report: claim; cite in brief, report." in section(c, "other")
    assert "You verify" not in section(c, "other"), "only a verifying role prints verifies"
    c.complete("report", "report A\n", answers="")
    c.complete("other", "other O1\n")
    c.complete("summary", "summary S1\n")
    assert "You verify report, other, summary." in section(c, "verification")


def test_run_bound_fields_print_as_the_run_source_in_the_identity_line():
    from commonplace.artifactrun.handouts import layout_bindings
    from commonplace.lib.directory_layout import parse_layout

    layout = parse_layout({"membership": "closed", "roles": {
        "head": {"path": "head.md", "type": "t/head.md", "identity": [{"from": "run", "fields": ["run-id"]}]},
        "body": {"path": "body.md", "type": "t/body.md", "identity": [
            {"from": "run", "fields": ["source-identity"]}, {"from": "head", "fields": ["run-id"]}]},
    }})
    assert layout_bindings(layout, "head")["identity"] == "run: run-id"
    assert layout_bindings(layout, "body")["identity"] == "head: run-id; run: source-identity"

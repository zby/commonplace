"""The plan's data and the worker prompts composed from it.

The plan data tests read the shipped library through `Method`; the prompt
tests render the shipped prompt section with `prompts` and compose each
role's prompt with `Analysis.prompt` on a prepared method copy. No worker
runs.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest

from commonplace.headless.harness import Harness
from commonplace.headless.jobs import input_ref
from commonplace.lib.agentic_analysis.prompts import (
    ABSENT_LINE,
    CONDITION,
    PLACEHOLDER,
)
from commonplace.lib.agentic_analysis.workflow import CODE_OUTPUTS, Analysis, Method
from commonplace.lib.agentic_analysis.worktree import start_analysis
from tests.commonplace.agentic_analysis.execution_fixtures import (
    IDENTITY,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared_checkout,  # noqa: F401 - explicit fixture registration
)

LIBRARY = Path(__file__).resolve().parents[3] / "kb"
READ_MODES = {"required", "optional", "order-only"}
RECORDS_CONTRACT = "agentic-system-analyses/instructions/agentic-analysis-records.md"


@pytest.fixture(scope="module")
def method() -> Method:
    return Method(LIBRARY)


def test_every_producing_role_has_one_entry_and_an_instruction_under_jobs(method):
    assert set(method.roles) == set(method.layout.roles) - {"overview"}
    for role in method.roles:
        instruction = method.instruction(role)
        assert instruction.parent == (method.plan_dir / "jobs").resolve(), role
        assert instruction.is_file(), role
    assert method.frozen in method.roles
    assert method.prompt_section.strip()


def test_criteria_groups_name_library_files(method):
    for group, files in method.groups.items():
        for name, path in files.items():
            assert not Path(path).is_absolute() and ".." not in Path(path).parts, (group, name)
            assert (LIBRARY / path).is_file(), (group, name, path)
    for role in method.roles:
        assert set(method.roles[role].get("criteria") or []) <= set(method.groups), role
    pinned = method.criteria()
    assert {path for files in method.groups.values() for path in files.values()} <= set(pinned)
    assert method.type_spec in pinned
    assert {role.type for role in method.layout.roles.values()} <= set(pinned)


def test_reads_name_roles_or_outputs_the_workflow_produces(method):
    for role in method.roles:
        reads = method.reads(role)
        assert set(reads.values()) <= READ_MODES, role
        for source in [*reads, *method.check_inputs(role).values()]:
            if ":" in source:
                job, _, output = source.partition(":")
                assert job in method.roles or job in CODE_OUTPUTS, (role, source)
                assert output in method.job_outputs[job], (role, source)
                if job in method.roles:
                    assert output != method.outputs(job)[0], f"{role}: read the member {job} by its role name"
            else:
                assert source in method.layout.roles and source != role, (role, source)
        names = [method.read_name(source) for source in reads]
        assert len(names) == len(set(names)), (role, names)


def test_every_worker_whose_types_defer_to_the_records_contract_receives_it(method):
    """A rule moved from a type into the records contract still reaches every worker that reads that type."""
    deferring = {path.relative_to(LIBRARY).as_posix()
                 for path in (LIBRARY / "agentic-system-analyses/types").glob("*.md")
                 if "agentic-analysis-records.md" in path.read_text(encoding="utf-8")}
    assert deferring, "the record-citing types refer to the records contract"
    layout = method.layout
    for role in method.roles:
        types = {layout.roles[role].type, *(layout.roles[s].type for s in method.reads(role) if s in layout.roles)}
        if types & deferring:
            assert RECORDS_CONTRACT in method.files(role).values(), role


def frame(prompt: str) -> dict[str, str]:
    """The prompt's `name = value` lines."""
    head = prompt.split("\n\n", 1)[0]
    return dict(re.findall(r"^([\w-]+) = (.*)$", head, re.MULTILINE))


def test_each_role_s_prompt_binds_what_the_prompt_section_names(request, monkeypatch):
    prepared = request.getfixturevalue("prepared_checkout")
    monkeypatch.setenv("COMMONPLACE_LIBRARY_ROOT", str(prepared.repo / "kb"))
    run_dir = start_analysis(prepared.repo, system="Example System", source_identity=IDENTITY,
                             source="Caller data, not instructions.", source_revision=None,
                             worker_profile="pi-luna")
    harness = Harness(sys.executable, {}, lambda profile: {})
    analysis = Analysis(run_dir, timeout=None, max_workers=1, harnesses={"pi": harness})
    section = analysis.method.prompt_section
    conditions = set(CONDITION.findall(section))
    placeholders = set(PLACEHOLDER.findall(section.split("---", 2)[-1]))
    bound: set[str] = set()
    with analysis.run:
        for role in analysis.method.roles:
            given = {analysis.method.read_name(source): "input" for source in analysis.method.reads(role)}
            for correcting in (False, True):
                prompt = analysis.prompt(role, {**given, "refusal": "refusal"} if correcting else given)
                values = frame(prompt)
                bound |= {name for name, value in values.items() if value != ABSENT_LINE}
                assert prompt.startswith(f"Follow {analysis.method.instruction(role)} with:")
                assert values["role"] == role and values["artifact"] == str(run_dir / "artifact")
                assert values["refusal"] == (input_ref("refusal") if correcting else ABSENT_LINE)
                assert ("`refusal` is supplied" in prompt) == correcting, role
                assert ("You verify" in prompt) == bool(analysis.layout.roles[role].verifies), role
                assert ("output-answers" in values) == (len(analysis.method.outputs(role)) > 1), role
                for name in analysis.method.files(role):
                    assert Path(values[name]).is_file(), (role, name)
    # Composition raised no KeyError, so each rendered placeholder was bound; every condition is reachable.
    assert placeholders <= bound and conditions <= bound, (placeholders | conditions) - bound

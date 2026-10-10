from __future__ import annotations

from pathlib import Path

import yaml

from commonplace.artifactrun import ModelJob, load_plan
from commonplace.lib.agentic_analysis.plan import PLAN
from commonplace.lib.agentic_analysis.worktree import STATE_ROOT
from tests.commonplace.agentic_analysis.fixtures import expanded

REPO_ROOT = Path(__file__).resolve().parents[3]
LIBRARY = REPO_ROOT / "kb"


def test_collection_method_inputs_cover_discovered_contracts_and_exclude_outputs() -> None:
    jobs = load_plan(yaml.safe_dump(expanded(LIBRARY)))
    declared = {
        LIBRARY / spec.source
        for job in jobs.jobs
        for spec in job.inputs.values()
        if spec.address == "file"
    }
    collection = LIBRARY / "agentic-system-analyses"
    contracts = {collection / "COLLECTION.md"}
    # The artifact type is fixed for the run rather than declared.
    contracts.update(
        path for path in (collection / "types").iterdir()
        if path != LIBRARY / jobs.type_spec
    )
    assert LIBRARY / jobs.type_spec not in declared
    contracts.update((collection / "instructions").glob("agentic-analysis-*.md"))
    workers = (LIBRARY / PLAN).parent / "jobs-engine"
    contracts.update(workers.glob("*.md"))
    assert contracts <= declared
    assert all(path.is_file() for path in declared)
    for job in jobs.jobs:
        if isinstance(job, ModelJob):
            instruction = LIBRARY / job.inputs[job.instruction].source
            assert instruction.parent == workers
            assert LIBRARY / job.inputs["worker-rules"].source == workers / "follow-worker-rules.md"
    for area in ("state", "retained", "retained-archive", "reviews", "comparisons"):
        assert not any(path.is_relative_to(collection / area) for path in declared)
    assert REPO_ROOT / STATE_ROOT == collection / "state"


def test_mission_files_leave_inputs_outputs_and_checks_to_the_prompt_section() -> None:
    """Step 5's criterion: a job instruction names the inputs its mission uses, never
    an output, an answers file or the check command, which the prompt section supplies."""
    workers = (LIBRARY / PLAN).parent / "jobs-engine"
    missions = [path for path in workers.glob("*.md") if path.name not in ("follow-worker-rules.md", "prompt-section.md")]
    assert missions
    for path in missions:
        text = path.read_text(encoding="utf-8")
        for named in ("`output`", "output-answers", "commonplace-validate", "validation-artifact", "Return one line"):
            assert named not in text, (path.name, named)


def test_every_worker_whose_types_defer_to_the_records_contract_receives_it() -> None:
    """The delivery invariant contract consolidation rests on: a rule moved from a
    type into the records contract still reaches every worker that reads that type."""
    jobs = load_plan(yaml.safe_dump(expanded(LIBRARY)))
    contract = "agentic-system-analyses/instructions/agentic-analysis-records.md"
    deferring = {path for path in (LIBRARY / "agentic-system-analyses/types").glob("*.md")
                 if "agentic-analysis-records.md" in path.read_text(encoding="utf-8")}
    assert deferring, "the record-citing types refer to the records contract"
    for job in jobs.jobs:
        if not isinstance(job, ModelJob):
            continue
        types = {LIBRARY / spec.source for name, spec in job.inputs.items()
                 if spec.address == "file" and (name == "member-type" or name.endswith("-type"))}
        if types & deferring:
            assert any(spec.source == contract for spec in job.inputs.values() if spec.address == "file"), job.name

"""Fidelity of the compact analysis plan to the hand-written plan it replaced.

`hand_written_plan.yaml` is the plan as it stood before the switch, frozen
here. The expansion must equal it after the renamings and the intended
differences listed below, each a decision recorded in
kb/reference/proposals/plans-without-structural-wrapper-code.md; any other
difference fails. Handlers are compared by substitution: a consumer wrapper
is replaced by the standard handler plus the entry's declared checks.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from commonplace.artifactrun import CodeJob, Input, ModelJob, load_plan
from commonplace.artifactrun.compact import expand
from commonplace.lib.agentic_analysis.analyses import analysis_layout
from commonplace.lib.agentic_analysis.plan import PLAN, expanded

LIBRARY = Path(__file__).resolve().parents[3] / "kb"
HAND_WRITTEN = Path(__file__).with_name("hand_written_plan.yaml")
PROMPT_SECTION = "agentic-system-analyses/instructions/analyse-agentic-system/jobs-engine/prompt-section.md"
RETIRED = {"agentic-system-analyses/instructions/agentic-analysis-boundary.md",
           "agentic-system-analyses/instructions/agentic-analysis-sources.md"}
"""Contracts whose content moved into types; jobs receive those types instead."""

JOB_RENAMES = {
    "reconcile": "reconciliation", "verify": "report-verification", "profile": "memory-profile",
    "verify-profile": "profile-verification", "synthesize": "synthesis",
    "verify-synthesis": "synthesis-verification",
}
# Input names that follow the one-name-per-concept rule for reads: a role read
# is named after its role, a single-output job's output after the job.
INPUT_RENAMES = {
    "boundary": {"source": "acquire"},
    "profile-verification": {"profile": "memory-profile", "profile-answers": "memory-profile-answers",
                             "profile-refusal": "memory-profile-refusal"},
    "synthesis": {"profile-verified": "memory-profile-verified"},
}
STANDARD = {"check": "commonplace.artifactrun.handlers.check",
            "apply": "commonplace.artifactrun.handlers.apply_verification",
            "report-check": "commonplace.artifactrun.handlers.artifact_check"}


def job_name(name: str) -> str:
    for prefix in ("check-", "apply-"):
        if name.startswith(prefix) and name.removeprefix(prefix) in JOB_RENAMES:
            return prefix + JOB_RENAMES[name.removeprefix(prefix)]
    return JOB_RENAMES.get(name, name)


def renamed(spec: Input) -> Input:
    """An input with the producer jobs it names renamed."""
    if spec.address in ("output", "attempt", "refusal"):
        producer, colon, output = spec.source.partition(":")
        return Input(spec.address, job_name(producer) + colon + output, spec.required,
                     spec.relation, spec.outcome, spec.order_only)
    return spec


@pytest.fixture(scope="module")
def plans():
    old = load_plan(HAND_WRITTEN.read_text(encoding="utf-8"))
    new = load_plan(yaml.safe_dump(expanded(LIBRARY)))
    return old, new


def expected_inputs(old_job, new, layout) -> dict[str, Input]:
    """The hand-written job's non-file inputs, renamed and with the intended differences applied."""
    name = job_name(old_job.name)
    renames = INPUT_RENAMES.get(name, {})
    inputs = {renames.get(key, key): renamed(spec) for key, spec in old_job.inputs.items() if spec.address != "file"}
    if name.startswith("check-") and name != "report-check":
        role = layout.roles[name.removeprefix("check-")]
        identity = {source.role for source in role.identity}
        # A check reads its producer's record order-only: identical reruns are no signal.
        inputs["producer-attempt"] = Input("attempt", role.name, order_only=True)
        for key, spec in list(inputs.items()):
            if spec.address == "role" and spec.source != role.name:
                if spec.source in identity:
                    inputs[key] = Input("role", spec.source)  # Identity sources are required.
                elif spec.source in role.cites:
                    inputs[key] = Input("role", spec.source, required=False)  # Cited roles are optional.
                else:
                    del inputs[key]  # Partners come from the layout, not from the old list.
    elif name.startswith("apply-"):
        # The apply receives every read of its verifier, outputs as well as members.
        verifier = new.job(name.removeprefix("apply-"))
        for key, spec in verifier.inputs.items():
            if spec.address == "output" and key != "opening":
                inputs[f"{key}-handed"] = Input("handed", f"verifier-attempt:{key}", required=spec.required)
        # A handed input follows the verifier's renamed input.
        for old_key, new_key in INPUT_RENAMES.get(verifier.name, {}).items():
            for key, spec in list(inputs.items()):
                if spec.address == "handed" and spec.source == f"verifier-attempt:{old_key}":
                    inputs[key] = Input("handed", f"verifier-attempt:{new_key}", spec.required)
    return inputs


def files(job) -> set[str]:
    return {spec.source for spec in job.inputs.values() if spec.address == "file"}


def test_the_expansion_has_the_hand_written_jobs_renamed(plans):
    old, new = plans
    assert [job_name(job.name) for job in old.jobs] == [job.name for job in new.jobs]


def test_each_job_equals_its_hand_written_form_after_the_intended_differences(plans):
    old, new = plans
    layout = analysis_layout()
    for old_job in old.jobs:
        job = new.job(job_name(old_job.name))
        actual = {key: spec for key, spec in job.inputs.items() if spec.address != "file"}
        assert actual == expected_inputs(old_job, new, layout), job.name
        assert job.outputs == old_job.outputs and job.role == old_job.role, job.name
        if isinstance(job, ModelJob):
            # The frame prints artifact and role, and the run supplies command-path,
            # so the per-job validation parameters are gone.
            expected = {key: value for key, value in old_job.parameters.items()
                        if key not in ("validation-artifact", "validation-role")}
            expected["command-path"] = "{param:command-path}"
            assert (job.parameters, job.max_attempts) == (expected, old_job.max_attempts), job.name
            # Model jobs now receive the prompt section and the type of every member they
            # write or read, derived from the layout instead of listed by hand.
            read = {spec.source for spec in job.inputs.values() if spec.address == "role"}
            derived = {PROMPT_SECTION, *(layout.roles[role].type for role in {job.role, *read})}
            assert files(job) == (files(old_job) - RETIRED) | derived, job.name


def test_handlers_are_substituted_by_standard_ones_and_declared_checks(plans):
    old, new = plans
    for old_job in old.jobs:
        job = new.job(job_name(old_job.name))
        if not isinstance(job, CodeJob):
            continue
        if old_job.handler.startswith(("commonplace.lib.agentic_analysis.opening.open",
                                       "commonplace.lib.agentic_analysis.opening.acquire",
                                       "commonplace.lib.agentic_analysis.publication.")):
            assert job.handler == old_job.handler, job.name  # The analysis's own jobs stay.
            continue
        kind = "report-check" if job.name == "report-check" else job.name.partition("-")[0]
        assert job.handler == STANDARD[kind], job.name
        assert job.options.get("frozen-source") == "boundary", job.name


def compact_entries() -> dict[str, dict]:
    """The compact plan's role entries by role name."""
    data = yaml.safe_load((LIBRARY / PLAN).read_text(encoding="utf-8"))
    return {entry["role"]: entry for entry in data["jobs"] if "role" in entry and "kind" not in entry}


def test_every_derived_job_carries_its_entry_s_declared_checks_and_feedback(plans):
    """The consumer's hooks are wired, not only the standard handler path."""
    _, new = plans
    entries = compact_entries()
    expected_hooks = {role: entry.get("checks") for role, entry in entries.items() if entry.get("checks")}
    assert set(expected_hooks) == {"boundary", "runtime", "memory", "epistemic", "report-verification",
                                   "memory-profile"}, "the migrated hooks, one per wrapper that had a check"
    for role, entry in entries.items():
        derived = "apply-" if new.job(role).role in {"report-verification", "profile-verification",
                                                      "synthesis-verification"} else "check-"
        job = new.job(derived + role)
        assert job.options.get("checks") == entry.get("checks"), job.name
        assert job.options.get("feedback") == entry.get("feedback"), job.name
        for check in entry.get("checks") or []:
            if isinstance(check, dict):
                for name in check["inputs"]:
                    assert name in job.inputs, f"{job.name}: declared check input {name} is wired"
    assert new.job("apply-report-verification").options["feedback"].endswith("cited_records")


def test_derived_criteria_include_what_the_hand_written_jobs_pinned(plans):
    old, new = plans
    layout = analysis_layout()
    for old_job in old.jobs:
        if isinstance(old_job, ModelJob):
            continue
        job = new.job(job_name(old_job.name))
        removed = files(old_job) - files(job) - RETIRED
        # Only the type closure of partners the layout no longer gives the check.
        partners = {spec.source for spec in old_job.inputs.values() if spec.address == "role"}
        kept = {spec.source for spec in job.inputs.values() if spec.address == "role"}
        dropped_types = {layout.roles[role].type for role in partners - kept}
        dropped = dropped_types | {path.removesuffix(".md") + ".schema.yaml" for path in dropped_types}
        assert removed <= dropped, (job.name, removed)


def test_verdict_gates_keep_their_verifies_relations(plans):
    old, new = plans
    for old_job in old.jobs:
        gates = {(spec.source, spec.relation) for spec in old_job.inputs.values() if spec.address == "judgment"}
        derived = {(spec.source, spec.relation) for spec in new.job(job_name(old_job.name)).inputs.values()
                   if spec.address == "judgment"}
        assert gates == derived, old_job.name
        assert all(relation.split(":")[1] == "verifies" for _, relation in derived)


def test_one_edit_to_a_compact_entry_changes_the_expansion():
    path = LIBRARY / PLAN
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    memory = next(entry for entry in data["jobs"] if entry.get("role") == "memory")
    memory["reads"]["runtime"] = "required"
    synthesis = next(entry for entry in data["jobs"] if entry.get("role") == "synthesis")
    synthesis["verified-by"] = ["report-verification"]
    plan = load_plan(yaml.safe_dump(expand(data, library=LIBRARY, plan_dir=path.parent)))
    assert plan.job("memory").inputs["runtime"] == Input("role", "runtime")
    assert "memory-profile-verified" not in plan.job("synthesis").inputs
    assert "runtime-verified" in plan.job("synthesis").inputs

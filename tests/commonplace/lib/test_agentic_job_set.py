"""Premerge contracts for the opt-in analysis migration skeleton.

Use the real shipped layout and instructions. No workers, network, source
acquisition, publication or production command switches are involved.
"""

from pathlib import Path

import pytest

from commonplace.lib.agentic_job_set import (
    HANDLER,
    MODEL_ROLES,
    RECORDS,
    REPORTS,
    contract_gaps,
    declaration,
    unported,
)
from commonplace.lib.agentic_set import SET_TYPE
from commonplace.lib.directory_layout import parse_layout
from commonplace.lib.note_parser import parse_document
from commonplace.workflow import CodeJob, ModelJob, advance, load_job_set, start_run

ROOT = Path(__file__).resolve().parents[3]
LIBRARY = ROOT / "kb"


@pytest.fixture
def graph(tmp_path):
    document, error = parse_document((LIBRARY / SET_TYPE).read_text(encoding="utf-8"))
    assert document is not None and not error
    layout = parse_layout(document.frontmatter["layout"])
    return load_job_set(declaration(LIBRARY, tmp_path / "run"), layout.roles), layout


def test_graph_covers_real_roles_once(graph):
    jobs, layout = graph
    assert jobs.type_spec == Path(SET_TYPE)
    assert {job.role for job in jobs.jobs if job.role} == set(layout.roles)
    models = [job for job in jobs.jobs if isinstance(job, ModelJob)]
    assert {job.name: job.role for job in models} == MODEL_ROLES
    assert len(jobs.jobs) == 24
    for job in models:
        refusal = job.inputs["refusal"]
        assert (refusal.address, refusal.source, refusal.required) == ("refusal", job.name, False)
        assert job.bound == (2 if job.name in ("boundary", "synthesize", "verify-synthesis") else 3)


def test_declared_method_inputs_exist_and_are_absolute(graph):
    jobs, _ = graph
    for job in jobs.jobs:
        for name, spec in job.inputs.items():
            if spec.address != "file" or (job.name, name) in (("open", "request"), ("publish", "manifest")):
                continue
            path = Path(spec.source)
            assert path.is_absolute() and path.is_file(), (job.name, name, path)
        if isinstance(job, ModelJob):
            assert {"instruction", "worker-rules", "collection", "member-type", "set-type",
                    "sources-contract", "records-contract", "boundary-contract"} <= set(job.inputs)


def test_verifiers_receive_the_contracts_they_judge(graph):
    jobs, layout = graph
    for name in ("reconcile", "verify"):
        for role in RECORDS:
            assert jobs.job(name).inputs[f"{role}-type"].source == str(LIBRARY / layout.roles[role].type)
    assert "memory-profile-type" in jobs.job("verify-profile").inputs
    assert "synthesis-type" in jobs.job("verify-synthesis").inputs
    assert jobs.job("verify-profile").inputs["profile"].source == "memory-profile"


def test_assembly_and_publication_track_both_ends_of_coverage(graph):
    jobs, layout = graph
    for name in ("assemble", "publish"):
        job = jobs.job(name)
        assert job.inputs["metadata"].source == "open:metadata"
        for origin, role in layout.roles.items():
            if name == "assemble" and origin == "overview":
                continue
            relations = [("cites", partner) for partner in role.cites]
            relations += [("identity", source.role) for source in role.identity]
            for kind, partner in relations:
                if origin == partner:
                    continue
                for subject in (origin, partner):
                    spec = job.inputs[f"coverage-{origin}-{kind}-{partner}-{subject}"]
                    assert (spec.address, spec.source, spec.required, spec.outcome) == (
                        "judgment", subject, False, "accepted",
                    )
                    assert spec.relation == f"{origin}:{kind}:{partner}"
    assert jobs.job("publish").inputs["manifest"].address == "file"


def test_checks_pin_answered_refusal_and_declared_partners(graph):
    jobs, layout = graph
    for name, role in MODEL_ROLES.items():
        if name.startswith("verify"):
            continue
        check = jobs.job(f"check-{name}")
        assert check.inputs["producer-attempt"].source == name
        answered = check.inputs["answered-refusal"]
        assert (answered.address, answered.source, answered.required) == (
            "handed", "producer-attempt:refusal", False,
        )
        partners = {source.role for source in layout.roles[role].identity} | set(layout.roles[role].cites)
        assert partners - {role} <= {spec.source for spec in check.inputs.values() if spec.address == "member"}
    for name in REPORTS:
        assert jobs.job(f"check-{name}").inputs["answers"].source == f"{name}:answers"


def test_apply_jobs_judge_handed_members_not_current_slots(graph):
    jobs, _ = graph
    for name in ("verify", "verify-profile", "verify-synthesis"):
        verifier = jobs.job(name)
        apply = jobs.job(f"apply-{name}")
        assert apply.inputs["verifier-attempt"].source == name
        assert not any(spec.address == "member" for spec in apply.inputs.values())
        expected = {f"verifier-attempt:{key}" for key, spec in verifier.inputs.items() if spec.address == "member"}
        assert {spec.source for spec in apply.inputs.values() if spec.address == "handed"} == expected


def test_profile_and_synthesis_have_explicit_verdict_gates(graph):
    jobs, _ = graph
    for name in ("profile", "synthesize"):
        gates = {spec.source: spec for spec in jobs.job(name).inputs.values() if spec.address == "judgment"}
        assert set(RECORDS) <= set(gates)
        for role in RECORDS:
            assert gates[role].required and gates[role].outcome == "accepted"
            assert gates[role].relation == f"record-verification:cites:{role}"
    profile = jobs.job("synthesize").inputs["profile-verified"]
    assert profile.relation == "profile-verification:cites:memory-profile"
    # Runtime is deliberately not a currency input of the other analysts.
    for name in ("memory", "epistemic"):
        assert not any(spec.address == "member" and spec.source == "runtime"
                       for spec in jobs.job(name).inputs.values())


def test_live_contract_gaps_are_explicit():
    gaps = contract_gaps(LIBRARY)
    assert not any(gap.startswith("missing verdict relation:") for gap in gaps)
    assert not any(gap.startswith("disposition:") for gap in gaps)
    assert any(gap.startswith("working set path:") for gap in gaps)
    assert any(gap.startswith("publication:") for gap in gaps)


def test_skeleton_stops_before_workers_or_external_effects(tmp_path, monkeypatch):
    monkeypatch.setenv("COMMONPLACE_LIBRARY_ROOT", str(LIBRARY))
    run_dir = tmp_path / "run"
    path = tmp_path / "jobs.yaml"
    path.write_text(declaration(LIBRARY, run_dir), encoding="utf-8")
    jobs = load_job_set(path.read_text(encoding="utf-8"))
    for job in jobs.jobs:
        if isinstance(job, CodeJob):
            assert job.handler == HANDLER
            assert job.resolve_handler() is unported
    with pytest.raises(NotImplementedError, match="handlers are not ported"):
        unported(object())
    start_run(run_dir, path, parameters={"system": "fixture"})
    status = advance(run_dir)
    assert not status.handouts and not status.open_attempts and not status.publishable
    assert len(status.stops) == 1
    assert status.stops[0].job == "open"
    assert "handlers are not ported" in status.stops[0].reason
    assert not (tmp_path / "related-systems").exists()
    assert not (tmp_path / "retained").exists()

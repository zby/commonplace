"""Contracts for the opt-in, fail-closed analysis YAML declaration.

Use the real shipped layout and instructions. No workers, network, source
acquisition, publication or production command switches are involved.
"""

from pathlib import Path

import pytest
import yaml

from commonplace.lib.agentic_job_set import (
    HANDLER,
    JOB_SET,
    MODEL_ROLES,
    RECORDS,
    REPORTS,
    contract_gaps,
    unported,
)
from commonplace.lib.agentic_set import SET_TYPE
from commonplace.lib.directory_layout import parse_layout
from commonplace.lib.note_parser import parse_document
from commonplace.workflow import CodeJob, ModelJob, advance, load_job_set, start_run
from commonplace.workflow.state import ABSENT, Resolved, Run
from commonplace.workflow.store import RunStore

ROOT = Path(__file__).resolve().parents[3]
LIBRARY = ROOT / "kb"
DECLARATION = LIBRARY / JOB_SET


@pytest.fixture
def graph():
    document, error = parse_document((LIBRARY / SET_TYPE).read_text(encoding="utf-8"))
    assert document is not None and not error
    layout = parse_layout(document.frontmatter["layout"])
    return load_job_set(DECLARATION.read_text(encoding="utf-8"), layout.roles), layout


def test_graph_covers_real_roles_once(graph):
    jobs, layout = graph
    assert jobs.type_spec == Path(SET_TYPE)
    assert {job.role for job in jobs.jobs if job.role} == set(layout.roles)
    models = [job for job in jobs.jobs if isinstance(job, ModelJob)]
    assert {job.name: job.role for job in models} == MODEL_ROLES
    assert len(jobs.jobs) == 25
    for job in models:
        refusal = job.inputs["refusal"]
        assert (refusal.address, refusal.source, refusal.required) == ("refusal", job.name, False)
        assert job.bound == (2 if job.name in ("boundary", "synthesize", "verify-synthesis") else 3)


def test_declared_file_inputs_are_portable_library_paths(graph):
    jobs, _ = graph
    assert jobs.job("open").inputs == {}
    assert jobs.job("publish").inputs["manifest"].address == "output"
    for job in jobs.jobs:
        for name, spec in job.inputs.items():
            if spec.address != "file":
                continue
            path = Path(spec.source)
            assert not path.is_absolute() and ".." not in path.parts, (job.name, name, path)
            assert (LIBRARY / path).is_file(), (job.name, name, path)
        if isinstance(job, ModelJob):
            assert {"instruction", "worker-rules", "collection", "sources-contract"} <= set(job.inputs)
            assert "set-type" not in job.inputs and "member-type" not in job.inputs
            assert not any(spec.source.endswith(".schema.yaml") for spec in job.inputs.values())


def test_verifiers_receive_the_contracts_they_judge(graph):
    jobs, layout = graph
    for name in ("reconcile", "verify"):
        for role in RECORDS:
            assert jobs.job(name).inputs[f"{role}-contract"].source == layout.roles[role].type
    assert "memory-profile-contract" in jobs.job("verify-profile").inputs
    assert "synthesis-contract" in jobs.job("verify-synthesis").inputs
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
    manifest = jobs.job("publish").inputs["manifest"]
    assert (manifest.address, manifest.source, manifest.required) == ("output", "assemble:manifest", True)
    assert jobs.job("assemble").outputs == ("overview", "manifest")


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
        expected = {f"verifier-attempt:{key}" for key, spec in verifier.inputs.items()
                    if spec.address == "member" or key == "set-check"}
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
    # Runtime must be present initially but its version is not a rerun trigger.
    for name in ("memory", "epistemic"):
        runtime = jobs.job(name).inputs["runtime"]
        assert (runtime.address, runtime.source, runtime.required, runtime.trigger) == (
            "member", "runtime", True, False,
        )


def test_model_contracts_are_selected_for_substantive_work(graph):
    jobs, layout = graph
    role_contracts = {
        "boundary": {"boundary"}, "runtime": {"runtime"}, "memory": {"memory"},
        "epistemic": {"epistemic"}, "reconcile": set(RECORDS),
        "verify": {*RECORDS, "record-verification"}, "profile": {"memory-profile"},
        "verify-profile": {"memory-profile", "profile-verification"},
        "synthesize": {"synthesis"}, "verify-synthesis": {"synthesis", "synthesis-verification"},
    }
    shared = "agentic-system-analyses/instructions/agentic-analysis-"
    for name, roles in role_contracts.items():
        job = jobs.job(name)
        expected = {
            f"agentic-system-analyses/instructions/analyse-agentic-system/jobs/{name}.md",
            "agentic-system-analyses/instructions/analyse-agentic-system/jobs/worker-rules.md",
            "agentic-system-analyses/COLLECTION.md", f"{shared}sources.md",
            *(layout.roles[role].type for role in roles),
        }
        if name != "boundary":
            expected.add(f"{shared}records.md")
        if name in ("boundary", "verify"):
            expected.add(f"{shared}boundary.md")
        assert {spec.source for spec in job.inputs.values() if spec.address == "file"} == expected


def schema_dependencies(path):
    """The local schema-reference closure; never acquire a remote reference."""
    result = {path}
    value = yaml.safe_load(path.read_text(encoding="utf-8"))

    def walk(value):
        if isinstance(value, dict):
            for key, child in value.items():
                if key == "$ref":
                    target = child.partition("#")[0]
                    if target:
                        assert "://" not in target
                        result.update(schema_dependencies((path.parent / target).resolve()))
                else:
                    walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(value)
    return result


def test_code_checks_declare_type_schema_and_shared_criteria(graph):
    jobs, layout = graph
    for job in jobs.jobs:
        if job.name in ("open", "acquire") or isinstance(job, ModelJob):
            continue
        files = {(LIBRARY / spec.source).resolve() for spec in job.inputs.values() if spec.address == "file"}
        assert (LIBRARY / SET_TYPE).resolve() in files
        assert {"sources-contract", "records-contract"} <= set(job.inputs)
        for path in files:
            if path.suffix == ".md":
                document, error = parse_document(path.read_text(encoding="utf-8"))
                assert not error
                schema = document.frontmatter.get("schema")
                if schema:
                    assert schema_dependencies((path.parent / schema).resolve()) <= files, job.name
        # Candidate and partner type documents belong to checks, even when the
        # model needs only some of their substantive content contracts.
        roles = {spec.source for spec in job.inputs.values() if spec.address == "member"}
        if job.name.startswith("check-"):
            roles.add(MODEL_ROLES[job.name.removeprefix("check-")])
        elif job.name.startswith("apply-"):
            verifier = jobs.job(job.name.removeprefix("apply-"))
            roles |= {verifier.role, *(spec.source for spec in verifier.inputs.values() if spec.address == "member")}
        assert {(LIBRARY / layout.roles[role].type).resolve() for role in roles} <= files


def test_round_close_check_is_a_required_pinned_verifier_input(graph):
    jobs, _ = graph
    check = jobs.job("set-check")
    assert check.outputs == ("findings",) and check.role is None
    assert {spec.source for spec in check.inputs.values() if spec.address == "member"} == {"boundary", *RECORDS}
    assert all(spec.required for spec in check.inputs.values())
    spec = jobs.job("verify").inputs["set-check"]
    assert (spec.address, spec.source, spec.required) == ("output", "set-check:findings", True)
    assert [job.name for job in jobs.jobs].index("set-check") < [job.name for job in jobs.jobs].index("verify")
    handed = jobs.job("apply-verify").inputs["set-check-seen"]
    assert (handed.address, handed.source, handed.required) == ("handed", "verifier-attempt:set-check", True)


@pytest.fixture
def engine_run(tmp_path, monkeypatch):
    """Only local metadata: never advance past the fail-closed opening job."""
    monkeypatch.setenv("COMMONPLACE_LIBRARY_ROOT", str(LIBRARY))
    monkeypatch.chdir(tmp_path)
    run_dir = tmp_path / "run"
    start_run(run_dir, DECLARATION, parameters={"system": "fixture"})
    return Run(RunStore(run_dir))


def test_engine_resolves_declaration_files_against_recorded_library(engine_run):
    run = engine_run
    assert run.parameters == {"system": "fixture"}
    assert run.jobs.job("open").inputs == {}
    for job in run.jobs.jobs:
        for spec in job.inputs.values():
            if spec.address == "file":
                assert run.file_path(spec) == LIBRARY / spec.source
                assert run.file_path(spec).is_file()


@pytest.mark.parametrize("name", ("memory", "epistemic"))
def test_presence_only_runtime_orders_initial_work_without_correction_cascade(engine_run, monkeypatch, name):
    run = engine_run
    job = run.jobs.job(name)
    current = {key: Resolved(f"version-{key}") for key in job.inputs}
    current["refusal"] = ABSENT
    current["runtime"] = ABSENT
    monkeypatch.setattr(run, "resolve", lambda key, inputs: current[key])
    assert not run.ready(job, set(MODEL_ROLES.values()))
    current["runtime"] = Resolved("runtime-first")
    assert run.ready(job, set(MODEL_ROLES.values()))
    completed = {"pins": {key: value.pin() for key, value in current.items()}}
    monkeypatch.setattr(run, "latest_completed", lambda job: completed)
    current["runtime"] = Resolved("runtime-corrected")
    assert not run.ready(job, set(MODEL_ROLES.values()))
    current["refusal"] = Resolved("new-verifier-refusal")
    assert run.ready(job, set(MODEL_ROLES.values()))


def test_publication_requires_holding_acceptances_not_every_possible_member(engine_run, monkeypatch):
    run = engine_run
    job = run.jobs.job("publish")
    required_members = {spec.source for spec in job.inputs.values() if spec.address == "member" and spec.required}
    assert required_members == {"boundary", "overview"}
    required_acceptances = {spec.source for spec in job.inputs.values() if spec.address == "judgment" and spec.required}
    assert required_acceptances == {"boundary", "overview"}
    for role in run.layout.roles:
        spec = job.inputs[f"{role}-accepted"]
        assert (spec.address, spec.source, spec.outcome) == ("judgment", role, "accepted")
    # A non-complete disposition needs no later member. A holding acceptance
    # lapsing must still block publish readiness, even though its member stays.
    pins = {key: Resolved(f"version-{key}") if spec.required else ABSENT for key, spec in job.inputs.items()}
    monkeypatch.setattr(run, "resolve", lambda key, inputs: pins[key])
    assert run.ready(job, {"boundary", "overview"})
    pins["overview-accepted"] = ABSENT
    assert not run.ready(job, {"boundary", "overview"})
    assert pins["overview"].version is not None
    # Readiness is not coverage or publication acceptance. The handler must
    # enforce those; until ported it refuses even this synthetically ready job.
    with pytest.raises(NotImplementedError, match="handlers are not ported"):
        job.resolve_handler()(object())


def test_live_contract_gaps_are_explicit():
    gaps = contract_gaps(LIBRARY)
    assert not any(gap.startswith("missing verdict relation:") for gap in gaps)
    assert not any(gap.startswith("disposition:") for gap in gaps)
    assert any(gap.startswith("working set path:") for gap in gaps)
    assert any(gap.startswith("publication:") for gap in gaps)
    assert any(gap.startswith("opening:") for gap in gaps)
    assert any(gap.startswith("legacy runs:") for gap in gaps)
    assert not any(gap.startswith("runtime context:") for gap in gaps)
    assert not any(gap.startswith("check criteria:") for gap in gaps)


def test_skeleton_stops_before_workers_or_external_effects(tmp_path, monkeypatch):
    monkeypatch.setenv("COMMONPLACE_LIBRARY_ROOT", str(LIBRARY))
    run_dir = tmp_path / "run"
    jobs = load_job_set(DECLARATION.read_text(encoding="utf-8"))
    for job in jobs.jobs:
        if isinstance(job, CodeJob):
            assert job.handler == HANDLER
            assert job.resolve_handler() is unported
            with pytest.raises(NotImplementedError, match="handlers are not ported"):
                job.resolve_handler()(object())
    with pytest.raises(NotImplementedError, match="handlers are not ported"):
        unported(object())
    start_run(run_dir, DECLARATION, parameters={"system": "fixture"})
    status = advance(run_dir)
    assert not status.handouts and not status.open_attempts and not status.publishable
    assert len(status.stops) == 1
    assert status.stops[0].job == "open"
    assert "handlers are not ported" in status.stops[0].reason
    assert not (tmp_path / "related-systems").exists()
    assert not (tmp_path / "retained").exists()

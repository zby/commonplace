"""Contracts for the analysis plan's expansion and its bound handlers.

Use the real shipped layout and instructions. No workers, network, source
acquisition, publication or production command switches are involved.
"""

from pathlib import Path

import pytest
import yaml

from commonplace.artifactrun import CodeJob, ModelJob, advance, load_plan, start_run
from commonplace.lib.agentic_analysis.analyses import ANALYSIS_TYPE
from commonplace.lib.agentic_analysis.plan import PLAN, expanded
from commonplace.lib.directory_layout import parse_layout
from commonplace.lib.note_parser import parse_document

REPORTS = ("runtime", "memory", "epistemic")
RECORDS = (*REPORTS, "reconciliation")
VERIFIERS = ("record-verification", "profile-verification", "synthesis-verification")
# A job that fills a role takes the role's name.
MODEL_ROLES = {role: role for role in (
    "boundary", *RECORDS, "memory-profile", "synthesis", *VERIFIERS)}
ROOT = Path(__file__).resolve().parents[3]
LIBRARY = ROOT / "kb"
DECLARATION = LIBRARY / PLAN
ENGINE_INSTRUCTIONS = {
    "boundary": "fix-boundary", "runtime": "trace-runtime", "memory": "analyse-memory",
    "epistemic": "trace-epistemic", "reconciliation": "reconcile-records",
    "record-verification": "verify-records", "memory-profile": "map-memory-profile",
    "profile-verification": "verify-memory-profile", "synthesis": "synthesize-findings",
    "synthesis-verification": "verify-synthesis",
}


@pytest.fixture
def graph():
    document, error = parse_document((LIBRARY / ANALYSIS_TYPE).read_text(encoding="utf-8"))
    assert document is not None and not error
    layout = parse_layout(document.frontmatter["layout"])
    return load_plan(yaml.safe_dump(expanded(LIBRARY)), layout.roles), layout


def test_graph_covers_real_roles_once(graph):
    jobs, layout = graph
    assert {job.role for job in jobs.jobs if job.role} == set(layout.roles)
    models = [job for job in jobs.jobs if isinstance(job, ModelJob)]
    assert {job.name: job.role for job in models} == MODEL_ROLES
    for job in models:
        refusal = job.inputs["refusal"]
        assert (refusal.address, refusal.source, refusal.required) == ("refusal", job.name, False)


def test_declared_file_inputs_are_portable_library_paths(graph):
    jobs, _ = graph
    for name in MODEL_ROLES:
        assert jobs.job(name).inputs["opening"].source == "open:metadata"
    boundary = jobs.job("boundary")
    assert boundary.inputs["instruction"].source.endswith("jobs-engine/fix-boundary.md")
    assert boundary.inputs["worker-rules"].source.endswith("jobs-engine/follow-worker-rules.md")
    incumbent = jobs.job("check-boundary").inputs["incumbent-boundary"]
    assert (incumbent.address, incumbent.source, incumbent.required) == ("role", "boundary", False)
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


def test_assembly_and_publication_are_gated_on_engine_coverage(graph):
    jobs, _ = graph
    for name, scope in (("assemble", "overview"), ("publish", "")):
        job = jobs.job(name)
        assert job.inputs["metadata"].source == "open:metadata"
        coverage = job.inputs["coverage"]
        assert (coverage.address, coverage.source, coverage.required) == ("coverage", scope, True)
        assert not any(spec.address == "judgment" for spec in job.inputs.values())
    manifest = jobs.job("publish").inputs["manifest"]
    assert (manifest.address, manifest.source, manifest.required) == ("output", "assemble:manifest", True)
    assert jobs.job("assemble").outputs == ("overview", "manifest")


def test_checks_pin_answers_answered_refusals_and_declared_partners(graph):
    jobs, layout = graph
    for name, role in MODEL_ROLES.items():
        if name in VERIFIERS:
            continue
        check = jobs.job(f"check-{name}")
        assert check.inputs["producer-attempt"].source == name
        assert check.inputs["producer-attempt"].order_only, "an identical rerun is no signal"
        answered = check.inputs["answered-refusal"]
        assert (answered.address, answered.source, answered.required) == (
            "handed", "producer-attempt:refusal", False,
        )
        # Identity sources are required partners; cited roles are optional ones.
        roles = {spec.source: spec.required for spec in check.inputs.values() if spec.address == "role"}
        for source in layout.roles[role].identity:
            assert roles[source.role] is True, (name, source.role)
        assert set(layout.roles[role].cites) - {role} <= set(roles)
    for name in REPORTS:
        assert jobs.job(f"check-{name}").inputs["answers"].source == f"{name}:answers"
    for producer in ("memory-profile", "synthesis", "profile-verification", "synthesis-verification"):
        assert jobs.job(producer).outputs[-1] == "answers"
        verifies = producer in VERIFIERS
        check = jobs.job(f"apply-{producer}" if verifies else f"check-{producer}")
        answers = check.inputs["answers"]
        assert (answers.address, answers.source, answers.required) == ("output", f"{producer}:answers", False)
        if verifies:
            answered = check.inputs["answered-refusal"]
            assert (answered.address, answered.source, answered.required) == (
                "handed", "verifier-attempt:refusal", False,
            )
    # The carried-limits rule reads both verifications, which the synthesis cites.
    assert {"record-verification", "profile-verification"} <= {
        spec.source for spec in jobs.job("check-synthesis").inputs.values() if spec.address == "role"
    }
    for verifier, subject in (("profile-verification", "memory-profile"), ("synthesis-verification", "synthesis")):
        job = jobs.job(verifier)
        assert job.inputs[f"{subject}-answers"].source == f"{subject}:answers"
        assert job.inputs[f"{subject}-refusal"].source == subject


def test_apply_jobs_judge_handed_members_not_current_slots(graph):
    jobs, _ = graph
    for name in VERIFIERS:
        verifier = jobs.job(name)
        apply = jobs.job(f"apply-{name}")
        assert apply.inputs["verifier-attempt"].source == name
        assert not any(spec.address == "role" for spec in apply.inputs.values())
        # Everything the verifier read as a member or an output, and its refusal.
        expected = {f"verifier-attempt:{key}" for key, spec in verifier.inputs.items()
                    if spec.address in ("role", "output") and key != "opening" or key == "refusal"}
        handed = {spec.source for spec in apply.inputs.values() if spec.address == "handed"}
        assert handed == expected


def test_profile_and_synthesis_have_explicit_verdict_gates(graph):
    jobs, _ = graph
    for name in ("memory-profile", "synthesis"):
        gates = {spec.source: spec for spec in jobs.job(name).inputs.values() if spec.address == "judgment"}
        assert set(RECORDS) <= set(gates)
        for role in RECORDS:
            assert gates[role].required and gates[role].outcome == "accepted"
            assert gates[role].relation == f"record-verification:verifies:{role}"
    profile = jobs.job("synthesis").inputs["memory-profile-verified"]
    assert profile.relation == "profile-verification:verifies:memory-profile"
    # Runtime must be present initially but its version is not a rerun trigger.
    for name in ("memory", "epistemic"):
        runtime = jobs.job(name).inputs["runtime"]
        assert (runtime.address, runtime.source, runtime.required, runtime.order_only) == (
            "role", "runtime", True, True,
        )


def test_model_contracts_are_selected_for_substantive_work(graph):
    jobs, layout = graph
    role_contracts = {
        "boundary": {"boundary"}, "runtime": {"runtime"}, "memory": {"memory"},
        "epistemic": {"epistemic"}, "reconciliation": set(RECORDS),
        "record-verification": {*RECORDS, "record-verification"}, "memory-profile": {"memory-profile"},
        "profile-verification": {"memory-profile", "profile-verification"},
        "synthesis": {"synthesis"}, "synthesis-verification": {"synthesis", "synthesis-verification"},
    }
    shared = "agentic-system-analyses/instructions/agentic-analysis-"
    for name, roles in role_contracts.items():
        job = jobs.job(name)
        expected = {
            f"agentic-system-analyses/instructions/analyse-agentic-system/jobs-engine/{ENGINE_INSTRUCTIONS[name]}.md",
            "agentic-system-analyses/instructions/analyse-agentic-system/jobs-engine/follow-worker-rules.md",
            "agentic-system-analyses/COLLECTION.md", f"{shared}sources.md",
            *(layout.roles[role].type for role in roles),
        }
        if name != "boundary":
            expected.add(f"{shared}records.md")
        if name in ("boundary", "record-verification"):
            expected.add(f"{shared}boundary.md")
        assert {spec.source for spec in job.inputs.values() if spec.address == "file"} == expected
    # Worker instructions name the contracts by these input keys.
    for name in ("reconciliation", "record-verification"):
        for role in RECORDS:
            assert jobs.job(name).inputs[f"{role}-contract"].source == layout.roles[role].type
    assert "memory-profile-contract" in jobs.job("profile-verification").inputs
    assert "synthesis-contract" in jobs.job("synthesis-verification").inputs
    assert jobs.job("profile-verification").inputs["memory-profile"].source == "memory-profile"


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


@pytest.mark.slow
def test_code_checks_declare_type_schema_and_shared_criteria(graph):
    jobs, layout = graph
    for job in jobs.jobs:
        if job.name in ("open", "acquire") or isinstance(job, ModelJob):
            continue
        files = {(LIBRARY / spec.source).resolve() for spec in job.inputs.values() if spec.address == "file"}
        assert (LIBRARY / ANALYSIS_TYPE).resolve() not in files, "the artifact type is fixed for the run"
        assert {"sources-contract", "records-contract"} <= set(job.inputs)
        for path in files:
            if path.suffix == ".md":
                document, error = parse_document(path.read_text(encoding="utf-8"))
                assert not error
                schema = (document.frontmatter or {}).get("schema")
                if schema:
                    assert schema_dependencies((path.parent / schema).resolve()) <= files, job.name
        # Candidate and partner type documents belong to checks, even when the
        # model needs only some of their substantive content contracts.
        roles = {spec.source for spec in job.inputs.values() if spec.address == "role"}
        if job.name.startswith("check-"):
            roles.add(MODEL_ROLES[job.name.removeprefix("check-")])
        elif job.name.startswith("apply-"):
            verifier = jobs.job(job.name.removeprefix("apply-"))
            roles |= {verifier.role, *(spec.source for spec in verifier.inputs.values() if spec.address == "role")}
        assert {(LIBRARY / layout.roles[role].type).resolve() for role in roles} <= files


def test_round_close_check_is_a_required_pinned_verifier_input(graph):
    jobs, _ = graph
    check = jobs.job("record-check")
    assert check.outputs == ("findings",) and check.role is None
    assert {spec.source for spec in check.inputs.values() if spec.address == "role"} == {"boundary", *RECORDS}
    assert all(spec.required for spec in check.inputs.values())
    spec = jobs.job("record-verification").inputs["record-check"]
    assert (spec.address, spec.source, spec.required) == ("output", "record-check:findings", True)
    names = [job.name for job in jobs.jobs]
    assert names.index("record-check") < names.index("record-verification")
    handed = jobs.job("apply-record-verification").inputs["record-check-seen"]
    assert (handed.address, handed.source, handed.required) == ("handed", "verifier-attempt:record-check", True)


@pytest.mark.slow
def test_bound_handlers_and_invalid_opening_fail_closed(tmp_path, monkeypatch):
    monkeypatch.setenv("COMMONPLACE_LIBRARY_ROOT", str(LIBRARY))
    run_dir = tmp_path / "run"
    jobs = load_plan(yaml.safe_dump(expanded(LIBRARY)))
    for job in jobs.jobs:
        if isinstance(job, CodeJob):
            assert job.handler.startswith(("commonplace.lib.agentic_analysis.", "commonplace.artifactrun.handlers."))
            assert callable(job.resolve_handler())
            for check in job.options.get("checks", ()):
                path = check["function"] if isinstance(check, dict) else check
                assert path.startswith("commonplace.lib.agentic_analysis.")
    start_run(run_dir, DECLARATION, parameters={"system": "fixture"})
    status = advance(run_dir)
    assert not status.handouts and not status.open_attempts and not status.publishable
    assert len(status.stops) == 1
    assert status.stops[0].job == "open"
    assert "requires a nonempty source-identity run parameter" in status.stops[0].reason
    assert not (tmp_path / "retained").exists()


def test_publication_declares_producer_provenance_and_full_criterion_closure(graph):
    jobs, layout = graph
    contracts = {
        ANALYSIS_TYPE, "types/type-spec.md", "types/note.md",
        "agentic-system-analyses/COLLECTION.md", "reference/validation-contract.md",
        *(f"agentic-system-analyses/instructions/agentic-analysis-{name}.md"
          for name in ("sources", "records", "boundary")),
        *(role.type for role in layout.roles.values()),
    }
    for name in ("assemble", "publish"):
        job = jobs.job(name)
        source = job.inputs["source"]
        assert (source.address, source.source, source.required) == ("output", "acquire:source", True)
        for producer, role in MODEL_ROLES.items():
            spec = job.inputs[f"{role}-attempt"]
            assert (spec.address, spec.source, spec.required) == ("attempt", producer, role == "boundary")
        files = {(LIBRARY / spec.source).resolve() for spec in job.inputs.values() if spec.address == "file"}
        # The artifact type itself is fixed for the run; its schema closure stays declared.
        assert {(LIBRARY / path).resolve() for path in contracts - {ANALYSIS_TYPE}} <= files
        # Close both the instance schemas and the meta-type used to validate
        # criterion documents, including references in inactive schema branches.
        for path in contracts:
            document, error = parse_document((LIBRARY / path).read_text(encoding="utf-8"))
            assert not error
            if document is None or document.frontmatter is None:
                continue
            schema = document.frontmatter.get("schema")
            if schema:
                assert schema_dependencies((LIBRARY / path).parent / schema) <= files
        assert jobs.job("assemble").outputs == ("overview", "manifest")
        assert jobs.job("publish").outputs == ("receipt",)

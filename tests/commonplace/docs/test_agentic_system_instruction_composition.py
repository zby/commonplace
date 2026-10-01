from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]


def prose(path: Path) -> str:
    """A document's text with whitespace collapsed, so a phrase matches
    wherever the file wraps its lines."""
    return " ".join(path.read_text(encoding="utf-8").split())


def instruction(name: str) -> str:
    collection = "kb/agentic-systems" if name in ("analyse-agentic-system", "synthesize-agent-memory-landscape") else "kb"
    return prose(REPO_ROOT / collection / "instructions" / name / "SKILL.md")


def job(name: str) -> str:
    return prose(
        REPO_ROOT / "kb/agentic-systems/instructions/analyse-agentic-system/jobs" / f"{name}.md"
    )


def test_analysis_failure_is_rerun_instead_of_recovered() -> None:
    orchestrator = instruction("analyse-agentic-system")
    run_state = (
        REPO_ROOT
        / "kb/agentic-systems/types/agentic-system-analysis-run-state.md"
    ).read_text(encoding="utf-8")

    assert "correctable pre-publication failure" in orchestrator
    assert "only when abandoning the run" in orchestrator
    assert "use a new run ID" in orchestrator
    assert "resume a failed run" in run_state


def contract(name: str) -> str:
    return prose(REPO_ROOT / "kb/agentic-systems/types" / f"{name}.md")


def shared_contract(name: str) -> str:
    return prose(REPO_ROOT / "kb/agentic-systems/instructions" / f"agentic-analysis-{name}.md")


def test_set_has_one_fixed_state_location() -> None:
    from commonplace.lib.agentic_workflow import MANIFEST

    overview = contract("agentic-system-analysis-overview")

    assert MANIFEST == "output/ARTIFACT.yaml"
    assert "reading entry point" in overview
    assert "Run state and compact reviews pin `ARTIFACT.yaml`" in overview


def test_repository_sources_are_read_from_the_frozen_checkout() -> None:
    boundary = job("boundary")
    rules = job("worker-rules")

    assert "related-systems/<owner>--<repo>/" in boundary
    assert "git check-ignore -q" in boundary
    assert "verify an existing checkout's origin" in boundary
    assert "compact source allowlist" in boundary
    assert "git checkout --detach <commit>" in boundary
    # The boundary validator guarantees the checkout, so jobs read it directly.
    assert "read and grep the files under `source.path`" in rules
    assert "do not fetch, check out or copy the source elsewhere" in rules
    # Every analytical worker receives the source and record contracts.
    assert "one code span containing the full commit-relative path" in shared_contract(
        "sources"
    )
    assert "searched roots or files" in shared_contract("records")


def test_analysis_uses_sources_and_supplied_execution_evidence() -> None:
    rules = job("worker-rules")
    assert "Do not execute the target, its tests or examples" in rules
    assert "Source-reading, quotation and Commonplace validation commands" in rules
    assert "supplied execution evidence" in job("runtime")
    assert "supplied execution evidence" in job("epistemic")
    runtime = contract("agentic-system-runtime-report")
    assert "Missing execution evidence does" in runtime
    assert "not establish absent behavior" in runtime
    assert "execution-preflight" not in runtime
    assert "Probe evidence" not in runtime


def test_pinned_source_reuses_the_checkout_without_refresh() -> None:
    orchestrator = instruction("analyse-agentic-system")
    boundary = job("boundary")

    assert "--param source-revision=<full 40-hex commit>" in orchestrator
    assert "git -C <checkout> rev-parse HEAD" in orchestrator
    assert "When `source-revision` is supplied" in boundary
    assert "`git rev-parse HEAD` to equal `source-revision`" in boundary
    assert "do not clone, fetch, pull or check out any revision" in boundary
    assert "write `problem`; never substitute another revision or source" in boundary
    assert "When `source-revision` is absent" in boundary


def test_transfer_scan_runs_after_complete_state() -> None:
    orchestrator = instruction("analyse-agentic-system")

    assert "only after the complete run state validates" in orchestrator
    assert "scan-agentic-system-transfer" in orchestrator


def test_candidate_artifact_does_not_establish_a_route_operated() -> None:
    epistemic = contract("agentic-system-epistemic-report")
    dispose = epistemic[epistemic.index("## Assessment limits") : epistemic.index("## Required blocks")]
    dispose = " ".join(dispose.split())

    assert "persisted candidate artifact" in dispose
    assert "no provenance or trace links to" in dispose
    assert "only that a candidate instance is available" in dispose
    assert "does not establish observed operation" in dispose
    assert "not establish which routes produced, checked or accepted it" in dispose
    assert "Per-object lifecycle disposition" not in epistemic
    assert "observed candidate state" not in job("epistemic")


def test_jobs_state_the_set_rules_they_depend_on() -> None:
    assert "epistemic has `EPI-`" in shared_contract("records")
    assert "No job rewrites it afterwards" in job("runtime")
    assert "`## Not reached`" in job("boundary")


def test_method_paths_exist_in_the_repository() -> None:
    from commonplace.lib.agentic_publication import METHOD_PATHS

    assert [path for path in METHOD_PATHS if not (REPO_ROOT / path).exists()] == []


def test_collection_method_inputs_cover_discovered_contracts_and_exclude_outputs() -> None:
    from commonplace.lib.agentic_publication import METHOD_PATHS
    from commonplace.lib.agentic_workflow import JOBS, STATE_ROOT

    declared = [REPO_ROOT / value for value in METHOD_PATHS]

    def pinned(path: Path) -> bool:
        return any(path == item or (item.is_dir() and path.is_relative_to(item)) for item in declared)

    collection = REPO_ROOT / "kb/agentic-systems"
    contracts = [collection / "COLLECTION.md"]
    contracts.extend((collection / "types").iterdir())
    contracts.extend((collection / "instructions").glob("agentic-analysis-*.md"))
    contracts.extend((REPO_ROOT / JOBS).glob("*.md"))
    assert contracts and all(pinned(path) for path in contracts)
    assert all(path.exists() for path in declared)
    for area in ("reports/state", "reports/retained", "reports/retained-archive", "reviews", "comparisons"):
        assert not pinned(collection / area / "example.md")
    assert REPO_ROOT / STATE_ROOT == collection / "reports/state"


def test_relocated_skills_keep_both_runtime_projections() -> None:
    for runtime in (".agents", ".claude"):
        for name in ("analyse-agentic-system", "synthesize-agent-memory-landscape"):
            projection = REPO_ROOT / runtime / "skills" / name
            assert projection.is_symlink()
            assert projection.resolve() == REPO_ROOT / "kb/agentic-systems/instructions" / name

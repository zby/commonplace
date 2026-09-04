from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]


def instruction(name: str) -> str:
    return (REPO_ROOT / "kb" / "instructions" / name / "SKILL.md").read_text(
        encoding="utf-8"
    )


def test_memory_review_publication_closes_the_comparison_handoff() -> None:
    writer = instruction("write-agent-memory-system-review")
    orchestrator = instruction("analyse-agentic-system")

    assert "Close the downstream comparison handoff" in writer
    assert "systems.csv" in writer and "systems-table.md" in writer
    assert "report the pair as stale" in writer
    assert "synthesize-agent-memory-landscape/SKILL.md" in writer
    assert "matrix/table authority or stale disposition" in orchestrator


def test_transfer_scan_follows_stable_result_verification() -> None:
    orchestrator = instruction("analyse-agentic-system")

    verification = orchestrator.index("### 10. Verify and freeze the stable result")
    transfer = orchestrator.index(
        "### 11. Route a selective transfer scan only after stable verification"
    )

    assert verification < transfer
    assert "only after step 10 has frozen and fingerprinted" in orchestrator[transfer:]


def test_response_fingerprint_contract_excludes_its_own_report() -> None:
    orchestrator = instruction("analyse-agentic-system")
    transfer = instruction("scan-agentic-system-transfer")
    contract = (
        REPO_ROOT
        / "kb"
        / "instructions"
        / "analyse-agentic-system"
        / "references"
        / "response-fingerprint.md"
    ).read_text(encoding="utf-8")

    assert "hash only its delimited stable block" in orchestrator
    assert "digest outside that block" in orchestrator
    assert "exact delimited stable response block" in transfer
    assert "Never hash the completed assistant message" in contract
    assert "AAS-STABLE-RESULT START" in contract
    assert "AAS-STABLE-RESULT END" in contract


def test_analysis_skill_uses_one_typed_result_shape_for_every_carrier() -> None:
    orchestrator = instruction("analyse-agentic-system")
    contract = (
        REPO_ROOT / "kb" / "types" / "agentic-system-analysis-result.md"
    ).read_text(encoding="utf-8")

    assert "single authority for the result's frontmatter" in orchestrator
    assert "A response's delimited stable block is the complete typed entry artifact" in orchestrator
    assert "copy those unchanged bytes to a temporary `.md` validation target" in orchestrator
    assert "The type fixes content shape, not lifecycle" in contract
    assert "A response-only result" in contract
    assert "A package has exactly one typed entry artifact" in orchestrator
    assert "wired; observed" in contract
    assert "implemented and observed" in contract


def test_lens_worker_return_matches_the_frozen_packet_before_merge() -> None:
    orchestrator = instruction("analyse-agentic-system")
    topology = orchestrator[
        orchestrator.index("#### Worker topology") : orchestrator.index(
            "### 4. Run and challenge the runtime baseline"
        )
    ]

    packet = topology.index("Freeze the packet before dispatch")
    match = topology.index("Before merging any return")
    artifact = topology.index("If a worker terminates after producing output")

    assert packet < match < artifact
    for field in (
        "run ID",
        "lens",
        "packet identity",
        "reviewed boundary",
        "source-register identity",
        "canonical-register identity",
    ):
        assert field in topology
    assert "apply step 2.4's correction check" in topology
    assert "Do not merge a mismatched return" in topology
    assert "every proposal tag is declared once and unique inside the lens" in topology


def test_epistemic_invocation_returns_a_sparse_canonical_overlay() -> None:
    orchestrator = instruction("analyse-agentic-system")
    epistemic = (
        REPO_ROOT
        / "kb"
        / "instructions"
        / "analyse-external-system-epistemic-architecture.md"
    ).read_text(encoding="utf-8")
    result_contract = (
        REPO_ROOT / "kb" / "types" / "agentic-system-analysis-result.md"
    ).read_text(encoding="utf-8")

    overlay = epistemic.index("## Orchestrated overlay mode")
    output = epistemic.index("## Required output")

    assert overlay < output
    assert "A lens return is a **sparse overlay**" in orchestrator
    assert "it never mints a canonical ID" in epistemic[overlay:output]
    assert "Assign stable IDs in standalone use" in epistemic[output:]
    assert "They do not reproduce the shared inventory under lens-local IDs" in (
        result_contract
    )


def test_dynamic_checks_preflight_before_execution() -> None:
    orchestrator = instruction("analyse-agentic-system")
    runtime = orchestrator[
        orchestrator.index("### 4. Run and challenge the runtime baseline")
        : orchestrator.index("### 5. Scope the two lenses")
    ]

    selected = runtime.index("select a focused test or probe")
    preflight = runtime.index("Before executing each selected test or probe")
    capsule = runtime.index("For every executed test or probe")

    assert selected < preflight < capsule
    assert "execution disposition to `not run`" in runtime
    assert "run-dependent conclusion as `uninspected`" in runtime
    assert "Only a target check that executed" in runtime
    assert "an observed interventional comparison plus design evidence" in orchestrator
    assert "every selected dynamic check has one preflight record" in orchestrator


def test_runtime_baseline_route_closure_contract_matches_run_state_type() -> None:
    orchestrator = instruction("analyse-agentic-system")
    run_state_type = (
        REPO_ROOT
        / "kb"
        / "reports"
        / "types"
        / "agentic-system-analysis-run-state.md"
    ).read_text(encoding="utf-8")
    fields = (
        "route-id",
        "immediate-return",
        "later-read-back",
        "delegated-visibility",
        "selection-predicate",
        "invalidation-or-expiry",
        "activation-or-effect",
        "evidence-and-limits",
    )

    for field in fields:
        assert field in orchestrator
        assert field in run_state_type
    assert "exactly one mapping for every canonical `RTE-*` row" in orchestrator
    assert "rejects duplicate, missing, or unknown routes" in run_state_type


def test_result_type_owns_probe_capsule_shape_not_its_lifecycle() -> None:
    orchestrator = instruction("analyse-agentic-system")
    contract = (
        REPO_ROOT / "kb" / "types" / "agentic-system-analysis-result.md"
    ).read_text(encoding="utf-8")

    capsule = contract.index("**probe evidence capsule**")
    runtime = contract.index("### Runtime account")

    assert capsule < runtime
    for field in (
        "intervention and comparison",
        "fixture or input identity",
        "command, test node, or reusable-script identity",
        "relevant environment",
        "raw output inline",
        "design and confounding limits",
        "exact conclusion supported",
    ):
        assert field in contract[capsule:runtime]
    assert "path plus immutable revision or SHA-256" in contract[capsule:runtime]
    assert "Execution disposition is separate from conclusion status" in contract
    assert "it does not authorize or choose that carrier's lifecycle" in contract
    assert "cannot support an `observed` or `causally supported` conclusion" in contract
    assert "Do not create a workshop, `cache/`, `state/`, or `retained/` artifact" in (
        orchestrator
    )


def test_candidate_artifact_does_not_establish_phase_observation() -> None:
    epistemic = (
        REPO_ROOT
        / "kb"
        / "instructions"
        / "analyse-external-system-epistemic-architecture.md"
    ).read_text(encoding="utf-8")
    example = epistemic[
        epistemic.index("Example: observed-run evidence")
        : epistemic.index("Use this schema:")
    ]

    assert "persisted claim artifact" in example
    assert "does not establish that any particular production phase ran" in example
    assert "architectural status as `implemented`" in example
    assert "observed candidate state" in example
    assert "as `not determinable`, not `phase evidenced` or `accepted`" in example
    assert "candidate-linked evidence of that phase" in example
    assert "neither a candidate artifact nor a candidate-linked trace" in example
    assert "use `no instance observed`" in example


def test_response_only_report_makes_commit_visibility_explicit() -> None:
    orchestrator = instruction("analyse-agentic-system")
    report = orchestrator[
        orchestrator.index("### 12. Save and report")
        : orchestrator.index("## Verify")
    ]

    assert "canonical-result commit visibility: none" in report
    assert "no standalone repository artifact was written" in report
    assert "separately authorized downstream operation captures it" in report
    assert "does not convert the response-only result into a published analysis" in report
    assert "does not grant write, capture, retention, or publication authority" in report
    assert "no standalone canonical result is commit-visible" in orchestrator


def test_repository_sources_use_commit_addressed_related_systems_checkouts() -> None:
    orchestrator = instruction("analyse-agentic-system")
    source_work = orchestrator[
        orchestrator.index("### 2. Freeze sources once")
        : orchestrator.index("### 3. Fix truth conditions")
    ]
    handoff = orchestrator[
        orchestrator.index("### 10. Verify and freeze the stable result")
        : orchestrator.index("### 11. Route a selective transfer scan")
    ]

    assert "related-systems/<owner>--<repo>/" in orchestrator
    assert "git check-ignore -q related-systems" in source_work
    assert "verify that `origin` resolves to the same repository" in source_work
    assert "git --no-replace-objects -C" in source_work
    assert "`git ls-tree`, `git show`, and `git grep`" in source_work
    assert "never reads from the checkout worktree" in source_work
    assert "every cited commit-relative path to resolve" in handoff
    assert "do not require the checkout's current HEAD to equal that commit" in handoff


def test_analysis_lifecycle_is_declared_before_source_work() -> None:
    orchestrator = instruction("analyse-agentic-system")
    opening = orchestrator[
        orchestrator.index("### 1. Open one run and declare the boundary")
        : orchestrator.index("### 2. Freeze sources once")
    ]

    assert "Before source work, name every consumer" in opening
    assert "Use an explicit response only" in opening
    assert "`kb/reports/cache/` is never canonical" in opening
    assert "phase: opened" in opening
    assert "relative to the run directory" in opening
    assert "normalized repository-relative `kb/` paths" in opening
    assert "Spell `validation-target` exactly like `assembled-entry`" in opening
    assert "Never advance its phase until the current phase validates" in opening


def test_unspecified_output_defaults_to_persistent_one_file_state() -> None:
    orchestrator = instruction("analyse-agentic-system")
    opening = orchestrator[
        orchestrator.index("### 1. Open one run and declare the boundary")
        : orchestrator.index("### 2. Freeze sources once")
    ]
    reporting = orchestrator[
        orchestrator.index("### 12. Save and report")
        : orchestrator.index("## Verify")
    ]

    assert "When the caller supplies no output path or lifecycle" in opening
    assert "use `state` as the canonical carrier" in opening
    assert "`one file` as the physical form" in opening
    assert "<run-id>/result.md" in opening
    assert "not satisfied merely by returning the file path" in opening
    assert "do not reproduce the full typed artifact in the response" in reporting
    assert "operator handoff does not authorize deletion" in reporting


def test_runtime_seal_and_packet_issue_are_checked_phase_gates() -> None:
    orchestrator = instruction("analyse-agentic-system")
    runtime = orchestrator[
        orchestrator.index("### 4. Run and challenge the runtime baseline")
        : orchestrator.index("### 6. Run the memory/context lens")
    ]
    topology = orchestrator[
        orchestrator.index("#### Worker topology")
        : orchestrator.index("### 4. Run and challenge the runtime baseline")
    ]

    assert "runtime-baseline.md" in runtime
    assert "phase: runtime-sealed" in runtime
    assert "No lens packet may be materialized or dispatched" in runtime
    assert "phase: lenses-issued" in topology
    assert "runtime-baseline-sha256" in topology
    assert "An invalidated packet cannot remain accepted" in topology


def test_final_validation_receipt_identifies_one_typed_result() -> None:
    orchestrator = instruction("analyse-agentic-system")
    verification = orchestrator[
        orchestrator.index("### 10. Verify and freeze the stable result")
        : orchestrator.index("### 11. Route a selective transfer scan")
    ]

    assert "commonplace-validate --json --output" in verification
    assert "do not redirect, copy, or reconstruct the receipt" in verification
    assert "summary.files_analysed` is `1`" in verification
    assert "type `agentic-system-analysis-result`" in verification
    assert "A zero `text_files` count is not a zero-subject result" in verification
    assert "phase: handoff-ready" in verification

"""Restricted scripted record jobs: local fixture sources, no model or publication."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from commonplace.artifactrun import start_run
from commonplace.artifactrun.run import CodeAttempt, Resolved, Run
from commonplace.artifactrun.store import RunStore, digest
from commonplace.lib.agentic_analysis import verification as handlers
from commonplace.lib.agentic_analysis.plan import PLAN
from tests.commonplace.agentic_analysis.execution_fixtures import (
    PARAMETERS,
    parameters,
    report,
    through_analysts,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    acquisition as local_acquisition,  # noqa: F401 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    candidate as boundary_candidate,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared_checkout,  # noqa: F401 - transitive local fixture
)
from tests.commonplace.artifactrun.support import Coordinator

pytestmark = pytest.mark.slow


@pytest.fixture
def records(request, tmp_path):
    start, _ = request.getfixturevalue("local_acquisition")
    a = start(analysts=True)
    data = yaml.safe_load((a.prepared.repo / "kb" / PLAN).read_text())
    data["jobs"] = data["jobs"][:15]
    declaration = tmp_path / "restricted-record-jobs.yaml"
    declaration.write_text(yaml.safe_dump(data))
    run_dir = a.coordinator.run_dir.with_name(a.coordinator.run_dir.name[:-2] + "02")
    start_run(run_dir, declaration, parameters=PARAMETERS)
    a.coordinator = Coordinator(run_dir, tmp_path, tmp_path / "handlers.log")
    c = a.coordinator
    c.advance()
    c.complete("boundary", boundary_candidate(a))
    through_analysts(a)
    assert c.handed() == {"reconcile"}
    return a


def document(a, kind, body, **changes):
    role_type = "reconciliation-report" if kind == "reconciliation" else "verification"
    fields = {"type": f"agentic-system-analyses/types/agentic-system-{role_type}.md",
              "description": f"Example System {kind} at the frozen local fixture boundary",
              "run-id": a.coordinator.run_dir.name, "reviewed-boundary": a.source()["revision"]}
    if kind == "verification":
        fields["verifies"] = "records"
    fields.update(changes)
    return "---\n" + yaml.safe_dump(fields) + f"---\n\n# Example System {kind}\n\n" + body + "\n"


def reconciliation(a, body="The fixture reports converge independently; SRC-1 fixes the evidence.", **changes):
    return document(a, "reconciliation", "## Reconciliation\n\n" + body, **changes)


def verdict(a, blockers="none", limits="none", **changes):
    return document(a, "verification", "## Verification\n\nChecked the scripted fixture records against SRC-1; no model ran.\n\n"
                    "## Blockers\n\n" + blockers + "\n\n## Limits\n\n" + limits, **changes)


def judgments(a, job):
    return [j for j in RunStore(a.coordinator.run_dir).judgment_records() if j["job"] == job]


def to_verifier(a):
    a.coordinator.complete("reconcile", reconciliation(a))
    assert not a.coordinator.status.stops
    assert a.coordinator.handed() == {"verify"}


def code_attempt(a, name, replacements=None):
    """Pin declared inputs for narrow handler-only tests, never discover files."""
    run = Run(RunStore(a.coordinator.run_dir))
    job = run.jobs.job(name)
    pins = {key: run.resolve(key, job.inputs) for key in job.inputs}
    for key, data in (replacements or {}).items():
        old = pins[key]
        pins[key] = Resolved(digest(data), data, old.role, old.producer)
    return CodeAttempt(run, job, pins)


def test_blocker_free_verdict_covers_only_checked_relations(records):
    a = records
    for name in ("reconcile", "verify"):
        h = a.coordinator.handout(name)
        assert "## Input reading batches" in h.prompt.read_text()
        assert "jobs-engine/" in h.prompt.read_text()
        assert "opening" in parameters(h)
        if name == "reconcile":
            to_verifier(a)
    assert judgments(a, "check-reconcile")[-1]["outcome"] == "accepted"
    p = parameters(a.coordinator.handout("verify"))
    assert Path(p["set-check"]).read_text() == "# Record set check\n\nnone\n"
    a.coordinator.complete("verify", verdict(a))
    applied = judgments(a, "apply-verify")
    assert len(applied) == 5
    assert all(j["outcome"] == "accepted" and not j["overrides"] for j in applied)
    assert {j["subject"]["role"] for j in applied} == {"record-verification", *handlers.RECORDS}
    assert all({"verifier-attempt", "set-check-seen"} <= j["basis"].keys() for j in applied)
    assert not a.coordinator.status.publishable


@pytest.mark.parametrize("body,changes,reason", [
    ("Amendment: RT-OBJ-missing now has a stronger value.", {}, "Amendment"),
    ("Unknown RT-OBJ-missing is used.", {}, "unresolved record"),
    ("SRC-1", {"reviewed-boundary": "b" * 40}, "identity"),
    ("SRC-1", {"run-id": "AAS-2026-10-07-other-0123456789ab-01"}, "run-id"),
])
def test_reconciliation_content_is_not_a_semantic_verdict(records, body, changes, reason):
    a = records
    a.coordinator.complete("reconcile", reconciliation(a, body, **changes))
    j = judgments(a, "check-reconcile")[-1]
    assert j["outcome"] == "refused" and reason in j["findings"]
    assert not (a.coordinator.run_dir / "artifact/reconciliation.md").exists()


@pytest.mark.parametrize("blockers,changes,reason", [
    ("- boundary: change target.", {}, "addressee"),
    ("- runtime:", {}, "finding"),
    ("not a list", {}, "Markdown list"),
    ("none", {"verifies": "profile"}, "verifies"),
    ("none", {"reviewed-boundary": "b" * 40}, "identity"),
])
def test_malformed_verdict_never_judges_records(records, blockers, changes, reason):
    a = records
    to_verifier(a)
    a.coordinator.complete("verify", verdict(a, blockers, **changes))
    applied = judgments(a, "apply-verify")
    assert len(applied) == 1 and applied[0]["outcome"] == "refused"
    assert reason in applied[0]["findings"]
    assert applied[0]["subject"]["role"] == "record-verification"


def test_routes_only_addressed_blockers_and_preserves_continuations(records):
    a = records
    to_verifier(a)
    a.coordinator.complete("verify", verdict(a, "- runtime: reconsider SRC-1.\n  The reader inference is unsupported.\n- reconciliation: clarify the relation."))
    applied = judgments(a, "apply-verify")
    assert [j["subject"]["role"] for j in applied] == ["record-verification", "runtime", "reconciliation"]
    assert {e["relation"] for e in applied[0]["scope"]} == {
        "record-verification:cites:boundary", "record-verification:identity:boundary"}
    p = parameters(a.coordinator.handout("runtime"))
    feedback = Path(p["refusal"]).read_text()
    assert "The reader inference is unsupported." in feedback
    assert "clarify the relation" not in feedback
    assert "## Cited records from other reports" in feedback


def test_declined_answers_rerun_verifier_without_semantic_override(records):
    a = records
    to_verifier(a)
    a.coordinator.complete("verify", verdict(a, "- runtime: reconsider SRC-1."))
    a.coordinator.complete("runtime", report(a, "runtime"), answers="- declined: SRC-1 still supports the bounded finding.\n")
    assert a.coordinator.handed() == {"verify"}, a.coordinator.status
    assert judgments(a, "check-runtime")[-1]["outcome"] == "accepted", "a decline may keep the exact report"
    refused = next(j for j in judgments(a, "apply-verify") if j["outcome"] == "refused")
    assert refused["id"] not in judgments(a, "check-runtime")[-1]["overrides"]
    p = parameters(a.coordinator.handout("verify"))
    assert Path(p["runtime-answers"]).read_text().startswith("- declined:")
    assert Path(p["previous-verification"]).read_text() == verdict(a, "- runtime: reconsider SRC-1.")
    a.coordinator.complete("verify", verdict(a))
    assert judgments(a, "apply-verify")[-4]["outcome"] == "accepted"


def test_set_check_uses_pinned_content_not_projection_or_later_members(records):
    a = records
    to_verifier(a)
    clean = code_attempt(a, "set-check")
    baseline = handlers.set_check(clean)
    (a.coordinator.run_dir / "artifact/runtime.md").write_text("untracked malformed projection")
    (a.coordinator.run_dir / "artifact/synthesis.md").write_text("untracked later member")
    assert handlers.set_check(clean) == baseline
    bad = report(a, "runtime").replace("## Runtime account", "## Wrong section").encode()
    findings = handlers.set_check(code_attempt(a, "set-check", {"runtime": bad}))["findings"].decode()
    assert "Runtime account" in findings
    assert "synthesis" not in findings and "overview" not in findings


def test_handed_set_check_failure_cannot_be_ignored(records):
    a = records
    to_verifier(a)
    a.coordinator.complete("verify", verdict(a))
    attempt = code_attempt(a, "apply-verify", {"set-check-seen": b"# Record set check\n\n- runtime.md: fixture failure\n"})
    handlers.apply_verify(attempt)
    result = attempt.judgments({}, 100, "scripted")
    assert len(result) == 1 and result[0]["outcome"] == "refused"
    assert "structural failures require explicit blockers" in result[0]["findings"]


def test_per_addressee_peer_fragments_are_cut_from_handed_reports(records):
    a = records
    to_verifier(a)
    a.coordinator.complete("verify", verdict(a))
    memory = report(a, "memory").replace(
        "### Operative objects\n\nnone declared in this member\n",
        "### Operative objects\n\n#### MEM-OBJ-store — Fixture store\n\nPinned peer finding at SRC-1.\n",
    ).encode()
    text = verdict(a, "- runtime: reconsider MEM-OBJ-store and SRC-1.\n- epistemic: reconsider SRC-1.").encode()
    attempt = code_attempt(a, "apply-verify", {"candidate": text, "memory-seen": memory})
    handlers.apply_verify(attempt)
    result = attempt.judgments({}, 100, "scripted")
    runtime = next(j for j in result if j["subject"]["role"] == "runtime")
    epistemic = next(j for j in result if j["subject"]["role"] == "epistemic")
    assert "#### MEM-OBJ-store — Fixture store" in runtime["findings"]
    assert "Pinned peer finding at SRC-1." in runtime["findings"]
    assert "MEM-OBJ-store" not in epistemic["findings"]
    assert "## Boundary and evidence" not in runtime["findings"]


def test_reconciliation_structural_repair_preserves_semantic_feedback(records):
    a = records
    to_verifier(a)
    a.coordinator.complete("verify", verdict(a, "- reconciliation: clarify SRC-1 relations."))
    a.coordinator.complete("reconcile", reconciliation(a, "Amendment: RT-OBJ-missing has a new value."))
    refused = judgments(a, "check-reconcile")[-1]
    assert refused["outcome"] == "refused"
    assert "- reconciliation: clarify SRC-1 relations." in refused["findings"]
    p = parameters(a.coordinator.handout("reconcile"))
    assert "- reconciliation: clarify SRC-1 relations." in Path(p["refusal"]).read_text()
    a.coordinator.complete("reconcile", reconciliation(a, "Clarified the fixture relations at SRC-1."))
    repaired = judgments(a, "check-reconcile")[-1]
    assert repaired["outcome"] == "accepted" and not repaired["overrides"]
    assert all(not e["relation"].startswith("record-verification:") for e in repaired["scope"])


def test_source_drift_is_a_set_check_finding(records):
    a = records
    to_verifier(a)
    attempt = code_attempt(a, "set-check")
    (a.checkout / "DIRTY.md").write_text("Local source drift; never execute.\n")
    assert "does not hold exactly" in handlers.set_check(attempt)["findings"].decode()

"""Local scripted profile/synthesis handlers; no models or retained publication.

Real CodeAttempt pins and real content contracts are used against the existing
local-only prepared checkout fixture. No full analytical run is constructed.
"""

from __future__ import annotations

import hashlib
import json

import pytest
import yaml

from commonplace.lib.agentic_analysis import profile as handlers
from commonplace.lib.systems_matrix import AXES
from commonplace.workflow import CodeAttempt, CodeJob, Input
from commonplace.workflow.state import Resolved, Run
from commonplace.workflow.store import RunStore
from tests.commonplace.agentic_analysis.execution_fixtures import (
    acquisition as local_acquisition,  # noqa: F401 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import candidate as boundary
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared_checkout,  # noqa: F401 - transitive local fixture
)
from tests.commonplace.agentic_analysis.execution_fixtures import report


def encoded(fields, body):
    return ("---\n" + yaml.safe_dump(fields, sort_keys=False) + "---\n\n" + body).encode()


def identity(a, kind, **extra):
    return {
        "type": f"agentic-system-analyses/types/{kind}.md",
        "description": "Example System at the frozen local scripted fixture boundary",
        "run-id": a.coordinator.run_dir.name,
        "reviewed-boundary": a.source()["revision"], **extra,
    }


def profile(a, **changes):
    fields = identity(a, "agent-memory-profile", **{
        "source-identity": a.source()["identity"],
        "memory-comparison": {
            "version": 2, "scope": "Local scripted fixture; memory surfaces not inspected.",
            "axes": {name: {"assessment": "uninspected", "units": [], "records": [],
                            "note": "No analytical inspection; no comparison conclusion warranted."}
                     for name in AXES},
        },
    })
    fields.update(changes)
    return encoded(fields, "# Example System memory profile\n\n## Comparison rationale\n\nNo analytical inspection was performed.\n")


def synthesis(a, limitations="none", **changes):
    fields = identity(a, "agentic-system-synthesis", **changes)
    return encoded(fields, "# Example System synthesis\n\n## Bounded synthesis\n\n"
                   "Local scripted fixture at SRC-1; no model analysis or execution evidence.\n\n"
                   f"## Limitations\n\n{limitations}\n")


def verdict(a, stage, blockers="none", limits="none", **changes):
    fields = identity(a, "agentic-system-verification", verifies=stage)
    fields.update(changes)
    return encoded(fields, "# Example System verification\n\n## Verification\n\n"
                   "Scripted fixture only; no analytical verification was performed.\n\n"
                   f"## Blockers\n\n{blockers}\n\n## Limits\n\n{limits}\n")


@pytest.fixture
def opened(request):
    start, _ = request.getfixturevalue("local_acquisition")
    a = start()
    assert not a.advance().stops
    return a


def attempt(a, stage, candidate, *, apply=False, answers=b"", refusal=None, previous=None):
    store = RunStore(a.coordinator.run_dir)
    run = Run(store)
    opening = next(r for r in store.attempt_records() if r["job"] == "open")
    values = {"metadata": (store.get(opening["outputs"]["metadata"]), None),
              "candidate": (candidate, f"{stage}-verification" if apply else
                            "memory-profile" if stage == "profile" else "synthesis"),
              "answers": (answers, None), "answered-refusal": (refusal, None)}
    snapshot = {"boundary": boundary(a).encode(),
                **{role: report(a, role).encode() for role in ("runtime", "memory", "epistemic")},
                "reconciliation": encoded(identity(a, "agentic-system-reconciliation-report"),
                                           "# Fixture reconciliation\n\n## Reconciliation\n\nNo amendments.\n")}
    snapshot["runtime"] = snapshot["runtime"].replace(
        b"### Operative objects\n\nnone declared in this member\n",
        "### Operative objects\n\n#### RT-OBJ-store — Store\n\nSRC-1 fixes the fixture store.\n".encode(),
    )
    if stage == "synthesis":
        snapshot.update({role: verdict(a, kind) for role, kind in
                         (("record-verification", "records"), ("profile-verification", "profile"))})
    if apply:
        snapshot[stage] = profile(a) if stage == "profile" else synthesis(a)
    for role, data in snapshot.items():
        actual = "memory-profile" if role == "profile" else role
        values[role + ("-seen" if apply else "")] = (data, actual)
    output = "verification" if apply else "profile" if stage == "profile" else "synthesis"
    record_name = "verifier-attempt" if apply else "producer-attempt"
    values[record_name] = (json.dumps({
        "state": "completed", "outputs": {output: hashlib.sha256(candidate).hexdigest()},
        "previous_outputs": {} if previous is None else {output: hashlib.sha256(previous).hexdigest()},
    }).encode(), None)
    from commonplace.lib.agentic_analysis.validation import CRITERIA

    for name, path in CRITERIA.items():
        file = run.library / path
        if file.is_file():
            values[name] = (file.read_bytes(), None)
    inputs = {name: Input("member" if role else "output", role or name, required=False)
              for name, (_, role) in values.items()}
    pins = {name: Resolved(hashlib.sha256(data).hexdigest() if data is not None else None, data, role)
            for name, (data, role) in values.items()}
    job = CodeJob("scripted-profile", inputs, (), "unused")
    return CodeAttempt(run, job, pins)


def judgments(attempt):
    return attempt.judgments({}, 100, "scripted")


@pytest.mark.parametrize("stage,handler", [("profile", handlers.check_profile), ("synthesis", handlers.check_synthesize)])
def test_valid_content_is_accepted_with_only_declared_relations(opened, stage, handler):
    a = opened
    data = profile(a) if stage == "profile" else synthesis(a)
    ctx = attempt(a, stage, data)
    assert handler(ctx) == {}
    (judgment,) = judgments(ctx)
    assert judgment["outcome"] == "accepted", judgment["findings"]
    role = "memory-profile" if stage == "profile" else "synthesis"
    assert f"{role}:identity:boundary" in {s["relation"] for s in judgment["scope"]}
    if stage == "profile":
        assert "memory-profile:identity:memory" in {s["relation"] for s in judgment["scope"]}


@pytest.mark.parametrize("stage,handler", [("profile", handlers.apply_verify_profile), ("synthesis", handlers.apply_verify_synthesis)])
@pytest.mark.parametrize("defect", ["identity", "grammar", "wrong-stage", "citation", "utf8"])
def test_invalid_verdict_refuses_only_candidate(opened, stage, handler, defect):
    a = opened
    data = verdict(a, stage)
    if defect == "identity":
        data = verdict(a, stage, **{"reviewed-boundary": "wrong"})
    elif defect == "grammar":
        data = verdict(a, stage, blockers="a prose blocker is invalid")
    elif defect == "wrong-stage":
        data = verdict(a, "records")
    elif defect == "citation":
        data = verdict(a, stage, blockers="- MEM-OBJ-unhanded is unsupported.")
    else:
        data = b"\xff"
    ctx = attempt(a, stage, data, apply=True)
    handler(ctx)
    (judgment,) = judgments(ctx)
    assert judgment["subject"]["role"] == f"{stage}-verification"
    assert judgment["outcome"] == "refused" and not judgment["scope"]
    assert not judgment["overrides"]


@pytest.mark.parametrize("stage,handler", [("profile", handlers.apply_verify_profile), ("synthesis", handlers.apply_verify_synthesis)])
@pytest.mark.parametrize("blockers", ["none", "- RT-OBJ-store: materially unsupported conclusion; a caveat cannot contain it.\n  Continued evidence explanation."])
def test_semantic_verdict_judges_exact_handed_subject_without_covering_blocked_gate(opened, stage, handler, blockers):
    a = opened
    ctx = attempt(a, stage, verdict(a, stage, blockers=blockers), apply=True)
    # Poison the mutable projection. The handler must not read it.
    path = a.coordinator.run_dir / "set" / ("memory-profile.md" if stage == "profile" else "synthesis.md")
    path.write_bytes(b"newer unhanded bytes")
    handler(ctx)
    valid, subject = judgments(ctx)
    assert valid["outcome"] == "accepted"
    relation = f"{stage}-verification:cites:{'memory-profile' if stage == 'profile' else 'synthesis'}"
    assert relation not in {s["relation"] for s in valid["scope"]}
    assert subject["scope"][0]["relation"] == relation
    assert subject["subject"]["version"] == ctx._pins[f"{stage}-seen"].version
    assert subject["outcome"] == ("accepted" if blockers == "none" else "refused")
    if blockers != "none":
        assert "Continued evidence explanation." in subject["findings"]
    assert not valid["overrides"] and not subject["overrides"]


@pytest.mark.parametrize("stage,handler", [("profile", handlers.check_profile), ("synthesis", handlers.check_synthesize)])
def test_correction_answers_use_exact_delivered_baseline(opened, stage, handler):
    a = opened
    data = profile(a) if stage == "profile" else synthesis(a)
    refusal = b"## Blockers\n\n- SRC-1: reconsider the bounded finding.\n"
    ctx = attempt(a, stage, data, refusal=refusal, answers=b"- corrected: fixed it.\n", previous=data)
    handler(ctx)
    assert "identical to its predecessor" in judgments(ctx)[0]["findings"]
    ctx = attempt(a, stage, data, refusal=refusal, answers=b"- declined: SRC-1 still warrants the bounded finding.\n", previous=data)
    handler(ctx)
    assert judgments(ctx)[0]["outcome"] == "accepted"
    assert not judgments(ctx)[0]["overrides"]


def test_structural_synthesis_refusal_preserves_semantic_blockers_and_limits(opened):
    data = synthesis(opened, **{"reviewed-boundary": "wrong"})
    refusal = (b"## Blockers\n\n- RT-OBJ-store: reconsider support.\n\n"
               b"## Limits\n\n- RT-OBJ-store: do not infer complete inventory.\n")
    ctx = attempt(opened, "synthesis", data, refusal=refusal,
                  answers=b"- declined: retained the bounded finding.\n")
    handlers.check_synthesize(ctx)
    (judgment,) = judgments(ctx)
    assert judgment["outcome"] == "refused"
    assert "reconsider support" in judgment["findings"]
    assert "## Limits" in judgment["findings"] and "do not infer complete inventory" in judgment["findings"]


def test_profile_revision_and_source_identity_are_invocation_guards(opened):
    a = opened
    data = profile(a, **{"source-identity": "wrong"})
    fields = yaml.safe_load(data.decode().split("---")[1])
    fields["memory-comparison"].pop("version")
    data = encoded(fields, "# Example System profile\n\n## Comparison rationale\n\nNo evidence added.\n")
    ctx = attempt(a, "profile", data)
    handlers.check_profile(ctx)
    text = judgments(ctx)[0]["findings"]
    assert "version: 2" in text and "source-identity" in text


def test_synthesis_limit_traceability_refuses_subject_not_valid_verdict(opened):
    a = opened
    data = verdict(a, "synthesis", limits="- RT-OBJ-store: missing inspection prevents complete store comparison.")
    ctx = attempt(a, "synthesis", data, apply=True)
    handlers.apply_verify_synthesis(ctx)
    valid, subject = judgments(ctx)
    assert valid["outcome"] == "accepted", valid["findings"]
    assert subject["outcome"] == "refused" and "limit not carried" in subject["findings"]
    assert "## Limits" in subject["findings"]
    # Same exact handed verdict, but a synthesis carrying its ID may pass.
    data = synthesis(a, "Store inspection incomplete | RT-OBJ-store | SRC-1 | complete comparison | inspect store")
    ctx._pins["synthesis-seen"] = Resolved(hashlib.sha256(data).hexdigest(), data, "synthesis")
    ctx._staged.clear()
    handlers.apply_verify_synthesis(ctx)
    assert judgments(ctx)[1]["outcome"] == "accepted"


@pytest.mark.parametrize("stage,handler", [("profile", handlers.apply_verify_profile), ("synthesis", handlers.apply_verify_synthesis)])
def test_invalid_verifier_correction_answers_cannot_accept_any_partner(opened, stage, handler):
    data = verdict(opened, stage)
    ctx = attempt(opened, stage, data, apply=True, previous=data,
                  refusal=b"## Blockers\n\n- Correct the verdict explanation.\n",
                  answers=b"- corrected: fixed the explanation.\n")
    handler(ctx)
    (judgment,) = judgments(ctx)
    assert judgment["outcome"] == "refused" and "identical to its predecessor" in judgment["findings"]


@pytest.mark.parametrize("prior_role", ["record-verification", "profile-verification"])
def test_synthesis_content_check_carries_each_pinned_prior_limit(opened, prior_role):
    a = opened
    ctx = attempt(a, "synthesis", synthesis(a))
    data = verdict(a, "records" if prior_role == "record-verification" else "profile",
                   limits="- RT-OBJ-store: incomplete store inspection prevents complete comparison.")
    ctx._pins[prior_role] = Resolved(hashlib.sha256(data).hexdigest(), data, prior_role)
    handlers.check_synthesize(ctx)
    assert judgments(ctx)[0]["outcome"] == "refused"
    assert "limit not carried" in judgments(ctx)[0]["findings"]


@pytest.mark.parametrize("stage,handler", [("profile", handlers.apply_verify_profile), ("synthesis", handlers.apply_verify_synthesis)])
def test_identical_verdict_bytes_record_different_handed_subject_versions(opened, stage, handler):
    data = verdict(opened, stage)
    first = attempt(opened, stage, data, apply=True)
    handler(first)
    second = attempt(opened, stage, data, apply=True)
    subject = stage + "-seen"
    changed = second.read(subject).replace(b"# Example System", b"# Revised Example System")
    second._pins[subject] = Resolved(hashlib.sha256(changed).hexdigest(), changed,
                                   "memory-profile" if stage == "profile" else "synthesis")
    handler(second)
    assert judgments(first)[0]["subject"]["version"] == judgments(second)[0]["subject"]["version"]
    assert judgments(first)[1]["subject"]["version"] != judgments(second)[1]["subject"]["version"]


def test_source_drift_refuses_acceptance(opened):
    a = opened
    (a.checkout / "README.md").write_text("Dirty frozen source\n")
    ctx = attempt(a, "profile", profile(a))
    handlers.check_profile(ctx)
    assert judgments(ctx)[0]["outcome"] == "refused"
    assert "checkout" in judgments(ctx)[0]["findings"]

"""The profile and synthesis jobs on the standard handlers; no models or retained publication.

Real CodeAttempt pins and real content contracts are used against the existing
local-only prepared checkout fixture. No full analytical run is constructed.
"""

from __future__ import annotations

import hashlib
import json

import pytest
import yaml

from commonplace.artifactrun import CodeAttempt
from commonplace.artifactrun.handlers import apply_verdict, check
from commonplace.artifactrun.run import Resolved, Run
from commonplace.artifactrun.store import RunStore
from commonplace.lib.systems_matrix import AXES
from tests.commonplace.agentic_analysis.execution_fixtures import (
    acquisition as local_acquisition,  # noqa: F401 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import candidate as boundary
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared_checkout,  # noqa: F401 - transitive local fixture
)
from tests.commonplace.agentic_analysis.execution_fixtures import report

pytestmark = pytest.mark.slow


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


def verdict(a, blockers="none", limits="none", **changes):
    fields = identity(a, "agentic-system-verification")
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
    """The derived check or apply job of the expanded plan, pinned to scripted bytes."""
    from commonplace.artifactrun import load_plan
    from commonplace.lib.agentic_analysis.plan import expanded

    run = Run(RunStore(a.coordinator.run_dir))
    run.jobs = load_plan(yaml.safe_dump(expanded(run.library)))  # The fixture ran only the opening.
    subject = "memory-profile" if stage == "profile" else "synthesis"
    role = f"{stage}-verification" if apply else subject
    job = run.jobs.job(("apply-" if apply else "check-") + role)
    snapshot = {"boundary": boundary(a).encode(),
                **{name: report(a, name).encode() for name in ("runtime", "memory", "epistemic")},
                "reconciliation": encoded(identity(a, "agentic-system-reconciliation-report"),
                                           "# Fixture reconciliation\n\n## Reconciliation\n\nNo amendments.\n")}
    snapshot["runtime"] = snapshot["runtime"].replace(
        b"### Operative objects\n\nnone declared in this member\n",
        b"### Operative objects\n\n#### RT-OBJ-store\n\nLabel: Store\n\nSRC-1 fixes the fixture store.\n",
    )
    if stage == "synthesis":
        snapshot.update({name: verdict(a) for name in ("record-verification", "profile-verification")})
    if apply:
        snapshot[subject] = profile(a) if stage == "profile" else synthesis(a)
    output = run.jobs.job(role).outputs[0]
    record = json.dumps({
        "outputs": {output: hashlib.sha256(candidate).hexdigest()},
        "previous_outputs": {} if previous is None else {output: hashlib.sha256(previous).hexdigest()},
    }).encode()
    values = {"candidate": candidate, "answers": answers, "answered-refusal": refusal,
              "verifier-attempt" if apply else "producer-attempt": record,
              **{f"{name}-seen" if apply else name: data for name, data in snapshot.items()}}
    pins = {}
    for name, spec in job.inputs.items():
        data = (run.library / spec.source).read_bytes() if spec.address == "file" else values.get(name)
        version = hashlib.sha256(data).hexdigest() if data is not None else None
        pins[name] = Resolved(version, data, run.jobs.input_role(job, name))
    return CodeAttempt(run, job, pins)


def judgments(attempt):
    return attempt.judgments({}, 100, "scripted")


@pytest.mark.parametrize("stage,handler", [("profile", check), ("synthesis", check)])
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


@pytest.mark.parametrize("stage,handler", [("profile", apply_verdict), ("synthesis", apply_verdict)])
@pytest.mark.parametrize("defect", ["identity", "grammar", "citation", "utf8"])
def test_invalid_verdict_refuses_only_candidate(opened, stage, handler, defect):
    a = opened
    data = verdict(a)
    if defect == "identity":
        data = verdict(a, **{"reviewed-boundary": "wrong"})
    elif defect == "grammar":
        data = verdict(a, blockers="a prose blocker is invalid")
    elif defect == "citation":
        data = verdict(a, blockers="- [MEM-OBJ-unhanded](memory.md#mem-obj-unhanded) is unsupported.")
    else:
        data = b"\xff"
    ctx = attempt(a, stage, data, apply=True)
    handler(ctx)
    (judgment,) = judgments(ctx)
    assert judgment["subject"]["role"] == f"{stage}-verification"
    assert judgment["outcome"] == "refused"
    subject = "memory-profile" if stage == "profile" else "synthesis"
    assert f"{stage}-verification:verifies:{subject}" not in {s["relation"] for s in judgment["scope"]}
    assert not judgment["overrides"]


@pytest.mark.parametrize("stage,handler", [("profile", apply_verdict), ("synthesis", apply_verdict)])
@pytest.mark.parametrize("blockers", ["none", "- RT-OBJ-store: materially unsupported conclusion; a caveat cannot contain it.\n  Continued evidence explanation."])
def test_semantic_verdict_judges_exact_handed_subject_without_covering_blocked_gate(opened, stage, handler, blockers):
    a = opened
    ctx = attempt(a, stage, verdict(a, blockers=blockers), apply=True)
    # Poison the mutable projection. The handler must not read it.
    path = a.coordinator.run_dir / "artifact" / ("memory-profile.md" if stage == "profile" else "synthesis.md")
    path.write_bytes(b"newer unhanded bytes")
    handler(ctx)
    valid, subject = judgments(ctx)
    assert valid["outcome"] == "accepted"
    relation = f"{stage}-verification:verifies:{'memory-profile' if stage == 'profile' else 'synthesis'}"
    assert relation not in {s["relation"] for s in valid["scope"]}
    assert subject["scope"][0]["relation"] == relation
    assert subject["subject"]["version"] == ctx._pins[f"{'memory-profile' if stage == 'profile' else stage}-seen"].version
    assert subject["outcome"] == ("accepted" if blockers == "none" else "refused")
    if blockers != "none":
        assert "Continued evidence explanation." in subject["findings"]
    assert not valid["overrides"] and not subject["overrides"]


@pytest.mark.parametrize("stage,handler,apply", [
    ("profile", check, False), ("synthesis", check, False),
    ("profile", apply_verdict, True), ("synthesis", apply_verdict, True),
])
def test_correction_answers_use_exact_delivered_baseline(opened, stage, handler, apply):
    a = opened
    data = verdict(a) if apply else profile(a) if stage == "profile" else synthesis(a)
    refusal = b"## Blockers\n\n- SRC-1: reconsider the bounded finding.\n"
    ctx = attempt(a, stage, data, apply=apply, refusal=refusal, answers=b"- corrected: fixed it.\n", previous=data)
    handler(ctx)
    corrected = judgments(ctx)
    assert corrected[0]["outcome"] == "refused" and "identical to its predecessor" in corrected[0]["findings"]
    if apply:
        assert len(corrected) == 1, "an invalid verifier correction accepts no partner"
    ctx = attempt(a, stage, data, apply=apply, refusal=refusal,
                  answers=b"- declined: SRC-1 still warrants the bounded finding.\n", previous=data)
    handler(ctx)
    assert judgments(ctx)[0]["outcome"] == "accepted"
    assert not judgments(ctx)[0]["overrides"]


def test_structural_synthesis_refusal_preserves_semantic_blockers_and_limits(opened):
    data = synthesis(opened, **{"reviewed-boundary": "wrong"})
    refusal = (b"## Blockers\n\n- RT-OBJ-store: reconsider support.\n\n"
               b"## Limits\n\n- RT-OBJ-store: do not infer complete inventory.\n")
    ctx = attempt(opened, "synthesis", data, refusal=refusal,
                  answers=b"- declined: retained the bounded finding.\n")
    check(ctx)
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
    check(ctx)
    text = judgments(ctx)[0]["findings"]
    assert "version: 2" in text and "source-identity" in text


def test_synthesis_limit_traceability_refuses_subject_not_valid_verdict(opened):
    a = opened
    data = verdict(a, limits="- [RT-OBJ-store](runtime.md#rt-obj-store): missing inspection prevents complete store comparison.")
    ctx = attempt(a, "synthesis", data, apply=True)
    apply_verdict(ctx)
    valid, subject = judgments(ctx)
    assert valid["outcome"] == "accepted", valid["findings"]
    assert subject["outcome"] == "refused" and "limit not carried" in subject["findings"]
    assert "## Limits" in subject["findings"]
    # Same exact handed verdict, but a synthesis carrying its ID may pass.
    data = synthesis(a, "Store inspection incomplete | [RT-OBJ-store](runtime.md#rt-obj-store) | SRC-1 | complete comparison | inspect store")
    ctx._pins["synthesis-seen"] = Resolved(hashlib.sha256(data).hexdigest(), data, "synthesis")
    ctx._staged.clear()
    apply_verdict(ctx)
    assert judgments(ctx)[1]["outcome"] == "accepted"


@pytest.mark.parametrize("prior_role", ["record-verification", "profile-verification"])
def test_synthesis_content_check_carries_each_pinned_prior_limit(opened, prior_role):
    a = opened
    ctx = attempt(a, "synthesis", synthesis(a))
    data = verdict(a, limits="- [RT-OBJ-store](runtime.md#rt-obj-store): incomplete store inspection prevents complete comparison.")
    ctx._pins[prior_role] = Resolved(hashlib.sha256(data).hexdigest(), data, prior_role)
    check(ctx)
    assert judgments(ctx)[0]["outcome"] == "refused"
    assert "limit not carried" in judgments(ctx)[0]["findings"]


def test_source_drift_refuses_acceptance(opened):
    a = opened
    (a.checkout / "README.md").write_text("Dirty frozen source\n")
    ctx = attempt(a, "profile", profile(a))
    check(ctx)
    assert judgments(ctx)[0]["outcome"] == "refused"
    assert "checkout" in judgments(ctx)[0]["findings"]

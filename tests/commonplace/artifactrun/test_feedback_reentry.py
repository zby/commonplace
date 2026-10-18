"""Feedback delivery through existing transitions, using disposable toy runs only.

These are scheduling regressions, not semantic audits or authorization to mutate
an analysis run. The legacy counter case emulates the older frozen counter; it
does not claim to run an entire historical method.
"""
import pytest

from commonplace.artifactrun import judge
from commonplace.artifactrun.reset import reset_run
from commonplace.artifactrun.run import Run
from commonplace.artifactrun.store import RunStore
from tests.commonplace.artifactrun.support import NO_BLOCKERS, custom_run


@pytest.mark.parametrize("roles", [("report",), ("report", "other"), ("summary",)])
@pytest.mark.parametrize("legacy_counter", [False, True])
def test_verifier_reset_delivers_every_author_refusal(coordinator, monkeypatch, roles, legacy_counter):
    c = coordinator
    c.through_publication()
    if legacy_counter:
        # Older engines count retained attempts, ignoring the new reset floor.
        monkeypatch.setattr(Run, "attempt_count", lambda run, name: sum(
            a["job"] == name for a in run.attempts.values()))
    before = Run(RunStore(c.run_dir))
    versions = {role: before.members()[role] for role in roles}
    reset_run(c.run_dir, "verification")
    assert Run(RunStore(c.run_dir)).latest_completed("verification") is None
    for role in roles:
        judge(c.run_dir, role=role, outcome="refused", version=versions[role],
              findings=f"bounded feedback for {role}")
    c.ran()
    c.advance()
    assert c.handed() == set(roles)
    # In particular, the old verdict cannot reapply and supersede the feedback.
    assert "apply-verification" not in c.ran()
    run = Run(RunStore(c.run_dir))
    for role in roles:
        assert run.refusal_in_force(run.jobs.filler(role)) is not None
        assert f"bounded feedback for {role}" in c.reachable(c.handout(role))
    if roles == ("summary",):
        c.complete("summary", "summary with explicit witness disposition\n")
        c.complete("verification", NO_BLOCKERS)
        c.complete("digest", "digest refreshed from corrected inputs\n")
        assert c.status.publishable and not c.status.stops


@pytest.mark.parametrize("compact", [False, True])
def test_verifier_self_feedback_exposes_ambiguous_scoped_basis(tmp_path, tmp_library, monkeypatch, compact):
    def edit(jobs):
        if not compact:
            # Compact expansion supplies this; the hand-written toy plan does not.
            jobs["verification"]["inputs"]["refusal"] = {
                "address": "refusal", "source": "verification", "required": False}
            jobs["apply-verification"]["inputs"]["answered-refusal"] = {
                "address": "handed", "source": "verifier-attempt:refusal", "required": False}

    c = custom_run(tmp_path, monkeypatch, edit, compact=compact)
    c.through_publication()
    before = Run(RunStore(c.run_dir))
    verifier = before.members()["verification"]
    application = before.latest_completed("apply-verification")
    reset_run(c.run_dir, "digest")
    after = Run(RunStore(c.run_dir))
    assert after.members()["verification"] == verifier
    assert after.latest_completed("apply-verification") == application
    judge(c.run_dir, role="verification", outcome="refused", version=verifier,
          findings="explicitly dispose of the installed-state witness")
    c.ran()
    c.advance()
    assert c.handed() == {"verification"}, "dependent digest must wait"
    assert "apply-verification" not in c.ran()
    assert "installed-state witness" in c.reachable(c.handout("verification"))
    assert Run(RunStore(c.run_dir)).refusal_in_force(before.jobs.filler("verification"))
    # Feedback delivery alone is insufficient. Its old verifier version enters
    # the answered-refusal basis beside the new one: scoped acceptance is
    # ambiguous. Preserve this counterexample instead of releasing that route.
    c.complete("verification", "Witness assessed; no forced positive.\n\n" + NO_BLOCKERS)
    assert "apply-verification" in c.ran()
    assert not c.handed()
    assert "basis holds 2 versions of verification" in c.stop("apply-verification").reason
    assert Run(RunStore(c.run_dir)).latest_completed("apply-verification") == application
    assert not c.status.publishable


def test_legacy_budget_exhaustion_is_not_silently_renewed(coordinator, monkeypatch):
    c = coordinator
    c.through_publication()
    version = Run(RunStore(c.run_dir)).members()["report"]
    reset_run(c.run_dir, "verification")
    # Model a retained author already at the old frozen engine's limit.
    monkeypatch.setattr(Run, "attempt_count", lambda run, name: 3 if name == "report" else sum(
        a["job"] == name for a in run.attempts.values()))
    judge(c.run_dir, role="report", outcome="refused", version=version, findings="repair required")
    c.advance()
    assert not c.handed()
    assert c.stop("report").reason == "max attempts (3) exhausted"
    assert not c.status.publishable

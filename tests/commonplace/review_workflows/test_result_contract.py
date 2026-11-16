"""The new review format, checked without a model or a legacy parser."""

import pytest

from commonplace.lib.review_workflows import result_contract as contract


def metadata():
    return {"description": "One retained assessment of the captured target against its criterion",
            "contract": "verdict", "note": "kb/notes/a.md", "criterion": "kb/test.md",
            "note-sha256": "0" * 64, "criterion-sha256": "1" * 64,
            "target-sha256": "2" * 64, "target-capture": "kb/reports/state/run/target.md",
            "observation": "kb/reports/state/run/observation.json", "contract-sha256": "3" * 64,
            "profile": {}, "model": None, "run": "kb/reports/state/run", "launch": "launch",
            "completed-at": "2026-11-15T10:00:00Z", "raw-output": "kb/reports/state/run/review.md",
            "raw-output-sha256": "4" * 64}


def fragment(outcome="pass", findings=None, **extra):
    return contract.render({"type": contract.TYPE, "findings": findings or [], "outcome": outcome, **extra},
                           "\n# Review\n\n## Summary\n\nAssessed the supplied text.\n")


def complete(tmp_path, text, target="A unique passage.", **kwargs):
    path = tmp_path / "kb/reports/state/review.md"
    from tests.commonplace.review_workflows.result_helpers import evidence
    given = kwargs.get("metadata", metadata())
    given.update({key.replace("_", "-"): value for key, value in evidence(tmp_path, target, text).items()})
    captured = kwargs.get("contracts", contract.capture_contract(tmp_path))
    given["contract-sha256"] = contract.fingerprint(captured)
    return contract.complete(tmp_path, path, text, metadata=given, target=target, contracts=captured)


@pytest.mark.parametrize("text,match", [
    ("## Result: PASS\n", "declare type"),
    (fragment() + "## Result: PASS\n", "footer"),
    (fragment(model="invented"), "controller-owned"),
    (fragment().replace("outcome: pass", "outcome: pass\noutcome: fail"), "duplicate key"),
    (fragment("warn"), "non-empty"),
    (fragment("report"), "schema"),
])
def test_reject_invalid_fragment(tmp_path, text, match):
    with pytest.raises(ValueError, match=match):
        complete(tmp_path, text)


def test_levels_and_exact_anchors(tmp_path):
    finding = {"scope": "passage", "quotes": ["unique passage"], "reason": "Needs support", "level": "info"}
    assert complete(tmp_path, fragment(findings=[finding])).data["findings"] == [finding]
    for quote, target, label in [("paraphrase", "A unique passage.", "absent"),
                                 ("aa", "aa and aa", "ambiguous")]:
        with pytest.raises(ValueError, match=f"finding 1: {label}.*normalized matches"):
            complete(tmp_path, fragment(findings=[dict(finding, quotes=[quote])]), target)
    with pytest.raises(ValueError, match="level"):
        complete(tmp_path, fragment(findings=[{k: v for k, v in finding.items() if k != "level"}]))


def test_anchor_survives_line_wrap_and_quote_marks(tmp_path):
    target = "A sentence that the note\nwraps across \u201ctwo\u201d lines.\n\nAnother paragraph.\n"
    finding = {"scope": "passage", "quotes": ['the note wraps across "two" lines'],
               "reason": "Needs support", "level": "info"}
    assert complete(tmp_path, fragment(findings=[finding]), target).data["findings"] == [finding]


def test_captured_schema_not_process_cache(tmp_path):
    captured = contract.capture_contract()
    complete(tmp_path, fragment(), contracts=captured)
    changed = dict(captured)
    name = "types/review-result.schema.yaml"
    changed[name] = changed[name].replace(b"required: [frontmatter, body, headings]",
                                         b"required: [frontmatter, body, headings, impossible]")
    assert contract.fingerprint(captured) != contract.fingerprint(changed)
    with pytest.raises(ValueError, match="impossible"):
        complete(tmp_path, fragment(), contracts=changed)
    complete(tmp_path, fragment(), contracts=captured)


FRICTION = "kb/instructions/composition-friction-gate.md"
PREMISES = "commonplace:instructions/premise-decomposition-gate.md"
SYNTHESIS = "kb/instructions/compression-bundle/high-impact-simplification-synthesis.md"
CRITIQUE_BODY = ("\n# Critique\n\n## Strongest case against it\nA.\n\n## How the note engages it\nB.\n\n"
                 "## Constructive findings\nNone.\n")
FRICTION_BODY = "\n# Friction\n\n## Filter\n**Filter:** SURVIVES\n\n## Thinnest joints\nA.\n\n## For the human\nB.\n"
PREMISES_BODY = "\n# Premises\n\n**Register:** claim\n\n## Premises and counterexamples\nA.\n\n## For the human\nB.\n"
SYNTHESIS_BODY = "\n# Synthesis\n\n## Opportunities\n\nNone\n"


def report(criterion, body, reasons=(), **extra):
    data = {"type": contract.TYPE, "outcome": "report", **extra,
            "findings": [{"scope": "document", "quotes": [], "reason": reason} for reason in reasons]}
    return contract.render(data, body), {**metadata(), "contract": "report", "criterion": criterion}


@pytest.mark.parametrize("criterion,body,reasons,extra", [
    # Critique keeps attack-outcome and its sections; no other method may borrow them.
    ("kb/instructions/critique-note.md", CRITIQUE_BODY, [], {}),
    ("kb/instructions/critique-note.md", FRICTION_BODY, [], {"attack-outcome": "lands"}),
    (FRICTION, FRICTION_BODY, [], {"attack-outcome": "lands"}),
    (FRICTION, FRICTION_BODY, ["WEAK - unrated"], {}),
    (PREMISES, PREMISES_BODY, ["DOUBTFUL - no routing"], {}),
    (SYNTHESIS, SYNTHESIS_BODY, ["One"] * 4, {}),
    # A report contract needs a report criterion.
    ("kb/test.md", SYNTHESIS_BODY, [], {}),
])
def test_report_shapes_are_enforced_per_criterion(tmp_path, criterion, body, reasons, extra):
    text, given = report(criterion, body, reasons, **extra)
    with pytest.raises(ValueError, match="schema"):
        complete(tmp_path, text, metadata=given)


def test_a_verdict_cannot_name_a_report_criterion(tmp_path):
    with pytest.raises(ValueError, match="schema"):
        complete(tmp_path, fragment(), metadata={**metadata(), "criterion": FRICTION})

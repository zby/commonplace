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


def test_complete_and_saved_validate_identically(tmp_path):
    candidate = complete(tmp_path, fragment())
    assert candidate.data["outcome"] == "pass"
    assert candidate.data["format"] == 2
    assert candidate.body.startswith("\n# Review")
    path = tmp_path / "kb/reports/state/review.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    (path.parent / ".commonplace-validation-ignore").touch()
    path.write_text(candidate.text)
    assert not contract.validate_saved(tmp_path, path, path.read_text()).fails


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


def test_report_is_not_a_verdict(tmp_path):
    text = contract.render({"type": contract.TYPE, "findings": [], "outcome": "report",
                            "attack-outcome": "no surviving attack"},
                           "# Critique\n\n## Strongest case against it\nAn attack.\n\n"
                           "## How the note engages it\nAnswers it.\n\n## Constructive findings\nNone.\n")
    candidate = complete(tmp_path, text, metadata={**metadata(), "contract": "report"})
    assert candidate.data["attack-outcome"] == "no surviving attack"


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

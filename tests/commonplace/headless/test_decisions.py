"""`decide()` on a fake harness; no model is called.

The fake worker writes the `decision` output from the task: the text after
`FIRST:` on a first attempt and after `RETRY:` once the prompt carries a
rejection (`\\n` in it is a newline), or the problem file for `PROBLEM`.
"""

import json
import re
import sys

import pytest

from commonplace.headless.decisions import decide, describe, parse, violations
from commonplace.headless.harness import Harness, Profile
from commonplace.headless.jobs import OutOfAttempts, Run

FAKE = r"""
import json, re, sys
from pathlib import Path
frame = Path(re.search(r"`([^`]+prompt\.txt)`", sys.argv[-1]).group(1)).read_text()
if "PROBLEM" in frame:
    Path(frame.split("problem file:\n")[1].splitlines()[0]).write_text(json.dumps({"kind": "unable", "message": "no"}))
    sys.exit(0)
key = "RETRY:" if "was rejected" in frame else "FIRST:"
text = frame.split(key, 1)[1].split("|", 1)[0].replace("\\n", "\n")
Path(re.search(r"^- decision\.md: (.+)$", frame, re.MULTILINE).group(1)).write_text(text)
"""

SCHEMA = {"disposition": ("keep", "revise"), "determined": bool, "target": (str, type(None))}


@pytest.fixture
def run(tmp_path):
    script = tmp_path / "fake.py"
    script.write_text(FAKE)
    harness = Harness(sys.executable, {"_subcommand": [str(script)]}, lambda profile: {})
    with Run(tmp_path / "run", tmp_path, Profile("fake", "m", "low"), harnesses={"fake": harness},
             sleep=lambda s: None) as run:
        yield run


def rejections(run) -> list:
    events = [json.loads(line) for line in (run.root / "log.jsonl").read_text().splitlines()]
    return [event["problems"] for event in events if event["event"] == "rejected"]


def test_parse_reads_frontmatter_or_a_yaml_file():
    assert parse("---\na: 1\n---\n# Body\n") == {"a": 1}
    assert parse("a: 1\n") == {"a": 1}
    with pytest.raises(ValueError):
        parse("a: [1\n")


def test_violations_name_missing_fields_and_values_outside_the_choices():
    assert violations({"disposition": "keep", "determined": True, "target": None}, SCHEMA) == []
    assert violations({"disposition": "maybe", "determined": "yes"}, SCHEMA) == [
        "`disposition` must be one of keep, revise, not 'maybe'",
        "`determined` must be a bool value, not 'yes'",
        "`target` is missing"]
    assert "- `target`: a str or null value" in describe(SCHEMA)


def test_decide_returns_the_parsed_decision_after_one_corrected_attempt(run):
    prompt = ("Decide. FIRST:---\\ndisposition: maybe\\ndetermined: true\\ntarget: null\\n---\\n|"
              " RETRY:---\\ndisposition: revise\\ndetermined: false\\ntarget: kb/a.md\\n---\\n# Packet\\n|")
    data, answer = decide(run, "packet", prompt, SCHEMA)
    assert data == {"disposition": "revise", "determined": False, "target": "kb/a.md"}
    assert answer.attempts == 2 and answer.outputs["decision"].endswith("# Packet\n")
    assert rejections(run) == [["`disposition` must be one of keep, revise, not 'maybe'"]]
    # A rerun replays both attempts and launches nothing new.
    again, replayed = decide(run, "packet", prompt, SCHEMA)
    assert again == data and replayed.record["launches"] == answer.record["launches"]


def test_decide_applies_the_extra_check_and_runs_out_of_attempts(run):
    prompt = "Decide. FIRST:disposition: keep\\ndetermined: true\\ntarget: null\\n| RETRY:not: [valid|"

    def needs_target(data, text):
        return [] if data["target"] else ["`target` is required"]
    with pytest.raises(OutOfAttempts) as spent:
        decide(run, "status", prompt, SCHEMA, check=needs_target, attempts=2)
    assert rejections(run)[0] == ["`target` is required"]
    assert re.search("does not parse", str(spent.value))


def test_a_worker_problem_is_returned_unchecked(run):
    data, answer = decide(run, "status", "PROBLEM", SCHEMA)
    assert data is None and answer.problem == "no"

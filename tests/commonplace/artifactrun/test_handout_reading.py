"""Reading aliases survive deduplication; malformed dispatches fail closed."""

import re

import pytest

from commonplace.artifactrun import open_handouts
from commonplace.artifactrun.handouts import Handout, validate_handout
from commonplace.artifactrun.run import Run
from commonplace.artifactrun.store import RunStore
from commonplace.cli.run import main
from tests.commonplace.artifactrun.test_prompt_section import sectioned_run

pytestmark = pytest.mark.usefixtures("tmp_library")


def test_shared_type_is_read_once_but_both_aliases_and_pins_survive(tmp_path, monkeypatch):
    c = sectioned_run(tmp_path, monkeypatch)
    c.through_brief()
    handout = c.handout("other")
    text = handout.prompt.read_text()
    head, reading = text.split("## Input reading batches\n")
    member = re.search(r"^member-type = (.+)$", head, re.MULTILINE)[1]
    assert f"brief-type = {member}\n" in head
    assert reading.count(member) == 1
    record = Run(RunStore(c.run_dir)).attempts[handout.attempt]
    assert record["pins"]["member-type"] == record["pins"]["brief-type"]
    # First occurrence (the member's own type) stays before other contracts.
    assert re.search(r"^1\. (.+)$", reading, re.MULTILINE)[1].startswith(member)


def test_generator_regression_blocks_dispatch_and_preserves_open_handout(tmp_path, monkeypatch, capsys):
    from commonplace.artifactrun import handouts

    original = handouts.reading_batches
    monkeypatch.setattr(handouts, "reading_batches", lambda paths: original([*paths, paths[0]]))
    with pytest.raises(ValueError, match="Handout validation failed: duplicate reading entry"):
        sectioned_run(tmp_path, monkeypatch)
    run_dir = tmp_path / "run"
    run = Run(RunStore(run_dir))
    opened = [record for record in run.attempts.values() if record["state"] == "open"]
    assert len(opened) == 1
    record = opened[0]
    prompt = run.store.handout_dir(record["id"]) / "prompt.md"
    before = prompt.read_bytes()
    with pytest.raises(ValueError, match="duplicate reading entry"):
        open_handouts(run_dir)
    assert main(["status", str(run_dir)]) == 1
    captured = capsys.readouterr()
    assert not captured.out
    assert f"attempt: {record['id']}" in captured.err
    assert "occurrences: batch" in captured.err
    assert "input names: member-type" in captured.err
    assert "Dispatch blocked; handout preserved unchanged." in captured.err
    assert prompt.read_bytes() == before
    assert Run(RunStore(run_dir)).attempts[record["id"]] == record


def test_resumed_handout_is_checked_again(tmp_path, monkeypatch):
    c = sectioned_run(tmp_path, monkeypatch)
    handout = c.handout("brief")
    text = handout.prompt.read_text()
    first = re.search(r"^1\. (.+)$", text, re.MULTILINE)[1]
    text = text.replace(f"1. {first}\n", f"1. {first}\n2. {first}\n")
    handout.prompt.write_text(text)
    with pytest.raises(ValueError, match="batch 1, item 1; batch 2, item 1"):
        open_handouts(c.run_dir)
    assert handout.prompt.read_text() == text


@pytest.mark.parametrize(("body", "duplicate"), [
    ("1. /a.md, /b.md\n2. /a.md", True),
    ("1. /a.md, /a.md", True),
    ("1. /a.md, /b.md", False),
    (("1. /a.md — read in bounded ranges\n\nOversized-file ranges:\n"
      "- /a.md: lines 1-20; 21-40"), False),
    (("1. /a.md — read in bounded ranges\n\nOversized-file ranges:\n"
      "- /a.md: lines 1-20; 1-20"), True),
])
def test_rendered_check_distinguishes_aliases_and_ranges(tmp_path, body, duplicate):
    prompt = tmp_path / "prompt.md"
    # Repeated named paths and prose outside the reading list are legitimate.
    prompt.write_text("first = /a.md\nsecond = /a.md\n\n"
                      "1. /a.md\n2. /a.md\n\n## Input reading batches\n\n"
                      + body + "\n\nIf you cannot produce the output, write the problem.\n")
    handout = Handout("000001-test", "test", prompt, {}, tmp_path / "problem.md",
                      tmp_path / "worker-identity.json")
    if duplicate:
        with pytest.raises(ValueError, match="duplicate reading entry"):
            validate_handout(handout)
    else:
        validate_handout(handout)

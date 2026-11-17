"""The revise workflow's call and operator keys, pinned against recorded runs.

A change that alters a call key asks an answered call again; a change that
alters an operator key withdraws an approval. The rewrite workflow shares the
publication stop and the revised candidate with revise (`edits.publish()`,
`edits.supply_revised()`). This test runs two revise scenarios with a
deterministic fake worker and compares every Workjig call key and every
operator proposal key with `revise_keys.json`: a plan that publishes without
a publication stop (`published`), and a candidate that adds a validation
warning and so waits at the publication stop (`at-publication`,
`after-revision`).

The keys also depend on the library files the scenario reads (passes,
execution instruction, contracts). When one of those changes, the recorded
input fingerprints differ and the test says so instead of comparing keys:
regenerate with `COMMONPLACE_REGENERATE_KEYS=1` after checking that the
change is only in those inputs.
"""
from __future__ import annotations

import functools
import itertools
import json
import os
import sys
import uuid
from pathlib import Path

import pytest

from commonplace.cli.review_workflows import main
from commonplace.headless.harness import Harness
from commonplace.headless.jobs import Run, recorded_calls
from commonplace.lib import library
from commonplace.lib.review_workflows import observations
from commonplace.lib.review_workflows import revise as revise_module
from tests.commonplace.review_workflows.test_revise import (
    EDIT_TYPES,
    FAKE,
    FIX,
    HELD_WORDS,
    NOTE,
    NOTE_PATH,
    PASSES,
    PROFILES,
    answer,
    approve,
    approve_publication,
    named_plan,
    rejected,
)
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, REPO_ROOT

GOLDEN = Path(__file__).with_name("revise_keys.json")

pytestmark = pytest.mark.skipif(sys.platform == "win32",
                                reason="checked-out library files may carry CRLF line ends, which change the keys")


@pytest.fixture
def stable(tmp_path, monkeypatch):
    """A repository and fake worker whose keys do not depend on the machine, the time or random IDs."""
    import subprocess
    root = tmp_path / "repo"
    files = {rel: (REPO_ROOT / rel).read_text() for rel in NOTE_TYPE_SPECS}
    files |= {f"kb/instructions/simplification-passes/{p.name}": p.read_text() for p in PASSES.glob("*.md")}
    files |= {rel: (REPO_ROOT / rel).read_text() for rel in (*EDIT_TYPES, FIX)}
    files |= {"kb/instructions/review-profiles.yaml": PROFILES, "kb/notes/COLLECTION.md": "# Notes\n"}
    for rel, text in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text)
    for args in (("init", "-q"), ("config", "user.email", "t@example.com"), ("config", "user.name", "t")):
        subprocess.run(["git", *args], cwd=root, check=True)
    (root / NOTE_PATH).write_text(NOTE.format(words=""))
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "seed"], cwd=root, check=True)
    monkeypatch.setattr(library, "_library_root", lambda _override: (root / "kb").resolve())
    monkeypatch.setattr(revise_module, "Run", functools.partial(Run, sleep=lambda seconds: None))
    counter = itertools.count()
    monkeypatch.setattr(uuid, "uuid4", lambda: uuid.UUID(int=next(counter)))
    monkeypatch.setattr(observations, "timestamp", lambda: "2026-11-16T00:00:00Z")
    monkeypatch.chdir(root)
    (tmp_path / "launches.log").touch()
    # `python3 -c` and a relative log path keep the worker's argv and environment, part of each key, fixed.
    harness = Harness("python3", {"_subcommand": ["-c", FAKE], "_env": {"FAKE_LOG": "../launches.log"}},
                      lambda profile: {"model": profile.launch_model}, model_used=lambda launch: "fake-model-1")
    inputs = {rel: observations.sha(text.encode("utf-8")) for rel, text in sorted(files.items())}
    return root, {"fake": harness}, tmp_path / "launches.log", inputs


def _keys(root: Path, run_dir: str) -> dict:
    run = root / run_dir
    calls = sorted(f"{call['call']} {call['key']}" for call in recorded_calls(run))
    operator = {}
    for path in sorted((run / "operator").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        operator[data["name"]] = {"input-key": data["input-key"], "key": data["key"]}
    return {"calls": calls, "operator": operator}


HELD_PATH = "kb/notes/held.md"
"""The note of the second scenario, whose candidate adds a validation warning and so stops at publication."""


def _run(repo, capsys, *args, path=NOTE_PATH):
    code = main(["run", "revise", path, *args, "--timeout", "30"], harnesses=repo[1])
    captured = capsys.readouterr()
    assert code == 0, captured.err or captured.out
    return json.loads(captured.out)


def test_revise_keys_are_unchanged(stable, capsys, tmp_path):
    root = stable[0]
    plan = named_plan(tmp_path, passes=("readability-and-flow", "plain-wording"))
    waiting = _run(stable, capsys, "--plan", str(plan))
    answer(stable, waiting, {"beta": rejected("a registered word")})
    approve(stable, capsys, waiting)
    done = _run(stable, capsys)
    assert done["published"] and done["waiting-for"] is None
    published = _keys(root, done["run-dir"])
    (root / HELD_PATH).write_text(NOTE.format(words=HELD_WORDS))
    ready = _run(stable, capsys, "--plan", str(named_plan(tmp_path)), path=HELD_PATH)
    assert ready["waiting-for"]["file"].endswith("/publication-answers.md")
    at_stop = _keys(root, ready["run-dir"])
    approve_publication(stable, capsys, ready)
    revised = tmp_path / "revised.md"
    revised.write_text((root / ready["run-dir"] / "artifact/final.md").read_text() + "The operator's sentence.\n")
    supplied = _run(stable, capsys, "--revised", str(revised), path=HELD_PATH)
    found = {"inputs": stable[3], "published": published, "at-publication": at_stop,
             "after-revision": _keys(root, supplied["run-dir"])}
    if os.environ.get("COMMONPLACE_REGENERATE_KEYS"):
        GOLDEN.write_text(json.dumps(found, indent=2) + "\n", encoding="utf-8")
    recorded = json.loads(GOLDEN.read_text(encoding="utf-8"))
    changed = sorted(rel for rel in {*recorded["inputs"], *found["inputs"]}
                     if recorded["inputs"].get(rel) != found["inputs"].get(rel))
    assert not changed, (f"library inputs changed since the keys were recorded: {', '.join(changed)}; check that "
                         "only these inputs changed, then regenerate with COMMONPLACE_REGENERATE_KEYS=1")
    assert found == recorded

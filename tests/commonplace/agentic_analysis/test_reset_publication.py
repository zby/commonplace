"""Withdrawing an unreleased publication: the journal states it recognises and the ones it refuses.

Publication runs for real with scripted guards; `withdraw_publication` runs
without mocks except the preparation record naming the origin.
`test_workflow.py` covers withdrawal through the CLI, with and without an
incumbent, a withdrawal interrupted before any incumbent existed, and the
refusal when nothing was published.
"""
import json
from pathlib import Path

import pytest

from commonplace.lib.agentic_analysis import effects, publication
from commonplace.lib.agentic_analysis.analyses import ANALYSIS_TYPE
from commonplace.lib.agentic_analysis.preparation import RUNTIME_MARKER
from commonplace.lib.agentic_analysis.publication import withdraw_publication
from tests.commonplace.agentic_analysis.test_publication import (
    LAYOUT,
    OLD_ID,
    WORKER,
    doc,
    fixture,
    scripted,  # noqa: F401 - fixture used by `published`
)

ANCHOR = "overview.md"


@pytest.fixture(params=[False, True], ids=["no-incumbent", "incumbent"])
def published(tmp_path, monkeypatch, request):
    """A complete publication in a source checkout, over an incumbent or none; returns (fixture, destination, old)."""
    request.getfixturevalue("scripted")
    f = fixture(tmp_path / "repo", "complete")
    (f.repo / RUNTIME_MARKER).parent.mkdir(parents=True)
    (f.repo / RUNTIME_MARKER).write_text("# Source-checkout marker.\n")
    destination = f.destination()
    f.metadata["review-path"] = (destination / ANCHOR).relative_to(f.repo).as_posix()
    old = {ANCHOR: doc({"run-id": OLD_ID}), "memory.md": b"old memory\r\n"} if request.param else None
    if old:
        destination.mkdir(parents=True)
        for name, data in old.items():
            (destination / name).write_bytes(data)
        f.metadata["expected-incumbent-sha256"] = publication._digest(old[ANCHOR])
    monkeypatch.setattr(publication, "inspect_destination", lambda **kwargs: {
        "expected_incumbent_sha256": f.metadata["expected-incumbent-sha256"]})
    origin = tmp_path / "origin"
    monkeypatch.setattr(publication, "preparation_for", lambda _: {"origin": str(origin)})
    overview, manifest = f.assemble()
    assert f.publish(overview, manifest)["published"] is True
    f.overview, f.origin = overview, origin
    return f, destination, old


def withdraw(f):
    return withdraw_publication(f.run_dir, f.metadata, anchor=ANCHOR)


def test_withdrawal_restores_the_incumbent_and_new_bytes_publish(published):
    f, destination, old = published
    original = effects.tree(destination)
    report = withdraw(f)
    assert report["state"] == "established"
    assert effects.tree(destination) == old
    evidence = Path(report["evidence"])
    assert effects.tree(evidence / destination.name) == original
    assert (evidence / "publish.json").is_file()
    assert not (f.run_dir / publication.JOURNAL).exists()
    # A corrected overview, freshly pinned, publishes over the restored incumbent.
    corrected = {**f.members, "overview": f.overview + b"\nCorrected unreleased account.\n"}
    manifest = publication._manifest(LAYOUT, ANALYSIS_TYPE, corrected, {**WORKER, "model": "fixture-model-1"})
    receipt = f.publish(corrected["overview"], manifest)
    assert receipt["published"] is True
    assert effects.tree(destination) != original
    assert effects.hashes(effects.tree(destination)) == receipt["members"]
    journal = json.loads((f.run_dir / publication.JOURNAL).read_text())
    assert journal["new"] == receipt["members"] and journal["state"] == "completed"
    assert journal["old"] == effects.hashes(old)


def test_withdrawal_refuses_altered_publication_bytes_without_mutation(published):
    f, destination, _ = published
    (destination / "memory.md").write_bytes(b"unexpected external edit")
    journal = (f.run_dir / publication.JOURNAL).read_bytes()
    with pytest.raises(ValueError, match="exact established"):
        withdraw(f)
    assert (destination / "memory.md").read_bytes() == b"unexpected external edit"
    assert (f.run_dir / publication.JOURNAL).read_bytes() == journal
    assert not (f.run_dir / "withdrawn").exists()


def test_withdrawal_refuses_an_integrated_publication(published):
    f, destination, _ = published
    integrated = f.origin / destination.relative_to(f.repo)
    integrated.mkdir(parents=True)
    (integrated / ANCHOR).write_bytes(f.overview)
    with pytest.raises(ValueError, match="already integrated"):
        withdraw(f)
    assert (f.run_dir / publication.JOURNAL).exists()


def test_a_rolled_back_journal_is_set_aside_without_moving_the_destination(published):
    f, destination, old = published
    journal = f.run_dir / publication.JOURNAL
    record = json.loads(journal.read_text())
    # What a rolled-back publication leaves: the opening incumbent in place, no archive.
    archive = Path(record["archive"]) if record["archive"] else None
    if archive is not None:
        destination.rename(destination.with_name("published"))
        archive.rename(destination)
    else:
        for path in destination.iterdir():
            path.unlink()
        destination.rmdir()
    journal.write_text(json.dumps({**record, "state": "rolled-back"}))
    report = withdraw(f)
    assert report["state"] == "rolled-back"
    assert effects.tree(destination) == old
    assert not journal.exists()
    assert (Path(report["evidence"]) / "publish.json").is_file()


@pytest.mark.parametrize("published", [True], ids=["incumbent"], indirect=True)
def test_a_second_withdrawal_finishes_one_interrupted_before_the_archive_returned(published):
    f, destination, old = published
    journal = f.run_dir / publication.JOURNAL
    record = json.loads(journal.read_text())
    original = effects.tree(destination)
    # Interrupted after marking the journal and moving the destination away, before the archive moved back.
    journal.write_text(json.dumps({**record, "state": "withdrawing"}))
    interrupted = f.run_dir / "withdrawn" / "20260101T000000Z-crash0"
    interrupted.mkdir(parents=True)
    destination.rename(interrupted / destination.name)
    report = withdraw(f)
    assert report["state"] == "established"
    assert effects.tree(destination) == old
    assert not Path(record["archive"]).exists()
    assert not journal.exists()
    assert effects.tree(interrupted / destination.name) == original

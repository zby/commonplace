"""Tests for the ingest drafting handoff: its record, acceptance check and publication.

The ingest skill publishes a worker's candidate on these commands alone. A
wrong pass would publish an ingest pinned to the wrong snapshot bytes or with
altered retained quotes, and a write before acceptance would lose the
incumbent, so each source-integrity rule is pinned.
"""

from pathlib import Path

import pytest
import yaml

from commonplace.cli.ingest_handoff import main as handoff_main
from commonplace.cli.validate_notes import main as validate_main
from commonplace.lib.ingest_handoff import (
    CANONICAL_EMPTY_QUOTES,
    HandoffError,
    HandoffRecord,
    check_handoff,
    close_handoff,
    load_record,
    prepare_handoff,
    prune_published,
    publish_handoff,
    verify_handoff,
)
from commonplace.lib.snapshot import snapshot_sha256
from commonplace.lib.validation import CheckResults, validate_ingest_contract
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, copy_repo_files, write

pytestmark = pytest.mark.usefixtures("tmp_library")

SNAPSHOT = (
    "---\n"
    "source: https://example.com/paper\n"
    "captured: 2026-11-01\n"
    "capture: web-fetch\n"
    "capture_scope: full-source\n"
    "genre: conceptual-essay\n"
    "description: Snapshot description that the ingest must not copy.\n"
    "type: types/snapshot.md\n"
    "---\n\n"
    "# A paper\n\n"
    "Shorter contexts help agents.\n"
)



def _populated_quotes(checksum: str) -> str:
    return (
        "## Quotes\n\n"
        "> Shorter contexts help agents.\n"
        f"> --- `kb/sources/.snapshots/paper.md` @ `sha256:{checksum}` — body\n\n"
    )


def _ingest(checksum: str, *, quotes: str = CANONICAL_EMPTY_QUOTES, extra: str = "") -> str:
    return (
        "---\n"
        'description: "An essay arguing that shorter contexts help agents, used as a fixture ingest."\n'
        "source: https://example.com/paper\n"
        'captured: "2026-11-01"\n'
        "capture: web-fetch\n"
        "capture_scope: full-source\n"
        "genre: conceptual-essay\n"
        f"snapshot_sha256: {checksum}\n"
        'ingested: "2026-11-02"\n'
        "type: types/ingest-report.md\n"
        "domains: [context, agents]\n"
        f"{extra}"
        "---\n\n"
        "# Ingest: A paper\n\n"
        "## Classification\n\nA conceptual essay.\n\n"
        "## Summary\n\nThe essay argues for shorter contexts.\n\n"
        f"{quotes}"
        "## Connections Found\n\nNone.\n\n"
        "## Extractable Value\n\n1. A framing. [quick-win]\n\n"
        "## Limitations (our opinion)\n\nNo evidence is reported.\n\n"
        "## Recommended Next Action\n\nNo action.\n"
    )


@pytest.fixture
def pair(tmp_path: Path) -> tuple[Path, Path, str]:
    copy_repo_files(
        tmp_path,
        *NOTE_TYPE_SPECS,
        "kb/types/ingest-report.md",
        "kb/types/ingest-report.schema.yaml",
    )
    snapshot = write(tmp_path / "kb/sources/.snapshots/paper.md", SNAPSHOT)
    checksum = snapshot_sha256(snapshot)
    ingest = write(tmp_path / "kb/sources/paper.ingest.md", _ingest(checksum))
    return ingest, snapshot, checksum


def _prepare(ingest: Path, **options: object) -> HandoffRecord:
    return prepare_handoff(ingest, repo_root=ingest.parents[2], **options)


def _failures(record: HandoffRecord) -> list[str]:
    return verify_handoff(record, repo_root=record.ingest.parents[2]).failures


def _contract_warnings(ingest: Path) -> list[str]:
    results = CheckResults(note_type="ingest-report")
    validate_ingest_contract(results, ingest.read_text(encoding="utf-8"), ingest)
    return results.warns


def test_a_new_report_is_drafted_outside_the_library_and_published(
    pair: tuple[Path, Path, str],
) -> None:
    ingest, _snapshot, checksum = pair
    draft = ingest.read_text(encoding="utf-8")
    ingest.unlink()
    root = ingest.parents[2]

    record = _prepare(ingest)
    assert record.candidate == root / "kb/reports/state/ingest/paper/candidate.md"
    assert record.snapshot_sha256 == checksum
    assert record.incumbent_sha256 is None
    assert record.retained_quotes_path.read_text(encoding="utf-8") == CANONICAL_EMPTY_QUOTES
    assert _failures(record) == [f"candidate: {record.candidate} is missing or empty"]

    record.candidate.write_text(draft, encoding="utf-8")
    assert _failures(record) == []
    assert not ingest.exists()

    assert publish_handoff(record, repo_root=root).failures == []
    assert ingest.read_text(encoding="utf-8") == draft
    # The directory stays as the record of the run; the candidate equals the ingest.
    assert not record.candidate.exists()
    ended = load_record(record.path, repo_root=root)
    assert ended.outcome == "published"
    with pytest.raises(HandoffError, match="already ended"):
        publish_handoff(ended, repo_root=root)


def test_a_failing_candidate_is_not_published_and_the_incumbent_is_untouched(
    pair: tuple[Path, Path, str],
) -> None:
    ingest, _snapshot, checksum = pair
    incumbent = ingest.read_bytes()
    record = _prepare(ingest)
    record.candidate.write_text(
        _ingest(checksum).replace("## Recommended Next Action\n\nNo action.\n", ""),
        encoding="utf-8",
    )

    result = publish_handoff(record, repo_root=ingest.parents[2])

    assert any(f.startswith("validation:") for f in result.failures)
    assert ingest.read_bytes() == incumbent
    assert record.candidate.is_file()

    close_handoff(record)
    assert ingest.read_bytes() == incumbent
    assert record.candidate.is_file()
    root = ingest.parents[2]
    assert load_record(record.path, repo_root=root).outcome == "closed"

    # A finished run does not block the next one; only the last run is kept.
    again = _prepare(ingest)
    assert again.outcome is None
    assert not again.candidate.exists()


def test_the_record_keeps_every_check_and_prune_removes_old_published_runs(
    pair: tuple[Path, Path, str],
) -> None:
    ingest, _snapshot, checksum = pair
    root = ingest.parents[2]
    record = _prepare(ingest)
    assert check_handoff(record, repo_root=root).failures
    record.candidate.write_text(_ingest(checksum), encoding="utf-8")
    assert publish_handoff(record, repo_root=root).failures == []

    checks = yaml.safe_load(record.path.read_text(encoding="utf-8"))["checks"]
    assert [bool(check["failures"]) for check in checks] == [True, False]

    assert prune_published(repo_root=root, older_than_days=1) == []
    assert record.path.is_file()
    assert prune_published(repo_root=root, older_than_days=0) == [record.path.parent]
    assert not record.path.parent.exists()


def test_prune_keeps_open_and_closed_runs(pair: tuple[Path, Path, str]) -> None:
    ingest, _snapshot, _checksum = pair
    root = ingest.parents[2]
    record = _prepare(ingest)
    assert prune_published(repo_root=root, older_than_days=0) == []
    close_handoff(record)
    assert prune_published(repo_root=root, older_than_days=0) == []
    assert record.path.is_file()


def test_an_incumbent_changed_during_drafting_is_not_overwritten(
    pair: tuple[Path, Path, str],
) -> None:
    ingest, _snapshot, checksum = pair
    record = _prepare(ingest)
    record.candidate.write_text(_ingest(checksum), encoding="utf-8")
    grounded = _ingest(checksum, quotes=_populated_quotes(checksum))
    ingest.write_text(grounded, encoding="utf-8")

    result = publish_handoff(record, repo_root=ingest.parents[2])

    assert any(f.startswith("incumbent: paper.ingest.md changed") for f in result.failures)
    assert ingest.read_text(encoding="utf-8") == grounded


def test_prepare_refuses_a_changed_observation_before_writing(
    pair: tuple[Path, Path, str],
) -> None:
    ingest, snapshot, _checksum = pair
    snapshot.write_text(SNAPSHOT + "An appended line.\n", encoding="utf-8")

    with pytest.raises(HandoffError, match="instruction re-ingest with Target"):
        _prepare(ingest)
    assert not (ingest.parents[2] / "kb/reports/state").exists()


def test_prepare_refuses_a_missing_snapshot_duplicate_quotes_and_an_open_run(
    pair: tuple[Path, Path, str],
) -> None:
    ingest, snapshot, checksum = pair
    _prepare(ingest)
    with pytest.raises(HandoffError, match="unfinished ingest run"):
        _prepare(ingest)

    ingest.write_text(_ingest(checksum, quotes=CANONICAL_EMPTY_QUOTES * 2), encoding="utf-8")
    with pytest.raises(HandoffError, match="2 Quotes blocks"):
        _prepare(ingest)

    snapshot.unlink()
    with pytest.raises(HandoffError, match="snapshot not available on this machine"):
        _prepare(ingest)


def test_snapshot_bytes_changed_after_dispatch_fail(pair: tuple[Path, Path, str]) -> None:
    ingest, snapshot, checksum = pair
    record = _prepare(ingest)
    record.candidate.write_text(_ingest(checksum), encoding="utf-8")
    snapshot.write_text(SNAPSHOT + "An appended line.\n", encoding="utf-8")

    assert any(f.startswith("snapshot: bytes changed since dispatch") for f in _failures(record))

    # A worker that re-pinned the candidate to the changed bytes is still refused.
    record.candidate.write_text(_ingest(snapshot_sha256(snapshot)), encoding="utf-8")
    assert any(f.startswith("snapshot: candidate snapshot_sha256") for f in _failures(record))


def test_a_refresh_must_keep_the_incumbent_quotes_byte_for_byte(
    pair: tuple[Path, Path, str],
) -> None:
    ingest, _snapshot, checksum = pair
    incumbent = _ingest(checksum, quotes=_populated_quotes(checksum))
    ingest.write_text(incumbent, encoding="utf-8")
    record = _prepare(ingest)
    assert record.retained_quotes_path.read_text(encoding="utf-8") == _populated_quotes(checksum)

    # The worker dropped the retained quotes for the empty block.
    record.candidate.write_text(_ingest(checksum), encoding="utf-8")
    assert any(f.startswith("quotes: the block does not equal") for f in _failures(record))

    record.candidate.write_text(
        incumbent.replace("> Shorter contexts", ">  Shorter contexts"), encoding="utf-8"
    )
    assert any(f.startswith("quotes: the block does not equal") for f in _failures(record))

    # Verification reads the incumbent, not the worker's convenience copy.
    record.retained_quotes_path.write_text(CANONICAL_EMPTY_QUOTES, encoding="utf-8")
    record.candidate.write_text(_ingest(checksum), encoding="utf-8")
    assert any(f.startswith("quotes: the block does not equal") for f in _failures(record))

    record.candidate.write_text(incumbent.replace("essay argues", "essay claims"), encoding="utf-8")
    assert _failures(record) == []


def test_occasion_is_required_exactly_when_supplied(pair: tuple[Path, Path, str]) -> None:
    ingest, _snapshot, checksum = pair
    record = _prepare(ingest, occasion="Why shorten?")
    record.candidate.write_text(_ingest(checksum), encoding="utf-8")
    assert any(f.startswith("occasion:") for f in _failures(record))

    record.candidate.write_text(_ingest(checksum, extra='occasion: "Why shorten?"\n'), encoding="utf-8")
    assert _failures(record) == []

    close_handoff(record)
    without = _prepare(ingest)
    without.candidate.write_text(_ingest(checksum, extra='occasion: "Why shorten?"\n'), encoding="utf-8")
    assert any(f.startswith("occasion:") for f in _failures(without))


def test_code_grounding_must_match_the_run(pair: tuple[Path, Path, str]) -> None:
    ingest, _snapshot, checksum = pair
    record = _prepare(ingest, code_grounded=True)
    record.candidate.write_text(_ingest(checksum), encoding="utf-8")
    failures = _failures(record)
    assert "code grounding: secondary_sources is missing" in failures
    assert "code grounding: '## Code Grounding' section is missing" in failures


@pytest.mark.parametrize(
    ("sentence", "expected"),
    [
        ("See [the copy](./.snapshots/paper.md).", "links into .snapshots/"),
        ("The code is in related-systems/tool/main.py.", "related-systems/ checkout"),
        ("Discovery in paper.connect.md found none.", "generated connect report"),
    ],
)
def test_local_only_references_warn_in_validation_and_fail_a_handoff(
    pair: tuple[Path, Path, str], sentence: str, expected: str
) -> None:
    ingest, _snapshot, checksum = pair
    content = _ingest(checksum).replace("A conceptual essay.", f"A conceptual essay. {sentence}")
    record = _prepare(ingest)
    record.candidate.write_text(content, encoding="utf-8")

    result = verify_handoff(record, repo_root=ingest.parents[2])
    assert any(expected in failure for failure in result.failures)
    assert not any(expected in warning for warning in result.warnings)

    ingest.write_text(content, encoding="utf-8")
    assert any(expected in warning for warning in _contract_warnings(ingest))


def test_candidate_links_resolve_from_the_ingest_path(pair: tuple[Path, Path, str]) -> None:
    ingest, _snapshot, checksum = pair
    write(ingest.parent / "neighbour.md", "# Neighbour\n")
    record = _prepare(ingest)

    record.candidate.write_text(
        _ingest(checksum).replace("None.", "- [Neighbour](./neighbour.md) — compares-with: fixture"),
        encoding="utf-8",
    )
    assert _failures(record) == []

    record.candidate.write_text(
        _ingest(checksum).replace("None.", "- [Missing](./missing.md) — compares-with: fixture"),
        encoding="utf-8",
    )
    assert any("missing.md" in f for f in _failures(record))


def test_quote_attributions_may_name_the_snapshot(pair: tuple[Path, Path, str]) -> None:
    ingest, _snapshot, checksum = pair
    ingest.write_text(_ingest(checksum, quotes=_populated_quotes(checksum)), encoding="utf-8")
    assert _contract_warnings(ingest) == []


def test_contract_warns_on_quotes_position_and_uncopied_capture_metadata(
    pair: tuple[Path, Path, str],
) -> None:
    ingest, _snapshot, checksum = pair
    content = _ingest(checksum)

    moved = content.replace(
        CANONICAL_EMPTY_QUOTES + "## Connections Found\n\nNone.\n\n",
        "## Connections Found\n\nNone.\n\n" + CANONICAL_EMPTY_QUOTES,
    )
    ingest.write_text(moved, encoding="utf-8")
    assert any("not immediately before" in w for w in _contract_warnings(ingest))

    ingest.write_text(content.replace("capture_scope: full-source\n", ""), encoding="utf-8")
    assert any("'capture_scope' was not copied" in w for w in _contract_warnings(ingest))

    ingest.write_text(content.replace('captured: "2026-11-01"', 'captured: "2026-11-02"'), encoding="utf-8")
    assert any("'captured' is" in w for w in _contract_warnings(ingest))

    # A quoted date equals the snapshot's bare YAML date.
    ingest.write_text(content, encoding="utf-8")
    assert _contract_warnings(ingest) == []


def test_commands_run_prepare_check_and_publish(
    pair: tuple[Path, Path, str],
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    ingest, _snapshot, checksum = pair
    root = ingest.parents[2]
    monkeypatch.chdir(root)
    refreshed = _ingest(checksum).replace("essay argues", "essay claims")

    assert handoff_main(["prepare", "kb/sources/paper.ingest.md"]) == 0
    fields = dict(line.split(": ", 1) for line in capsys.readouterr().out.splitlines())
    assert fields["handoff_record"] == "kb/reports/state/ingest/paper/handoff.yaml"
    assert fields["candidate_path"] == "kb/reports/state/ingest/paper/candidate.md"
    assert fields["snapshot_sha256"] == checksum

    candidate = root / fields["candidate_path"]
    candidate.write_text(refreshed.replace(CANONICAL_EMPTY_QUOTES, ""), encoding="utf-8")
    assert validate_main([fields["candidate_path"], "--handoff", fields["handoff_record"]]) == 1
    out = capsys.readouterr().out
    assert out.startswith("HANDOFF FAILED: kb/reports/state/ingest/paper/candidate.md for kb/sources/paper.ingest.md")
    assert "- quotes: expected exactly one Quotes block, found 0" in out
    assert handoff_main(["publish", fields["handoff_record"]]) == 1
    assert "Not published" in capsys.readouterr().out

    assert validate_main(["kb/sources/paper.ingest.md", "--handoff", fields["handoff_record"]]) == 2
    capsys.readouterr()

    candidate.write_text(refreshed, encoding="utf-8")
    assert validate_main([fields["candidate_path"], "--handoff", fields["handoff_record"]]) == 0
    assert capsys.readouterr().out.startswith("HANDOFF CLEAN:")
    assert handoff_main(["publish", fields["handoff_record"]]) == 0
    assert ingest.read_text(encoding="utf-8") == refreshed
    capsys.readouterr()

    assert handoff_main(["prune", "--days", "0"]) == 0
    assert "removed: kb/reports/state/ingest/paper" in capsys.readouterr().out
    assert not (root / "kb/reports/state/ingest/paper").exists()

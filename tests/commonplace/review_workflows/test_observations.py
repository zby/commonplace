"""Captured inputs, draft identity and independent fixture trials on a fake harness."""
import json

import pytest

from commonplace.cli.review_workflows import main
from commonplace.lib.review_workflows import fixtures, observations
from tests.commonplace.review_workflows.test_gates import _project, note, review, write


@pytest.fixture
def repo(tmp_path, monkeypatch):
    return _project(tmp_path, monkeypatch, installed=False)


def records(root, run):
    return sorted((root / run / "artifact/reviews").glob("*/observation.json"))


def test_capture_exact_bytes_and_replay_retains_completion(repo, capsys):
    root = repo[0]
    target = root / "kb/notes/alpha.md"
    data = note("Alpha", "Uncommitted body.").replace("\n", "\r\n").rstrip("\r\n").encode()
    target.write_bytes(data)
    code, report, _ = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate")
    assert code == 0, report
    [record] = records(root, report["run-dir"])
    retained = json.loads(record.read_text())
    captured = next(x for x in retained["inputs"] if x["role"] == "target")
    assert (record.parent / captured["path"]).read_bytes() == data
    [result] = retained["completed-results"]
    result_bytes = (record.parent / result).read_bytes()
    target.write_text(note("Alpha", "Changed after capture."))
    code, again, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate",
                                  "--resume", report["run-dir"], "--force")
    assert code == 0 and launches == [], again
    assert (record.parent / result).read_bytes() == result_bytes
    assert len(records(root, report["run-dir"])) == 1
    (record.parent / captured["path"]).write_text("tampered")
    assert main(["run", "gates", "kb/notes/alpha.md", "--criteria", "prose/body-gate",
                 "--resume", report["run-dir"], "--force"], harnesses=repo[1]) == 2


def test_draft_and_show_do_not_publish(repo, capsys):
    root = repo[0]
    path = root / "kb/draft.md"
    path.write_text("---\ntype: types/review-gate.md\ndescription: A draft gate checking one supplied artifact\n"
                    "gate_id: experimental/check\nname: Draft\nlens: experimental\nwatches: [body]\n"
                    "staleness: changed\nreading-scope: linked-files\n---\n\n# Draft\n\n"
                    "## Failure mode\nMissing evidence.\n\n## Test\nCheck the evidence.\n")
    # The explicit selector validates the actual gate type, unlike catalog fixture stubs.
    from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, REPO_ROOT
    for name in (*NOTE_TYPE_SPECS, "kb/types/review-gate.md", "kb/types/review-gate.schema.yaml"):
        (root / name).write_bytes((REPO_ROOT / name).read_bytes())
    runs = []
    for _ in range(2):
        code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criterion-file", "kb/draft.md")
        assert code == 0 and len(launches) == 1, report
        runs.append(report["run-dir"])
    assert runs[0] != runs[1]
    assert not list((root / "kb/reports/state/review/results").rglob("*.md"))
    assert main(["show", runs[0], "--json"], harnesses=repo[1]) == 0
    shown = json.loads(capsys.readouterr().out)
    assert shown["observations"][0]["results"][0]["findings"] == []
    path.write_text(path.read_text().replace("linked-files", "corpus"))
    assert main(["run", "gates", "kb/notes/alpha.md", "--criterion-file", "kb/draft.md"], harnesses=repo[1]) == 2


@pytest.mark.parametrize("installed", [False, True])
def test_fixture_trials_are_independent_and_resume_is_not_a_trial(tmp_path, monkeypatch, capsys, installed):
    repo = _project(tmp_path, monkeypatch, installed=installed)
    root, harnesses, log = repo
    write(root, "kb/notes/alpha.md", note("Alpha", "Captured uncommitted text."))
    code, source, _ = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate")
    assert code == 0
    [record] = records(root, source["run-dir"])
    with pytest.raises(ValueError, match="substitute"):
        fixtures.create(root, source["run-dir"], record.parent.name)
    fixture = fixtures.create(root, source["run-dir"], record.parent.name, substitute_executor=True)
    name = fixture.relative_to(root).as_posix()
    live = {str(p): p.read_bytes() for p in (root / "kb/reports/state/review/results").rglob("*.md") if p.is_file()}
    runs = []
    for _ in range(2):
        before = len(log.read_text().splitlines())
        assert main(["run", "gates", "--fixture", name], harnesses=harnesses) == 0
        report = json.loads(capsys.readouterr().out)
        runs.append(report["run-dir"])
        assert len(log.read_text().splitlines()) == before + 1
        assert report["effective-configuration"] == "unassessed"
        assert not report["changed"]
    assert runs[0] != runs[1]
    before = log.read_text()
    assert main(["run", "gates", "--fixture", name, "--resume", runs[0]], harnesses=harnesses) == 0
    capsys.readouterr()
    assert log.read_text() == before
    assert {str(p): p.read_bytes() for p in (root / "kb/reports/state/review/results").rglob("*.md") if p.is_file()} == live
    (fixture / "inputs/criterion.md").write_text("tampered")
    with pytest.raises(ValueError, match="changed"):
        fixtures.load(root, name)


def test_unsafe_capture_and_old_run_are_rejected(repo, capsys):
    root = repo[0]
    with pytest.raises(ValueError, match="unsafe"):
        observations.safe_path(root, "../outside")
    (root / "escape").symlink_to(root.parent, target_is_directory=True)
    with pytest.raises(ValueError, match="escapes"):
        observations.safe_path(root, "escape/file")
    old = root / "kb/reports/state/review/runs/old"
    old.mkdir(parents=True)
    (old / "sweep.json").write_text('{"profile": {}}')
    assert main(["run", "gates", "kb/notes/alpha.md", "--criteria", "prose/body-gate", "--resume", str(old)],
                harnesses=repo[1]) == 2
    assert "old-format" in capsys.readouterr().err


def test_explicit_input_and_historical_content_repair(repo, capsys):
    root = repo[0]
    support = "kb/notes/support.md"
    original = note("Support", "Historical support content.")
    write(root, support, original)
    source = "kb/reports/state/other-run/findings.md"
    (root / source).parent.mkdir(parents=True)
    write(root, source, "Self-contained finding. See [unavailable provenance](missing.md).\r\n")
    code, report, _ = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate",
                             "--input", f"findings={source}")
    assert code == 0, report
    assert not list((root / "kb/reports/state/review/results").rglob("*.md"))
    [record] = records(root, report["run-dir"])
    held = json.loads(record.read_text())
    [supplied] = [item for item in held["inputs"] if item["role"] == "operational"]
    assert (record.parent / supplied["path"]).read_bytes() == (root / source).read_bytes()
    write(root, support, note("Support", "Changed after observation."))
    with pytest.raises(ValueError, match="historical dirty content unavailable"):
        fixtures.create(root, report["run-dir"], record.parent.name, substitute_executor=True)
    write(root, "repair.md", original)
    fixture = fixtures.create(root, report["run-dir"], record.parent.name,
                              substitute_executor=True, repairs={support: "repair.md"})
    assert main(["run", "gates", "--fixture", fixture.relative_to(root).as_posix()], harnesses=repo[1]) == 0
    trial = json.loads(capsys.readouterr().out)
    tree = root / trial["evidence-root"]
    assert (tree / support).read_text() == original
    assert not (tree / source).exists()
    assert not (tree / "kb/reports/state/other-run/missing.md").exists()
    assert main(["show", trial["run-dir"], "--json"], harnesses=repo[1]) == 0
    shown = json.loads(capsys.readouterr().out)
    assert len(shown["observations"]) == 1
    assert shown["observations"][0]["results"][0]["outcome"] == "pass"
    (tree / "kb/notes/alpha.md").write_text("unexpected mutation")
    assert main(["run", "gates", "--fixture", fixture.relative_to(root).as_posix(),
                 "--resume", trial["run-dir"]], harnesses=repo[1]) == 2
    assert "trial tree changed" in capsys.readouterr().err


def test_rejection_replay_and_contract_freshness(repo, capsys):
    from commonplace.lib.review_workflows import results
    root = repo[0]
    write(root, "kb/notes/alpha.md", note("Alpha", "MALFORMED first answer."))
    code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate")
    assert code == 0 and len(launches) == 2
    [record] = records(root, report["run-dir"])
    data = observations.load(record.parent)
    assert data["content-rejections"] == 1
    code, _, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate",
                               "--resume", report["run-dir"], "--force")
    assert code == 0 and not launches
    data = observations.load(record.parent)
    assert data["content-rejections"] == 1 and data["rejection-events"] == 2
    criterion = "kb/instructions/review-gates/prose/body-gate.md"
    assert results.freshness(root, "kb/notes/alpha.md", criterion).state == "fresh"
    contract = root / "kb/types/review-result.md"
    contract.write_text(contract.read_text() + "\nA compatible contract wording change.\n")
    assert results.freshness(root, "kb/notes/alpha.md", criterion).changed == ("output-contract",)
    assert main(["show", report["run-dir"], "--json"], harnesses=repo[1]) == 0
    capsys.readouterr()
    completed = record.parent / data["completed-results"][0]
    completed.write_text(completed.read_text() + "tampered\n")
    assert main(["show", report["run-dir"], "--json"], harnesses=repo[1]) == 2
    assert "retained completed result changed" in capsys.readouterr().err

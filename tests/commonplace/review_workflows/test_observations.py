"""Captured inputs, draft identity and independent fixture trials on a fake harness."""
import json
import shutil
import sys
import tarfile
from pathlib import Path

import pytest

from commonplace.cli.review_workflows import main
from commonplace.headless.jobs import Run
from commonplace.lib import frontmatter
from commonplace.lib.review_workflows import fixtures, observations
from tests.commonplace.link_helpers import junction
from tests.commonplace.review_workflows.test_gates import (
    _project,
    git,
    note,
    review,
    write,
)


@pytest.fixture
def repo(tmp_path, monkeypatch):
    return _project(tmp_path, monkeypatch, installed=False)


def records(root, run):
    return sorted((root / run / "artifact/reviews").glob("*/observation.json"))


@pytest.mark.parametrize("installed", [False, True])
def test_fixture_excludes_ignored_ambient_files_but_retains_explicit_input(tmp_path, monkeypatch, capsys, installed):
    repo = _project(tmp_path, monkeypatch, installed=installed)
    root, harnesses, _ = repo
    (root / "kb/messages").mkdir(parents=True)
    (root / "kb/sources/cache").mkdir(parents=True)
    write(root, ".gitignore", "kb/messages/\nkb/sources/cache/\n*.cache\n")
    write(root, "kb/messages/private.md", "ambient mailbox")
    write(root, "kb/sources/cache/private.txt", "ambient source snapshot")
    write(root, "kb/sources/cache/selected.txt", "explicit operational evidence")
    write(root, "kb/notes/retained.cache", "tracked despite ignore rule")
    git(root, "add", "-f", "kb/notes/retained.cache")
    git(root, "add", ".gitignore")
    git(root, "commit", "-qm", "Declare ignored ambient data")
    write(root, "kb/notes/draft.md", "Untracked authored text")
    forbidden = {root / "kb/messages/private.md", root / "kb/sources/cache/private.txt"}
    read_bytes = Path.read_bytes

    def guarded_read(path):
        assert path not in forbidden, "ambient data must not even be read for its hash"
        return read_bytes(path)

    monkeypatch.setattr(Path, "read_bytes", guarded_read)
    code, report, _ = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate",
                             "--input", "evidence=kb/sources/cache/selected.txt")
    assert code == 0
    [record_path] = records(root, report["run-dir"])
    record = observations.load(record_path.parent)
    assert record["library-policy"] == observations.LIBRARY_POLICY
    # Exercise captured-content restoration without smuggling the explicit
    # ignored input into the library inventory during that restoration.
    write(root, "kb/notes/alpha.md", note("Alpha", "Changed after the observation."))
    fixture = fixtures.create(root, report["run-dir"], record_path.parent.name, substitute_executor=True)
    with tarfile.open(fixture / "library.tar") as archive:
        names = archive.getnames()
        assert not any(name.startswith(("messages/", "sources/cache/")) for name in names)
        if not installed:
            assert "notes/retained.cache" in names
            assert "notes/draft.md" in names
    with tarfile.open(fixture / "kb.tar") as archive:
        assert not any(name.startswith(("kb/messages/", "kb/sources/cache/")) for name in archive.getnames())
    explicit = next(item for item in record["inputs"] if item["role"] == "operational")
    assert (fixture / explicit["path"]).read_text() == "explicit operational evidence"
    assert main(["--fixture", fixture.relative_to(root).as_posix()], harnesses=harnesses) == 0
    trial = json.loads(capsys.readouterr().out)
    tree = root / trial["evidence-root"]
    assert not (tree / "kb/messages/private.md").exists()
    assert not (tree / "kb/sources/cache/selected.txt").exists()
    [held] = records(tree, "kb/reports/state/review/runs/v2/trial")
    data = observations.load(held.parent)
    assert data["library-sha256"] == record["library-sha256"]
    assert any(item["role"] == "operational" for item in data["inputs"])


def test_fixture_refuses_to_reinterpret_old_inventory_policy(repo, capsys):
    root = repo[0]
    code, report, _ = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate")
    assert code == 0
    [path] = records(root, report["run-dir"])
    original = path.read_bytes()
    data = json.loads(original)
    del data["library-policy"]
    path.write_text(json.dumps(data))
    old = path.read_bytes()
    with pytest.raises(ValueError, match="unsupported library inventory policy"):
        fixtures.create(root, report["run-dir"], path.parent.name, substitute_executor=True)
    assert path.read_bytes() == old
    path.write_bytes(original)
    fixture = fixtures.create(root, report["run-dir"], path.parent.name, substitute_executor=True)
    data = json.loads((fixture / "fixture.json").read_text())
    del data["library-policy"]
    (fixture / "fixture.json").write_text(json.dumps(data))
    with pytest.raises(ValueError, match="unsupported fixture library inventory policy"):
        fixtures.load(root, fixture.relative_to(root).as_posix())


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
    assert observations.read_inputs(record.parent, retained)[captured["path"]] == data
    assert not (record.parent / "inputs").exists()
    [result] = retained["completed-results"]
    result_bytes = (record.parent / result).read_bytes()
    target.write_text(note("Alpha", "Changed after capture."))
    code, again, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate",
                                  "--resume", report["run-dir"], "--force")
    assert code == 0 and launches == [], again
    assert (record.parent / result).read_bytes() == result_bytes
    assert len(records(root, report["run-dir"])) == 1
    # Corrupt the authoritative Workjig request, not a redundant observation copy.
    [payload] = [path for path in (root / report["run-dir"] / "calls/payloads").rglob("*")
                 if path.is_file() and b"Uncommitted body." in path.read_bytes()]
    payload.write_bytes(payload.read_bytes().replace(b"Uncommitted body.", b"Tampered body."))
    assert main(["kb/notes/alpha.md", "--criteria", "prose/body-gate",
                 "--resume", report["run-dir"], "--force"], harnesses=repo[1]) == 2


@pytest.mark.parametrize("grouping", ["pair", "bundle"])
def test_workjig_owns_inputs_and_shared_executor_survives_run_copy(repo, capsys, grouping, tmp_path):
    root = repo[0]
    code, report, _ = review(repo, capsys, "kb/notes/alpha.md", "--criteria",
                             "prose/body-gate", "prose/description-gate", "--grouping", grouping)
    assert code == 0, json.dumps(report, indent=2)
    run = root / report["run-dir"]
    paths = records(root, report["run-dir"])
    assert len(paths) == 2
    held = [observations.load(path.parent) for path in paths]
    assert all(data["version"] == observations.VERSION for data in held)
    assert held[0]["executor"] == held[1]["executor"]
    assert len(list((run / "provenance").glob("*.json"))) == 1
    for path, data in zip(paths, held, strict=True):
        assert not (path.parent / "inputs").exists()
        assert all(set(call) == {"call", "key"} for call in data["calls"])
        assert "launch-evidence" not in data
        inputs = observations.read_inputs(path.parent, data)
        criterion = next(item for item in data["inputs"] if item["role"] == "criterion")
        assert inputs[criterion["path"]] == (root / data["request"]["criterion"]).read_bytes()
    # Resolving a copied run must never fall back to the original absolute path.
    copied = tmp_path / "exported-run"
    shutil.copytree(run, copied)
    directory = copied / paths[0].parent.relative_to(run)
    assert observations.read_inputs(directory) == observations.read_inputs(paths[0].parent)
    (copied / "calls/run.json").unlink()
    with pytest.raises(ValueError, match="Workjig input evidence unavailable"):
        observations.load(directory)
    # Shared provenance remains integrity checked, not an unchecked convenience cache.
    (run / held[0]["executor"]["path"]).write_text("{}")
    for path in paths:
        with pytest.raises(ValueError, match="executor provenance changed"):
            observations.load(path.parent)


def test_retained_v2_observation_remains_a_fixture_source(repo, capsys):
    root = repo[0]
    code, report, _ = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate")
    assert code == 0
    [path] = records(root, report["run-dir"])
    data = observations.load(path.parent)
    captured = observations.read_inputs(path.parent, data)
    data["executor"] = observations.executor_record(path.parent, data)
    data["version"] = 2
    for item in data["inputs"]:
        target = path.parent / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(captured[item["path"]])
        item.pop("input", None)
    [name] = data["completed-results"]
    saved = path.parent / name
    text = saved.read_text()
    original_capture = frontmatter.parse(text).data["target-capture"]
    legacy_capture = (path.parent / "inputs/target/kb/notes/alpha.md").relative_to(root).as_posix()
    saved.write_text(text.replace(original_capture, legacy_capture), encoding="utf-8", newline="\n")
    data["completed-result-sha256"][name] = observations.sha(saved.read_bytes())
    observations.atomic_json(path, data)
    assert observations.read_inputs(path.parent) == captured
    before = saved.read_bytes()
    code, resumed, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate",
                                    "--resume", report["run-dir"], "--force")
    assert code == 0 and not launches, resumed
    assert saved.read_bytes() == before
    fixture = fixtures.create(root, report["run-dir"], path.parent.name, substitute_executor=True)
    assert fixtures.load(root, fixture.relative_to(root).as_posix())[1]["source-executor"] == data["executor"]
    # Independent exports contain bytes, not live references back to the run.
    shutil.rmtree(root / report["run-dir"])
    assert fixtures.load(root, fixture.relative_to(root).as_posix())
    assert main(["--fixture", fixture.relative_to(root).as_posix()], harnesses=repo[1]) == 0
    capsys.readouterr()


def test_interruption_before_workjig_registration_can_resume(repo, capsys, monkeypatch):
    root = repo[0]

    def interrupt(*args, **kwargs):
        raise OSError("stopped before Workjig registration")

    with monkeypatch.context() as patch:
        patch.setattr(Run, "ask", interrupt)
        assert main(["kb/notes/alpha.md", "--criteria", "prose/body-gate", "--timeout", "30"],
                    harnesses=repo[1]) == 2
    assert "stopped before Workjig registration" in capsys.readouterr().err
    [path] = (root / "kb/reports/state/review/runs/v2").glob("*/artifact/reviews/*/observation.json")
    data = observations.load(path.parent)
    assert data["calls"] == [] and not (path.parent / "inputs").exists()
    run = observations.run_root(path.parent).relative_to(root).as_posix()
    assert main(["show", run, "--json"], harnesses=repo[1]) == 0
    capsys.readouterr()
    code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate",
                                   "--resume", run)
    assert code == 0 and len(launches) == 1, report
    assert observations.read_inputs(path.parent)


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
    assert main(["kb/notes/alpha.md", "--criterion-file", "kb/draft.md"], harnesses=repo[1]) == 2


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
        assert main(["--fixture", name], harnesses=harnesses) == 0
        report = json.loads(capsys.readouterr().out)
        runs.append(report["run-dir"])
        assert len(log.read_text().splitlines()) == before + 1
        assert report["effective-configuration"] == "unassessed"
        assert not report["changed"]
    assert runs[0] != runs[1]
    before = log.read_text()
    assert main(["--fixture", name, "--resume", runs[0]], harnesses=harnesses) == 0
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
    escape = root / "escape"
    if sys.platform == "win32":
        junction(escape, root.parent)
    else:
        escape.symlink_to(root.parent, target_is_directory=True)
    with pytest.raises(ValueError, match="escapes"):
        observations.safe_path(root, "escape/file")
    old = root / "kb/reports/state/review/runs/old"
    old.mkdir(parents=True)
    (old / "sweep.json").write_text('{"profile": {}}')
    assert main(["kb/notes/alpha.md", "--criteria", "prose/body-gate", "--resume", str(old)],
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
    assert observations.read_inputs(record.parent, held)[supplied["path"]] == (root / source).read_bytes()
    write(root, support, note("Support", "Changed after observation."))
    with pytest.raises(ValueError, match="historical dirty content unavailable"):
        fixtures.create(root, report["run-dir"], record.parent.name, substitute_executor=True)
    write(root, "repair.md", original)
    fixture = fixtures.create(root, report["run-dir"], record.parent.name,
                              substitute_executor=True, repairs={support: "repair.md"})
    assert main(["--fixture", fixture.relative_to(root).as_posix()], harnesses=repo[1]) == 0
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
    assert main(["--fixture", fixture.relative_to(root).as_posix(),
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
    contract.write_text(contract.read_text(encoding="utf-8") + "\nA compatible contract wording change.\n",
                        encoding="utf-8", newline="\n")
    assert results.freshness(root, "kb/notes/alpha.md", criterion).changed == ("output-contract",)
    assert main(["show", report["run-dir"], "--json"], harnesses=repo[1]) == 0
    capsys.readouterr()
    completed = record.parent / data["completed-results"][0]
    completed.write_text(completed.read_text() + "tampered\n")
    assert main(["show", report["run-dir"], "--json"], harnesses=repo[1]) == 2
    assert "retained completed result changed" in capsys.readouterr().err

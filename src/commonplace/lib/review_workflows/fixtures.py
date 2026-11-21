"""Single-atom retained baselines and fresh trials, using the ordinary gate or edit implementation.

A fixture holds one observation: a review of one pair, or one edit
execution. A trial reruns it in an independent tree through the same code
that produced it (`gates.ask()` or `edit_operations.ask()`).
"""
from __future__ import annotations

import io
import json
import os
import subprocess
import tarfile
import uuid
from dataclasses import asdict, replace
from pathlib import Path

from commonplace.headless.harness import HARNESSES, Profile
from commonplace.headless.jobs import LaunchFailed, NoProgress, OutOfAttempts
from commonplace.lib.library import library_root
from commonplace.lib.review_workflows import (
    edit_operations,
    gates,
    observations,
    result_contract,
)

FIXTURES = gates.STATE / "fixtures"
VERSION = 2
"""Self-contained fixture format; independent of the observation storage format."""


def _command(root: Path, *args: str) -> bytes:
    return subprocess.run(args, cwd=root, check=True, capture_output=True).stdout



def _unpack(archive: Path, destination: Path) -> None:
    """Extract only confined files/directories and internal symbolic links."""
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(archive) as source:
        for item in source:
            path = observations.safe_path(destination, item.name)
            if item.isdir():
                path.mkdir(parents=True, exist_ok=True)
            elif item.issym():
                target = (path.parent / item.linkname).resolve()
                if not target.is_relative_to(destination.resolve()):
                    raise ValueError(f"archive link escapes fixture: {item.name}")
                path.parent.mkdir(parents=True, exist_ok=True)
                path.symlink_to(item.linkname)
            elif item.isfile():
                path.parent.mkdir(parents=True, exist_ok=True)
                with source.extractfile(item) as content:
                    path.write_bytes(content.read())
                path.chmod(item.mode & 0o777)
            else:
                raise ValueError(f"unsupported fixture archive member: {item.name}")


def create(root: Path, run_path: str, observation: str, *, substitute_executor: bool = False,
           repairs: dict[str, str] | None = None) -> Path:
    run = observations.safe_path(root, run_path)
    source_root = root
    if (run / "trial.json").exists():
        source_root = run / "tree"
        run = source_root / gates.RUNS / "trial"
    directory = observations.find(run / "artifact", observation)
    record = observations.load(directory)
    if record.get("version") not in observations.READ_VERSIONS:
        raise ValueError("fixture needs a supported retained observation")
    if record.get("library-policy") != observations.LIBRARY_POLICY:
        raise ValueError("observation uses an unsupported library inventory policy; start a new observation, "
                         "do not reinterpret its historical library digest")
    request = record["request"]
    head = record.get("kb-commit")
    if not head:
        raise ValueError("observation has no recoverable KB commit")
    if not substitute_executor:
        raise ValueError("supply --substitute-current-executor to retain a new baseline using the current executable")
    repairs = repairs or {}
    if set(repairs) - set(record["content-state"]):
        raise ValueError("repair names content not declared by the observation")
    captured = observations.read_inputs(directory, record)
    originals = {}
    for item in record["inputs"]:
        data = captured[item["path"]]
        if observations.sha(data) != item["sha256"]:
            raise ValueError(f"retained input hash mismatch: {item['path']}")
        captured[item["path"]] = data
        if item["role"] in ("target", "criterion", "operational"):
            originals[item["origin"]] = data
    overlays = {}
    for name, state in record["content-state"].items():
        if state["kind"] != "file":
            continue
        supplied = observations.safe_path(root, repairs[name]).read_bytes() if name in repairs else None
        if name not in repairs:
            path = observations.safe_path(source_root, name)
            if path.is_file():
                supplied = path.read_bytes()
            captured_value = originals.get(name)
            if captured_value is not None and observations.sha(captured_value) == state["sha256"]:
                supplied = captured_value
        if supplied is None or observations.sha(supplied) != state["sha256"]:
            raise ValueError(f"historical dirty content unavailable: {name}; supply exact bytes with --repair")
        overlays[name] = supplied
    library = library_root().resolve() if source_root == root else Path(record["library-root"]).resolve()
    if source_root != root and not library.is_relative_to(source_root.resolve()):
        raise ValueError("trial library is outside its retained tree")
    local_library = library == (source_root / "kb").resolve()
    library_bytes = {name: (library / name).read_bytes() for name in observations.library_files(library)}
    library_hash = lambda: observations.sha(json.dumps(
        {name: observations.sha(value) for name, value in library_bytes.items()}, sort_keys=True).encode())
    if library_hash() != record["library-sha256"]:
        for origin, data in originals.items():
            relative = origin.removeprefix("commonplace:") if not local_library else origin.removeprefix("kb/")
            if relative not in library_bytes:
                continue
            if (origin.startswith("commonplace:") and not local_library) or (origin.startswith("kb/") and local_library):
                library_bytes[relative] = data
        for name, data in overlays.items():
            if local_library and name.startswith("kb/") and name.removeprefix("kb/") in library_bytes:
                library_bytes[name.removeprefix("kb/")] = data
        if library_hash() != record["library-sha256"]:
            raise ValueError("historical library content unavailable; restore the recorded library before fixture creation")
    fixture = root / FIXTURES / f"{observation}-{uuid.uuid4().hex[:12]}"
    fixture.mkdir(parents=True, exist_ok=False)
    (fixture / "kb.tar").write_bytes(_command(source_root, "git", "archive", "--format=tar", head))
    for name, data in {**captured, **{f"overlays/{name}": data for name, data in overlays.items()}}.items():
        target = observations.safe_path(fixture, name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    package = Path(__file__).resolve().parents[2]
    code = observations.code_files()
    with tarfile.open(fixture / "executor.tar", "w") as archive:
        for name in code:
            archive.add(package / name, arcname=name, recursive=False)
    with tarfile.open(fixture / "library.tar", "w") as archive:
        for name, data in library_bytes.items():
            info = tarfile.TarInfo(name)
            info.size = len(data)
            info.mode = 0o644
            archive.addfile(info, io.BytesIO(data))
    data = {"version": VERSION, "source-observation": str(directory.relative_to(root)),
            "kb-commit": head, "request": request,
            "inputs": [{key: value for key, value in item.items() if key != "input"} for item in record["inputs"]],
            "code": code, "source-executor": observations.executor_record(directory, record),
            "packages": observations.package_versions(),
            "content-state": record["content-state"], "library-sha256": record["library-sha256"],
            "library-policy": observations.LIBRARY_POLICY,
            "library": "kb" if local_library else ".fixture-library",
            "profile": request["profile"], "substitutions": ["current executable", "pair grouping, one worker"],
            "gaps": ["dependency artifacts and user-level harness configuration not pinned",
                     "effective tool/MCP availability must be inspected after each launch",
                     "Git history omitted; tree content reconstructed from archive",
                     "ignored source snapshots included only when explicitly supplied as inputs"],
            "files": {p.relative_to(fixture).as_posix(): observations.sha(p.read_bytes())
                      for p in sorted(fixture.rglob("*")) if p.is_file()}}
    observations.atomic_json(fixture / "fixture.json", data)
    return fixture


def load(root: Path, name: str) -> tuple[Path, dict]:
    fixture = observations.safe_path(root, name)
    data = json.loads((fixture / "fixture.json").read_bytes())
    if data.get("version") != VERSION:
        raise ValueError("unsupported fixture version")
    if data.get("library-policy") != observations.LIBRARY_POLICY:
        raise ValueError("unsupported fixture library inventory policy; create a new baseline")
    for path, digest in data["files"].items():
        if observations.sha(observations.safe_path(fixture, path).read_bytes()) != digest:
            raise ValueError(f"fixture content changed: {path}")
    if observations.code_files() != data["code"] or observations.package_versions() != data["packages"]:
        raise ValueError("executable source or package versions differ from fixture baseline; create a separately identified baseline")
    return fixture, data


def trial(root: Path, fixture_name: str, run_dir: Path, *, harnesses=HARNESSES, family: str = "reviews") -> dict:
    """Rerun the fixture's observation in a new tree; `family` names the command's kind, reviews or edits."""
    fixture, data = load(root, fixture_name)
    if (data["request"]["kind"] == edit_operations.KIND) != (family == edit_operations.FAMILY):
        raise ValueError("the fixture holds an edit execution; use `commonplace-revise try --fixture`"
                         if family != edit_operations.FAMILY else
                         "the fixture holds a review; use `commonplace-review --fixture`")
    if data["profile"]["harness"] not in harnesses:
        raise ValueError("fixture harness is unavailable")
    if harnesses is HARNESSES and data["profile"]["harness"] != "claude-code":
        raise ValueError("fixture trials currently support the Claude Code adapter only")
    tree = run_dir / "tree"
    receipt = run_dir / "trial.json"
    identity = observations.sha((fixture / "fixture.json").read_bytes())
    if receipt.exists():
        previous = json.loads(receipt.read_bytes())
        if previous["fixture-sha256"] != identity:
            raise ValueError("resume names another fixture")
    else:
        if tree.exists():
            raise ValueError("incomplete trial preparation; preserve it and start a new trial")
        _unpack(fixture / "kb.tar", tree)
        for name, state in data["content-state"].items():
            path = observations.safe_path(tree, name)
            if path.is_symlink() or state["kind"] in ("deleted", "symlink"):
                path.unlink(missing_ok=True)
            if state["kind"] == "file":
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(observations.safe_path(fixture / "overlays", name).read_bytes())
            elif state["kind"] == "symlink":
                if not (path.parent / state["target"]).resolve().is_relative_to(tree.resolve()):
                    raise ValueError(f"overlay symlink escapes trial: {name}")
                path.parent.mkdir(parents=True, exist_ok=True)
                path.symlink_to(state["target"])
        if (fixture / "library.tar").exists():
            _unpack(fixture / "library.tar", tree / data["library"])
        reconstructed = observations.library_files(tree / data["library"], use_git=False)
        if observations.sha(json.dumps(reconstructed, sort_keys=True).encode()) != data["library-sha256"]:
            raise ValueError("reconstructed library differs from the recorded baseline")
        for item in data["inputs"]:
            if item["role"] == "target" or (item["role"] == "criterion" and not item["origin"].startswith("commonplace:")):
                target = observations.safe_path(tree, item["origin"])
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(observations.safe_path(fixture, item["path"]).read_bytes())
            elif item["role"] == "contract":
                base = tree / ("kb" if Path(item["origin"]).name == "COLLECTION.md" else data["library"])
                target = observations.safe_path(base, item["origin"])
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(observations.safe_path(fixture, item["path"]).read_bytes())
        _command(tree, "git", "init", "-q")
        _command(tree, "git", "-c", "user.name=Fixture", "-c", "user.email=fixture@localhost", "add", ".")
        # A tracked library file may match an ignore rule; an installed library
        # may itself live under a hidden directory. Preserve the exact selected
        # inventory when this independent tree becomes a Git checkout.
        if reconstructed:
            subprocess.run(["git", "add", "-f", "--pathspec-from-file=-", "--pathspec-file-nul"], cwd=tree,
                           input=b"".join(os.fsencode(str(Path(data["library"]) / name)) + b"\0"
                                          for name in reconstructed), capture_output=True, check=True)
        _command(tree, "git", "-c", "user.name=Fixture", "-c", "user.email=fixture@localhost",
                 "-c", "commit.gpgsign=false", "-c", f"core.hooksPath={tree / '.git/no-hooks'}",
                 "commit", "-qm", "Fixture baseline")
        observations.atomic_json(receipt, {"fixture": fixture.relative_to(root).as_posix(),
                                           "fixture-sha256": identity, "gaps": data["gaps"],
                                           "tree-state": gates.checkout_state(tree)})
    request = data["request"]
    # Keep the original criterion identity; supply its captured bytes directly.
    criterion = next(item for item in data["inputs"] if item["role"] == "criterion")
    pair = gates.Pair(request["note"], request["criterion"], request["kind"], request["criterion-id"])
    profile = Profile(**data["profile"])
    profile = replace(profile, flags={**profile.flags, "_env": {
        **harnesses[profile.harness].defaults.get("_env", {}), **profile.flags.get("_env", {}),
        "COMMONPLACE_LIBRARY_ROOT": str(tree / data["library"])}})
    trial_run = tree / gates.RUNS / "trial"
    trial_run.mkdir(parents=True, exist_ok=True)
    contracts = {item["origin"]: observations.safe_path(fixture, item["path"]).read_bytes()
                 for item in data["inputs"] if item["role"] == "contract"}
    from commonplace.headless.jobs import Run
    before = gates.checkout_state(tree)
    if before != json.loads(receipt.read_bytes())["tree-state"]:
        raise ValueError("trial tree changed; restore its baseline before resuming, or start a new trial")
    operational = {Path(item["path"]).stem: {
        "origin": item["origin"], "text": observations.safe_path(fixture, item["path"]).read_bytes().decode("utf-8")}
        for item in data["inputs"] if item["role"] == "operational"}
    with Run(trial_run, tree, profile, timeout=request["timeout"], harnesses=harnesses, max_workers=1) as run:
        run.library_root = tree / data["library"]
        if family == edit_operations.FAMILY:
            reports, stopped = _edit(run, tree, data, fixture, criterion, contracts, operational)
        else:
            reports, stopped = _review(run, tree, pair, fixture, criterion, contracts, operational)
    result = {"run-dir": run_dir.relative_to(root).as_posix(), "fixture-sha256": identity,
              "evidence-root": tree.relative_to(root).as_posix(),
              "stopped": stopped, "observations": reports,
              "changed": gates.changed_paths(before, gates.checkout_state(tree)),
              "gaps": data["gaps"], "effective-configuration": "unassessed"}
    observations.atomic_json(run_dir / "trial-result.json", result)
    return result


def _review(run, tree: Path, pair, fixture: Path, criterion: dict, contracts: dict, operational: dict):
    reports, stopped = gates.ask(run, tree, [pair], {pair.note: (tree / pair.note).read_bytes().decode("utf-8")},
                                max_workers=1, captured_criteria={pair.criterion: observations.safe_path(
                                    fixture, criterion["path"]).read_bytes().decode("utf-8")}, contracts=contracts,
                                operational_inputs=operational)
    return [{**asdict(report), "result": None} for report in reports], stopped


def _edit(run, tree: Path, data: dict, fixture: Path, criterion: dict, contracts: dict, operational: dict):
    """Rerun one edit execution from its captured operation, text, inputs and contract."""
    request = data["request"]
    target = next(item for item in data["inputs"] if item["role"] == "target")
    operation = edit_operations.parse(
        request["criterion"], observations.safe_path(fixture, criterion["path"]).read_bytes().decode("utf-8"))
    execution = (tree / data["library"] / edit_operations.EXECUTION_REL).read_text(encoding="utf-8")
    report = {"note": request["note"], "operation": request["criterion"], "job": request["call-job"],
              "state": "not-run", "outcome": None, "problem": None}
    stopped = None
    try:
        edit = edit_operations.ask(run, tree, operation, request["note"],
                                   observations.safe_path(fixture, target["path"]).read_bytes().decode("utf-8"),
                                   operational, job=request["call-job"], contracts=contracts, execution=execution)
        report.update({"state": "edited", "outcome": edit.outcome})
    except NoProgress as spent:
        report.update({"state": "no-progress", "problem": str(spent)})
    except OutOfAttempts as spent:
        report.update({"state": "out-of-attempts", "problem": str(spent)})
    except result_contract.ControllerError as error:
        report.update({"state": "controller-error", "problem": str(error)})
        stopped = str(error)
    except LaunchFailed as failure:
        report["state"], stopped = "stopped", str(failure)
    return [report], stopped

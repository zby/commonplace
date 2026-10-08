"""Prepare a commit-bound Commonplace worktree and its command environment."""

from __future__ import annotations

import datetime
import json
import os
import re
import subprocess
import tomllib
import uuid
from hashlib import sha256
from pathlib import Path

from commonplace.lib.agentic_analysis.sets import (
    ARCHIVE_ROOT,
    RETAINED_ROOT,
    normalize_source_identity,
    source_slug,
)
from commonplace.lib.note_parser import parse_document

STATE_ROOT = Path("kb/agentic-system-analyses/state")

STARTUP_DIRECTORIES = (
    ".agents/skills", ".claude/skills", ".claude/agents", ".claude/hooks",
    ".codex/skills", ".codex/agents", ".pi/skills", ".pi/agents",
    ".pi/extensions", ".pi/prompts", ".cursor/rules",
)
STARTUP_FILES = {
    ".claude/settings.json", ".claude/settings.local.json", ".codex/config.toml",
    ".pi/settings.json", ".pi/SYSTEM.md", ".pi/APPEND_SYSTEM.md",
}
STARTUP_FILENAMES = {
    "AGENTS.md", "AGENTS.MD", "AGENTS.override.md", "CLAUDE.md", "CLAUDE.MD",
    "GEMINI.md", ".cursorrules",
}


def _git_paths(origin: Path, args: list[str]) -> set[str]:
    result = subprocess.run(
        ["git", *args], cwd=origin, capture_output=True, text=True, check=False
    )
    if result.returncode:
        raise ValueError(f"could not inspect startup files: {result.stderr.strip()}")
    return set(filter(None, result.stdout.split("\0")))


def require_committed_startup(origin: Path, commit: str) -> None:
    """The dirty-origin exception never permits different startup instructions.

    Inspect index and working tree independently (their changes can cancel),
    plus untracked and ignored startup files, except ignored local harness
    settings. Skill links also protect their
    repository-local targets, where the actual instruction bytes live.
    """
    protected = {origin / path for path in (*STARTUP_DIRECTORIES, *STARTUP_FILES)}
    for directory in STARTUP_DIRECTORIES:
        skills = origin / directory
        if skills.name == "skills" and skills.is_dir():
            for skill in skills.iterdir():
                if skill.is_symlink():
                    target = skill.resolve()
                    if target.is_relative_to(origin):
                        protected.add(target)
    paths: set[str] = set()
    ignored_startup = sorted({
        *STARTUP_FILENAMES,
        *(path.relative_to(origin).as_posix() for path in protected),
    })
    for args in (
        ["diff", "--name-only", "--no-renames", "-z", commit, "HEAD"],
        ["diff", "--cached", "--name-only", "--no-renames", "-z"],
        ["diff", "--name-only", "--no-renames", "-z"],
        ["ls-files", "--others", "--exclude-standard", "-z"],
    ):
        paths.update(_git_paths(origin, args))
    # An ignored `settings.local.json` holds one user's harness permissions.
    # No commit can contain it, so requiring a match would stop every checkout
    # where that harness has run. Tracked or unignored copies stay checked.
    paths.update(
        name for name in _git_paths(origin, [
            "ls-files", "--others", "--ignored", "--exclude-standard", "-z", "--",
            *ignored_startup,
        ])
        if Path(name).name != "settings.local.json"
    )
    changed = sorted(
        name for name in paths
        if Path(name).name in STARTUP_FILENAMES
        or any((origin / name).is_relative_to(path) for path in protected)
    )
    if changed:
        raise ValueError(
            "startup instructions or configuration differ from the selected commit: "
            + ", ".join(changed)
            + "; commit or remove these changes first; --allow-dirty-origin does not bypass this check"
        )


def _run(args: list[str], *, cwd: Path, env: dict[str, str] | None = None) -> str:
    try:
        result = subprocess.run(args, cwd=cwd, env=env, capture_output=True, text=True, check=False)
    except OSError as error:
        raise ValueError(f"could not run {args[0]}: {error}") from error
    if result.returncode:
        raise ValueError(
            f"{args[0]} failed (exit {result.returncode}): "
            f"{result.stderr.strip() or result.stdout.strip()}"
        )
    return result.stdout.strip()


def command_environment(worktree: Path) -> dict[str, str]:
    """Use local commands; inherited Python overrides must not select another tree."""
    env = dict(os.environ)
    for key in ("PYTHONPATH", "PYTHONHOME", "UV_WORKING_DIR"):
        env.pop(key, None)
    environment = worktree / ".venv"
    bin_dir = environment / ("Scripts" if os.name == "nt" else "bin")
    env["PATH"] = str(bin_dir) + os.pathsep + env.get("PATH", "")
    env["VIRTUAL_ENV"] = str(environment)
    env["UV_PROJECT_ENVIRONMENT"] = str(environment)
    return env


def _install(worktree: Path) -> dict[str, str]:
    env = command_environment(worktree)
    _run(
        ["uv", "sync", "--frozen", "--no-dev", "--project", str(worktree)],
        cwd=worktree,
        env=env,
    )
    bin_dir = worktree / ".venv" / ("Scripts" if os.name == "nt" else "bin")
    python = bin_dir / ("python.exe" if os.name == "nt" else "python3")
    # Test both package binding and executable discovery in the environment that
    # will be inherited by the harness and its child processes.
    probe = _run(
        [str(python), "-c", (
            "import json, shutil; import commonplace.workflow.engine as m; "
            "print(json.dumps({'module': m.__file__, "
            "'workflow': shutil.which('commonplace-workflow'), "
            "'run': shutil.which('commonplace-run'), "
            "'validate': shutil.which('commonplace-validate')}))"
        )],
        cwd=worktree,
        env=env,
    )
    try:
        found = json.loads(probe)
        expected = worktree / RUNTIME_MARKER
        if Path(found["module"]).resolve() != expected.resolve():
            raise ValueError("the installed package resolves outside the analysis worktree")
        for key in ("workflow", "run", "validate"):
            # Resolve the directory, not the executable: uv may use symlinks.
            if not found[key] or Path(found[key]).parent.resolve() != bin_dir.resolve():
                raise ValueError(f"{key} command resolves outside the local environment")
    except (KeyError, TypeError, json.JSONDecodeError) as error:
        raise ValueError("could not verify the analysis command environment") from error
    return {"python": str(python), "path-prefix": str(bin_dir)}


RUNTIME_MARKER = "src/commonplace/workflow/engine.py"


def source_checkout(path: Path) -> Path | None:
    """The nearest Commonplace source checkout containing ``path``, if any."""
    path = path.resolve()
    for directory in (path, *path.parents):
        if (directory / RUNTIME_MARKER).is_file():
            return directory
    return None


def require_run_code(run: Path, *, cwd: Path | None = None) -> None:
    """Refuse a command whose code is not the run's own checkout's.

    A run inside a Commonplace source checkout pins that checkout's method.
    The shared editable installation runs another checkout's code, so a
    worker that drops the local command directory would silently mix methods.
    Runs outside a source checkout (consuming projects) are not bound.
    """
    checkout = source_checkout(run)
    if checkout is None:
        return
    import commonplace

    loaded = Path(commonplace.__file__).resolve().parents[2]
    bin_dir = checkout / ".venv" / ("Scripts" if os.name == "nt" else "bin")
    repair = (
        f"run it from {checkout}, calling the command in {bin_dir}/"
        if bin_dir.is_dir() else f"run it from {checkout} with that checkout's commands"
    )
    if loaded != checkout:
        raise ValueError(
            f"this run belongs to the checkout {checkout}, but this command "
            f"runs code from {loaded}; {repair}"
        )
    if cwd is not None and source_checkout(cwd) != checkout:
        raise ValueError(
            f"this run belongs to the checkout {checkout}, but the working "
            f"directory is {cwd}; {repair}"
        )


def _require_current_revision(origin: Path, commit: str) -> None:
    """An implicit HEAD behind the default branch is a stale launching checkout."""
    for branch in ("main", "master"):
        ref = f"refs/heads/{branch}"
        if subprocess.run(
            ["git", "rev-parse", "--verify", "--quiet", ref],
            cwd=origin, capture_output=True, check=False,
        ).returncode:
            continue
        behind = int(_run(["git", "rev-list", "--count", f"{commit}..{ref}"], cwd=origin))
        ahead = int(_run(["git", "rev-list", "--count", f"{ref}..{commit}"], cwd=origin))
        if behind and not ahead:
            raise ValueError(
                f"HEAD is {behind} commits behind {branch}: this checkout and the "
                "session started in it hold an older method; start from the "
                f"current {branch}, or pass --revision to select this revision deliberately"
            )
        return


def prepare_analysis(
    origin: Path,
    *,
    name: str,
    allow_dirty_origin: bool = False,
    revision: str | None = None,
    worktree: Path | None = None,
) -> dict[str, object]:
    """Create a new worktree, never copy dirty bytes, and retain setup evidence.

    Failed installation leaves the worktree for diagnosis. No analysis is opened
    or advanced, and no existing worktree is reused or removed.
    """
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
        raise ValueError("name must contain lowercase letters, digits and hyphens")
    origin = Path(_run(["git", "rev-parse", "--show-toplevel"], cwd=origin)).resolve()
    commit = _run(
        ["git", "rev-parse", "--verify", "--end-of-options", f"{revision or 'HEAD'}^{{commit}}"],
        cwd=origin,
    )
    if revision is None:
        _require_current_revision(origin, commit)
    require_committed_startup(origin, commit)
    dirty = bool(_run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=origin))
    if dirty and not allow_dirty_origin:
        raise ValueError(
            "origin has uncommitted changes; commit them or use --allow-dirty-origin "
            "to exclude them from the analysis"
        )
    try:
        project = tomllib.loads(_run(["git", "show", f"{commit}:pyproject.toml"], cwd=origin))
        if project.get("project", {}).get("name") != "llm-commonplace":
            raise ValueError("not the Commonplace source project")
        _run(["git", "cat-file", "-e", f"{commit}:uv.lock"], cwd=origin)
        _run(["git", "cat-file", "-e", f"{commit}:{RUNTIME_MARKER}"], cwd=origin)
        _run(["git", "cat-file", "-e", f"{commit}:AGENTS.md"], cwd=origin)
    except (ValueError, tomllib.TOMLDecodeError) as error:
        raise ValueError(f"analysis preparation requires a committed Commonplace source checkout: {error}") from error

    token = uuid.uuid4().hex[:12]
    if worktree is None:
        worktree = origin / ".commonplace/worktrees" / f"{name}-{token}"
    elif not worktree.is_absolute():
        worktree = origin / worktree
    # Do not accept an existing empty directory or a dangling symlink either.
    if worktree.exists() or worktree.is_symlink():
        raise ValueError(f"worktree destination already exists: {worktree}")
    worktree = worktree.resolve()
    record_path = worktree.with_name(worktree.name + ".preparation.json")
    if record_path.exists() or record_path.is_symlink():
        raise ValueError(f"preparation record already exists: {record_path}")
    if worktree.is_relative_to(origin):
        for path in (worktree, record_path):
            ignored = subprocess.run(
                ["git", "check-ignore", "--quiet", str(path)], cwd=origin, check=False
            )
            if ignored.returncode:
                raise ValueError("a worktree and its record inside the origin must be under an ignored directory")
    worktree.parent.mkdir(parents=True, exist_ok=True)
    _run(["git", "worktree", "add", "--detach", str(worktree), commit], cwd=origin)
    record: dict[str, object] = {
        "format": 1,
        "token": token,
        "origin": str(origin),
        "worktree": str(worktree),
        "commit": commit,
        "origin-dirty": dirty,
        "uncommitted-changes-excluded": dirty,
        "prepared-at": datetime.datetime.now(datetime.UTC).isoformat(),
        "record": str(record_path),
        "status": "installing",
        "agents-md": str(worktree / "AGENTS.md"),
        "agents-md-sha256": sha256((worktree / "AGENTS.md").read_bytes()).hexdigest(),
    }
    record_path.write_text(json.dumps(record, indent=2) + "\n")
    try:
        if Path(_run(["git", "rev-parse", "--show-toplevel"], cwd=worktree)).resolve() != worktree:
            raise ValueError("Git does not recognize the analysis worktree as its own root")
        record.update(_install(worktree))
        if _run(["git", "rev-parse", "HEAD"], cwd=worktree) != commit:
            raise ValueError("the analysis worktree commit changed during setup")
        if _run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=worktree):
            raise ValueError("the new analysis worktree is not clean")
        require_committed_startup(origin, commit)
        record["status"] = "ready"
    except ValueError as error:
        record.update(status="failed", error=str(error))
        record_path.write_text(json.dumps(record, indent=2) + "\n")
        raise ValueError(f"analysis setup failed in {worktree}; retained {record_path}: {error}") from error
    record_path.write_text(json.dumps(record, indent=2) + "\n")
    return record


def preparation_for(worktree: Path, *, require_token: bool = True) -> dict[str, object]:
    """Read a ready record bound to this exact worktree."""
    worktree = Path(worktree).resolve()
    record_path = worktree.with_name(worktree.name + ".preparation.json")
    try:
        record = json.loads(record_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"ready analysis preparation record required: {record_path}") from error
    if not isinstance(record, dict) or record.get("status") != "ready" or record.get("worktree") != str(worktree):
        raise ValueError(f"preparation record does not name a ready worktree: {record_path}")
    token = record.get("token")
    if require_token and (not isinstance(token, str) or re.fullmatch(r"[0-9a-f]{12}", token) is None):
        raise ValueError(f"preparation record has no valid worktree token: {record_path}")
    return record


def reject_legacy_run(run: Path) -> None:
    """Never reinterpret legacy or mixed state as a generic engine run."""
    legacy = [name for name in ("workflow-state", "output", "opening.json", "run-state.md")
              if os.path.lexists(run / name)]
    if legacy:
        raise ValueError("legacy/mixed run directories are retired; start a new run: " + ", ".join(legacy))


def start_analysis(worktree: Path, *, system: str, source_identity: str,
                   source: str, source_revision: str | None = None) -> Path:
    """Allocate a prepared analysis and pin its declaration, without advancing."""
    from commonplace.lib.agentic_analysis.checkout import github_checkout_path
    from commonplace.lib.agentic_analysis.declaration import JOB_SET
    from commonplace.workflow import start_run

    worktree = worktree.resolve()
    preparation = preparation_for(worktree)
    require_run_code(worktree, cwd=Path.cwd())
    for label, value in (("system", system), ("source-identity", source_identity), ("source", source)):
        if not value.strip() or "\n" in value or "\r" in value:
            raise ValueError(f"{label} must be a nonempty single-line value")
    identity = normalize_source_identity(source_identity.strip())
    if not identity:
        raise ValueError("source-identity normalizes to an empty identity")
    if source_revision is not None and (re.fullmatch(r"[0-9a-f]{40}", source_revision) is None
                                       or github_checkout_path(identity) is None):
        raise ValueError("source-revision requires a full 40-hex commit and GitHub repository identity")
    if _run(["git", "rev-parse", "HEAD"], cwd=worktree) != preparation["commit"]:
        raise ValueError("worktree HEAD differs from its preparation commit")
    require_committed_startup(worktree, str(preparation["commit"]))
    slug = source_slug(identity, system)
    date = datetime.datetime.now(datetime.UTC).date().isoformat()
    prefix = f"AAS-{date}-{slug}-{preparation['token']}"
    parameters = {"system": system, "source-identity": identity, "source": source}
    if source_revision is not None:
        parameters["source-revision"] = source_revision
    root = worktree / STATE_ROOT
    root.mkdir(parents=True, exist_ok=True)
    for number in range(1, 100):
        run = root / f"{prefix}-{number:02d}"
        try:
            run.mkdir()  # Atomic allocation: never reuse another run's state.
        except FileExistsError:
            continue
        start_run(run, worktree / "kb" / JOB_SET, parameters=parameters)
        return run
    raise ValueError("analysis run sequence exhausted for this source and worktree")


def _frontmatter(text: str, path: Path) -> dict[str, object]:
    document, error = parse_document(text)
    if error or document is None or not isinstance(document.frontmatter, dict):
        raise ValueError(f"cannot read frontmatter in {path}: {error}")
    return document.frontmatter


def _changed_paths(worktree: Path, *args: str) -> list[str]:
    """Keep NUL-delimited Git paths intact, including leading whitespace."""
    result = subprocess.run(
        ["git", "diff", "--no-renames", "--name-only", "-z", *args],
        cwd=worktree, capture_output=True, check=False,
    )
    if result.returncode:
        raise ValueError(f"could not inspect changed paths: {result.stderr.decode(errors='replace').strip()}")
    return [os.fsdecode(path) for path in result.stdout.split(b"\0") if path]


def _integration_publication(run_dir: Path, worktree: Path, method: str) -> tuple[list[str], str]:
    """Prove current engine completion AND exact publication, without recovery writes.

    Caller holds the run and publication locks. A journal label is not proof.
    Reuse publication's pure preparation checks, never its effect recognizer.
    """
    from commonplace.lib.agentic_analysis.declaration import JOB_SET
    from commonplace.lib.agentic_analysis.publication import (
        JOURNAL,
        _hashes,
        _prepare_publication,
        _tree,
    )
    from commonplace.workflow.state import CodeAttempt, Run
    from commonplace.workflow.store import RunStore

    store = RunStore(run_dir)
    metadata = store.read_metadata()
    if (metadata["declaration"] != (worktree / "kb" / JOB_SET).read_text(encoding="utf-8")
            or Path(metadata["job_set"]) != worktree / "kb" / JOB_SET):
        raise ValueError("integration requires the fixed shipped analysis job set")
    if metadata["type"] != (worktree / "kb" / metadata["type_spec"]).read_text(encoding="utf-8"):
        raise ValueError("integration requires the unchanged shipped set type")
    run = Run(store)
    publication = run.jobs.job("publish")
    if publication.handler != "commonplace.lib.agentic_analysis.publication.publish_analysis":
        raise ValueError("integration requires the shipped publication handler")
    completed = run.latest_completed("publish")
    if completed is None or not run.publishable():
        raise ValueError("integration requires engine publication completion and current coverage")
    for job in run.jobs.jobs:
        records = [r for r in run.attempts.values() if r["job"] == job.name]
        latest = max(records, key=lambda r: r["seq"], default=None)
        if (latest is not None and latest["state"] != "completed") or run.ready(job, run.permitted()):
            raise ValueError("integration refuses open, failed, uncertain or stale engine results")
    pins = {name: run.resolve(name, publication.inputs) for name in publication.inputs}
    if ({name: pin.pin() for name, pin in pins.items()} != completed["pins"]):
        raise ValueError("publication completion inputs have changed")
    for pin in pins.values():
        if pin.data is not None and sha256(pin.data).hexdigest() != pin.version:
            raise ValueError("publication input bytes differ from their engine version")
    prepared = _prepare_publication(CodeAttempt(run, publication, pins))
    if prepared is None:
        raise ValueError("integration requires a published complete disposition, not a local result")
    opened, repo, destination, files = prepared
    if repo != worktree or opened["run-id"] != run_dir.name or opened["inputs-commit"] != method:
        raise ValueError("publication does not pin this run and method")
    if any(opened.get(name) != run.parameters.get(name) for name in
           ("system", "source-identity", "source", "source-revision")):
        raise ValueError("publication source and system pins differ from run parameters")
    overview = _frontmatter(files["overview.md"].decode("utf-8"), destination / "overview.md")
    if (overview.get("run-id") != run_dir.name or overview.get("inputs-commit") != method
            or overview.get("result-disposition") != "complete"
            or not isinstance(overview.get("reviewed-boundary"), str)
            or not overview["reviewed-boundary"]):
        raise ValueError("published overview has mismatched run, method, disposition or source pins")
    journal_path = run_dir / JOURNAL
    if journal_path.resolve() != journal_path:
        raise ValueError("publication journal redirects")
    journal = json.loads(journal_path.read_bytes())
    intent = {"version": 1, "run-id": run_dir.name, "destination": str(destination),
              "source-identity": opened["source-identity"],
              "expected": opened["expected-incumbent-sha256"], "new": _hashes(files)}
    if (not isinstance(journal, dict) or set(journal) != {*intent, "old", "archive", "state"}
            or any(journal.get(k) != v for k, v in intent.items())
            or journal["state"] != "completed" or _tree(destination) != files):
        raise ValueError("publication journal or exact retained bytes differ from completed inputs")
    relative = destination.relative_to(worktree)
    if relative.parent != RETAINED_ROOT:
        raise ValueError("publication destination is outside retained sets")
    paths = [relative.as_posix()]
    # Compare the archive to Git's entire incumbent tree, not only its overview.
    old_names = _run(["git", "ls-tree", "--name-only", f"{method}:{relative.as_posix()}"], cwd=worktree) if subprocess.run(
        ["git", "cat-file", "-e", f"{method}:{relative.as_posix()}"], cwd=worktree,
        capture_output=True, check=False,
    ).returncode == 0 else ""
    old = None
    if old_names:
        old = {}
        for name in old_names.splitlines():
            if Path(name).name != name:
                raise ValueError("incumbent contains non-direct members")
            result = subprocess.run(["git", "show", f"{method}:{relative.as_posix()}/{name}"],
                                    cwd=worktree, capture_output=True, check=True)
            old[name] = result.stdout
    if journal["old"] != _hashes(old):
        raise ValueError("journal incumbent differs from the method commit's exact tree")
    expected = "absent" if old is None else sha256(old["overview.md"]).hexdigest()
    if intent["expected"] != expected:
        raise ValueError("opened incumbent differs from method commit")
    if old is None:
        if journal["archive"] is not None:
            raise ValueError("unexpected publication archive")
    else:
        old_id = _frontmatter(old["overview.md"].decode("utf-8"), relative / "overview.md").get("run-id")
        if not isinstance(old_id, str) or re.fullmatch(r"AAS-[a-zA-Z0-9-]+", old_id) is None:
            raise ValueError("incumbent has an invalid run ID")
        archive = worktree / ARCHIVE_ROOT / old_id
        if journal["archive"] != str(archive) or _tree(archive) != old:
            raise ValueError("publication archive is missing or differs from the exact incumbent")
        paths.append(archive.relative_to(worktree).as_posix())
    return paths, overview["reviewed-boundary"]


def integrate_analysis(run_dir: Path, *, model: str | None = None) -> str:
    """Authorize Git integration while serializing cooperating run/publisher mutations."""
    from commonplace.lib.agentic_analysis.guards import publication_lock
    from commonplace.workflow.store import RunStore

    run_dir = Path(run_dir).absolute()
    if run_dir.resolve() != run_dir:
        raise ValueError("analysis run must not traverse symlinks")
    reject_legacy_run(run_dir)
    if not (run_dir / "run.json").is_file():
        raise ValueError("integration requires a new-engine run.json")
    if (run_dir.parent.name != STATE_ROOT.name
            or len(run_dir.parents) <= len(STATE_ROOT.parts)):
        raise ValueError(f"analysis run must be directly under {STATE_ROOT}")
    worktree = run_dir.parents[len(STATE_ROOT.parts)]
    if worktree / STATE_ROOT != run_dir.parent:
        raise ValueError(f"analysis run must be directly under {STATE_ROOT}")
    require_run_code(run_dir, cwd=Path.cwd())
    with RunStore(run_dir).lock(), publication_lock(worktree):
        return _integrate_analysis(run_dir, model=model)


def _integrate_analysis(run_dir: Path, *, model: str | None = None) -> str:
    """Commit one completed publication in its worktree and merge it into main.

    Calling this is the separate authorization to transfer a published run.
    A conflict is aborted in main; its publication branch remains for review.
    """
    run_dir = Path(run_dir).resolve()
    if (run_dir.parent.name != STATE_ROOT.name
            or len(run_dir.parents) <= len(STATE_ROOT.parts)):
        raise ValueError(f"analysis run must be directly under {STATE_ROOT}")
    worktree = run_dir.parents[len(STATE_ROOT.parts)]
    if worktree / STATE_ROOT != run_dir.parent:
        raise ValueError(f"analysis run must be directly under {STATE_ROOT}")
    record = preparation_for(worktree)
    origin = Path(str(record["origin"]))
    if Path(_run(["git", "rev-parse", "--show-toplevel"], cwd=origin)).resolve() != origin:
        raise ValueError("preparation origin is not its current Git root")
    if _run(["git", "symbolic-ref", "--quiet", "HEAD"], cwd=origin) != "refs/heads/main":
        raise ValueError("integration requires the origin checkout on main")
    if _run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=origin):
        raise ValueError("integration requires a clean origin checkout")
    method = str(record["commit"])
    if _run(["git", "rev-parse", "HEAD"], cwd=worktree) != method:
        raise ValueError("worktree HEAD differs from its preparation commit")
    require_committed_startup(worktree, method)
    if subprocess.run(["git", "merge-base", "--is-ancestor", method, "main"], cwd=origin, check=False).returncode:
        raise ValueError("the method commit is not an ancestor of main")

    run_id = run_dir.name
    token = str(record["token"])
    if re.fullmatch(rf"AAS-\d{{4}}-\d{{2}}-\d{{2}}-[a-z0-9-]+-{token}-\d{{2}}", run_id) is None:
        raise ValueError("run ID does not match the worktree preparation token")
    paths, source_revision = _integration_publication(run_dir, worktree, method)
    if _changed_paths(origin, method, "HEAD", "--", *paths):
        raise ValueError("origin publication paths changed since the method commit")

    branch = f"analysis/{run_id}"
    if subprocess.run(["git", "show-ref", "--verify", "--quiet", f"refs/heads/{branch}"], cwd=worktree, check=False).returncode == 0:
        raise ValueError(f"publication branch already exists: {branch}")
    staged = _changed_paths(worktree, "--cached")
    if staged:
        raise ValueError("worktree already has staged changes")
    tracked = _changed_paths(worktree, "HEAD")
    outside = [path for path in tracked if not any(path == allowed or path.startswith(allowed + "/") for allowed in paths)]
    if outside:
        raise ValueError("tracked changes outside publication paths: " + ", ".join(outside))

    _run(["git", "switch", "-c", branch], cwd=worktree)
    _run(["git", "add", "--", *paths], cwd=worktree)
    changed = _changed_paths(worktree, "--cached")
    if not changed or any(not any(path == allowed or path.startswith(allowed + "/") for allowed in paths) for path in changed):
        raise ValueError("publication staging is empty or includes another path")
    body = f"Run: {run_id}\nMethod: {method}\nSource: {source_revision}"
    if model:
        body += f"\n\nModel: {model}"
    _run(["git", "commit", "-m", "Publish analysis result", "-m", body], cwd=worktree)
    merge = subprocess.run(["git", "merge", "--no-ff", "--no-edit", branch], cwd=origin, capture_output=True, text=True, check=False)
    if merge.returncode:
        merge_head = Path(_run(["git", "rev-parse", "--git-path", "MERGE_HEAD"], cwd=origin))
        if (origin / merge_head).exists():
            _run(["git", "merge", "--abort"], cwd=origin)
        raise ValueError(f"integration stopped; publication branch kept: {merge.stderr.strip() or merge.stdout.strip()}")
    return _run(["git", "rev-parse", "HEAD"], cwd=origin)

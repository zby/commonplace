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

from commonplace.lib.agentic_set import ARCHIVE_ROOT, RETAINED_ROOT, analysis_layout
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
            "import json, shutil; import commonplace.lib.agentic_workflow as m; "
            "print(json.dumps({'module': m.__file__, "
            "'workflow': shutil.which('commonplace-workflow'), "
            "'validate': shutil.which('commonplace-validate')}))"
        )],
        cwd=worktree,
        env=env,
    )
    try:
        found = json.loads(probe)
        expected = worktree / "src/commonplace/lib/agentic_workflow.py"
        if Path(found["module"]).resolve() != expected.resolve():
            raise ValueError("the installed package resolves outside the analysis worktree")
        for key in ("workflow", "validate"):
            # Resolve the directory, not the executable: uv may use symlinks.
            if not found[key] or Path(found[key]).parent.resolve() != bin_dir.resolve():
                raise ValueError(f"{key} command resolves outside the local environment")
    except (KeyError, TypeError, json.JSONDecodeError) as error:
        raise ValueError("could not verify the analysis command environment") from error
    return {"python": str(python), "path-prefix": str(bin_dir)}


RUNTIME_MARKER = "src/commonplace/lib/agentic_workflow.py"


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
        _run(["git", "cat-file", "-e", f"{commit}:src/commonplace/lib/agentic_workflow.py"], cwd=origin)
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


def integrate_analysis(run_dir: Path, *, model: str | None = None) -> str:
    """Commit one completed publication in its worktree and merge it into main.

    Calling this is the separate authorization to transfer a published run.
    A conflict is aborted in main; its publication branch remains for review.
    """
    run_dir = Path(run_dir).resolve()
    if run_dir.parent.name != STATE_ROOT.name:
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
    method = str(record["commit"])
    if _run(["git", "rev-parse", "HEAD"], cwd=worktree) != method:
        raise ValueError("worktree HEAD differs from its preparation commit")
    if subprocess.run(["git", "merge-base", "--is-ancestor", method, "main"], cwd=origin, check=False).returncode:
        raise ValueError("the method commit is not an ancestor of main")

    run_id = run_dir.name
    token = str(record["token"])
    if re.fullmatch(rf"AAS-\d{{4}}-\d{{2}}-\d{{2}}-[a-z0-9-]+-{token}-\d{{2}}", run_id) is None:
        raise ValueError("run ID does not match the worktree preparation token")
    state_path = run_dir / "run-state.md"
    state = _frontmatter(state_path.read_text(encoding="utf-8"), state_path)
    if state.get("run-id") != run_id or state.get("run-status") != "complete":
        raise ValueError("integration requires this run's complete run-state")
    generated = state.get("generated-review")
    if not isinstance(generated, dict) or not isinstance(generated.get("path"), str):
        raise TypeError("complete run-state has no published overview path")
    overview_rel = Path(generated["path"])
    if (overview_rel.parent.parent != RETAINED_ROOT or overview_rel.name != analysis_layout().path("overview")
            or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", overview_rel.parent.name)):
        raise ValueError("published overview must be under retained/<slug>/")
    overview_path = worktree / overview_rel
    overview = _frontmatter(overview_path.read_text(encoding="utf-8"), overview_path)
    if overview.get("run-id") != run_id or overview.get("inputs-commit") != method:
        raise ValueError("published overview does not pin this run and method commit")
    source_revision = overview.get("reviewed-boundary")
    if not isinstance(source_revision, str) or not source_revision:
        raise ValueError("published overview has no source revision")

    paths = [overview_rel.parent.as_posix()]
    old_location = f"{method}:{overview_rel.as_posix()}"
    if subprocess.run(["git", "cat-file", "-e", old_location], cwd=worktree, capture_output=True, check=False).returncode == 0:
        old = _frontmatter(_run(["git", "show", old_location], cwd=worktree), overview_rel)
        old_id = old.get("run-id")
        if not isinstance(old_id, str) or not re.fullmatch(r"AAS-\d{4}-\d{2}-\d{2}-[a-z0-9-]+-\d{2}", old_id):
            raise ValueError("method commit has an invalid incumbent run ID")
        archive = ARCHIVE_ROOT / old_id
        if not (worktree / archive).is_dir():
            raise ValueError(f"publication archive is missing: {archive}")
        paths.append(archive.as_posix())

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
    _run(["git", "add", "-A", "--", *paths], cwd=worktree)
    changed = _changed_paths(worktree, "--cached")
    if not changed or any(not any(path == allowed or path.startswith(allowed + "/") for allowed in paths) for path in changed):
        raise ValueError("publication staging is empty or includes another path")
    body = f"Run: {run_id}\nMethod: {method}\nSource: {source_revision}"
    if model:
        body += f"\n\nModel: {model}"
    _run(["git", "commit", "-m", "Publish analysis result", "-m", body], cwd=worktree)
    merge = subprocess.run(["git", "merge", "--no-ff", "--no-edit", branch], cwd=origin, capture_output=True, text=True, check=False)
    if merge.returncode:
        if (origin / ".git/MERGE_HEAD").exists():
            _run(["git", "merge", "--abort"], cwd=origin)
        raise ValueError(f"integration stopped; publication branch kept: {merge.stderr.strip() or merge.stdout.strip()}")
    return _run(["git", "rev-parse", "HEAD"], cwd=origin)

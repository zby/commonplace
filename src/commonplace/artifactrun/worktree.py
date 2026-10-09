"""Commit-bound worktrees, the code that runs in them, and transfer back to main.

A run's method is the commit its worktree was prepared at. These checks keep
the running code, the startup instructions and the worktree tied to that
commit, and move a finished result back to ``main`` as one merge.
"""

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


def _git(repo_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            ["git", *args], cwd=repo_root, check=False,
            capture_output=True, text=True, timeout=30,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise ValueError(f"cannot run git {args[0]} in the repository") from exc


def _git_paths(origin: Path, args: list[str]) -> set[str]:
    result = _git(origin, *args)
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


def run_command(args: list[str], *, cwd: Path, env: dict[str, str] | None = None) -> str:
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
    run_command(
        ["uv", "sync", "--frozen", "--no-dev", "--project", str(worktree)],
        cwd=worktree,
        env=env,
    )
    bin_dir = worktree / ".venv" / ("Scripts" if os.name == "nt" else "bin")
    python = bin_dir / ("python.exe" if os.name == "nt" else "python3")
    # Test both package binding and executable discovery in the environment that
    # will be inherited by the harness and its child processes.
    probe = run_command(
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
            raise ValueError("the installed package resolves outside the prepared worktree")
        for key in ("workflow", "run", "validate"):
            # Resolve the directory, not the executable: uv may use symlinks.
            if not found[key] or Path(found[key]).parent.resolve() != bin_dir.resolve():
                raise ValueError(f"{key} command resolves outside the local environment")
    except (KeyError, TypeError, json.JSONDecodeError) as error:
        raise ValueError("could not verify the worktree command environment") from error
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
        if _git(origin, "rev-parse", "--verify", "--quiet", ref).returncode:
            continue
        behind = int(run_command(["git", "rev-list", "--count", f"{commit}..{ref}"], cwd=origin))
        ahead = int(run_command(["git", "rev-list", "--count", f"{ref}..{commit}"], cwd=origin))
        if behind and not ahead:
            raise ValueError(
                f"HEAD is {behind} commits behind {branch}: this checkout and the "
                "session started in it hold an older method; start from the "
                f"current {branch}, or pass --revision to select this revision deliberately"
            )
        return


def prepare_worktree(
    origin: Path,
    *,
    name: str,
    allow_dirty_origin: bool = False,
    revision: str | None = None,
    worktree: Path | None = None,
) -> dict[str, object]:
    """Create a new worktree, never copy dirty bytes, and retain setup evidence.

    Failed installation leaves the worktree for diagnosis. No run is started,
    and no existing worktree is reused or removed.
    """
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
        raise ValueError("name must contain lowercase letters, digits and hyphens")
    origin = Path(run_command(["git", "rev-parse", "--show-toplevel"], cwd=origin)).resolve()
    commit = run_command(
        ["git", "rev-parse", "--verify", "--end-of-options", f"{revision or 'HEAD'}^{{commit}}"],
        cwd=origin,
    )
    if revision is None:
        _require_current_revision(origin, commit)
    require_committed_startup(origin, commit)
    dirty = bool(run_command(["git", "status", "--porcelain", "--untracked-files=all"], cwd=origin))
    if dirty and not allow_dirty_origin:
        raise ValueError(
            "origin has uncommitted changes; commit them or use --allow-dirty-origin "
            "to exclude them from the worktree"
        )
    try:
        project = tomllib.loads(run_command(["git", "show", f"{commit}:pyproject.toml"], cwd=origin))
        if project.get("project", {}).get("name") != "llm-commonplace":
            raise ValueError("not the Commonplace source project")
        run_command(["git", "cat-file", "-e", f"{commit}:uv.lock"], cwd=origin)
        run_command(["git", "cat-file", "-e", f"{commit}:{RUNTIME_MARKER}"], cwd=origin)
        run_command(["git", "cat-file", "-e", f"{commit}:AGENTS.md"], cwd=origin)
    except (ValueError, tomllib.TOMLDecodeError) as error:
        raise ValueError(f"worktree preparation requires a committed Commonplace source checkout: {error}") from error

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
            if _git(origin, "check-ignore", "--quiet", str(path)).returncode:
                raise ValueError("a worktree and its record inside the origin must be under an ignored directory")
    worktree.parent.mkdir(parents=True, exist_ok=True)
    run_command(["git", "worktree", "add", "--detach", str(worktree), commit], cwd=origin)
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
        if Path(run_command(["git", "rev-parse", "--show-toplevel"], cwd=worktree)).resolve() != worktree:
            raise ValueError("Git does not recognize the prepared worktree as its own root")
        record.update(_install(worktree))
        if run_command(["git", "rev-parse", "HEAD"], cwd=worktree) != commit:
            raise ValueError("the prepared worktree commit changed during setup")
        if run_command(["git", "status", "--porcelain", "--untracked-files=all"], cwd=worktree):
            raise ValueError("the new prepared worktree is not clean")
        require_committed_startup(origin, commit)
        record["status"] = "ready"
    except ValueError as error:
        record.update(status="failed", error=str(error))
        record_path.write_text(json.dumps(record, indent=2) + "\n")
        raise ValueError(f"worktree setup failed in {worktree}; retained {record_path}: {error}") from error
    record_path.write_text(json.dumps(record, indent=2) + "\n")
    return record


def preparation_for(worktree: Path, *, require_token: bool = True) -> dict[str, object]:
    """Read a ready record bound to this exact worktree."""
    worktree = Path(worktree).resolve()
    record_path = worktree.with_name(worktree.name + ".preparation.json")
    try:
        record = json.loads(record_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"ready worktree preparation record required: {record_path}") from error
    if not isinstance(record, dict) or record.get("status") != "ready" or record.get("worktree") != str(worktree):
        raise ValueError(f"preparation record does not name a ready worktree: {record_path}")
    token = record.get("token")
    if require_token and (not isinstance(token, str) or re.fullmatch(r"[0-9a-f]{12}", token) is None):
        raise ValueError(f"preparation record has no valid worktree token: {record_path}")
    return record


def changed_paths(worktree: Path, *args: str) -> list[str]:
    """Keep NUL-delimited Git paths intact, including leading whitespace."""
    result = subprocess.run(
        ["git", "diff", "--no-renames", "--name-only", "-z", *args],
        cwd=worktree, capture_output=True, check=False,
    )
    if result.returncode:
        raise ValueError(f"could not inspect changed paths: {result.stderr.decode(errors='replace').strip()}")
    return [os.fsdecode(path) for path in result.stdout.split(b"\0") if path]


def _status_entries(porcelain: str) -> list[tuple[str, str]]:
    """Parse ``git status --porcelain -z`` into ``(code, path)`` pairs.

    A rename or copy entry is followed by its origin path, reported as a
    second entry with the same code so both sides are checked.
    """
    fields = porcelain.split("\0")
    entries: list[tuple[str, str]] = []
    index = 0
    while index < len(fields):
        field_text = fields[index]
        index += 1
        if len(field_text) < 4:
            continue
        code, path = field_text[:2], field_text[3:]
        entries.append((code, path))
        if code[0] in "RC" and index < len(fields):
            entries.append((code, fields[index]))
            index += 1
    return entries


def require_clean_worktree(repo_root: Path, outputs: tuple[str, ...]) -> None:
    """Require a worktree clean outside the given output locations.

    ``outputs`` are path prefixes ending in ``/``. Under them, an untracked
    file or an unstaged modification of a tracked file is allowed: a sibling
    run's uncommitted publication, new or replacing an earlier one. Anywhere
    else no tracked file may be modified or staged, and no untracked file may
    sit under ``kb/``. Ignored paths never count.
    """
    status = _git(repo_root, "status", "--porcelain", "-z", "--untracked-files=all")
    if status.returncode != 0:
        raise ValueError("cannot inspect the repository's Git status")
    changed: list[str] = []
    untracked: list[str] = []
    for code, path in _status_entries(status.stdout):
        in_outputs = path.startswith(outputs)
        if code == "??":
            if path.startswith("kb/") and not in_outputs:
                untracked.append(path)
        elif not (code == " M" and in_outputs):
            changed.append(path)
    problems = []
    if changed:
        problems.append("tracked files with local changes: " + ", ".join(sorted(changed)))
    if untracked:
        problems.append(
            "untracked files under kb/ outside the publication outputs: "
            + ", ".join(sorted(untracked))
        )
    if problems:
        raise ValueError(
            "publication requires a clean worktree outside its output locations; "
            + "; ".join(problems)
        )


def running_package_root() -> Path:
    """The checkout whose ``src/commonplace`` supplies the running code.

    Commonplace is installed editable from one checkout; commands run inside
    a batch worktree still execute that checkout's source.
    """
    import commonplace

    return Path(commonplace.__file__).resolve().parents[2]


def require_running_package_unchanged(inputs_commit: str) -> None:
    """Require the executing package source to equal ``inputs-commit``.

    The opening metadata pins the publishing tree's method; this check covers
    the code actually running, which may come from another checkout.
    """
    root = running_package_root()
    if not (root / ".git").exists():
        raise ValueError(
            f"running commonplace package is not a source checkout ({root}); "
            "cannot confirm it matches inputs-commit"
        )
    if _git(root, "cat-file", "-e", f"{inputs_commit}^{{commit}}").returncode != 0:
        raise ValueError(
            f"inputs-commit {inputs_commit} is unknown to the checkout running "
            f"commonplace ({root})"
        )
    changed = _git(root, "diff", "--name-only", inputs_commit, "--", "src/commonplace")
    untracked = _git(root, "ls-files", "--others", "--exclude-standard", "--", "src/commonplace")
    if changed.returncode != 0 or untracked.returncode != 0:
        raise ValueError("cannot compare the running package source against inputs-commit")
    paths = sorted({*changed.stdout.split(), *untracked.stdout.split()})
    if paths:
        raise ValueError(
            f"running commonplace source ({root}) differs from inputs-commit "
            f"{inputs_commit}: " + ", ".join(paths)
        )


def prepared_origin(worktree: Path) -> tuple[dict[str, object], Path, str]:
    """The ready preparation, its origin on clean ``main``, and the method commit.

    The worktree must still be at the method commit with its startup files,
    and the method commit must be an ancestor of ``main``.
    """
    record = preparation_for(worktree)
    origin = Path(str(record["origin"]))
    if Path(run_command(["git", "rev-parse", "--show-toplevel"], cwd=origin)).resolve() != origin:
        raise ValueError("preparation origin is not its current Git root")
    if run_command(["git", "symbolic-ref", "--quiet", "HEAD"], cwd=origin) != "refs/heads/main":
        raise ValueError("integration requires the origin checkout on main")
    if run_command(["git", "status", "--porcelain", "--untracked-files=all"], cwd=origin):
        raise ValueError("integration requires a clean origin checkout")
    method = str(record["commit"])
    if run_command(["git", "rev-parse", "HEAD"], cwd=worktree) != method:
        raise ValueError("worktree HEAD differs from its preparation commit")
    require_committed_startup(worktree, method)
    if _git(origin, "merge-base", "--is-ancestor", method, "main").returncode:
        raise ValueError("the method commit is not an ancestor of main")
    return record, origin, method


def committed_tree(worktree: Path, commit: str, relative: str) -> dict[str, bytes] | None:
    """A directory's direct files at ``commit``, or None when it is absent there."""
    if _git(worktree, "cat-file", "-e", f"{commit}:{relative}").returncode:
        return None
    names = run_command(["git", "ls-tree", "--name-only", f"{commit}:{relative}"], cwd=worktree)
    files = {}
    for name in names.splitlines():
        if Path(name).name != name:
            raise ValueError(f"{relative} at {commit} contains non-direct members")
        files[name] = subprocess.run(["git", "show", f"{commit}:{relative}/{name}"],
                                     cwd=worktree, capture_output=True, check=True).stdout
    return files


def merge_paths(worktree: Path, origin: Path, method: str, *, branch: str, paths: list[str],
                subject: str, body: str) -> str:
    """Commit exactly ``paths`` on a new worktree branch and merge it into main.

    Refuses when the origin changed those paths since ``method``, when the
    worktree has staged changes or tracked changes outside them, or when the
    branch exists. A conflict is aborted in main; the branch remains for review.
    """
    def inside(path: str) -> bool:
        return any(path == allowed or path.startswith(allowed + "/") for allowed in paths)

    if changed_paths(origin, method, "HEAD", "--", *paths):
        raise ValueError("origin paths changed since the method commit")
    if _git(worktree, "show-ref", "--verify", "--quiet", f"refs/heads/{branch}").returncode == 0:
        raise ValueError(f"branch already exists: {branch}")
    if changed_paths(worktree, "--cached"):
        raise ValueError("worktree already has staged changes")
    outside = [path for path in changed_paths(worktree, "HEAD") if not inside(path)]
    if outside:
        raise ValueError("tracked changes outside the merged paths: " + ", ".join(outside))
    run_command(["git", "switch", "-c", branch], cwd=worktree)
    run_command(["git", "add", "--", *paths], cwd=worktree)
    staged = changed_paths(worktree, "--cached")
    if not staged or not all(inside(path) for path in staged):
        raise ValueError("staging is empty or includes another path")
    run_command(["git", "commit", "-m", subject, "-m", body], cwd=worktree)
    merge = subprocess.run(["git", "merge", "--no-ff", "--no-edit", branch], cwd=origin,
                           capture_output=True, text=True, check=False)
    if merge.returncode:
        merge_head = Path(run_command(["git", "rev-parse", "--git-path", "MERGE_HEAD"], cwd=origin))
        if (origin / merge_head).exists():
            run_command(["git", "merge", "--abort"], cwd=origin)
        raise ValueError(f"integration stopped; branch {branch} kept: {merge.stderr.strip() or merge.stdout.strip()}")
    return run_command(["git", "rev-parse", "HEAD"], cwd=origin)

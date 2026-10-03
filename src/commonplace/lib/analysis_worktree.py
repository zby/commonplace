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
    plus untracked and ignored startup files. Skill links also protect their
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
        ["ls-files", "--others", "--ignored", "--exclude-standard", "-z", "--",
         *ignored_startup],
    ):
        paths.update(_git_paths(origin, args))
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


def prepare_analysis(
    origin: Path,
    *,
    name: str,
    allow_dirty_origin: bool = False,
    revision: str = "HEAD",
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
        ["git", "rev-parse", "--verify", "--end-of-options", f"{revision}^{{commit}}"],
        cwd=origin,
    )
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

    if worktree is None:
        worktree = origin / ".commonplace/worktrees" / f"{name}-{uuid.uuid4().hex[:12]}"
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

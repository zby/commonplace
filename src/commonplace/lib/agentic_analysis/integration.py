"""Guarded, journaled transfer of exact publications; no analytical or audit inputs.

PROTOCOL is checked in the selected commit before an automatic controller exists.
Lock order: run, worktree publication, Git-common-directory integration. The last
lock survives into mutating Git children, as does the controller's target lease.
Unknown staging/branches/merge states require operator repair, never Git reset.
"""
from __future__ import annotations

import json
import os
import subprocess
from contextlib import contextmanager
from contextvars import ContextVar
from hashlib import sha256
from pathlib import Path

from commonplace.lib.agentic_analysis.durable import save
from commonplace.lib.agentic_analysis.effects import UncertainEffectError, hashes
from commonplace.lib.agentic_analysis.effects import tree as read_tree
from commonplace.lib.agentic_analysis.preparation import (
    changed_paths,
    committed_tree,
    preparation_for,
    require_committed_startup,
    require_run_code,
)

PROTOCOL = "commonplace.analysis-integration.v1"
JOURNAL = "effects/integrate.json"
_FDS = ContextVar("integration_fds", default=())


def git(repo: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True,
                            check=False, pass_fds=_FDS.get())
    if check and result.returncode:
        raise ValueError(f"git {args[0]} failed: {result.stderr.strip() or result.stdout.strip()}")
    return result.stdout.strip() if check else str(result.returncode)


@contextmanager
def origin_lock(worktree: Path):
    """One persistent inode for all cooperating transfers, including manual ones.

    Close, never explicitly unlock: an orphan Git child may still own the open
    file description. Non-cooperating Git writers remain an operator exclusion.
    """
    import fcntl

    common = Path(git(worktree, "rev-parse", "--path-format=absolute", "--git-common-dir")).resolve()
    path = common / "commonplace-analysis-integration.lock"
    fd = os.open(path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    inherited = os.environ.get("COMMONPLACE_ANALYSIS_LEASE_FD")
    fds = (fd,)
    try:
        if inherited is not None:
            lease_fd = int(inherited)
            os.fstat(lease_fd)
            fds += (lease_fd,)
        fcntl.flock(fd, fcntl.LOCK_EX)
        token = _FDS.set(fds)
        try:
            yield
        finally:
            _FDS.reset(token)
    finally:
        os.close(fd)


def _binding(run: Path, tree: Path) -> tuple[dict, Path, str, list[str], str, dict]:
    from commonplace.lib.agentic_analysis import run_ids
    from commonplace.lib.agentic_analysis.worktree import _integration_publication

    preparation = preparation_for(tree)
    origin = Path(preparation["origin"])
    method = preparation["commit"]
    if not run_ids.is_run_id(run.name, token=preparation["token"]):
        raise ValueError("run ID does not match the worktree preparation token")
    if Path(git(origin, "rev-parse", "--show-toplevel")).resolve() != origin:
        raise ValueError("preparation origin is not its current Git root")
    if git(tree, "rev-parse", "--path-format=absolute", "--git-common-dir") != git(
            origin, "rev-parse", "--path-format=absolute", "--git-common-dir"):
        raise ValueError("worktree and origin do not share a Git repository")
    require_committed_startup(tree, method)
    paths, source = _integration_publication(run, tree, method)
    expected = {path: hashes(read_tree(tree / path)) for path in paths}
    if any(value is None for value in expected.values()):
        raise ValueError("proven publication disappeared")
    binding = {"schema": PROTOCOL, "run": str(run), "worktree": str(tree), "origin": str(origin),
               "method-commit": method, "receipt-sha256": sha256((run / "receipt.json").read_bytes()).hexdigest(),
               "paths": paths, "trees": expected, "branch": f"analysis/{run.name}"}
    return preparation, origin, method, paths, source, binding


def _exact(tree: Path, revision: str, record: dict) -> None:
    for path, expected in record["trees"].items():
        files = committed_tree(tree, revision, path)
        if files is None or {name: sha256(data).hexdigest() for name, data in files.items()} != expected:
            raise ValueError(f"exact Git bytes differ from publication: {revision}:{path}")
        # A symlink blob can have the same bytes as an ordinary member.
        modes = git(tree, "ls-tree", "-r", revision, "--", path).splitlines()
        if any(not line.startswith("100644 blob ") for line in modes):
            raise ValueError("publication Git members must be ordinary non-executable files")


def _commit(tree: Path, record: dict) -> str | None:
    branch = record["branch"]
    if git(tree, "show-ref", "--verify", "--quiet", f"refs/heads/{branch}", check=False) != "0":
        if record.get("publication-commit"):
            raise ValueError("journaled publication branch is missing")
        return None
    commit = git(tree, "rev-parse", f"refs/heads/{branch}")
    if commit == record["method-commit"]:
        if record.get("publication-commit"):
            raise ValueError("journaled publication commit disappeared")
        return None
    if record.get("publication-commit", commit) != commit:
        raise ValueError("publication branch differs from journal")
    if git(tree, "show", "-s", "--format=%P", commit) != record["method-commit"]:
        raise ValueError("publication commit must have exactly the method parent")
    changed = changed_paths(tree, record["method-commit"], commit)
    if not changed or any(not _inside(path, record["paths"]) for path in changed):
        raise ValueError("publication commit changes unrelated paths")
    if git(tree, "show", "-s", "--format=%B", commit) != record["message"]:
        raise ValueError("publication commit attribution differs from intent")
    _exact(tree, commit, record)
    return commit


def _inside(path: str, paths: list[str]) -> bool:
    return any(path == allowed or path.startswith(allowed + "/") for allowed in paths)


def _merged(origin: Path, commit: str, record: dict) -> str | None:
    if git(origin, "merge-base", "--is-ancestor", commit, "refs/heads/main", check=False) != "0":
        if record.get("merge-commit"):
            raise ValueError("journaled integration is no longer in main history")
        return None
    # Match the exact merge, including the origin HEAD saved before its effect.
    candidates = ([record["merge-commit"]] if record.get("merge-commit") else
                  git(origin, "rev-list", "--first-parent", "--merges",
                      f"{record['origin-head']}..refs/heads/main").splitlines())
    for merge in candidates:
        if (git(origin, "show", "-s", "--format=%P", merge) == f"{record['origin-head']} {commit}"
                and git(origin, "merge-base", "--is-ancestor", merge, "refs/heads/main", check=False) == "0"):
            if record.get("merge-commit") and record["merge-commit"] != merge:
                raise ValueError("integration merge differs from journal")
            _exact(origin, merge, record)
            if (git(origin, "rev-parse", "HEAD") == merge
                    and git(origin, "symbolic-ref", "--quiet", "HEAD", check=False) == "0"):
                for path, expected in record["trees"].items():
                    if hashes(read_tree(origin / path)) != expected:
                        raise ValueError("exact origin checkout bytes differ from integration")
            return merge
    raise ValueError("publication is reachable from main without its established integration merge")


def _inspect(run: Path, tree: Path) -> dict:
    _, origin, method, _, _, binding = _binding(run, tree)
    _unfinished(tree)
    path = run / JOURNAL
    if not path.exists():
        branch = binding["branch"]
        if git(tree, "show-ref", "--verify", "--quiet", f"refs/heads/{branch}", check=False) == "0":
            raise ValueError("analysis branch already exists without integration intent")
        return {"state": "pending", **binding}
    record = json.loads(path.read_text())
    if any(record.get(key) != value for key, value in binding.items()):
        raise ValueError("integration intent differs from the pinned publication")
    commit = _commit(tree, record)
    head = git(tree, "rev-parse", "HEAD")
    if head not in (method, commit) or (commit and git(tree, "symbolic-ref", "--quiet", "HEAD") != f"refs/heads/{record['branch']}"):
        raise ValueError("worktree HEAD differs from integration intent")
    if changed_paths(tree, "--cached"):
        raise ValueError("ambiguous staged integration state; preserve for operator repair")
    if commit:
        if changed_paths(tree, "HEAD"):
            raise ValueError("committed publication worktree has tracked changes")
        merge = _merged(origin, commit, record)
        return {**record, "state": "integrated" if merge else "committed",
                "publication-commit": commit, "merge-commit": merge}
    return {**record, "state": "pending"}


def inspect_integration(run: Path) -> dict:
    """Read-only evidence view, not liveness or authorization to start an effect."""
    from commonplace.lib.agentic_analysis.worktree import analysis_run

    run, tree = analysis_run(run)
    require_run_code(run, cwd=Path.cwd())
    try:
        return _inspect(run, tree)
    except (ValueError, OSError, KeyError, TypeError, UncertainEffectError) as error:
        return {"state": "operator-attention", "error": str(error)}


def _unfinished(repo: Path) -> None:
    for name in ("MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "rebase-merge", "rebase-apply"):
        if Path(git(repo, "rev-parse", "--path-format=absolute", "--git-path", name)).exists():
            raise ValueError("repository has an unfinished Git operation")


def _origin_ready(origin: Path, method: str, paths: list[str]) -> None:
    if git(origin, "symbolic-ref", "--quiet", "HEAD") != "refs/heads/main":
        raise ValueError("integration requires the origin checkout on main")
    if git(origin, "status", "--porcelain", "--untracked-files=all"):
        raise ValueError("integration requires a clean origin checkout")
    if git(origin, "merge-base", "--is-ancestor", method, "main", check=False) != "0":
        raise ValueError("the method commit is not an ancestor of main")
    if changed_paths(origin, method, "HEAD", "--", *paths):
        raise ValueError("origin paths changed since the method commit")
    _unfinished(origin)


def integrate(run: Path, *, model: str | None = None) -> str:
    from commonplace.headless.jobs import run_lock
    from commonplace.lib.agentic_analysis.guards import publication_lock
    from commonplace.lib.agentic_analysis.worktree import analysis_run, inspect_analysis

    run, tree = analysis_run(run)
    require_run_code(run, cwd=Path.cwd())
    if model is not None and (not model.strip() or any(c in model for c in "\n\r\x00")):
        raise ValueError("model must be nonempty single-line text")
    with run_lock(run), publication_lock(tree), origin_lock(tree):
        ownership = inspect_analysis(run)
        audit = ownership.get("advisory-audit") or {}
        if (ownership.get("unsettled-launches") or audit.get("unsettled-launches")
                or audit.get("state") in ("running", "interrupted")):
            raise ValueError("unsettled worker or advisory audit ownership; preserve publication")
        _, origin, method, paths, source, binding = _binding(run, tree)
        view = _inspect(run, tree)
        if model is not None and "model" in view and model != view["model"]:
            raise ValueError("model attribution differs from integration intent")
        if view["state"] == "integrated":
            save(run / JOURNAL, view)
            return view["merge-commit"]
        _origin_ready(origin, method, paths)
        if changed_paths(tree, "--cached"):
            raise ValueError("worktree already has staged changes")
        outside = [path for path in changed_paths(tree, "HEAD") if not _inside(path, paths)]
        if outside:
            raise ValueError("tracked changes outside the merged paths: " + ", ".join(outside))
        if not (run / JOURNAL).exists():
            if git(tree, "rev-parse", "HEAD") != method:
                raise ValueError("worktree HEAD differs from its preparation commit")
            body = f"Run: {run.name}\nMethod: {method}\nSource: {source}"
            if model:
                body += f"\n\nModel: {model}"
            view = {**binding, "state": "pending", "model": model,
                    "origin-head": git(origin, "rev-parse", "HEAD"),
                    "message": f"Publish analysis result\n\n{body}"}
            save(run / JOURNAL, view)
        if view["state"] != "committed":
            branch = view["branch"]
            if git(tree, "show-ref", "--verify", "--quiet", f"refs/heads/{branch}", check=False) != "0":
                git(tree, "switch", "-c", branch)
            elif git(tree, "symbolic-ref", "--quiet", "HEAD") != f"refs/heads/{branch}":
                raise ValueError("intent branch exists but is not checked out")
            git(tree, "add", "--", *paths)
            staged = changed_paths(tree, "--cached")
            if not staged or any(not _inside(path, paths) for path in staged):
                raise ValueError("staging is empty or includes another path")
            _exact(tree, git(tree, "write-tree"), view)
            git(tree, "commit", "-m", view["message"])
            commit = _commit(tree, view)
            view.update(state="committed", **{"publication-commit": commit})
            save(run / JOURNAL, view)
        if changed_paths(tree, "HEAD"):
            raise ValueError("committed publication worktree has tracked changes")
        _origin_ready(origin, method, paths)
        view["origin-head"] = git(origin, "rev-parse", "HEAD")
        save(run / JOURNAL, view)
        try:
            git(origin, "merge", "--no-ff", "--no-edit", view["branch"])
        except ValueError:
            merge_head = Path(git(origin, "rev-parse", "--path-format=absolute", "--git-path", "MERGE_HEAD"))
            if merge_head.exists() and merge_head.read_text().strip() == view["publication-commit"]:
                git(origin, "merge", "--abort")
            raise
        merge = _merged(origin, view["publication-commit"], view)
        if merge is None:
            raise ValueError("merge returned without established integration")
        if git(origin, "status", "--porcelain", "--untracked-files=all"):
            raise ValueError("origin is not clean after integration; preserve evidence")
        view.update(state="integrated", **{"merge-commit": merge})
        save(run / JOURNAL, view)
        return merge

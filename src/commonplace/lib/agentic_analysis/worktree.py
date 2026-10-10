"""Start, prove and integrate analysis runs in prepared worktrees."""

from __future__ import annotations

import datetime
import json
import os
import re
from hashlib import sha256
from pathlib import Path

from commonplace.artifactrun.worktree import (
    committed_tree,
    merge_paths,
    preparation_for,
    prepared_origin,
    require_committed_startup,
    require_run_code,
    run_command,
)
from commonplace.lib.agentic_analysis.analyses import (
    ARCHIVE_ROOT,
    RETAINED_ROOT,
    WORKER_PROFILES,
    resolve_worker_profile,
    source_slug,
)
from commonplace.lib.note_parser import parse_document
from commonplace.lib.source_identity import normalize_source_identity

STATE_ROOT = Path("kb/agentic-system-analyses/state")


def start_analysis(worktree: Path, *, system: str, source_identity: str,
                   source: str, source_revision: str | None = None, worker_profile: str | None = None,
                   harness: str | None = None) -> Path:
    """Allocate a prepared analysis and pin its declaration, without advancing.

    ``worker_profile`` names the run's worker profile; without it, ``harness``'s default applies.
    """
    from commonplace.artifactrun import start_run
    from commonplace.artifactrun.sources import github_checkout_path
    from commonplace.lib.agentic_analysis.plan import PLAN

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
    if run_command(["git", "rev-parse", "HEAD"], cwd=worktree) != preparation["commit"]:
        raise ValueError("worktree HEAD differs from its preparation commit")
    require_committed_startup(worktree, str(preparation["commit"]))
    slug = source_slug(identity, system)
    date = datetime.datetime.now(datetime.UTC).date().isoformat()
    prefix = f"AAS-{date}-{slug}-{preparation['token']}"
    worker = resolve_worker_profile((worktree / "kb" / WORKER_PROFILES).read_bytes(), worker_profile, harness=harness)
    # The prepared checkout's commands; every worker's content check runs them.
    commands = worktree / ".venv" / ("Scripts" if os.name == "nt" else "bin")
    parameters = {"system": system, "source-identity": identity, "source": source,
                  "worker-profile": worker["profile"], "command-path": str(commands)}
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
        start_run(run, worktree / "kb" / PLAN, parameters=parameters)
        return run
    raise ValueError("analysis run sequence exhausted for this source and worktree")


def _frontmatter(text: str, path: Path) -> dict[str, object]:
    document, error = parse_document(text)
    if error or document is None or not isinstance(document.frontmatter, dict):
        raise ValueError(f"cannot read frontmatter in {path}: {error}")
    return document.frontmatter


def _frontmatter(text: str, path: Path) -> dict[str, object]:
    document, error = parse_document(text)
    if error or document is None or not isinstance(document.frontmatter, dict):
        raise ValueError(f"cannot read frontmatter in {path}: {error}")
    return document.frontmatter


def _integration_publication(run_dir: Path, worktree: Path, method: str) -> tuple[list[str], str]:
    """Prove current engine completion AND exact publication, without recovery writes.

    Caller holds the run and publication locks. The publish job's current
    receipt names what was published; the retained tree must match it exactly,
    and the archive must hold the method commit's exact incumbent. The effect's
    own journal is recovery evidence for publication, not read here.
    """
    from commonplace.artifactrun import current_outputs, inspect
    from commonplace.artifactrun.effects import hashes, tree
    from commonplace.lib.agentic_analysis.plan import PLAN

    view = inspect(run_dir)
    fixed = view["declaration"]
    shipped = worktree / "kb" / PLAN
    # The run fixed the plan's expansion; the shipped file is the compact plan.
    if Path(fixed["plan"]) != shipped or fixed.get("plan_sha256") != sha256(shipped.read_bytes()).hexdigest():
        raise ValueError("integration requires the fixed shipped analysis plan")
    if fixed["type_sha256"] != sha256((worktree / "kb" / fixed["type_spec"]).read_bytes()).hexdigest():
        raise ValueError("integration requires the unchanged shipped artifact type")
    outputs = current_outputs(run_dir, "publish")
    if (outputs is None or view["condition"] != "publishable"
            or view["failed_attempts"] or view["exhausted_jobs"]):
        raise ValueError("integration requires a current publication completion and current coverage")
    receipt = json.loads(outputs.get("receipt", b"null"))
    if not isinstance(receipt, dict) or receipt.get("published") is not True:
        raise ValueError("integration requires a published complete disposition, not a local result")
    if receipt.get("run-id") != run_dir.name or receipt.get("inputs-commit") != method:
        raise ValueError("publication does not pin this run and method")
    if any(receipt.get(name) != view["parameters"].get(name) for name in
           ("system", "source-identity", "source", "source-revision")):
        raise ValueError("publication source and system pins differ from run parameters")
    destination = Path(receipt["destination"])
    files = tree(destination)
    if files is None or hashes(files) != receipt["members"]:
        raise ValueError("exact retained bytes differ from the publication receipt")
    overview = _frontmatter(files["overview.md"].decode("utf-8"), destination / "overview.md")
    if (overview.get("run-id") != run_dir.name or overview.get("inputs-commit") != method
            or overview.get("result-disposition") != "complete"
            or not isinstance(overview.get("reviewed-boundary"), str)
            or not overview["reviewed-boundary"]):
        raise ValueError("published overview has mismatched run, method, disposition or source pins")
    relative = destination.relative_to(worktree)
    if relative.parent != RETAINED_ROOT:
        raise ValueError("publication destination is outside retained artifacts")
    paths = [relative.as_posix()]
    # Compare the archive to Git's entire incumbent tree, not only its overview.
    old = committed_tree(worktree, method, relative.as_posix())
    expected = "absent" if old is None else sha256(old["overview.md"]).hexdigest()
    if receipt["expected-incumbent-sha256"] != expected:
        raise ValueError("opened incumbent differs from method commit")
    if old is not None:
        old_id = _frontmatter(old["overview.md"].decode("utf-8"), relative / "overview.md").get("run-id")
        if not isinstance(old_id, str) or re.fullmatch(r"AAS-[a-zA-Z0-9-]+", old_id) is None:
            raise ValueError("incumbent has an invalid run ID")
        archive = worktree / ARCHIVE_ROOT / old_id
        if tree(archive) != old:
            raise ValueError("publication archive is missing or differs from the exact incumbent")
        paths.append(archive.relative_to(worktree).as_posix())
    return paths, overview["reviewed-boundary"]


def integrate_analysis(run_dir: Path, *, model: str | None = None) -> str:
    """Commit one completed publication in its worktree and merge it into main.

    Calling this is the separate authorization to transfer a published run.
    The run and publication locks serialize cooperating run and publisher
    mutations. A conflict is aborted in main; its branch remains for review.
    """
    from commonplace.artifactrun import run_lock
    from commonplace.lib.agentic_analysis.guards import publication_lock

    run_dir = Path(run_dir).absolute()
    if run_dir.resolve() != run_dir:
        raise ValueError("analysis run must not traverse symlinks")
    if not (run_dir / "run.json").is_file():
        raise ValueError("integration requires an engine run's run.json")
    if (run_dir.parent.name != STATE_ROOT.name
            or len(run_dir.parents) <= len(STATE_ROOT.parts)):
        raise ValueError(f"analysis run must be directly under {STATE_ROOT}")
    worktree = run_dir.parents[len(STATE_ROOT.parts)]
    if worktree / STATE_ROOT != run_dir.parent:
        raise ValueError(f"analysis run must be directly under {STATE_ROOT}")
    require_run_code(run_dir, cwd=Path.cwd())
    with run_lock(run_dir), publication_lock(worktree):
        record, origin, method = prepared_origin(worktree)
        run_id = run_dir.name
        if re.fullmatch(rf"AAS-\d{{4}}-\d{{2}}-\d{{2}}-[a-z0-9-]+-{record['token']}-\d{{2}}", run_id) is None:
            raise ValueError("run ID does not match the worktree preparation token")
        paths, source_revision = _integration_publication(run_dir, worktree, method)
        body = f"Run: {run_id}\nMethod: {method}\nSource: {source_revision}"
        if model:
            body += f"\n\nModel: {model}"
        return merge_paths(worktree, origin, method, branch=f"analysis/{run_id}", paths=paths,
                           subject="Publish analysis result", body=body)

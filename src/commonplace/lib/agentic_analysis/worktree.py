"""Start, inspect, prove and integrate analysis runs in prepared worktrees.

A run directory holds what the workflow (``workflow.py``) wrote: ``parameters.json``
at start, ``code/<job>.json`` for its code jobs (``opening`` is the pinned
metadata), ``answers/`` for the workers' cached answers, ``log.jsonl``,
``artifact/`` with the accepted members, and ``receipt.json`` once
publication ran.
"""

from __future__ import annotations

import datetime
import fcntl
import json
import os
from hashlib import sha256
from pathlib import Path

from commonplace.lib.agentic_analysis import run_ids
from commonplace.lib.agentic_analysis.analyses import (
    ARCHIVE_ROOT,
    RETAINED_ROOT,
    WORKER_PROFILES,
    analysis_layout,
    resolve_worker_profile,
    source_slug,
)
from commonplace.lib.agentic_analysis.preparation import (
    committed_tree,
    merge_paths,
    preparation_for,
    prepared_origin,
    require_committed_startup,
    require_run_code,
    run_command,
)
from commonplace.lib.note_parser import parse_document
from commonplace.lib.source_identity import normalize_source_identity

STATE_ROOT = Path("kb/agentic-system-analyses/state")
PARAMETERS = "parameters.json"
RECEIPT = "receipt.json"
OPENING = Path("code") / "opening.json"


def start_analysis(worktree: Path, *, system: str, source_identity: str, source: str,
                   source_revision: str | None = None, worker_profile: str) -> Path:
    """Allocate a run directory in a prepared worktree and pin its parameters, without running it."""
    from commonplace.lib.agentic_analysis.sources import github_checkout_path

    worktree = worktree.resolve()
    preparation = preparation_for(worktree)
    require_run_code(worktree, cwd=Path.cwd())
    for label, value in (("system", system), ("source-identity", source_identity), ("source", source)):
        if not value.strip() or "\n" in value or "\r" in value:
            raise ValueError(f"{label} must be a nonempty single-line value")
    identity = normalize_source_identity(source_identity.strip())
    if not identity:
        raise ValueError("source-identity normalizes to an empty identity")
    if source_revision is not None and (not run_ids.is_commit(source_revision)
                                       or github_checkout_path(identity) is None):
        raise ValueError("source-revision requires a full 40-hex commit and GitHub repository identity")
    if run_command(["git", "rev-parse", "HEAD"], cwd=worktree) != preparation["commit"]:
        raise ValueError("worktree HEAD differs from its preparation commit")
    require_committed_startup(worktree, str(preparation["commit"]))
    worker = resolve_worker_profile((worktree / "kb" / WORKER_PROFILES).read_bytes(), worker_profile)
    # The prepared checkout's commands; every worker's content check runs them.
    commands = worktree / ".venv" / ("Scripts" if os.name == "nt" else "bin")
    parameters = {"system": system, "source-identity": identity, "source": source,
                  "worker-profile": worker["profile"], "command-path": str(commands)}
    if source_revision is not None:
        parameters["source-revision"] = source_revision
    root = worktree / STATE_ROOT
    root.mkdir(parents=True, exist_ok=True)
    date = datetime.datetime.now(datetime.UTC).date().isoformat()
    for number in range(1, 100):
        run_dir = root / run_ids.run_id(date, source_slug(identity, system), preparation["token"], number)
        try:
            run_dir.mkdir()                           # atomic allocation: never another run's state
        except FileExistsError:
            continue
        (run_dir / PARAMETERS).write_text(json.dumps(parameters, indent=2) + "\n")
        return run_dir
    raise ValueError("analysis run sequence exhausted for this source and worktree")


def analysis_run(run_dir: Path) -> tuple[Path, Path]:
    """The run directory and its worktree, after the location checks every run command makes."""
    run_dir = Path(run_dir).absolute()
    if run_dir.resolve() != run_dir:
        raise ValueError("analysis run must not traverse symlinks")
    if not (run_dir / PARAMETERS).is_file():
        raise ValueError(f"analysis run requires {PARAMETERS}")
    if (run_dir.parent.name != STATE_ROOT.name
            or len(run_dir.parents) <= len(STATE_ROOT.parts)):
        raise ValueError(f"analysis run must be directly under {STATE_ROOT}")
    worktree = run_dir.parents[len(STATE_ROOT.parts)]
    if worktree / STATE_ROOT != run_dir.parent:
        raise ValueError(f"analysis run must be directly under {STATE_ROOT}")
    return run_dir, worktree


def _frontmatter(text: str, path: Path) -> dict[str, object]:
    document, error = parse_document(text)
    if error or document is None or not isinstance(document.frontmatter, dict):
        raise ValueError(f"cannot read frontmatter in {path}: {error}")
    return document.frontmatter


def _events(run_dir: Path) -> list[dict]:
    path = run_dir / "log.jsonl"
    return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []


def _locked(run_dir: Path) -> bool:
    """Whether another process holds the run lock now."""
    path = run_dir / "lock"
    if not path.exists():
        return False
    fd = os.open(path, os.O_RDWR)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        return True
    finally:
        os.close(fd)
    return False


def inspect_analysis(run_dir: Path) -> dict:
    """A status view over the run's log, answer cache, artifact and receipt; reads only.

    ``state`` is read from the latest `run`'s events (those after its ``start``):
    ``running`` (a process holds the lock), ``published`` (the run ended with
    the receipt, which says so), ``local`` (a non-complete boundary completed
    without publication), ``stopped`` (the run ended with a stop; ``stopped``
    has its reason), ``withdrawn`` (the publication was reset; a rerun
    publishes again), ``interrupted`` (the run neither ended nor holds the
    lock) or ``allocated`` (never run). ``jobs`` lists each worker job's
    launches, answers (with the cache file to delete for a retry), counted
    failures and rejections.
    """
    run_dir, worktree = analysis_run(run_dir)
    events = _events(run_dir)
    receipt = json.loads((run_dir / RECEIPT).read_text()) if (run_dir / RECEIPT).exists() else None
    starts = [i for i, e in enumerate(events) if e["event"] == "start"]
    latest = events[starts[-1]:] if starts else events
    ended = next((e for e in reversed(latest) if e["event"] in ("stopped", "published", "withdrawn")), None)
    if _locked(run_dir):
        state = "running"
    elif receipt is not None and (ended is None or ended["event"] == "published"):
        state = "published" if receipt.get("published") else "local"     # the receipt stands until a later stop
    elif ended is not None and ended["event"] != "published":
        state = ended["event"]
    else:
        state = "interrupted" if latest else "allocated"
    stop = ended if ended is not None and ended["event"] == "stopped" else None
    jobs: dict[str, dict] = {}
    answers = run_dir / "answers"
    for path in sorted(answers.glob("*.json")) if answers.is_dir() else []:
        record = json.loads(path.read_text())
        job = jobs.setdefault(record["job"], {"launches": 0, "answers": [], "failures": [], "rejected": 0})
        job["answers"].append({"cache": str(path), "attempt": record["attempt"], "model": record.get("model"),
                               "seconds": record.get("seconds"), "problem": record.get("problem"),
                               "inputs": sorted(record.get("inputs", {}))})
    for event in events:
        if event["event"] == "launch":
            jobs.setdefault(event["job"], {"launches": 0, "answers": [], "failures": [], "rejected": 0})
            jobs[event["job"]]["launches"] += 1
        elif event["event"] in ("failed", "incomplete"):
            jobs.setdefault(event["job"], {"launches": 0, "answers": [], "failures": [], "rejected": 0})
            jobs[event["job"]]["failures"].append({k: v for k, v in event.items() if k in ("kind", "reason", "missing")})
        elif event["event"] == "rejected":
            jobs[event["job"]]["rejected"] += 1
    artifact = run_dir / "artifact"
    members = {p.name: sha256(p.read_bytes()).hexdigest() for p in sorted(artifact.iterdir())
               if p.is_file()} if artifact.is_dir() else {}
    boundary = next((e.get("disposition") for e in events if e["event"] == "boundary"), None)
    return {
        "run-id": run_dir.name, "worktree": str(worktree), "state": state,
        "stopped": None if stop is None else stop["reason"],
        "parameters": json.loads((run_dir / PARAMETERS).read_text()),
        "opening": json.loads((run_dir / OPENING).read_text()) if (run_dir / OPENING).exists() else None,
        "result-disposition": boundary,
        "verdicts": [{k: v for k, v in e.items() if k != "time"} for e in events if e["event"] == "verdict"],
        "problems": [{"job": e["job"], "key": e["key"]} for e in events if e["event"] == "answered" and e["problem"]],
        "jobs": jobs, "members": members, "receipt": receipt,
    }


def _integration_publication(run_dir: Path, worktree: Path, method: str) -> tuple[list[str], str]:
    """Prove the run's exact publication from its records, without recovery writes.

    Caller holds the run and publication locks. The receipt names what was
    published; the retained tree must match it exactly, and the archive must
    hold the method commit's exact incumbent. The effect's own journal is
    recovery evidence for publication, not read here.
    """
    from commonplace.lib.agentic_analysis.effects import hashes, tree

    if not (run_dir / OPENING).is_file() or not (run_dir / RECEIPT).is_file():
        raise ValueError("integration requires the run's opening metadata and publication receipt")
    opened = json.loads((run_dir / OPENING).read_text())
    parameters = json.loads((run_dir / PARAMETERS).read_text())
    if opened.get("inputs-commit") != method or opened.get("run-id") != run_dir.name:
        raise ValueError("opening metadata does not pin this run and method")
    receipt = json.loads((run_dir / RECEIPT).read_text())
    if not isinstance(receipt, dict) or receipt.get("published") is not True:
        raise ValueError("integration requires a published complete disposition, not a local result")
    if receipt.get("run-id") != run_dir.name or receipt.get("inputs-commit") != method:
        raise ValueError("publication does not pin this run and method")
    if any(receipt.get(name) != parameters.get(name) for name in
           ("system", "source-identity", "source", "source-revision")):
        raise ValueError("publication source and system pins differ from run parameters")
    destination = Path(receipt["destination"])
    files = tree(destination)
    if files is None or hashes(files) != receipt["members"]:
        raise ValueError("exact retained bytes differ from the publication receipt")
    entry = analysis_layout().path("overview")
    overview = _frontmatter(files[entry].decode("utf-8"), destination / entry)
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
    expected = "absent" if old is None else sha256(old[entry]).hexdigest()
    if receipt["expected-incumbent-sha256"] != expected:
        raise ValueError("opened incumbent differs from method commit")
    if old is not None:
        old_id = _frontmatter(old[entry].decode("utf-8"), relative / entry).get("run-id")
        if not run_ids.is_archived_run_id(old_id):
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
    from commonplace.headless.jobs import run_lock
    from commonplace.lib.agentic_analysis.guards import publication_lock

    run_dir, worktree = analysis_run(run_dir)
    require_run_code(run_dir, cwd=Path.cwd())
    with run_lock(run_dir), publication_lock(worktree):
        record, origin, method = prepared_origin(worktree)
        run_id = run_dir.name
        if not run_ids.is_run_id(run_id, token=record["token"]):
            raise ValueError("run ID does not match the worktree preparation token")
        paths, source_revision = _integration_publication(run_dir, worktree, method)
        body = f"Run: {run_id}\nMethod: {method}\nSource: {source_revision}"
        if model:
            body += f"\n\nModel: {model}"
        return merge_paths(worktree, origin, method, branch=f"analysis/{run_id}", paths=paths,
                           subject="Publish analysis result", body=body)

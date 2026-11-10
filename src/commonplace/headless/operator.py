"""Explicit operator answers, bound to a stop's proposal and its inputs.

`answer()` materializes an editable proposal and waits until `approve()`
records its text. Repeating a workflow never approves. Callers supply a key
covering the inputs that produce the proposal; changed inputs replace the
proposal and invalidate its approval. Approval holds the same lock as Run.
`edited()` tells a workflow that the file was changed after its approval, so
it can report an edit that has no effect yet.
"""

from __future__ import annotations

import json
import shlex
import uuid
from pathlib import Path

from commonplace.headless.jobs import Run, digest, run_lock


def _paths(root: Path, name: str) -> tuple[Path, Path]:
    artifact = (root / "artifact").resolve()
    path = (artifact / name).resolve()
    if Path(name).is_absolute() or not path.is_relative_to(artifact) or path == artifact:
        raise ValueError(f"proposal is outside the run's artifact directory: {name}")
    name = path.relative_to(artifact).as_posix()
    records = root / "operator"
    record = records / f"{digest(name)}.json"
    if not record.resolve().is_relative_to(root.resolve()):
        raise ValueError("operator records are outside the run")
    return path, record


def _write(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    try:
        temporary.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def answer(run: Run, name: str, proposal: str, *, key: str) -> str | None:
    """Return only an approved answer; otherwise materialize the proposal and wait.

    `key` covers the proposal's inputs, including its instruction and profile.
    The editable file is never itself an answer. A pre-existing file without
    a matching record is replaced, not implicitly approved.
    """
    path, record = _paths(run.root, name)
    data = json.loads(record.read_text(encoding="utf-8")) if record.is_file() else None
    if data is None or data["input-key"] != key or data["proposal"] != proposal:
        data = {"name": name, "input-key": key, "proposal": proposal,
                "key": digest(json.dumps([name, key, proposal]))}
        run.accept(name, proposal)
        _write(record, data)
    elif not path.is_file():
        run.accept(name, data["proposal"])
    return data.get("answer")


def edited(run: Run, name: str) -> bool:
    """Whether the editable file changed or disappeared after approval; it is not the approved input."""
    path, record = _paths(run.root, name)
    data = json.loads(record.read_text(encoding="utf-8")) if record.is_file() else {}
    return "answer" in data and (not path.is_file() or path.read_text(encoding="utf-8") != data["answer"])


def invalidate(run: Run, name: str) -> None:
    """Withdraw an answer under the caller's run lock without granting new authority.

    Publication uses this when its inspection files were changed after being
    generated. Editable selection proposals keep their ordinary semantics.
    """
    _, record = _paths(run.root, name)
    if record.is_file():
        data = json.loads(record.read_text(encoding="utf-8"))
        if "answer" in data:
            del data["answer"]
            _write(record, data)


def approve(root: Path, name: str, key: str) -> dict:
    """Capture this proposal's current text as its answer, without launching work.

    `key` is the proposal identity reported at the stop. An old approval
    command cannot approve a replacement proposal at the same path.
    """
    if not root.is_dir():
        raise ValueError(f"not a run directory: {root}")
    with run_lock(root):
        path, record = _paths(root, name)
        if not record.is_file():
            raise ValueError(f"no operator proposal: {name}")
        data = json.loads(record.read_text(encoding="utf-8"))
        if key != data["key"]:
            raise ValueError(f"proposal changed: {name}; repeat the workflow and inspect its current stop")
        data["answer"] = path.read_text(encoding="utf-8")
        _write(record, data)
        return {"file": str(path), "key": key, "answer-sha256": digest(data["answer"])}


def waiting(run: Run, root: Path, name: str, what: str, command: str) -> dict:
    """Report the editable file, explicit approval command and command to repeat."""
    path, record = _paths(run.root, name)
    data = json.loads(record.read_text(encoding="utf-8"))
    file = path.relative_to(root.resolve()).as_posix()
    run_dir = run.root.resolve().relative_to(root.resolve()).as_posix()
    return {"what": what, "file": file, "key": data["key"],
            "approve-command": shlex.join(["commonplace-review", "approve", run_dir, file, "--key", data["key"]]),
            "command": command}

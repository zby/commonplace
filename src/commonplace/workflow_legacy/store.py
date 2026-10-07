"""The run's records on disk, under `workflow-state/` in the run directory.

    run.json          the definition and parameters, written by `create`
    state.json        every job's record, the workflow's failure counts, and
                      the moves a step still owes; replaced whole by each step
    effects/<name>.json
                      one effect's start or completion, written at once
    reports.jsonl     the agent orchestrator's reports, one per line
    lock              the file a running step locks
    jobs/<name>/      a job's prompt file, block records, and kept files
    workflow/         block records for steps that code executes
    effect-blocks/    block records for effects out of step with the run

Every record carries a format version. A record that is missing where the run
requires it, does not parse, or has another shape raises StateError.
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any, BinaryIO

from commonplace.workflow_legacy.job import STATE_DIR

try:
    import fcntl
except ImportError:  # pragma: no cover - Windows
    fcntl = None
    import msvcrt

FORMAT = 2


class RunBusy(Exception):
    """Another `step` is running on the same run."""


class StateError(Exception):
    """The run's state records cannot be trusted.

    Raised when a record the run requires is missing, does not parse, does
    not agree with the other records, or was written by a different format
    version. It is never read as an ordinary outcome such as a missing
    acceptance or an effect that never started, because that reading could
    repeat an effect. The run needs the operator.
    """


_OPTIONAL_STR = (str, type(None))
_OPTIONAL_DICT = (dict, type(None))

JOB_FIELDS: dict[str, Any] = {
    "handouts": int,
    "failures": int,
    "blocks_toward_limit": int,
    "blocks": int,
    "outstanding": _OPTIONAL_STR,
    "last_input": _OPTIONAL_STR,
    "accepted": _OPTIONAL_DICT,
    "messages": list,
    "history": list,
    "stopped": _OPTIONAL_DICT,
}
"""A job's record.

handouts
    Hand-outs in the run, shown as the attempt number.
failures
    Failed attempts since the last acceptance, block or reopening.
blocks_toward_limit
    Blocks since the last acceptance or release, counted against the repair
    limit. It counts blocks, not repairs that were made.
blocks
    Blocks in the run; numbers the block records.
outstanding
    The input state of a hand-out not yet judged.
last_input
    The input state of the last hand-out; an output in place is judged against
    it when no hand-out is outstanding.
accepted
    The input state and output hash of the acceptance.
messages
    Why the last attempt failed, for the next prompt.
history
    The failed attempts since the last block, for the block record.
stopped
    The block that permits only stopping, until the operator releases it.
"""

WORKFLOW_FIELDS: dict[str, Any] = {
    "places": dict,
    "blocks": int,
    "stopped": _OPTIONAL_DICT,
}
STATE_FIELDS: dict[str, Any] = {
    "format": int,
    "jobs": dict,
    "workflow": dict,
    "unreached": list,
    "moves": list,
    "kept": int,
}
EFFECT_FIELDS: dict[str, Any] = {
    "format": int,
    "name": str,
    "status": str,
    "inputs": list,
    "state": str,
    "required": bool,
}
REPORT_FIELDS: dict[str, Any] = {
    "format": int,
    "number": int,
    "event": str,
    "job": _OPTIONAL_STR,
    "text": str,
    "recorded_at": str,
}
MOVE_FIELDS: dict[str, Any] = {"source": str, "target": str, "sha": str}
EMPTY_STATE: dict[str, Any] = {
    "format": FORMAT,
    "jobs": {},
    "workflow": {"places": {}, "blocks": 0, "stopped": None},
    "unreached": [],
    "moves": [],
    "kept": 0,
}


def new_job() -> dict[str, Any]:
    return {
        "handouts": 0,
        "failures": 0,
        "blocks_toward_limit": 0,
        "blocks": 0,
        "outstanding": None,
        "last_input": None,
        "accepted": None,
        "messages": [],
        "history": [],
        "stopped": None,
    }


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(data: Any) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")


def file_sha(path: Path) -> str | None:
    """The hash of a file's bytes, or None when there is no file."""
    try:
        return sha(path.read_bytes())
    except (FileNotFoundError, IsADirectoryError, NotADirectoryError):
        return None


def write_atomic(path: Path, text: str) -> None:
    """Replace a file whole: readers see the old bytes or the new ones."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


def dump(data: Any) -> str:
    return json.dumps(data, indent=2, sort_keys=True) + "\n"


def _check(data: Any, fields: dict[str, Any], where: str) -> None:
    if not isinstance(data, dict) or set(data) != set(fields):
        raise StateError(f"{where}: the record does not have the expected fields")
    for key, kind in fields.items():
        value = data[key]
        if isinstance(value, bool) and kind is int:
            raise StateError(f"{where}: {key} has the wrong type")
        if not isinstance(value, kind):
            raise StateError(f"{where}: {key} has the wrong type")


class RunStore:
    """Reads and writes the records of one run directory."""

    def __init__(self, run_dir: Path) -> None:
        self.run_dir = run_dir
        self.root = run_dir / STATE_DIR
        self.run_file = self.root / "run.json"
        self.state_file = self.root / "state.json"
        self.reports_file = self.root / "reports.jsonl"
        self.effects_dir = self.root / "effects"
        self.lock_file = self.root / "lock"

    def relative(self, path: Path) -> str:
        return path.relative_to(self.run_dir).as_posix()

    # The lock

    @contextmanager
    def locked(self) -> Iterator[None]:
        """Hold the run's lock, or raise RunBusy."""
        self.root.mkdir(parents=True, exist_ok=True)
        with self.lock_file.open("a+b") as handle:
            try:
                _lock(handle)
            except OSError:
                raise RunBusy(f"another step is running on {self.run_dir}") from None
            try:
                yield
            finally:
                _unlock(handle)

    # Records

    def read_json(self, path: Path) -> dict[str, Any]:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            raise StateError(f"{path} cannot be read: {error}") from None
        if not isinstance(data, dict) or data.get("format") != FORMAT:
            raise StateError(f"{path} is not a record of format {FORMAT}")
        return data

    def load_state(self) -> dict[str, Any]:
        """The run's state. A run never stepped has the empty state; a
        missing state beside effect records cannot be trusted."""
        if not self.state_file.exists():
            if self.effect_files():
                raise StateError(
                    f"{self.state_file} is missing, but the run has effect records"
                )
            return copy.deepcopy(EMPTY_STATE)
        data = self.read_json(self.state_file)
        where = str(self.state_file)
        _check(data, STATE_FIELDS, where)
        for name, record in data["jobs"].items():
            _check(record, JOB_FIELDS, f"{where}, job {name}")
        _check(data["workflow"], WORKFLOW_FIELDS, f"{where}, workflow")
        for move in data["moves"]:
            _check(move, MOVE_FIELDS, f"{where}, moves")
        return data

    def save_state(self, state: dict[str, Any]) -> None:
        write_atomic(self.state_file, dump(state))

    def effect_files(self) -> list[Path]:
        return sorted(self.effects_dir.glob("*.json"))

    def load_effects(self) -> dict[str, dict[str, Any]]:
        effects = {}
        for path in self.effect_files():
            record = self.read_json(path)
            _check(record, EFFECT_FIELDS, str(path))
            if record["name"] != path.stem or record["status"] not in (
                "started",
                "completed",
            ):
                raise StateError(f"{path} does not agree with its name or status")
            effects[path.stem] = record
        return effects

    def save_effect(self, record: dict[str, Any]) -> None:
        write_atomic(self.effects_dir / f"{record['name']}.json", dump(record))

    def drop_effect(self, name: str) -> None:
        (self.effects_dir / f"{name}.json").unlink(missing_ok=True)

    def read_reports(self) -> list[dict[str, Any]]:
        if not self.reports_file.exists():
            return []
        reports = []
        try:
            lines = self.reports_file.read_text(encoding="utf-8").splitlines()
        except OSError as error:
            raise StateError(f"{self.reports_file} cannot be read: {error}") from None
        for number, line in enumerate(lines, start=1):
            try:
                record = json.loads(line)
            except ValueError:
                raise StateError(
                    f"{self.reports_file}, line {number}, is not a report"
                ) from None
            _check(record, REPORT_FIELDS, f"{self.reports_file}, line {number}")
            if record["format"] != FORMAT:
                raise StateError(
                    f"{self.reports_file}, line {number}, has another format"
                )
            reports.append(record)
        return reports

    def append_report(self, record: dict[str, Any]) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        with self.reports_file.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())

    # Files a step writes

    def job_dir(self, name: str) -> Path:
        return self.root / "jobs" / name

    def prompt_path(self, name: str) -> Path:
        return self.job_dir(name) / "prompt.md"

    def job_record_path(self, name: str, number: int) -> Path:
        return self.job_dir(name) / f"block-{number}.md"

    def kept_path(self, name: str, number: int, original: Path) -> Path:
        return self.job_dir(name) / "kept" / f"{number}-{original.name}"

    def workflow_record_path(self, number: int) -> Path:
        return self.root / "workflow" / f"block-{number}.md"

    def effect_record_path(self, name: str) -> Path:
        return self.root / "effect-blocks" / f"{name}.md"

    def move(self, moves: list[dict[str, str]]) -> None:
        """Move every listed file that is still in place with its recorded hash
        and whose target does not exist yet.

        Each target is a new path, so an existing target is the receipt of a
        finished move: a later file with the same bytes at the source is not
        moved again.
        """
        for move in moves:
            source = self.run_dir / move["source"]
            target = self.run_dir / move["target"]
            if target.exists() or file_sha(source) != move["sha"]:
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            os.replace(source, target)


def _lock(handle: BinaryIO) -> None:
    if fcntl is not None:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    else:  # pragma: no cover - Windows
        handle.seek(0)
        msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)


def _unlock(handle: BinaryIO) -> None:
    if fcntl is not None:
        fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
    else:  # pragma: no cover - Windows
        handle.seek(0)
        msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)

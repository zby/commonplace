"""Files under a run directory: the artifact, content-addressed versions and records.

The run directory holds `run.json`, the typed artifact under `artifact/`, and the
engine's state under `state/`: versions by content digest, attempt and
judgment records, and hand-out directories. Every file is written whole, by
rename, so a reader sees either the old file or the new one.

The store owns the commit protocol. An attempt is opened, then either
committed with its outputs and judgments, or failed. A commit writes the
judgments first and the attempt record last: the completed attempt record is
what makes its judgments count, so an interruption between the two leaves
judgments that every reader ignores.
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
import shutil
import threading
from collections.abc import Iterator, Sequence
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from .plan import OUTCOMES


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(record: Any) -> bytes:
    return (json.dumps(record, sort_keys=True, indent=1) + "\n").encode("utf-8")


# Run directories whose lock this process holds, so nested holders do not deadlock.
_HELD: set[Path] = set()
"""Runs this thread holds; re-entry is per thread, so another thread waits on the run's lock below."""
_LOCKS: dict[Path, threading.RLock] = {}
_LOCKS_GUARD = threading.Lock()


def attempt_id(seq: int, job: str) -> str:
    """An attempt's ID: its sequence number and its job."""
    return f"{seq:06d}-{job}"


class RunStore:
    def __init__(self, run_dir: Path) -> None:
        self.run_dir = run_dir
        self.metadata = run_dir / "run.json"
        self.artifact_dir = run_dir / "artifact"
        self.state = run_dir / "state"
        self.versions = self.state / "versions"
        self.attempts = self.state / "attempts"
        self.judgments = self.state / "judgments"
        self.handouts = self.state / "handouts"

    def create(self, metadata: dict) -> None:
        for directory in (self.artifact_dir, self.versions, self.attempts, self.judgments, self.handouts):
            directory.mkdir(parents=True, exist_ok=True)
        self.write_json(self.metadata, metadata)

    @contextmanager
    def lock(self) -> Iterator[None]:
        """Hold the run lock; re-entering it on the same thread is a no-op.

        Another thread of this process waits, as another process does on the
        file lock, so concurrent advances cannot race on sequence numbers.
        """
        key = self.run_dir.resolve()
        with _LOCKS_GUARD:
            local = _LOCKS.setdefault(key, threading.RLock())
        with local:
            if key in _HELD:
                yield
                return
            with open(self.state / "lock", "a") as handle:
                fcntl.flock(handle, fcntl.LOCK_EX)
                _HELD.add(key)
                try:
                    yield
                finally:
                    _HELD.discard(key)
                    fcntl.flock(handle, fcntl.LOCK_UN)

    # Writing

    @staticmethod
    def write_bytes(path: Path, data: bytes) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_name(f".{path.name}.tmp")
        temporary.write_bytes(data)
        os.replace(temporary, path)

    def write_json(self, path: Path, record: Any) -> None:
        self.write_bytes(path, canonical(record))

    def put(self, data: bytes) -> str:
        version = digest(data)
        path = self.versions / version
        if not path.exists():
            self.write_bytes(path, data)
        return version

    def get(self, version: str) -> bytes:
        return (self.versions / version).read_bytes()

    def next_seq(self) -> int:
        counter = self.state / "seq"
        seq = int(counter.read_text()) + 1 if counter.exists() else 1
        self.write_bytes(counter, f"{seq}\n".encode())
        return seq

    # Reading

    def read_metadata(self) -> dict:
        return json.loads(self.metadata.read_text(encoding="utf-8"))

    @staticmethod
    def _records(directory: Path) -> list[dict]:
        if not directory.is_dir():
            return []
        return [json.loads(path.read_text(encoding="utf-8"))
                for path in sorted(directory.glob("*.json"))]

    def attempt_records(self) -> list[dict]:
        records = self._records(self.attempts)
        for record in records:
            _check_attempt(record)
        return records

    def judgment_records(self) -> list[dict]:
        records = self._records(self.judgments)
        for record in records:
            _check_judgment(record)
        return records

    # Attempts and judgments

    def handout_dir(self, attempt: str) -> Path:
        return self.handouts / attempt

    def open_attempt(self, record: dict) -> None:
        """Record an attempt as open: handed out, not yet reported."""
        self._write_attempt({**record, "state": "open"})

    def commit_attempt(self, record: dict, judgments: Sequence[dict] = ()) -> None:
        """Complete an attempt with its judgments; the attempt record goes last."""
        for judgment in judgments:
            _check_judgment(judgment)
            self.write_json(self.judgments / f"{judgment['id']}.json", judgment)
        self._write_attempt({**record, "state": "completed",
                             "judgments": [judgment["id"] for judgment in judgments]})

    def fail_attempt(self, record: dict, reason: str, **details: Any) -> None:
        """Close an attempt as failed. A failed attempt records no inputs."""
        self._write_attempt({**record, **details, "state": "failed", "pins": {}, "reason": reason})

    def _write_attempt(self, record: dict) -> None:
        _check_attempt(record)
        self.write_json(self.attempts / f"{record['id']}.json", record)

    def remove(self, path: Path) -> None:
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()


class RecordError(ValueError):
    """A record under `state/` that does not have the shape the engine writes."""


ATTEMPT_STATES = ("open", "completed", "failed")
ATTEMPT_FIELDS = ("id", "seq", "job", "kind", "state", "pins")
JUDGMENT_FIELDS = ("id", "seq", "attempt", "job", "subject", "outcome", "installs",
                   "scope", "findings", "overrides", "basis")


def _check_attempt(record: Any) -> None:
    missing = [field for field in ATTEMPT_FIELDS if not isinstance(record, dict) or field not in record]
    if missing:
        raise RecordError(f"attempt record {record.get('id') if isinstance(record, dict) else record!r} "
                          f"lacks {', '.join(missing)}")
    if record["state"] not in ATTEMPT_STATES:
        raise RecordError(f"attempt record {record['id']}: state {record['state']!r} is not one of {ATTEMPT_STATES}")
    if record["state"] == "completed" and "outputs" not in record:
        raise RecordError(f"attempt record {record['id']}: a completed attempt names its outputs")
    if "uncertain" in record and not isinstance(record["uncertain"], bool):
        raise RecordError(f"attempt record {record['id']}: uncertain must be a boolean")


def _check_judgment(record: Any) -> None:
    missing = [field for field in JUDGMENT_FIELDS if not isinstance(record, dict) or field not in record]
    if missing:
        raise RecordError(f"judgment record {record.get('id') if isinstance(record, dict) else record!r} "
                          f"lacks {', '.join(missing)}")
    if record["outcome"] not in OUTCOMES:
        raise RecordError(f"judgment record {record['id']}: outcome {record['outcome']!r}")

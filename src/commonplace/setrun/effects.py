"""External effects a run's code jobs perform outside the engine's store.

The engine commits attempts; an effect that changes files elsewhere keeps its
own journal so a retry can recognize an earlier outcome instead of repeating
it. An outcome it cannot establish raises ``UncertainEffectError``.
"""
from __future__ import annotations

import fcntl
import json
import os
import re
import shutil
import tempfile
from collections.abc import Callable, Iterator, Mapping
from contextlib import contextmanager
from hashlib import sha256
from pathlib import Path

from commonplace.workflow import UncertainEffectError


def atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary_path = Path(temporary)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
    except Exception:
        temporary_path.unlink(missing_ok=True)
        raise



def tree(path: Path) -> dict[str, bytes] | None:
    if not os.path.lexists(path):
        return None
    if path.resolve() != path or not path.is_dir():
        raise UncertainEffectError(f"publication tree redirects or is not a directory: {path}")
    result = {}
    for file in path.iterdir():
        if not file.is_file() or file.is_symlink():
            raise UncertainEffectError(f"unexpected publication tree entry: {file}")
        result[file.name] = file.read_bytes()
    return result


def hashes(tree: Mapping[str, bytes] | None):
    return None if tree is None else {name: sha256(data).hexdigest() for name, data in sorted(tree.items())}


def safe(path: Path) -> Path:
    if path.resolve() != path:
        raise UncertainEffectError(f"publication path must not traverse symlinks: {path}")
    return path


def write_json(path: Path, record: dict) -> None:
    atomic_write(path, (json.dumps(record, sort_keys=True, indent=2) + "\n").encode())


def install_tree(*, journal: Path, destination: Path, archive_root: Path,
                 files: Mapping[str, bytes], anchor: str, expected: str, identity: Mapping[str, str],
                 archive_name: Callable[[Mapping[str, bytes]], str],
                 inspect_incumbent: Callable[[], None]) -> dict:
    """Install exact bytes as a directory, or recognize a journaled result.

    ``anchor`` names the member whose digest identifies the incumbent:
    ``expected`` is that digest, or ``absent`` for no incumbent.
    ``archive_name`` names the incumbent's archive directory under
    ``archive_root``. ``identity`` fields bind the journal to its run. A
    partial effect raises ``UncertainEffectError``.

    Caller holds the publication lock after any per-run engine lock, through
    journal recognition, incumbent inspection, mutation and rollback. Byte
    guards preserve detected unexpected writes, but cannot prevent TOCTOU from
    non-cooperating writers: those still require authority-level exclusivity.
    """
    destination, archive_root, journal = safe(destination), safe(archive_root), safe(journal)
    intent = {"version": 1, **identity, "destination": str(destination),
              "expected": expected, "new": hashes(files)}
    if journal.exists():
        try:
            record = json.loads(journal.read_bytes())
            if (not isinstance(record, dict) or any(record.get(k) != v for k, v in intent.items())
                    or set(record) != {*intent, "old", "archive", "state"}
                    or record["state"] not in ("started", "completed", "rolled-back")):
                raise ValueError("journal input identity or structure differs")
            old = record["old"]
            if old is not None and (not isinstance(old, dict) or anchor not in old
                    or any(Path(name).name != name or not re.fullmatch(r"[0-9a-f]{64}", str(value))
                           for name, value in old.items())):
                raise ValueError("invalid old tree identity")
            if ("absent" if old is None else old[anchor]) != expected:
                raise ValueError("old tree differs from opened incumbent")
            if (old is None) != (record["archive"] is None):
                raise ValueError("archive and old tree disagree")
            archive = Path(record["archive"]) if record["archive"] else None
            if archive is not None and (archive.parent != archive_root or archive.name in ("", ".", "..")):
                raise ValueError("invalid archive path")
            now = hashes(tree(destination))
            archived = hashes(tree(safe(archive))) if archive else None
            if now == intent["new"] and (old is None or archived == old):
                write_json(journal, {**record, "state": "completed"})
                return {"state": "published", "destination": str(destination), "members": intent["new"]}
            if record["state"] == "completed":
                raise ValueError("completed publication no longer has its exact bytes")
            if now != old or archived is not None:
                raise ValueError("interrupted publication is not its exact old or completed state")
        except (OSError, ValueError, TypeError, KeyError) as error:
            raise UncertainEffectError(f"cannot establish publication outcome: {error}") from error
    else:
        record = None
    # Full incumbent validation and source ownership precede any effect.
    inspect_incumbent()
    old_tree = tree(destination)
    actual = "absent" if old_tree is None else sha256(old_tree.get(anchor, b"")).hexdigest()
    if actual != expected:
        raise ValueError("publication destination changed since opening inspection")
    archive = None
    if old_tree is not None:
        name = archive_name(old_tree)
        if Path(name).name != name or name in ("", ".", ".."):
            raise ValueError("archive name must be one path component")
        archive = safe(archive_root / name)
        if os.path.lexists(archive):
            raise ValueError("archive destination already exists")
    if record is not None and (record["old"] != hashes(old_tree)
                               or record["archive"] != (str(archive) if archive else None)):
        raise UncertainEffectError("incumbent differs from journaled starting bytes")
    record = {**intent, "old": hashes(old_tree), "archive": str(archive) if archive else None, "state": "started"}
    write_json(journal, record)
    moved = created = False
    try:
        if tree(destination) != old_tree:
            raise ValueError("incumbent changed before mutation")
        if archive:
            archive.parent.mkdir(parents=True, exist_ok=True)
            destination.rename(archive)
            moved = True
        destination.mkdir(parents=True, exist_ok=False)
        created = True
        for name, data in files.items():
            if Path(name).name != name or name in (".", ".."):
                raise ValueError("publication members must be direct files")
            atomic_write(destination / name, data)
        if tree(destination) != dict(files):
            raise UncertainEffectError("installed publication bytes differ")
        write_json(journal, {**record, "state": "completed"})
    except Exception as error:
        try:
            if created:
                partial = tree(destination)
                if partial is None or any(name not in files or data != files[name] for name, data in partial.items()):
                    raise ValueError("new tree has unexpected bytes; preserve it")
                shutil.rmtree(destination)
            if moved:
                if hashes(tree(archive)) != record["old"]:
                    raise ValueError("archive changed; preserve it")
                if os.path.lexists(destination):
                    raise ValueError("destination reappeared; preserve it and the archive")
                archive.rename(destination)
            if tree(destination) != old_tree:
                raise ValueError("old state was not restored")
            write_json(journal, {**record, "state": "rolled-back"})
        except Exception as rollback:  # noqa: BLE001 - any rollback failure leaves an uncertain effect
            raise UncertainEffectError(f"publication failed ({error}); rollback uncertain ({rollback})") from error
        raise
    return {"state": "published", "destination": str(destination), "members": intent["new"]}


@contextmanager
def publication_lock(path: Path) -> Iterator[None]:
    """Serialize cooperating publishers through one lock file, including rollback.

    The lock file belongs in an ignored directory and persists. Never unlink
    it: waiters must keep using the same inode. Acquire any per-run lock
    first, then this lock; do not acquire a run lock while holding this one.
    This advisory lock is not exclusive ownership of publication files.
    Non-cooperating writes still require authority-level exclusivity.
    """
    if path.resolve() != path:
        raise ValueError("publication lock must not traverse symlinks")
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)

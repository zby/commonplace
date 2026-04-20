"""In-process CLI invoker used by review tests.

Replaces `subprocess.run([sys.executable, "-m", "commonplace.cli.review.X", ...])`
with an in-process call to the module's `main(argv, cwd=...)`. Captures stdout
and stderr, returns a subprocess.CompletedProcess-like result.
"""

from __future__ import annotations

import contextlib
import io
from importlib import import_module
from pathlib import Path
from types import SimpleNamespace


def run_cli(
    module: str,
    *args: str,
    cwd: Path,
    db_path: Path | None = None,
    check: bool = True,
) -> SimpleNamespace:
    mod = import_module(f"commonplace.cli.review.{module}")
    argv = list(args)
    if db_path is not None and "--db" not in argv:
        argv.extend(["--db", str(db_path)])
    stdout_buf = io.StringIO()
    stderr_buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(stdout_buf), contextlib.redirect_stderr(stderr_buf):
            rc = mod.main(argv, cwd=cwd)
    except SystemExit as exc:
        rc = exc.code if isinstance(exc.code, int) else 1
    result = SimpleNamespace(
        returncode=rc or 0,
        stdout=stdout_buf.getvalue(),
        stderr=stderr_buf.getvalue(),
    )
    if check and result.returncode != 0:
        raise AssertionError(
            f"CLI {module} exited {result.returncode}\nstderr: {result.stderr}\nstdout: {result.stdout}"
        )
    return result

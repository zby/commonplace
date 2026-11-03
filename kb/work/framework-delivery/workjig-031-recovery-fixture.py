"""Bounded Workjig 0.3.1 recovery acceptance fixture; no workers or source overlay.

Run with the Python interpreter belonging to the installed Commonplace uv tool.
The temporary records are deleted on exit. This is an acceptance fixture for the
next Windows run, not a Workjig repair or a Commonplace software test.
"""

from __future__ import annotations

import importlib.metadata
import json
import platform
import sys
import tempfile
from pathlib import Path


def main() -> None:
    distribution = importlib.metadata.distribution("workjig")
    version = distribution.version
    if version != "0.3.1":
        raise RuntimeError(f"Expected installed workjig 0.3.1, found {version}")
    import workjig
    from workjig import RecordError, Run, RunBusyError, busy, hold

    module_path = Path(workjig.__file__).resolve()
    distribution_root = distribution.locate_file("").resolve()
    direct_url = distribution.read_text("direct_url.json")
    if not module_path.is_relative_to(distribution_root):
        raise RuntimeError(f"Source overlay: {module_path} is outside {distribution_root}")
    if direct_url and json.loads(direct_url).get("dir_info", {}).get("editable"):
        raise RuntimeError("Expected a non-editable installed Workjig distribution")

    checks: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="workjig-031-recovery-") as scratch:
        workdir = Path(scratch)
        for name, contents in (("empty", b""), ("interrupted", b"interrupted")):
            records = workdir / name
            records.mkdir()
            lock = records / ".lock"
            lock.write_bytes(contents)
            errors: list[str] = []
            for _ in range(2):
                try:
                    with Run(records, workdir):
                        raise AssertionError("Run accepted interrupted first-open records")
                except RecordError as error:
                    assert "run record is missing" in str(error), str(error)
                    errors.append(str(error))
                assert lock.read_bytes() == contents
                assert not busy(records)
                with hold(records):
                    assert busy(records)
                    assert lock.read_bytes() == contents
                assert lock.read_bytes() == contents
                assert not busy(records)
                assert not (records / "run.json").exists()
            try:
                with Run(records, workdir):
                    raise AssertionError("hold reclassified interrupted records as fresh")
            except RecordError as error:
                assert "run record is missing" in str(error), str(error)
            assert lock.read_bytes() == contents
            assert not (records / "run.json").exists()
            assert not busy(records)
            checks.append({"case": name, "result": "pass", "lock_hex": contents.hex(),
                           "run_rejected": True, "hold_preserved_bytes": True,
                           "repetitions": 2, "record_error": errors[0]})

        fresh = workdir / "fresh-run"
        with Run(fresh, workdir):
            assert busy(fresh)
            try:
                with hold(fresh):
                    raise AssertionError("hold acquired a lock already owned by Run")
            except RunBusyError:
                pass
        assert (fresh / "run.json").is_file()
        assert not busy(fresh)
        checks.append({"case": "fresh-run", "result": "pass", "run_json_created": True})

        held = workdir / "fresh-hold"
        for _ in range(2):
            with hold(held):
                assert busy(held)
                try:
                    with Run(held, workdir):
                        raise AssertionError("Run acquired a lock already owned by hold")
                except RunBusyError:
                    pass
            assert not busy(held)
        with Run(held, workdir):
            pass
        assert (held / "run.json").is_file()
        checks.append({"case": "fresh-hold-then-run", "result": "pass",
                       "run_json_created": True, "repetitions": 2})

        result = {"fixture": "workjig-031-recovery", "platform": platform.platform(),
                  "python": sys.version, "executable": sys.executable,
                  "workjig_version": version, "workjig_module": str(module_path),
                  "distribution_root": str(distribution_root), "direct_url": direct_url,
                  "checks": checks, "temporary_root": scratch}
    result["temporary_root_removed"] = not Path(scratch).exists()
    assert result["temporary_root_removed"]
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

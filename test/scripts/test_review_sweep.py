from __future__ import annotations

import json
import os
import stat
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = REPO_ROOT / "scripts" / "review_sweep.sh"


def write_executable(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")
    path.chmod(path.stat().st_mode | stat.S_IXUSR)


def make_fake_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    (repo / "scripts").mkdir(parents=True, exist_ok=True)
    (repo / "kb" / "instructions" / "review-gates" / "prose").mkdir(parents=True, exist_ok=True)
    return repo


def test_review_sweep_aborts_immediately_on_usage_exhaustion(tmp_path: Path) -> None:
    repo = make_fake_repo(tmp_path)
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()

    selector_output = [
        {"note_path": "kb/notes/first.md", "gate_id": "prose/source-residue"},
        {"note_path": "kb/notes/second.md", "gate_id": "prose/source-residue"},
    ]
    selector_path = tmp_path / "selector.json"
    selector_path.write_text(json.dumps(selector_output), encoding="utf-8")

    bundle_log = tmp_path / "run_review_bundle.log"

    write_executable(
        bin_dir / "uv",
        f"""#!/usr/bin/env bash
if [[ "$1" == "run" && "$2" == "scripts/gate_selector.py" ]]; then
  cat "{selector_path}"
  exit 0
fi
if [[ "$1" == "run" && "$2" == "scripts/run_review_bundle.py" ]]; then
  printf "invoked\\n" >> "{bundle_log}"
  printf "%s\\n" "You're out of extra usage · resets at 7pm"
  exit 1
fi
echo "unexpected uv args: $*" >&2
exit 2
""",
    )

    env = os.environ.copy()
    env["PATH"] = f"{bin_dir}:{env['PATH']}"
    env["COMMONPLACE_REVIEW_MODEL"] = "test-model"

    result = subprocess.run(
        ["bash", str(SCRIPT_PATH), "prose"],
        cwd=repo,
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )

    assert result.returncode == 1
    assert "You're out of extra usage" in result.stdout
    assert "aborting sweep immediately" in result.stderr
    assert bundle_log.read_text(encoding="utf-8").splitlines() == ["invoked"]

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
if [[ "$1" == "run" && "$2" == "scripts/review_target_selector.py" ]]; then
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
    env["REVIEW_SWEEP_JOBS"] = "1"

    result = subprocess.run(
        ["bash", str(SCRIPT_PATH), "--model", "test-model", "prose"],
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


def test_review_sweep_passes_current_flag_to_selector(tmp_path: Path) -> None:
    repo = make_fake_repo(tmp_path)
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()

    selector_log = tmp_path / "selector.log"

    write_executable(
        bin_dir / "uv",
        f"""#!/usr/bin/env bash
if [[ "$1" == "run" && "$2" == "scripts/review_target_selector.py" ]]; then
  printf "%s\\n" "$*" > "{selector_log}"
  printf "[]"
  exit 0
fi
echo "unexpected uv args: $*" >&2
exit 2
""",
    )

    env = os.environ.copy()
    env["PATH"] = f"{bin_dir}:{env['PATH']}"

    result = subprocess.run(
        ["bash", str(SCRIPT_PATH), "--model", "test-model", "--current", "prose"],
        cwd=repo,
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )

    assert result.returncode == 0
    logged = selector_log.read_text(encoding="utf-8")
    assert "scripts/review_target_selector.py --model test-model prose --json --current" in logged


def test_review_sweep_runs_up_to_four_reviews_in_parallel_by_default(tmp_path: Path) -> None:
    repo = make_fake_repo(tmp_path)
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()

    selector_output = [
        {"note_path": f"kb/notes/note-{idx}.md", "gate_id": "prose/source-residue"}
        for idx in range(5)
    ]
    selector_path = tmp_path / "selector.json"
    selector_path.write_text(json.dumps(selector_output), encoding="utf-8")

    lock_dir = tmp_path / "lock"
    current_file = tmp_path / "current.txt"
    max_file = tmp_path / "max.txt"

    write_executable(
        bin_dir / "uv",
        f"""#!/usr/bin/env bash
if [[ "$1" == "run" && "$2" == "scripts/review_target_selector.py" ]]; then
  cat "{selector_path}"
  exit 0
fi
if [[ "$1" == "run" && "$2" == "scripts/run_review_bundle.py" ]]; then
  while ! mkdir "{lock_dir}" 2>/dev/null; do sleep 0.01; done
  current=0
  max_seen=0
  if [[ -f "{current_file}" ]]; then
    current=$(cat "{current_file}")
  fi
  if [[ -f "{max_file}" ]]; then
    max_seen=$(cat "{max_file}")
  fi
  current=$((current + 1))
  if (( current > max_seen )); then
    max_seen=$current
  fi
  printf "%s" "$current" > "{current_file}"
  printf "%s" "$max_seen" > "{max_file}"
  rmdir "{lock_dir}"
  sleep 0.2
  while ! mkdir "{lock_dir}" 2>/dev/null; do sleep 0.01; done
  current=$(cat "{current_file}")
  current=$((current - 1))
  printf "%s" "$current" > "{current_file}"
  rmdir "{lock_dir}"
  printf "completed %s\\n" "$5"
  exit 0
fi
echo "unexpected uv args: $*" >&2
exit 2
""",
    )

    env = os.environ.copy()
    env["PATH"] = f"{bin_dir}:{env['PATH']}"

    result = subprocess.run(
        ["bash", str(SCRIPT_PATH), "--model", "test-model", "prose"],
        cwd=repo,
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )

    assert result.returncode == 0
    assert "Reviewed: 5 notes" in result.stdout
    assert int(max_file.read_text(encoding="utf-8")) >= 4


def test_review_sweep_passes_runner_to_run_review_bundle(tmp_path: Path) -> None:
    repo = make_fake_repo(tmp_path)
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()

    selector_output = [
        {"note_path": "kb/notes/first.md", "gate_id": "prose/source-residue"},
    ]
    selector_path = tmp_path / "selector.json"
    selector_path.write_text(json.dumps(selector_output), encoding="utf-8")

    bundle_log = tmp_path / "bundle.log"

    write_executable(
        bin_dir / "uv",
        f"""#!/usr/bin/env bash
if [[ "$1" == "run" && "$2" == "scripts/review_target_selector.py" ]]; then
  cat "{selector_path}"
  exit 0
fi
if [[ "$1" == "run" && "$2" == "scripts/run_review_bundle.py" ]]; then
  printf "%s\\n" "$*" > "{bundle_log}"
  printf "completed 1 1\\n"
  exit 0
fi
echo "unexpected uv args: $*" >&2
exit 2
""",
    )

    env = os.environ.copy()
    env["PATH"] = f"{bin_dir}:{env['PATH']}"
    env["REVIEW_SWEEP_JOBS"] = "1"

    result = subprocess.run(
        ["bash", str(SCRIPT_PATH), "--model", "test-model", "--runner", "codex", "--current", "prose"],
        cwd=repo,
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )

    assert result.returncode == 0
    logged = bundle_log.read_text(encoding="utf-8")
    assert "scripts/run_review_bundle.py --runner codex --model test-model kb/notes/first.md prose/source-residue" in logged

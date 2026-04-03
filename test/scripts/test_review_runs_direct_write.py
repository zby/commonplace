from __future__ import annotations

import importlib.util
import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


review_db = load_module("review_db_review_runs_test", SCRIPTS_DIR / "review_db.py")
review_metadata = load_module("review_metadata_review_runs_test", SCRIPTS_DIR / "review_metadata.py")
run_review_bundle = load_module("run_review_bundle_review_runs_test", SCRIPTS_DIR / "run_review_bundle.py")
warn_selector = load_module("warn_selector_review_runs_test", SCRIPTS_DIR / "warn_selector.py")


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_note(path: Path, title: str, body: str) -> Path:
    return write(
        path,
        f"""---
description: Test note
type: note
traits: []
status: current
---

# {title}
{body}
""",
    )


def make_gate(path: Path, gate_id: str, lens: str) -> Path:
    return write(
        path,
        f"""---
gate_id: {gate_id}
name: {path.stem.replace("-", " ").title()}
lens: {lens}
watches: [body]
staleness: changed
---

## Failure mode

Fixture gate.

## Test

Fixture test.
""",
    )


def init_repo(path: Path) -> None:
    subprocess.run(["git", "init"], cwd=path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Test User"], cwd=path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=path, check=True, capture_output=True)


def commit_all(path: Path, message: str) -> str:
    subprocess.run(["git", "add", "."], cwd=path, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", message], cwd=path, check=True, capture_output=True)
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=path, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def build_repo_fixture(tmp_path: Path) -> tuple[Path, Path]:
    repo = tmp_path / "repo"
    repo.mkdir()
    init_repo(repo)

    note = make_note(repo / "kb" / "notes" / "sample.md", "Sample", "\nBody.\n")
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "prose" / "source-residue.md",
        "prose/source-residue",
        "prose",
    )
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "semantic" / "grounding-alignment.md",
        "semantic/grounding-alignment",
        "semantic",
    )
    commit_all(repo, "fixture")
    db_path = repo / "kb" / "reports" / "review-store.sqlite"
    return repo, db_path


def run_script(repo: Path, script_name: str, *args: str, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / script_name), *args],
        cwd=repo,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )


def test_create_write_finalize_review_run(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_MODEL"] = "test-model"
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose",
        "semantic/grounding-alignment",
        "--runner",
        "codex",
        env=env,
    )
    review_run_id = int(created.stdout.strip())

    prose_review = write(
        repo / "tmp" / "prose.md",
        """## Findings

**WARN — Residue remains.** The note still carries a domain-specific term.
""",
    )
    semantic_review = write(
        repo / "tmp" / "semantic.md",
        """## Result: PASS

Grounding is aligned.
""",
    )

    prose_result = run_script(
        repo,
        "write_gate_review.py",
        "--review-run-id",
        str(review_run_id),
        "--gate-id",
        "prose/source-residue",
        "--input-file",
        str(prose_review),
        env=env,
    )
    semantic_result = run_script(
        repo,
        "write_gate_review.py",
        "--review-run-id",
        str(review_run_id),
        "--gate-id",
        "semantic/grounding-alignment",
        "--input-file",
        str(semantic_review),
        env=env,
    )
    assert int(prose_result.stdout.strip()) > 0
    assert int(semantic_result.stdout.strip()) > 0

    finalized = run_script(
        repo,
        "finalize_review_run.py",
        "--review-run-id",
        str(review_run_id),
        env=env,
    )
    assert finalized.stdout.strip() == f"completed {review_run_id} 2"

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run_row = conn.execute("SELECT status FROM review_runs WHERE id = ?", (review_run_id,)).fetchone()
        assert run_row["status"] == "completed"
        gate_rows = conn.execute(
            "SELECT review_run_id, gate_id, decision FROM gate_reviews WHERE review_run_id = ? ORDER BY gate_id",
            (review_run_id,),
        ).fetchall()
        assert [(row["gate_id"], row["decision"]) for row in gate_rows] == [
            ("prose/source-residue", "concern"),
            ("semantic/grounding-alignment", "pass"),
        ]
        acceptance_rows = conn.execute(
            "SELECT gate_id, accepted_review_id, acceptance_kind FROM acceptance_events ORDER BY gate_id"
        ).fetchall()
        assert len(acceptance_rows) == 2
        assert all(row["accepted_review_id"] is not None for row in acceptance_rows)
        assert all(row["acceptance_kind"] == "full-review" for row in acceptance_rows)


def test_create_review_run_json_output(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_MODEL"] = "test-model"
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose",
        "semantic/grounding-alignment",
        "--runner",
        "codex",
        "--json",
        env=env,
    )
    payload = json.loads(created.stdout)
    assert payload["note_path"] == "kb/notes/sample.md"
    assert payload["model_id"] == "test-model"
    assert payload["runner"] == "codex"
    assert payload["gate_ids"] == [
        "prose/source-residue",
        "semantic/grounding-alignment",
    ]
    assert payload["gates"] == [
        {
            "gate_id": "prose/source-residue",
            "path": "kb/instructions/review-gates/prose/source-residue.md",
            "text": "## Failure mode\n\nFixture gate.\n\n## Test\n\nFixture test.\n",
        },
        {
            "gate_id": "semantic/grounding-alignment",
            "path": "kb/instructions/review-gates/semantic/grounding-alignment.md",
            "text": "## Failure mode\n\nFixture gate.\n\n## Test\n\nFixture test.\n",
        },
    ]
    assert isinstance(payload["review_run_id"], int)


def test_duplicate_gate_write_fails_within_run(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_MODEL"] = "test-model"
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose/source-residue",
        "--runner",
        "codex",
        env=env,
    )
    review_run_id = int(created.stdout.strip())
    review_file = write(repo / "tmp" / "review.md", "## Result: PASS\n\nLooks good.\n")

    run_script(
        repo,
        "write_gate_review.py",
        "--review-run-id",
        str(review_run_id),
        "--gate-id",
        "prose/source-residue",
        "--input-file",
        str(review_file),
        env=env,
    )

    duplicate = subprocess.run(
        [
            sys.executable,
            str(SCRIPTS_DIR / "write_gate_review.py"),
            "--review-run-id",
            str(review_run_id),
            "--gate-id",
            "prose/source-residue",
            "--input-file",
            str(review_file),
        ],
        cwd=repo,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )
    assert duplicate.returncode != 0
    assert "UNIQUE constraint failed" in duplicate.stderr


def test_warn_selector_uses_latest_review_when_acceptance_has_no_review_id(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_MODEL"] = "test-model"
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose/source-residue",
        "--runner",
        "codex",
        env=env,
    )
    review_run_id = int(created.stdout.strip())
    review_file = write(
        repo / "tmp" / "review.md",
        """## Findings

**WARN — Fix me.** This warning should remain visible after an ack.
""",
    )
    gate_review_id = int(
        run_script(
            repo,
            "write_gate_review.py",
            "--review-run-id",
            str(review_run_id),
            "--gate-id",
            "prose/source-residue",
            "--input-file",
            str(review_file),
            env=env,
        ).stdout.strip()
    )
    run_script(
        repo,
        "finalize_review_run.py",
        "--review-run-id",
        str(review_run_id),
        env=env,
    )

    note_path = repo / "kb" / "notes" / "sample.md"
    note_path.write_text(note_path.read_text(encoding="utf-8") + "\nTrivial.\n", encoding="utf-8")
    commit_all(repo, "trivial note change")

    with review_db.connect(db_path) as conn:
        review_run = review_db.load_review_run(conn, review_run_id=review_run_id)
        assert review_run is not None
        gate_row = review_db.load_review_run_gates(conn, review_run_id=review_run_id)[0]
        review_db.append_acceptance_event(
            conn,
            note_path=review_run.note_path,
            gate_id=gate_row.gate_id,
            model_id=review_run.model_id,
            accepted_review_id=None,
            accepted_note_sha=review_metadata.git_blob_sha(note_path, write_object=True),
            accepted_note_commit=review_metadata.last_commit_for_path(repo, Path("kb/notes/sample.md")),
            accepted_gate_sha=gate_row.gate_sha,
            accepted_at=review_metadata.iso_now(),
            acceptance_kind="trivial-change-ack",
        )
        conn.commit()

    result = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "warn_selector.py"), "--json", "kb/notes/sample.md"],
        cwd=repo,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    assert payload[0]["note_path"] == "kb/notes/sample.md"
    warn = payload[0]["warns"][0]
    assert warn["review_id"] == gate_review_id
    assert "Fix me" in warn["text"]
    assert "Fix me" in warn["review_text"]


def test_run_review_bundle_with_fake_claude(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    fake_claude = fake_bin / "claude"
    fake_claude.write_text(
        f"""#!/usr/bin/env python3
import json
import sys

for event in [
    {{"type": "system", "subtype": "init"}},
    {{
        "type": "assistant",
        "message": {{
            "id": "msg-1",
            "content": [
                {{"type": "text", "text": "Working through the requested links.\\n"}},
                {{"type": "tool_use", "name": "Read", "input": {{"file_path": "kb/notes/sample.md"}}}},
            ],
        }},
    }},
    {{
        "type": "assistant",
        "message": {{
            "id": "msg-2",
            "content": [
                {{
                    "type": "text",
                    "text": "# Review Bundle\\n\\nReview run id: 1\\nTarget: kb/notes/sample.md\\n\\n=== GATE REVIEW START: prose/source-residue ===\\n## Findings\\n\\n**WARN — Residue remains.** Temporary review.\\n=== GATE REVIEW END: prose/source-residue ===\\n\\n=== GATE REVIEW START: semantic/grounding-alignment ===\\n## Result: PASS\\n\\nLooks good.\\n=== GATE REVIEW END: semantic/grounding-alignment ===\\n",
                }},
            ],
        }},
    }},
    {{"type": "result", "subtype": "success", "is_error": False, "result": "done"}},
]:
    print(json.dumps(event), flush=True)
""",
        encoding="utf-8",
    )
    fake_claude.chmod(0o755)

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_MODEL"] = "test-model"
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    env["PATH"] = f"{fake_bin}:{env['PATH']}"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPTS_DIR / "run_review_bundle.py"),
            "kb/notes/sample.md",
            "prose",
            "semantic/grounding-alignment",
            "--runner",
            "claude-code",
            "--db",
            str(db_path),
        ],
        cwd=repo,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "completed" in result.stdout

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run_count = conn.execute("SELECT count(*) FROM review_runs").fetchone()[0]
        gate_count = conn.execute("SELECT count(*) FROM gate_reviews").fetchone()[0]
        acceptance_count = conn.execute("SELECT count(*) FROM acceptance_events").fetchone()[0]
        raw_bundle = conn.execute("SELECT raw_bundle_markdown FROM review_runs").fetchone()[0]
        assert run_count == 1
        assert gate_count == 2
        assert acceptance_count == 2
        assert "=== GATE REVIEW START: prose/source-residue ===" in raw_bundle


def test_extract_bundle_reviews_ignores_text_outside_gate_blocks() -> None:
    bundle = """Working notes before the bundle.

# Review Bundle

=== GATE REVIEW START: prose/source-residue ===
## Findings

**WARN — Residue remains.**
=== GATE REVIEW END: prose/source-residue ===

Extra trailing note.

=== GATE REVIEW START: semantic/grounding-alignment ===
## Result: PASS

Looks good.
=== GATE REVIEW END: semantic/grounding-alignment ===
"""

    parsed = run_review_bundle.extract_bundle_reviews(
        bundle,
        expected_gate_ids=["prose/source-residue", "semantic/grounding-alignment"],
    )

    assert parsed["prose/source-residue"].startswith("## Findings")
    assert parsed["semantic/grounding-alignment"].startswith("## Result: PASS")


def test_run_review_bundle_parse_failure_persists_raw_bundle(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    fake_claude = fake_bin / "claude"
    fake_claude.write_text(
        """#!/usr/bin/env python3
import json

for event in [
    {"type": "system", "subtype": "init"},
    {
        "type": "assistant",
        "message": {
            "id": "msg-1",
            "content": [
                {
                    "type": "text",
                    "text": "# Review Bundle\\n\\n=== GATE REVIEW START: prose/source-residue ===\\n## Findings\\n\\n**WARN — Residue remains.**\\n=== GATE REVIEW END: prose/source-residue ===\\n",
                },
            ],
        },
    },
    {"type": "result", "subtype": "success", "is_error": False, "result": "done"},
]:
    print(json.dumps(event), flush=True)
""",
        encoding="utf-8",
    )
    fake_claude.chmod(0o755)

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_MODEL"] = "test-model"
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    env["PATH"] = f"{fake_bin}:{env['PATH']}"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPTS_DIR / "run_review_bundle.py"),
            "kb/notes/sample.md",
            "prose",
            "semantic/grounding-alignment",
            "--runner",
            "claude-code",
            "--db",
            str(db_path),
        ],
        cwd=repo,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run_row = conn.execute(
            "SELECT status, failure_reason, raw_bundle_markdown FROM review_runs"
        ).fetchone()
        assert run_row["status"] == "failed"
        assert "missing gate reviews in bundle output" in run_row["failure_reason"]
        assert "=== GATE REVIEW START: prose/source-residue ===" in run_row["raw_bundle_markdown"]

from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

from commonplace.review import review_db, review_metadata, run_review_bundle
from commonplace.review.finalization import record_and_finalize_run
from commonplace.review.protocol.parser import extract_bundle_reviews


REPO_ROOT = Path(__file__).resolve().parents[3]

TEST_MODEL = "test-model"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_note(path: Path, title: str, body: str, *, traits: str = "[]", note_type: str = "kb/types/note.md") -> Path:
    return write(
        path,
        f"""---
description: Test note
type: {note_type}
traits: {traits}
status: current
---

# {title}
{body}
""",
    )


def make_gate(
    path: Path,
    gate_id: str,
    lens: str,
    *,
    requires_trait: str | None = None,
    requires_type: str | None = None,
) -> Path:
    requires_trait_line = f"requires_trait: {requires_trait}\n" if requires_trait else ""
    requires_type_line = f"requires-type: {requires_type}\n" if requires_type else ""
    return write(
        path,
        f"""---
gate_id: {gate_id}
name: {path.stem.replace("-", " ").title()}
lens: {lens}
watches: [body]
staleness: changed
{requires_trait_line}{requires_type_line}---

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

    make_note(repo / "kb" / "notes" / "sample.md", "Sample", "\nBody.\n")
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


def build_repo_fixture_with_trait_gate(tmp_path: Path) -> tuple[Path, Path]:
    repo = tmp_path / "repo"
    repo.mkdir()
    init_repo(repo)

    make_note(repo / "kb" / "notes" / "sample.md", "Sample", "\nBody.\n")
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "prose" / "source-residue.md",
        "prose/source-residue",
        "prose",
    )
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "frontmatter" / "claim-strength.md",
        "frontmatter/claim-strength",
        "frontmatter",
        requires_trait="title-as-claim",
    )
    commit_all(repo, "fixture")
    db_path = repo / "kb" / "reports" / "review-store.sqlite"
    return repo, db_path


def build_repo_fixture_with_type_gate(tmp_path: Path) -> tuple[Path, Path]:
    repo = tmp_path / "repo"
    repo.mkdir()
    init_repo(repo)

    make_note(repo / "kb" / "notes" / "sample.md", "Sample", "\nBody.\n", note_type="kb/types/definition.md")
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "prose" / "source-residue.md",
        "prose/source-residue",
        "prose",
    )
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "frontmatter" / "definition-precision.md",
        "frontmatter/definition-precision",
        "frontmatter",
        requires_type="kb/types/definition.md",
    )
    make_gate(
        repo / "kb" / "instructions" / "review-gates" / "frontmatter" / "related-system-fit.md",
        "frontmatter/related-system-fit",
        "frontmatter",
        requires_type="kb/types/note.md",
    )
    commit_all(repo, "fixture")
    db_path = repo / "kb" / "reports" / "review-store.sqlite"
    return repo, db_path


def install_fake_codex_bundle_runner(fake_codex: Path, *, reasoning_effort: str = "xhigh") -> None:
    session_id = "019d6000-17a2-73b0-b341-3f36434aa48b"
    fake_codex.write_text(
        f"""#!/usr/bin/env python3
import json
import os
from pathlib import Path

session_id = "{session_id}"
home = Path(os.environ["HOME"])
session_dir = home / ".codex" / "sessions" / "2026" / "04" / "04"
session_dir.mkdir(parents=True, exist_ok=True)
session_log = session_dir / f"rollout-2026-04-04T09-00-00-{{session_id}}.jsonl"
prompt = os.sys.argv[-1]
events = [
    {{
        "type": "session_meta",
        "payload": {{
            "id": session_id,
            "timestamp": "2026-04-04T07:00:00.000Z",
            "cwd": os.getcwd(),
            "originator": "codex_exec",
            "cli_version": "0.0.0",
            "model_provider": "openai",
        }},
    }},
    {{
        "type": "turn_context",
        "payload": {{
            "cwd": os.getcwd(),
            "approval_policy": "never",
            "sandbox_policy": {{
                "type": "workspace-write",
                "writable_roots": [os.getcwd()],
                "network_access": True,
            }},
            "model": "gpt-5.4",
            "collaboration_mode": {{
                "mode": "default",
                "settings": {{
                    "model": "gpt-5.4",
                    "reasoning_effort": "{reasoning_effort}",
                }},
            }},
            "effort": "{reasoning_effort}",
        }},
    }},
    {{
        "type": "response_item",
        "payload": {{
            "type": "message",
            "role": "user",
            "content": [{{"type": "input_text", "text": prompt}}],
        }},
    }},
    {{
        "type": "event_msg",
        "payload": {{
            "type": "task_started",
            "turn_id": "turn-1",
        }},
    }},
    {{
        "type": "event_msg",
        "payload": {{
            "type": "token_count",
            "info": {{
                "model_context_window": 272000,
                "last_token_usage": {{
                    "input_tokens": 100,
                    "cached_input_tokens": 50,
                    "output_tokens": 25,
                    "reasoning_output_tokens": 10,
                    "total_tokens": 175,
                }},
                "total_token_usage": {{
                    "input_tokens": 100,
                    "cached_input_tokens": 50,
                    "output_tokens": 25,
                    "reasoning_output_tokens": 10,
                    "total_tokens": 175,
                }},
            }},
            "rate_limits": {{"primary": {{"used_percent": 7}}}},
        }},
    }},
    {{
        "type": "event_msg",
        "payload": {{
            "type": "task_complete",
            "turn_id": "turn-1",
            "last_agent_message": "=== GATE REVIEW START: prose/source-residue ===\\nNeeds revision.\\n\\n## Result: WARN\\n=== GATE REVIEW END: prose/source-residue ===\\n\\n=== GATE REVIEW START: semantic/grounding-alignment ===\\nLooks good.\\n\\n## Result: PASS\\n=== GATE REVIEW END: semantic/grounding-alignment ===",
        }},
    }},
]
with session_log.open("w", encoding="utf-8") as handle:
    for event in events:
        handle.write(json.dumps(event) + "\\n")

print(f"session id: {{session_id}}", flush=True)
print("=== GATE REVIEW START: prose/source-residue ===", flush=True)
print("Needs revision.", flush=True)
print("", flush=True)
print("## Result: WARN", flush=True)
print("=== GATE REVIEW END: prose/source-residue ===", flush=True)
print("", flush=True)
print("=== GATE REVIEW START: semantic/grounding-alignment ===", flush=True)
print("Looks good.", flush=True)
print("", flush=True)
print("## Result: PASS", flush=True)
print("=== GATE REVIEW END: semantic/grounding-alignment ===", flush=True)
""",
        encoding="utf-8",
    )
    fake_codex.chmod(0o755)


def run_script(repo: Path, script_name: str, *args: str, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    module_name = Path(script_name).stem
    return subprocess.run(
        [sys.executable, "-m", f"commonplace.cli.review.{module_name}", *args],
        cwd=repo,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )


def test_create_write_finalize_review_run(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose",
        "semantic/grounding-alignment",
        "--runner",
        "codex",
        "--model",
        TEST_MODEL,
        env=env,
    )
    review_run_id = int(created.stdout.strip())
    assert run_review_bundle.bundle_artifact_dir(repo, review_run_id).is_dir()

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
            ("prose/source-residue", "warn"),
            ("semantic/grounding-alignment", "pass"),
        ]
        semantic_row = conn.execute(
            """
            SELECT rationale_markdown
            FROM gate_reviews
            WHERE review_run_id = ? AND gate_id = ?
            """,
            (review_run_id, "semantic/grounding-alignment"),
        ).fetchone()
        assert semantic_row is not None
        assert semantic_row["rationale_markdown"] == "Grounding is aligned.\n\n## Result: PASS\n"
        acceptance_rows = conn.execute(
            "SELECT gate_id, accepted_review_id, acceptance_kind FROM acceptance_events ORDER BY gate_id"
        ).fetchall()
        assert len(acceptance_rows) == 2
        assert all(row["accepted_review_id"] is not None for row in acceptance_rows)
        assert all(row["acceptance_kind"] == "full-review" for row in acceptance_rows)


def test_ingest_bundle_output_finalizes_review_run(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose",
        "semantic/grounding-alignment",
        "--runner",
        "codex",
        "--model",
        TEST_MODEL,
        "--with-prompt",
        env=env,
    )
    payload = json.loads(created.stdout)
    review_run_id = payload["review_run_id"]
    bundle_output_path = repo / payload["bundle_output_path"]
    write(
        bundle_output_path,
        """# Review Bundle

=== GATE REVIEW START: prose/source-residue ===
## Findings

**WARN — Residue remains.** Temporary review.
=== GATE REVIEW END: prose/source-residue ===

=== GATE REVIEW START: semantic/grounding-alignment ===
Looks good.

## Result: PASS
=== GATE REVIEW END: semantic/grounding-alignment ===
""",
    )

    result = run_script(
        repo,
        "ingest_bundle_output.py",
        "--review-run-id",
        str(review_run_id),
        "--input-file",
        str(bundle_output_path),
        env=env,
    )

    assert result.stdout.strip() == f"completed {review_run_id} 2"

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run_row = conn.execute(
            "SELECT status, raw_bundle_markdown FROM review_runs WHERE id = ?",
            (review_run_id,),
        ).fetchone()
        assert run_row is not None
        assert run_row["status"] == "completed"
        assert "## Result: WARN" in run_row["raw_bundle_markdown"]
        gate_rows = conn.execute(
            "SELECT gate_id, decision FROM gate_reviews WHERE review_run_id = ? ORDER BY gate_id",
            (review_run_id,),
        ).fetchall()
        assert [(row["gate_id"], row["decision"]) for row in gate_rows] == [
            ("prose/source-residue", "warn"),
            ("semantic/grounding-alignment", "pass"),
        ]
        acceptance_rows = conn.execute(
            "SELECT gate_id, accepted_review_id FROM acceptance_events ORDER BY gate_id"
        ).fetchall()
        assert len(acceptance_rows) == 2
        assert all(row["accepted_review_id"] is not None for row in acceptance_rows)

    artifact_dir = run_review_bundle.bundle_artifact_dir(repo, review_run_id)
    assert (artifact_dir / "bundle-output.md").is_file()
    assert (artifact_dir / "prose__source-residue.md").is_file()
    assert (artifact_dir / "semantic__grounding-alignment.md").is_file()


def test_create_review_run_json_output(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose",
        "semantic/grounding-alignment",
        "--runner",
        "codex",
        "--model",
        TEST_MODEL,
        "--json",
        env=env,
    )
    payload = json.loads(created.stdout)
    assert run_review_bundle.bundle_artifact_dir(repo, payload["review_run_id"]).is_dir()
    assert payload["note_path"] == "kb/notes/sample.md"
    assert payload["model_id"] == TEST_MODEL
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


def test_create_review_run_with_prompt_uses_bundle_prompt_artifact(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose",
        "semantic/grounding-alignment",
        "--runner",
        "codex",
        "--model",
        TEST_MODEL,
        "--with-prompt",
        env=env,
    )

    payload = json.loads(created.stdout)
    review_run_id = payload["review_run_id"]
    artifact_dir = run_review_bundle.bundle_artifact_dir(repo, review_run_id)
    prompt_path = repo / payload["prompt_path"]

    assert payload["artifact_dir"] == f"kb/reports/bundle-reviews/review-run-{review_run_id}"
    assert payload["bundle_output_path"] == f"kb/reports/bundle-reviews/review-run-{review_run_id}/bundle-output.md"
    assert payload["prompt_path"] == f"kb/reports/bundle-reviews/review-run-{review_run_id}/prompt.md"
    assert "prompt" not in payload
    assert prompt_path.is_file()
    prompt_text = prompt_path.read_text(encoding="utf-8")
    assert "Write gate reviews for kb/notes/sample.md" in prompt_text
    assert f"Write exactly one markdown document to `{payload['bundle_output_path']}`." in prompt_text
    assert "Return exactly one markdown document in this process's stdout." not in prompt_text
    assert "=== GATE REVIEW START: prose/source-residue ===" in prompt_text
    assert "Requested gate definitions (authoritative for this run):" in prompt_text
    assert artifact_dir.is_dir()
    assert not (artifact_dir / "bundle-output.md").exists()


def test_create_review_run_allows_dirty_note_and_records_worktree_provenance(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    note_path = repo / "kb" / "notes" / "sample.md"
    note_path.write_text(note_path.read_text(encoding="utf-8") + "\nDirty change.\n", encoding="utf-8")

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.cli.review.create_review_run",
            "kb/notes/sample.md",
            "prose",
            "--runner",
            "codex",
            "--model",
            TEST_MODEL,
        ],
        cwd=repo,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    review_run_id = int(result.stdout.strip())
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT reviewed_note_sha, reviewed_note_commit FROM review_runs WHERE id = ?",
            (review_run_id,),
        ).fetchone()
    assert row is not None
    assert row["reviewed_note_sha"] == review_metadata.git_blob_sha(note_path)
    assert row["reviewed_note_commit"] is None


def test_create_review_run_allows_untracked_note_and_records_worktree_provenance(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    note_path = make_note(repo / "kb" / "notes" / "draft.md", "Draft", "\nDraft body.\n")

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.cli.review.create_review_run",
            "kb/notes/draft.md",
            "prose",
            "--runner",
            "codex",
            "--model",
            TEST_MODEL,
        ],
        cwd=repo,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    review_run_id = int(result.stdout.strip())
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT note_path, reviewed_note_sha, reviewed_note_commit FROM review_runs WHERE id = ?",
            (review_run_id,),
        ).fetchone()
    assert row is not None
    assert row["note_path"] == "kb/notes/draft.md"
    assert row["reviewed_note_sha"] == review_metadata.git_blob_sha(note_path)
    assert row["reviewed_note_commit"] is None


def test_create_review_run_rejects_dirty_gate(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    gate_path = repo / "kb" / "instructions" / "review-gates" / "prose" / "source-residue.md"
    gate_path.write_text(gate_path.read_text(encoding="utf-8") + "\nExtra gate note.\n", encoding="utf-8")

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.cli.review.create_review_run",
            "kb/notes/sample.md",
            "prose",
            "--runner",
            "codex",
            "--model",
            TEST_MODEL,
        ],
        cwd=repo,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "gate has uncommitted changes: kb/instructions/review-gates/prose/source-residue.md" in result.stderr


def test_create_review_run_filters_trait_gated_gates_for_inapplicable_note(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture_with_trait_gate(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose/source-residue",
        "frontmatter/claim-strength",
        "--runner",
        "codex",
        "--model",
        TEST_MODEL,
        "--json",
        env=env,
    )

    payload = json.loads(created.stdout)
    assert payload["gate_ids"] == ["prose/source-residue"]


def test_create_review_run_filters_type_gated_gates_for_inapplicable_note(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture_with_type_gate(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose/source-residue",
        "frontmatter/definition-precision",
        "frontmatter/related-system-fit",
        "--runner",
        "codex",
        "--model",
        TEST_MODEL,
        "--json",
        env=env,
    )

    payload = json.loads(created.stdout)
    assert payload["gate_ids"] == ["prose/source-residue", "frontmatter/definition-precision"]


def test_duplicate_gate_write_fails_within_run(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose/source-residue",
        "--runner",
        "codex",
        "--model",
        TEST_MODEL,
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
            "-m",
            "commonplace.cli.review.write_gate_review",
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


def test_warn_selector_uses_latest_current_review_when_acceptance_has_no_review_id(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose/source-residue",
        "--runner",
        "codex",
        "--model",
        TEST_MODEL,
        env=env,
    )
    review_run_id = int(created.stdout.strip())
    review_file = write(
        repo / "tmp" / "review.md",
        """## Result: WARN

### Summary
The note still needs one small fix.

### Findings
- WARN: Fix me. This warning should remain visible after an ack.
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
            accepted_note_sha=review_metadata.git_blob_sha(note_path),
            accepted_note_commit=review_metadata.last_commit_for_path(repo, Path("kb/notes/sample.md")),
            accepted_gate_sha=gate_row.gate_sha,
            accepted_at=review_metadata.iso_now(),
            acceptance_kind="trivial-change-ack",
        )
        conn.commit()

    result = subprocess.run(
        [sys.executable, "-m", "commonplace.cli.review.warn_selector", "--json", "kb/notes/sample.md"],
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


def test_warn_selector_skips_legacy_reviews_without_review_run_id(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    note_path = repo / "kb" / "notes" / "sample.md"
    gate_path = repo / "kb" / "instructions" / "review-gates" / "prose" / "source-residue.md"
    note_sha = review_metadata.git_blob_sha(note_path)
    gate_sha = review_metadata.git_blob_sha(gate_path)
    note_commit = review_metadata.last_commit_for_path(repo, Path("kb/notes/sample.md"))
    reviewed_at = review_metadata.iso_now()

    review_db.ensure_db(repo, db_path)
    with review_db.connect(db_path) as conn:
        review_id = review_db.insert_gate_review(
            conn,
            review_run_id=None,
            note_path="kb/notes/sample.md",
            gate_id="prose/source-residue",
            model_id="test-model",
            decision="warn",
            rationale_markdown="### Findings\n- WARN: Legacy warn.\n\n## Result: WARN\n",
            evidence_json=None,
            gate_sha=gate_sha,
            reviewed_note_sha=note_sha,
            reviewed_note_commit=note_commit,
            reviewed_at=reviewed_at,
            review_kind="manual-import",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/sample.md",
            gate_id="prose/source-residue",
            model_id="test-model",
            accepted_review_id=review_id,
            accepted_note_sha=note_sha,
            accepted_note_commit=note_commit,
            accepted_gate_sha=gate_sha,
            accepted_at=reviewed_at,
            acceptance_kind="manual-override",
        )
        conn.commit()

    result = subprocess.run(
        [sys.executable, "-m", "commonplace.cli.review.warn_selector", "--json", "kb/notes/sample.md"],
        cwd=repo,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )
    assert json.loads(result.stdout) == []


def test_warn_selector_falls_back_to_summary_for_current_warn_without_warn_bullets(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose/source-residue",
        "--runner",
        "codex",
        "--model",
        TEST_MODEL,
        env=env,
    )
    review_run_id = int(created.stdout.strip())
    review_file = write(
        repo / "tmp" / "review.md",
        """## Result: WARN

### Summary
The note overstates one claim and needs a framing adjustment.
""",
    )
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
    run_script(
        repo,
        "finalize_review_run.py",
        "--review-run-id",
        str(review_run_id),
        env=env,
    )

    result = subprocess.run(
        [sys.executable, "-m", "commonplace.cli.review.warn_selector", "--json", "kb/notes/sample.md"],
        cwd=repo,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    assert payload[0]["note_path"] == "kb/notes/sample.md"
    assert payload[0]["warns"][0]["text"] == "The note overstates one claim and needs a framing adjustment."


def test_warn_selector_ignores_active_model_and_collapses_per_gate(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)

    warn_env = os.environ.copy()
    warn_env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose/source-residue",
        "--runner",
        "codex",
        "--model",
        "model-a",
        env=warn_env,
    )
    warn_run_id = int(created.stdout.strip())
    warn_review = write(
        repo / "tmp" / "warn-review.md",
        """## Result: WARN

### Summary
The note still needs one small fix.

### Findings
- WARN: Cross-model warn that should remain visible.
""",
    )
    warn_review_id = int(
        run_script(
            repo,
            "write_gate_review.py",
            "--review-run-id",
            str(warn_run_id),
            "--gate-id",
            "prose/source-residue",
            "--input-file",
            str(warn_review),
            env=warn_env,
        ).stdout.strip()
    )
    run_script(
        repo,
        "finalize_review_run.py",
        "--review-run-id",
        str(warn_run_id),
        env=warn_env,
    )

    pass_env = os.environ.copy()
    pass_env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose/source-residue",
        "--runner",
        "codex",
        "--model",
        "model-b",
        env=pass_env,
    )
    pass_run_id = int(created.stdout.strip())
    pass_review = write(
        repo / "tmp" / "pass-review.md",
        """## Result: PASS

Looks good.
""",
    )
    run_script(
        repo,
        "write_gate_review.py",
        "--review-run-id",
        str(pass_run_id),
        "--gate-id",
        "prose/source-residue",
        "--input-file",
        str(pass_review),
        env=pass_env,
    )
    run_script(
        repo,
        "finalize_review_run.py",
        "--review-run-id",
        str(pass_run_id),
        env=pass_env,
    )

    selector_env = os.environ.copy()
    selector_env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    result = subprocess.run(
        [sys.executable, "-m", "commonplace.cli.review.warn_selector", "--json", "kb/notes/sample.md"],
        cwd=repo,
        env=selector_env,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    assert payload[0]["note_path"] == "kb/notes/sample.md"
    assert len(payload[0]["warns"]) == 1
    warn = payload[0]["warns"][0]
    assert warn["gate_id"] == "prose/source-residue"
    assert warn["review_id"] == warn_review_id
    assert "Cross-model warn" in warn["text"]


def test_run_review_bundle_with_fake_claude(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    fake_claude = fake_bin / "claude"
    fake_claude.write_text(
        """#!/usr/bin/env python3
import json
import sys

for event in [
    {"type": "system", "subtype": "init"},
    {
        "type": "assistant",
        "requestId": "req-1",
        "uuid": "uuid-1",
        "sessionId": "session-1",
        "timestamp": "2026-04-05T12:00:00Z",
        "message": {
            "id": "msg-1",
            "model": "claude-sonnet-4-6",
            "usage": {"input_tokens": 100, "output_tokens": 20},
            "content": [
                {"type": "text", "text": "Working through the requested links.\\n"},
                {"type": "tool_use", "name": "Read", "input": {"file_path": "kb/notes/sample.md"}},
            ],
        },
    },
    {
        "type": "assistant",
        "requestId": "req-2",
        "uuid": "uuid-2",
        "sessionId": "session-1",
        "timestamp": "2026-04-05T12:00:02Z",
        "message": {
            "id": "msg-2",
            "model": "claude-sonnet-4-6",
            "usage": {"input_tokens": 120, "output_tokens": 40},
            "content": [
                {
                    "type": "text",
                    "text": "# Review Bundle\\n\\nReview run id: 1\\nTarget: kb/notes/sample.md\\n\\n=== GATE REVIEW START: prose/source-residue ===\\n## Findings\\n\\n**WARN — Residue remains.** Temporary review.\\n=== GATE REVIEW END: prose/source-residue ===\\n\\n=== GATE REVIEW START: semantic/grounding-alignment ===\\nLooks good.\\n\\n## Result: PASS\\n=== GATE REVIEW END: semantic/grounding-alignment ===\\n",
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
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    env["PATH"] = f"{fake_bin}:{env['PATH']}"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.cli.review.run_review_bundle",
            "kb/notes/sample.md",
            "prose",
            "semantic/grounding-alignment",
            "--runner",
            "claude-code",
            "--model",
            "claude-requested",
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
    assert "requested model partition claude-requested" in result.stderr
    assert "claude-sonnet-4-6" in result.stderr

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run_count = conn.execute("SELECT count(*) FROM review_runs").fetchone()[0]
        gate_count = conn.execute("SELECT count(*) FROM gate_reviews").fetchone()[0]
        acceptance_count = conn.execute("SELECT count(*) FROM acceptance_events").fetchone()[0]
        run_row = conn.execute("SELECT id, model_id, telemetry_json, raw_bundle_markdown FROM review_runs").fetchone()
        assert run_count == 1
        assert gate_count == 2
        assert acceptance_count == 2
        assert run_row is not None
        assert run_row["model_id"] == "claude-sonnet-4-6"
        telemetry = json.loads(run_row["telemetry_json"])
        assert telemetry["model"] == "claude-sonnet-4-6"
        assert telemetry["models"] == ["claude-sonnet-4-6"]
        assert "=== GATE REVIEW START: prose/source-residue ===" in run_row["raw_bundle_markdown"]
        gate_rows = conn.execute("SELECT gate_id, model_id FROM gate_reviews ORDER BY gate_id").fetchall()
        assert [(row["gate_id"], row["model_id"]) for row in gate_rows] == [
            ("prose/source-residue", "claude-sonnet-4-6"),
            ("semantic/grounding-alignment", "claude-sonnet-4-6"),
        ]
        acceptance_rows = conn.execute("SELECT gate_id, model_id FROM acceptance_events ORDER BY gate_id").fetchall()
        assert [(row["gate_id"], row["model_id"]) for row in acceptance_rows] == [
            ("prose/source-residue", "claude-sonnet-4-6"),
            ("semantic/grounding-alignment", "claude-sonnet-4-6"),
        ]

    artifact_dir = run_review_bundle.bundle_artifact_dir(repo, run_row["id"])
    assert (artifact_dir / "bundle-output.md").is_file()
    assert (artifact_dir / "prose__source-residue.md").is_file()
    assert (artifact_dir / "semantic__grounding-alignment.md").is_file()


def test_run_review_bundle_allows_dirty_note_and_records_worktree_provenance(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    note_path = repo / "kb" / "notes" / "sample.md"
    note_path.write_text(note_path.read_text(encoding="utf-8") + "\nDirty change.\n", encoding="utf-8")
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
        "requestId": "req-1",
        "uuid": "uuid-1",
        "sessionId": "session-1",
        "timestamp": "2026-04-05T12:00:00Z",
        "message": {
            "id": "msg-1",
            "model": "claude-sonnet-4-6",
            "usage": {"input_tokens": 100, "output_tokens": 20},
            "content": [
                {
                    "type": "text",
                    "text": "=== GATE REVIEW START: prose/source-residue ===\\nLooks good.\\n\\n## Result: PASS\\n=== GATE REVIEW END: prose/source-residue ===\\n"
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
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    env["PATH"] = f"{fake_bin}:{env['PATH']}"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.cli.review.run_review_bundle",
            "kb/notes/sample.md",
            "prose",
            "--runner",
            "claude-code",
            "--model",
            "claude-requested",
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
        row = conn.execute(
            "SELECT reviewed_note_sha, reviewed_note_commit FROM review_runs"
        ).fetchone()
    assert row is not None
    assert row["reviewed_note_sha"] == review_metadata.git_blob_sha(note_path)
    assert row["reviewed_note_commit"] is None


def test_run_review_bundle_rejects_dirty_gate(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    gate_path = repo / "kb" / "instructions" / "review-gates" / "prose" / "source-residue.md"
    gate_path.write_text(gate_path.read_text(encoding="utf-8") + "\nExtra gate note.\n", encoding="utf-8")

    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.cli.review.run_review_bundle",
            "kb/notes/sample.md",
            "prose",
            "--runner",
            "codex",
            "--model",
            TEST_MODEL,
            "--db",
            str(db_path),
        ],
        cwd=repo,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "gate has uncommitted changes: kb/instructions/review-gates/prose/source-residue.md" in result.stderr


def test_run_review_bundle_rekeys_to_actual_codex_model_partition(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    fake_home = tmp_path / "home"
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    fake_codex = fake_bin / "codex"
    install_fake_codex_bundle_runner(fake_codex, reasoning_effort="xhigh")

    env = os.environ.copy()
    env["HOME"] = str(fake_home)
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    env["PATH"] = f"{fake_bin}:{env['PATH']}"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.cli.review.run_review_bundle",
            "kb/notes/sample.md",
            "prose",
            "semantic/grounding-alignment",
            "--runner",
            "codex",
            "--model",
            "gpt-5-4-high",
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
    assert "requested model partition gpt-5-4-high" in result.stderr
    assert "gpt-5-4-xhigh" in result.stderr

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run_row = conn.execute(
            "SELECT model_id, telemetry_json FROM review_runs"
        ).fetchone()
        assert run_row is not None
        assert run_row["model_id"] == "gpt-5-4-xhigh"
        telemetry = json.loads(run_row["telemetry_json"])
        assert telemetry["model"] == "gpt-5.4"
        assert telemetry["reasoning_effort"] == "xhigh"

        gate_rows = conn.execute(
            "SELECT gate_id, model_id FROM gate_reviews ORDER BY gate_id"
        ).fetchall()
        assert [(row["gate_id"], row["model_id"]) for row in gate_rows] == [
            ("prose/source-residue", "gpt-5-4-xhigh"),
            ("semantic/grounding-alignment", "gpt-5-4-xhigh"),
        ]

        acceptance_rows = conn.execute(
            "SELECT gate_id, model_id FROM acceptance_events ORDER BY gate_id"
        ).fetchall()
        assert [(row["gate_id"], row["model_id"]) for row in acceptance_rows] == [
            ("prose/source-residue", "gpt-5-4-xhigh"),
            ("semantic/grounding-alignment", "gpt-5-4-xhigh"),
        ]


def test_record_and_finalize_run_rekeys_existing_gate_reviews_to_actual_model_partition(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    created = run_script(
        repo,
        "create_review_run.py",
        "kb/notes/sample.md",
        "prose",
        "semantic/grounding-alignment",
        "--runner",
        "codex",
        "--model",
        TEST_MODEL,
        env=env,
    )
    review_run_id = int(created.stdout.strip())

    prose_review = write(
        repo / "tmp" / "prose.md",
        """## Findings

**WARN — Residue remains.** Temporary review.
""",
    )
    semantic_review = write(
        repo / "tmp" / "semantic.md",
        """## Result: PASS

Looks good.
""",
    )

    run_script(
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
    run_script(
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

    with review_db.connect(db_path) as conn:
        gate_count = record_and_finalize_run(
            conn,
            review_run_id=review_run_id,
            actual_model_id="actual-model",
        )
        conn.commit()
    assert gate_count == 2

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        run_row = conn.execute("SELECT status, model_id FROM review_runs WHERE id = ?", (review_run_id,)).fetchone()
        assert run_row is not None
        assert run_row["status"] == "completed"
        gate_rows = conn.execute(
            "SELECT gate_id, decision, model_id FROM gate_reviews WHERE review_run_id = ? ORDER BY gate_id",
            (review_run_id,),
        ).fetchall()
        assert run_row["model_id"] == "actual-model"
        assert [(row["gate_id"], row["decision"], row["model_id"]) for row in gate_rows] == [
            ("prose/source-residue", "warn", "actual-model"),
            ("semantic/grounding-alignment", "pass", "actual-model"),
        ]
        acceptance_rows = conn.execute(
            "SELECT gate_id, accepted_review_id, model_id FROM acceptance_events WHERE note_path = ? ORDER BY gate_id",
            ("kb/notes/sample.md",),
        ).fetchall()
        assert len(acceptance_rows) == 2
        assert all(row["accepted_review_id"] is not None for row in acceptance_rows)
        assert [(row["gate_id"], row["model_id"]) for row in acceptance_rows] == [
            ("prose/source-residue", "actual-model"),
            ("semantic/grounding-alignment", "actual-model"),
        ]


def test_extract_bundle_reviews_ignores_text_outside_gate_blocks() -> None:
    bundle = """Working notes before the bundle.

# Review Bundle

=== GATE REVIEW START: prose/source-residue ===
## Findings

**WARN — Residue remains.**
=== GATE REVIEW END: prose/source-residue ===

Extra trailing note.

=== GATE REVIEW START: semantic/grounding-alignment ===
Looks good.

## Result: PASS
=== GATE REVIEW END: semantic/grounding-alignment ===
"""

    parsed = extract_bundle_reviews(
        bundle,
        expected_gate_ids=["prose/source-residue", "semantic/grounding-alignment"],
    )

    assert parsed["prose/source-residue"].startswith("## Findings")
    assert parsed["semantic/grounding-alignment"] == "Looks good.\n\n## Result: PASS\n"


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
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    env["PATH"] = f"{fake_bin}:{env['PATH']}"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.cli.review.run_review_bundle",
            "kb/notes/sample.md",
            "prose",
            "semantic/grounding-alignment",
            "--runner",
            "claude-code",
            "--model",
            "claude-requested",
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
            "SELECT id, status, failure_reason, raw_bundle_markdown FROM review_runs"
        ).fetchone()
        assert run_row["status"] == "failed"
        assert "missing gate reviews in bundle output" in run_row["failure_reason"]
        assert "=== GATE REVIEW START: prose/source-residue ===" in run_row["raw_bundle_markdown"]

    artifact_dir = run_review_bundle.bundle_artifact_dir(repo, run_row["id"])
    assert (artifact_dir / "bundle-output.md").is_file()
    assert not (artifact_dir / "prose__source-residue.md").exists()


def test_run_review_bundle_dry_run_does_not_persist_review_run(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    env = os.environ.copy()
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "commonplace.cli.review.run_review_bundle",
            "kb/notes/sample.md",
            "prose",
            "semantic/grounding-alignment",
            "--runner",
            "codex",
            "--model",
            TEST_MODEL,
            "--dry-run",
            "--db",
            str(db_path),
        ],
        cwd=repo,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Write gate reviews for kb/notes/sample.md" in result.stdout
    assert not db_path.exists()

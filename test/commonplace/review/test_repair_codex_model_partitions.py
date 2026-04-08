from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

from commonplace.review import review_db


REPO_ROOT = Path(__file__).resolve().parents[3]


def write_codex_session_log(home: Path, *, review_run_id: int, model: str, reasoning_effort: str) -> Path:
    session_dir = home / ".codex" / "sessions" / "2026" / "04" / "04"
    session_dir.mkdir(parents=True, exist_ok=True)
    session_path = session_dir / "rollout-2026-04-04T09-00-00-019d6000-17a2-73b0-b341-3f36434aa48b.jsonl"
    events = [
        {
            "type": "session_meta",
            "payload": {
                "id": "019d6000-17a2-73b0-b341-3f36434aa48b",
                "timestamp": "2026-04-04T07:00:00.000Z",
                "cwd": str(REPO_ROOT),
                "originator": "codex_exec",
                "cli_version": "0.0.0",
                "model_provider": "openai",
            },
        },
        {
            "type": "turn_context",
            "payload": {
                "cwd": str(REPO_ROOT),
                "approval_policy": "never",
                "sandbox_policy": {"type": "workspace-write", "writable_roots": [str(REPO_ROOT)]},
                "model": model,
                "collaboration_mode": {
                    "mode": "default",
                    "settings": {
                        "model": model,
                        "reasoning_effort": reasoning_effort,
                    },
                },
                "effort": reasoning_effort,
            },
        },
        {
            "type": "response_item",
            "payload": {
                "type": "message",
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": f"# Review Bundle\n\nReview run id: {review_run_id}\nTarget: kb/notes/sample.md\n",
                    }
                ],
            },
        },
        {
            "type": "event_msg",
            "payload": {
                "type": "task_started",
                "turn_id": "turn-1",
            },
        },
        {
            "type": "event_msg",
            "payload": {
                "type": "token_count",
                "info": {
                    "model_context_window": 272000,
                    "last_token_usage": {
                        "input_tokens": 12,
                        "cached_input_tokens": 4,
                        "output_tokens": 6,
                        "reasoning_output_tokens": 8,
                        "total_tokens": 30,
                    },
                    "total_token_usage": {
                        "input_tokens": 120,
                        "cached_input_tokens": 40,
                        "output_tokens": 60,
                        "reasoning_output_tokens": 80,
                        "total_tokens": 300,
                    },
                },
                "rate_limits": {"primary": {"used_percent": 9}},
            },
        },
        {
            "type": "event_msg",
            "payload": {
                "type": "task_complete",
                "turn_id": "turn-1",
                "last_agent_message": "Finished review bundle",
            },
        },
    ]
    with session_path.open("w", encoding="utf-8") as handle:
        for event in events:
            handle.write(json.dumps(event) + "\n")
    return session_path


def test_repair_codex_model_partitions_rekeys_review_artifacts(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    fake_home = tmp_path / "home"
    review_db.ensure_db(REPO_ROOT, db_path)

    with review_db.connect(db_path) as conn:
        review_run_id = review_db.insert_review_run(
            conn,
            note_path="kb/notes/sample.md",
            model_id="gpt-5-4-high",
            runner="codex",
            reviewed_note_sha="note-sha",
            reviewed_note_commit=None,
            started_at="2026-04-04T09:00:00+02:00",
            completed_at="2026-04-04T09:00:10+02:00",
            status="completed",
        )
        gate_review_id = review_db.insert_gate_review(
            conn,
            review_run_id=review_run_id,
            note_path="kb/notes/sample.md",
            gate_id="semantic/grounding-alignment",
            model_id="gpt-5-4-high",
            decision="pass",
            rationale_markdown="Looks good.\n\n## Result: PASS\n",
            evidence_json=None,
            gate_sha="gate-sha",
            reviewed_note_sha="note-sha",
            reviewed_note_commit=None,
            reviewed_at="2026-04-04T09:00:10+02:00",
            review_kind="full-review",
        )
        review_db.append_acceptance_event(
            conn,
            note_path="kb/notes/sample.md",
            gate_id="semantic/grounding-alignment",
            model_id="gpt-5-4-high",
            accepted_review_id=gate_review_id,
            accepted_note_sha="note-sha",
            accepted_note_commit=None,
            accepted_gate_sha="gate-sha",
            accepted_at="2026-04-04T09:00:10+02:00",
            acceptance_kind="full-review",
        )
        conn.commit()

    session_path = write_codex_session_log(
        fake_home,
        review_run_id=review_run_id,
        model="gpt-5.4",
        reasoning_effort="xhigh",
    )

    env = os.environ.copy()
    env["HOME"] = str(fake_home)
    env["COMMONPLACE_REVIEW_DB"] = str(db_path)
    result = subprocess.run(
        [sys.executable, "-m", "commonplace.review.repair_codex_model_partitions"],
        cwd=REPO_ROOT,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )

    assert "scanned: 1" in result.stdout
    assert "session_matched: 1" in result.stdout
    assert "telemetry_updated: 1" in result.stdout
    assert "model_rekeyed: 1" in result.stdout

    with sqlite3.connect(db_path) as conn:
        run_row = conn.execute(
            "SELECT model_id, telemetry_json FROM review_runs WHERE id = ?",
            (review_run_id,),
        ).fetchone()
        assert run_row is not None
        assert run_row[0] == "gpt-5-4-xhigh"
        telemetry = json.loads(run_row[1])
        assert telemetry["model"] == "gpt-5.4"
        assert telemetry["reasoning_effort"] == "xhigh"
        assert telemetry["session_path"] == str(session_path)

        gate_row = conn.execute("SELECT model_id FROM gate_reviews WHERE review_run_id = ?", (review_run_id,)).fetchone()
        assert gate_row is not None
        assert gate_row[0] == "gpt-5-4-xhigh"

        acceptance_row = conn.execute(
            "SELECT model_id FROM acceptance_events WHERE accepted_review_id = ?",
            (gate_review_id,),
        ).fetchone()
        assert acceptance_row is not None
        assert acceptance_row[0] == "gpt-5-4-xhigh"

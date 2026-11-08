"""Protect discovery consumers against incomplete captures and duplicate dispatch.

These tests exercise capture -> inventory -> selection -> URL files. No network,
source execution or retained analysis contents are needed.
"""

import hashlib
import json

import pytest

from scripts.triage_gist_repositories import dispatch, inventory, render

CUTOFF = "2026-06-18T13:26:05Z"


def fixture_capture(tmp_path):
    capture = tmp_path / "capture"
    capture.mkdir()
    (tmp_path / "kb/work/agentic-system-completion").mkdir(parents=True)
    (tmp_path / "kb/work/agentic-system-completion/targets.md").write_text("# Holds\n")
    comment = {
        "id": 123,
        "url": "https://api.github.com/gists/abc/comments/123",
        "created_at": "2026-07-01T00:00:00Z",
        "updated_at": "2026-07-01T00:00:00Z",
        "body": "https://github.com/Old/Memory.git and https://github.com/old/memory/blob/main/x "
        "https://github.com/notifications/unsubscribe-auth/x",
    }
    (capture / "page-01.json").write_text(json.dumps([comment]))
    (capture / "page-01.headers").write_text(
        "HTTP/2 200\ndate: Sat, 07 Nov 2026 18:33:22 GMT\n"
    )
    repos = capture / "repos"
    repos.mkdir()
    (repos / "old--memory.json").write_text(
        json.dumps(
            {
                "full_name": "New/Memory",
                "html_url": "https://github.com/New/Memory",
                "default_branch": "main",
                "private": False,
                "size": 10,
            }
        )
    )
    (repos / "old--memory.README.md").write_text(
        "# Public memory implementation\n" * 20
    )
    return capture


def test_capture_to_canonical_dispatch_keeps_evidence_bindings(tmp_path):
    capture = fixture_capture(tmp_path)
    result = inventory(capture, tmp_path, CUTOFF)
    assert result["comment_count"] == result["new_comments"] == 1
    assert len(result["repositories"]) == 1
    assert (
        result["pages"][0]["sha256"]
        == hashlib.sha256((capture / "page-01.json").read_bytes()).hexdigest()
    )
    selection = [
        {"key": "old/memory", "reason": "A lead", "question": "What persists?"}
    ]
    chosen = dispatch(result, selection, capture, tmp_path)
    out = tmp_path / "output"
    render(result, chosen, out)
    assert (out / "dispatch-urls.txt").read_text() == "https://github.com/New/Memory\n"
    assert chosen[0]["source_revision"] is None
    assert chosen[0]["comments"][0]["url"].endswith("#gistcomment-123")
    assert "recommended" in (out / "candidates.md").read_text()


@pytest.mark.parametrize("failure", ["missing-next", "duplicate-comment"])
def test_incomplete_or_unstable_pagination_cannot_publish_inventory(tmp_path, failure):
    capture = fixture_capture(tmp_path)
    (capture / "page-01.headers").write_text('HTTP/2 200\nLink: <page=2>; rel="next"\n')
    if failure == "duplicate-comment":
        (capture / "page-02.json").write_bytes((capture / "page-01.json").read_bytes())
        (capture / "page-02.headers").write_text("HTTP/2 200\n")
    with pytest.raises(ValueError, match="Missing next page|Duplicate comment"):
        inventory(capture, tmp_path, CUTOFF)


@pytest.mark.parametrize(
    "failure", ["canonical-coverage", "canonical-hold", "duplicate-selection"]
)
def test_alias_reconciliation_prevents_redundant_or_owned_dispatch(tmp_path, failure):
    capture = fixture_capture(tmp_path)
    if failure == "canonical-coverage":
        (tmp_path / "kb/agentic-system-analyses/retained/new--memory").mkdir(
            parents=True
        )
    if failure == "canonical-hold":
        (tmp_path / "kb/work/agentic-system-completion/targets.md").write_text(
            "https://github.com/new/memory"
        )
    result = inventory(capture, tmp_path, CUTOFF)
    selection = [
        {"key": "old/memory", "reason": "A lead", "question": "What persists?"}
    ]
    if failure == "duplicate-selection":
        selection *= 2
    with pytest.raises(ValueError, match="coverage/ownership|Duplicate canonical"):
        dispatch(result, selection, capture, tmp_path)

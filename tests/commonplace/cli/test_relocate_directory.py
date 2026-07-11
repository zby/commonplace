from __future__ import annotations

import subprocess
from pathlib import Path

from commonplace.lib import relocation
from commonplace.review import review_db, review_target_selector
from tests.commonplace.cli.relocation_review_helpers import (
    GATE_ID,
    TEST_MODEL,
    make_gate,
    make_reviewable_note,
    review_state_rows,
    seed_accepted_review,
)


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def _init_git(repo_root: Path) -> None:
    subprocess.run(["git", "init", "-q"], cwd=repo_root, check=True)
    subprocess.run(["git", "config", "user.email", "t@t.t"], cwd=repo_root, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=repo_root, check=True)


def test_rewrite_links_to_moved_files_updates_matching_links(tmp_path: Path) -> None:
    source = tmp_path / "kb" / "notes" / "old" / "foo.md"
    source_b = tmp_path / "kb" / "notes" / "old" / "bar.md"
    new_a = tmp_path / "kb" / "new" / "foo.md"
    new_b = tmp_path / "kb" / "new" / "bar.md"
    ref_file = tmp_path / "kb" / "notes" / "outer.md"

    moves = {source.resolve(): new_a.resolve(), source_b.resolve(): new_b.resolve()}

    content = """[foo](./old/foo.md) and [bar](./old/bar.md) and [skip](./other.md)"""
    updated, changes = relocation.rewrite_links_to_moved_files(content, ref_file, moves)
    # ref_file is at kb/notes/outer.md, so new location kb/new/foo.md is ../new/foo.md
    assert "[foo](../new/foo.md)" in updated
    assert "[bar](../new/bar.md)" in updated
    assert "[skip](./other.md)" in updated
    assert len(changes) == 2


def test_rebase_and_rewrite_in_moved_file_rebases_external_and_updates_internal(tmp_path: Path) -> None:
    old_self = tmp_path / "kb" / "notes" / "old" / "self.md"
    old_sibling = tmp_path / "kb" / "notes" / "old" / "sibling.md"
    new_self = tmp_path / "kb" / "new" / "self.md"
    new_sibling = tmp_path / "kb" / "new" / "sibling.md"
    write(tmp_path / "kb" / "notes" / "definitions" / "concept.md", "x")

    moves = {old_self.resolve(): new_self.resolve(), old_sibling.resolve(): new_sibling.resolve()}

    content = """Internal: [sibling](./sibling.md)
External: [concept](../definitions/concept.md)
"""
    updated, changes = relocation.rebase_and_rewrite_in_moved_file(
        content, old_self, new_self, moves
    )
    # Internal link to sibling stays relative but points to the new location
    assert "[sibling](./sibling.md)" in updated
    # External link to definitions/ must be rebased (new location is one level shallower)
    assert "[concept](../notes/definitions/concept.md)" in updated


def test_add_single_redirect_adds_one_entry(tmp_path: Path) -> None:
    content = """site_name: X
plugins:
  - redirects:
      redirect_maps:
        'notes/a.md': 'notes/b.md'
"""
    updated, changes = relocation.add_single_redirect(
        content, "notes/old-dir/index.md", "new-dir/index.md"
    )
    assert "'notes/old-dir/index.md': 'new-dir/index.md'" in updated
    assert "'notes/a.md': 'notes/b.md'" in updated  # preserved
    assert len(changes) == 1


def test_relocate_directory_dry_run(tmp_path: Path) -> None:
    _init_git(tmp_path)
    source_dir = tmp_path / "kb" / "notes" / "related-systems"
    source_dir.mkdir(parents=True)

    write(source_dir / "foo.md", "# Foo\n\n[bar](./bar.md)\n[def](../definitions/d.md)\n")
    write(source_dir / "bar.md", "# Bar\n")
    write(tmp_path / "kb" / "notes" / "definitions" / "d.md", "# D\n")
    write(tmp_path / "kb" / "notes" / "outer.md", "# Outer\n\n[foo](./related-systems/foo.md)\n")
    write(tmp_path / "mkdocs.yml", """site_name: X
plugins:
  - redirects:
      redirect_maps:
        'notes/stale.md': 'notes/new.md'
""")

    exit_code = relocation.relocate_directory(
        root=tmp_path,
        source_arg="kb/notes/related-systems",
        dest_path="kb/agent-memory-systems",
        redirect_from="notes/related-systems/index.md",
        redirect_to="agent-memory-systems/index.md",
        apply=False,
    )
    assert exit_code == 0

    # Dry run: source still exists, destination does not
    assert source_dir.is_dir()
    assert not (tmp_path / "kb" / "agent-memory-systems").exists()


def test_relocate_directory_apply_moves_and_rewrites(tmp_path: Path) -> None:
    _init_git(tmp_path)
    source_dir = tmp_path / "kb" / "notes" / "related-systems"
    source_dir.mkdir(parents=True)
    write(source_dir / "foo.md", "# Foo\n\n[bar](./bar.md)\n[def](../definitions/d.md)\n")
    write(source_dir / "bar.md", "# Bar\n")
    write(tmp_path / "kb" / "notes" / "definitions" / "d.md", "# D\n")
    write(tmp_path / "kb" / "notes" / "outer.md", "# Outer\n\n[foo](./related-systems/foo.md)\n")
    write(tmp_path / "mkdocs.yml", """site_name: X
plugins:
  - redirects:
      redirect_maps:
        'notes/stale.md': 'notes/new.md'
""")

    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=tmp_path, check=True)

    exit_code = relocation.relocate_directory(
        root=tmp_path,
        source_arg="kb/notes/related-systems",
        dest_path="kb/agent-memory-systems",
        redirect_from="notes/related-systems/foo.md",
        redirect_to="agent-memory-systems/foo.md",
        apply=True,
    )
    assert exit_code == 0

    # Source is gone, destination exists
    assert not source_dir.exists()
    dest = tmp_path / "kb" / "agent-memory-systems"
    assert (dest / "foo.md").is_file()
    assert (dest / "bar.md").is_file()

    # Moved file: external link rebased to new depth
    foo_content = (dest / "foo.md").read_text()
    assert "[bar](./bar.md)" in foo_content  # internal preserved
    assert "[def](../notes/definitions/d.md)" in foo_content  # external rebased

    # Unmoved file: link to moved file rewritten
    outer_content = (tmp_path / "kb" / "notes" / "outer.md").read_text()
    assert "[foo](../agent-memory-systems/foo.md)" in outer_content

    # mkdocs has exactly ONE new redirect (plus the pre-existing stale one)
    mkdocs_content = (tmp_path / "mkdocs.yml").read_text()
    assert "'notes/related-systems/foo.md': 'agent-memory-systems/foo.md'" in mkdocs_content
    assert "'notes/stale.md': 'notes/new.md'" in mkdocs_content


def test_relocate_directory_apply_leaves_review_state_rows_unchanged_and_paths_derived(
    tmp_path: Path, capsys
) -> None:
    source_dir = tmp_path / "kb" / "notes" / "related-systems"
    foo = make_reviewable_note(source_dir / "foo.md", "Foo")
    bar = make_reviewable_note(source_dir / "bar.md", "Bar")
    make_gate(tmp_path)

    db_path = tmp_path / "kb" / "reports" / "review-store.sqlite"
    seed_accepted_review(tmp_path, db_path, note_path="kb/notes/related-systems/foo.md")
    seed_accepted_review(tmp_path, db_path, note_path="kb/notes/related-systems/bar.md")
    with review_db.connect(db_path) as conn:
        rows_before = review_state_rows(conn)

    exit_code = relocation.relocate_directory(
        root=tmp_path,
        source_arg="kb/notes/related-systems",
        dest_path="kb/agent-memory-systems",
        apply=True,
    )

    output = capsys.readouterr().out.lower()
    assert exit_code == 0
    assert "review" not in output
    assert not foo.exists()
    assert not bar.exists()
    assert (tmp_path / "kb" / "agent-memory-systems" / "foo.md").is_file()
    assert (tmp_path / "kb" / "agent-memory-systems" / "bar.md").is_file()

    with review_db.connect(db_path) as conn:
        rows_after = review_state_rows(conn)
        plans = [
            review_db.load_review_job_plan(conn, review_job_id=1),
            review_db.load_review_job_plan(conn, review_job_id=2),
        ]
        old_foo_pairs = review_db.load_review_pairs_for_note(
            conn,
            note_path="kb/notes/related-systems/foo.md",
            model_partition=TEST_MODEL,
        )
        old_bar_pairs = review_db.load_review_pairs_for_note(
            conn,
            note_path="kb/notes/related-systems/bar.md",
            model_partition=TEST_MODEL,
        )
        new_foo_pairs = review_db.load_review_pairs_for_note(
            conn,
            note_path="kb/agent-memory-systems/foo.md",
            model_partition=TEST_MODEL,
        )
        new_bar_pairs = review_db.load_review_pairs_for_note(
            conn,
            note_path="kb/agent-memory-systems/bar.md",
            model_partition=TEST_MODEL,
        )

    assert rows_after == rows_before
    assert [pair.note_path for pair in old_bar_pairs + old_foo_pairs] == [
        "kb/notes/related-systems/bar.md",
        "kb/notes/related-systems/foo.md",
    ]
    assert new_foo_pairs == []
    assert new_bar_pairs == []
    assert all(plan is not None for plan in plans)
    assert "prompt_path" not in rows_after["review_jobs"][0]
    assert "bundle_output_path" not in rows_after["review_jobs"][0]
    assert "result_path" not in rows_after["review_pairs"][0]
    assert [plan.prompt_path for plan in plans if plan is not None] == [
        "kb/reports/bundle-reviews/review-job-1/prompt.md",
        "kb/reports/bundle-reviews/review-job-2/prompt.md",
    ]
    assert [plan.bundle_output_path for plan in plans if plan is not None] == [
        "kb/reports/bundle-reviews/review-job-1/bundle-output.md",
        "kb/reports/bundle-reviews/review-job-2/bundle-output.md",
    ]
    assert [pair.result_path for pair in old_foo_pairs + old_bar_pairs] == [
        "kb/reports/bundle-reviews/review-job-1/pair-1-source-residue.md",
        "kb/reports/bundle-reviews/review-job-2/pair-1-source-residue.md",
    ]

    stale = review_target_selector.select_stale_criteria(
        tmp_path,
        model=TEST_MODEL,
        criterion_ids=[GATE_ID],
        note_filter=[
            "kb/agent-memory-systems/bar.md",
            "kb/agent-memory-systems/foo.md",
        ],
        db_path=db_path,
    )
    assert [(record.note_path, record.criterion_id, record.reason) for record in stale] == [
        ("kb/agent-memory-systems/bar.md", GATE_ID, "missing-review"),
        ("kb/agent-memory-systems/foo.md", GATE_ID, "missing-review"),
    ]


def test_relocate_directory_rejects_existing_destination(tmp_path: Path) -> None:
    _init_git(tmp_path)
    source_dir = tmp_path / "kb" / "notes" / "related-systems"
    source_dir.mkdir(parents=True)
    write(source_dir / "foo.md", "x")
    (tmp_path / "kb" / "agent-memory-systems").mkdir()
    write(tmp_path / "mkdocs.yml", """plugins:
  - redirects:
      redirect_maps: {}
""")

    exit_code = relocation.relocate_directory(
        root=tmp_path,
        source_arg="kb/notes/related-systems",
        dest_path="kb/agent-memory-systems",
        apply=False,
    )
    assert exit_code == 1

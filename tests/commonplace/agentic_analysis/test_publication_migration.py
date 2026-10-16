"""Naming-only migration: preserved publication bytes, no analysis execution."""
from __future__ import annotations

import json
from hashlib import sha256

import pytest
import yaml

from scripts import migrate_analysis_publications as migration


def artifact(root, name, identity):
    directory = root / migration.RETAINED_ROOT / name
    directory.mkdir(parents=True)
    (directory / "memory.md").write_text(f'---\nsource-identity: "{identity}"\n---\n# Memory\n')
    (directory / "overview.md").write_text('---\nsystem: Wiki\nrun-id: AAS-2026-10-15-wiki-old-token-01\n---\n# Wiki\n')
    manifest = {"members": {name: {"sha256": sha256((directory / name).read_bytes()).hexdigest()}
                            for name in ("memory.md", "overview.md")}}
    (directory / "ARTIFACT.yaml").write_text(yaml.safe_dump(manifest))
    return directory


def test_migration_plan_keeps_document_paths_and_run_ids(tmp_path):
    artifact(tmp_path, "llm-wiki", "https://github.com/nvk/llm-wiki")
    artifact(tmp_path, "paper", "https://example.invalid/paper")
    plan = migration.migration_plan(tmp_path)
    assert {entry["new"].rsplit("/", 1)[-1] for entry in plan} == {"nvk--llm-wiki", "paper"}
    assert {entry["run-id"] for entry in plan} == {"AAS-2026-10-15-wiki-old-token-01"}


@pytest.mark.parametrize("mutation", ["bytes", "occupied", "duplicate", "symlink"])
def test_migration_refuses_uncertain_inputs_before_any_move(tmp_path, mutation):
    directory = artifact(tmp_path, "llm-wiki", "https://github.com/nvk/llm-wiki")
    if mutation == "bytes":
        (directory / "memory.md").write_text("changed")
    elif mutation == "occupied":
        directory.with_name("nvk--llm-wiki").mkdir()
    elif mutation == "duplicate":
        artifact(tmp_path, "another", "https://github.com/nvk/llm-wiki")
    else:
        (directory / "extra").symlink_to(directory / "memory.md")
    with pytest.raises(ValueError):
        migration.migration_plan(tmp_path)
    assert directory.is_dir()


def test_required_retained_link_edit_is_rejected_before_any_move(tmp_path):
    first = artifact(tmp_path, "wiki", "https://github.com/nvk/wiki")
    second = artifact(tmp_path, "peer", "https://github.com/Pratiyush/wiki")
    memory = first / "memory.md"
    memory.write_text(memory.read_text() + "[Peer](../peer/overview.md)\n")
    manifest = yaml.safe_load((first / "ARTIFACT.yaml").read_text())
    manifest["members"]["memory.md"]["sha256"] = sha256(memory.read_bytes()).hexdigest()
    (first / "ARTIFACT.yaml").write_text(yaml.safe_dump(manifest))
    before = migration.file_hashes(first)
    with pytest.raises(ValueError, match="would change accepted bytes"):
        migration.main(["--root", str(tmp_path), "--apply"])
    assert first.is_dir() and second.is_dir()
    assert migration.file_hashes(first) == before


def test_apply_uses_relocation_and_verifies_unchanged_bytes(tmp_path):
    old = artifact(tmp_path, "llm-wiki", "https://github.com/nvk/llm-wiki")
    before = migration.file_hashes(old)
    backlink = tmp_path / "kb" / "index.md"
    backlink.write_text("[Wiki](agentic-system-analyses/retained/llm-wiki/overview.md)\n")
    record = tmp_path / "migration.json"
    assert migration.main(["--root", str(tmp_path), "--apply", "--record", str(record)]) == 0
    new = old.with_name("nvk--llm-wiki")
    assert migration.file_hashes(new) == before
    assert "retained/nvk--llm-wiki/overview.md" in backlink.read_text()
    assert json.loads(record.read_text())["all-bytes-unchanged"] is True
    assert migration.main(["--root", str(tmp_path)]) == 0
    assert migration.file_hashes(new) == before

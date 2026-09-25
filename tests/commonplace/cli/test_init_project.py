from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.cli import init_project as init_project_module
from commonplace.cli.init_project import (
    init_project,
    installation_warnings,
    main,
)
from commonplace.lib import library
from commonplace.lib.project_paths import is_collection_dir
from commonplace.lib.validation import validate_collection_landings
from commonplace.scaffold_manifest import MANIFEST


def relative_files(root: Path) -> set[Path]:
    return {
        path.relative_to(root)
        for path in root.rglob("*")
        if path.is_file()
    }


def relative_directories(root: Path) -> set[Path]:
    return {
        path.relative_to(root)
        for path in root.rglob("*")
        if path.is_dir()
    }


def test_init_project_creates_core_layout_and_is_idempotent(tmp_path: Path) -> None:
    report = init_project(tmp_path)

    assert report.created
    assert {
        Path("kb/notes"),
        Path("kb/reference"),
        Path("kb/sources"),
        Path("kb/instructions"),
        Path("kb/reports"),
        Path("kb/reports/cache"),
        Path("kb/reports/state"),
        Path("kb/reports/retained"),
        Path("kb/reports/types"),
    } <= relative_directories(tmp_path)
    assert (tmp_path / "kb" / "sources" / ".gitignore").read_text(
        encoding="utf-8"
    ) == ".snapshots/\n"
    reports_ignore = (tmp_path / "kb" / "reports" / ".gitignore").read_text(
        encoding="utf-8"
    )
    assert "cache/**" in reports_ignore
    assert "state/**" in reports_ignore
    assert (tmp_path / "kb" / "log.md").is_file()

    rerun = init_project(tmp_path)
    assert (
        rerun.created,
        rerun.refreshed,
        rerun.removed,
        bool(rerun.preserved_identical),
        rerun.preserved_different,
    ) == ([], [], [], True, [])


def test_init_project_does_not_copy_the_library(tmp_path: Path) -> None:
    init_project(tmp_path)

    files = relative_files(tmp_path)
    expected = {
        Path("kb/notes/COLLECTION.md"),
        Path("kb/notes/README.md"),
        Path("kb/reference/COLLECTION.md"),
        Path("kb/reference/README.md"),
        Path("kb/instructions/COLLECTION.md"),
        Path("kb/instructions/README.md"),
        Path("kb/sources/COLLECTION.md"),
        Path("kb/sources/README.md"),
        Path("kb/work/COLLECTION.md"),
        Path("kb/work/README.md"),
        Path("kb/reports/COLLECTION.md"),
        Path("kb/reports/README.md"),
        Path("kb/reports/.gitignore"),
        Path("kb/reports/types/connect-report.md"),
        Path("kb/reports/types/connect-report.schema.yaml"),
        Path("kb/sources/types/ingest-report.md"),
        Path("kb/sources/types/snapshot.md"),
        Path("kb/sources/.gitignore"),
        Path("AGENTS.md.template"),
        Path("CLAUDE.md.template"),
        library.ROUTING,
        library.SETTINGS,
        Path(".gitignore"),
    }
    assert expected <= files
    assert not (tmp_path / "kb" / "commonplace").exists()
    assert not (tmp_path / "kb" / "types").exists()
    stub_files = {
        path for path in files if path.parts[:2] in {(".claude", "skills"), (".agents", "skills")}
    }
    assert {path.name for path in stub_files} == {"SKILL.md", library.STUB_MARKER}


def test_init_project_writes_stubs_that_point_into_the_library(tmp_path: Path) -> None:
    init_project(tmp_path)
    root = library.library_root()

    names = (*MANIFEST.promoted_skills, MANIFEST.router_skill)
    for skills_dir in MANIFEST.skills_dirs:
        for name in names:
            stub = (tmp_path / skills_dir / name / "SKILL.md").read_text(encoding="utf-8")
            real = root / "instructions" / name / "SKILL.md"
            assert stub.startswith("---\n")
            assert f"name: {name}\n" in stub
            assert real.as_posix() in stub
            assert ("$ARGUMENTS" in stub) == ("$ARGUMENTS" in real.read_text(encoding="utf-8"))


def test_init_project_writes_routing_file_with_skill_index(tmp_path: Path) -> None:
    init_project(tmp_path)
    root = library.library_root()

    routing = (tmp_path / library.ROUTING).read_text(encoding="utf-8")
    assert f"Library root: {root.as_posix()}" in routing
    for name in (*MANIFEST.promoted_skills, MANIFEST.router_skill):
        assert f"- `{name}` — " in routing
        assert (root / "instructions" / name / "SKILL.md").as_posix() in routing


def test_init_project_merges_read_rule_into_existing_settings(tmp_path: Path) -> None:
    settings = tmp_path / library.SETTINGS
    settings.parent.mkdir(parents=True)
    settings.write_bytes(b"\xef\xbb\xbf" + json.dumps({"permissions": {"allow": ["Bash(ls:*)"]}}).encode())

    init_project(tmp_path)
    init_project(tmp_path)

    allow = json.loads(settings.read_text(encoding="utf-8"))["permissions"]["allow"]
    assert allow == ["Bash(ls:*)", library.read_rule()]


def test_init_project_gitignores_its_outputs(tmp_path: Path) -> None:
    (tmp_path / ".gitignore").write_text("node_modules/\n", encoding="utf-8")

    init_project(tmp_path)
    init_project(tmp_path)

    lines = (tmp_path / ".gitignore").read_text(encoding="utf-8").splitlines()
    assert lines[0] == "node_modules/"
    assert lines.count(library.GITIGNORE_BEGIN) == 1
    assert "/.commonplace/" in lines
    assert "/.claude/settings.local.json" in lines
    assert "/.claude/skills/cp-skill-write/" in lines


def test_check_reports_current_and_stale_outputs(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    init_project(tmp_path)
    assert main(["--root", str(tmp_path), "--check"]) == 0

    stub = tmp_path / ".claude" / "skills" / "cp-skill-write" / "SKILL.md"
    stub.write_text("edited", encoding="utf-8")
    capsys.readouterr()

    assert main(["--root", str(tmp_path), "--check"]) == 1
    assert "stale: .claude/skills/cp-skill-write" in capsys.readouterr().out
    assert library.stale_outputs(tmp_path)

    report = init_project(tmp_path)
    assert Path(".claude/skills/cp-skill-write/SKILL.md") in report.refreshed
    assert library.stale_outputs(tmp_path) == []


def test_migration_removes_matching_copies_and_keeps_differing_ones(tmp_path: Path) -> None:
    root = library.library_root()
    legacy = tmp_path / "kb" / "commonplace" / "instructions"
    legacy.mkdir(parents=True)
    shutil.copy2(root / "instructions" / "FIX-SYSTEM.md", legacy / "FIX-SYSTEM.md")
    (legacy / "re-ingest.md").write_text("locally edited\n", encoding="utf-8")
    types = tmp_path / "kb" / "types"
    types.mkdir(parents=True)
    shutil.copy2(root / "types" / "note.md", types / "note.md")
    (types / "my-shared-type.md").write_text("project-owned\n", encoding="utf-8")
    old_skill = tmp_path / ".claude" / "skills" / "cp-skill-validate"
    shutil.copytree(root / "instructions" / "cp-skill-validate", old_skill)

    report = init_project(tmp_path)

    assert Path("kb/commonplace/instructions/FIX-SYSTEM.md") in report.removed
    assert Path("kb/commonplace/instructions/re-ingest.md") in report.migration_kept
    assert (legacy / "re-ingest.md").read_text(encoding="utf-8") == "locally edited\n"
    assert not (types / "note.md").exists()
    assert (types / "my-shared-type.md").exists()
    assert Path("kb/types/my-shared-type.md") not in report.migration_kept
    assert (old_skill / library.STUB_MARKER).is_file()


def test_init_project_retires_baselines_recorded_under_the_old_library_copy(tmp_path: Path) -> None:
    from commonplace.review import review_db
    from tests.commonplace.review.pair_helpers import accept_pair, insert_completed_pair

    note_path = "kb/notes/sample.md"
    legacy_gate = "kb/commonplace/instructions/review-gates/prose/sample-gate.md"
    project_gate = "kb/instructions/project-gate.md"
    for rel in (note_path, legacy_gate, project_gate):
        (tmp_path / rel).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / rel).write_text(f"# {rel}\n", encoding="utf-8")
    db_path = review_db.resolve_db_path(tmp_path)
    review_db.ensure_db(db_path)
    with review_db.connect(db_path) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=tmp_path, path=note_path)
        for criterion in (legacy_gate, project_gate):
            criterion_snapshot = review_db.snapshot_file(conn, repo_root=tmp_path, path=criterion)
            pair = insert_completed_pair(
                conn,
                note_path=note_path,
                criterion_id=criterion,
                model_partition="test-model",
                outcome="pass",
                reviewed_note_snapshot_id=note_snapshot.snapshot_id,
                reviewed_criterion_snapshot_id=criterion_snapshot.snapshot_id,
                completed_at="2026-07-01T00:00:00+00:00",
            )
            accept_pair(
                conn,
                review_pair_id=pair,
                note_path=note_path,
                criterion_id=criterion,
                model_partition="test-model",
                baseline_note_snapshot_id=note_snapshot.snapshot_id,
                baseline_criterion_snapshot_id=criterion_snapshot.snapshot_id,
                baseline_updated_at="2026-07-01T00:00:00+00:00",
            )
        conn.commit()

    report = init_project(tmp_path)

    with review_db.connect(db_path) as conn:
        remaining = {criterion for _, criterion, _ in review_db.load_current_freshness_baselines(conn)}
    assert remaining == {project_gate}
    assert report.retired_baselines == [f"{note_path} × {legacy_gate} (test-model)"]


def test_migration_never_deletes_through_a_symlinked_skill_directory(tmp_path: Path) -> None:
    root = library.library_root()
    outside = tmp_path / "outside" / "cp-skill-validate"
    shutil.copytree(root / "instructions" / "cp-skill-validate", outside)
    project = tmp_path / "project"
    (project / ".claude" / "skills").mkdir(parents=True)
    link = project / ".claude" / "skills" / "cp-skill-validate"
    link.symlink_to(outside, target_is_directory=True)

    report = init_project(project)

    assert (outside / "SKILL.md").read_bytes() == (root / "instructions" / "cp-skill-validate" / "SKILL.md").read_bytes()
    assert link.is_symlink()
    assert Path(".claude/skills/cp-skill-validate") in report.skipped_foreign


def test_init_project_reports_skill_copies_it_replaced_with_stubs(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    root = library.library_root()
    old_copy = tmp_path / ".claude" / "skills" / "cp-skill-write"
    shutil.copytree(root / "instructions" / "cp-skill-write", old_copy)

    exit_code = main(["--root", str(tmp_path)])

    assert exit_code == 0
    assert (old_copy / library.STUB_MARKER).is_file()
    assert "git rm -r --cached .claude/skills/cp-skill-write" in capsys.readouterr().out


def test_init_project_migrates_pointers_to_global_types(tmp_path: Path) -> None:
    notes = tmp_path / "kb" / "notes"
    notes.mkdir(parents=True)
    (notes / "COLLECTION.md").write_text("# Notes\n", encoding="utf-8")
    (notes / "a.md").write_text(
        "---\ndescription: Repo-relative pointer to a global type\ntype: kb/types/note.md\n---\n\n"
        "# A\n\n- kb/types/note.md stays as prose in the body\n",
        encoding="utf-8",
    )
    (notes / "b.md").write_text(
        "---\ndescription: Relative pointer\ntype: ../types/definition.md\n---\n\n# B\n", encoding="utf-8"
    )
    (notes / "c.md").write_text(
        '---\n{\n  "description": "JSON-style frontmatter",\n  "type": "kb/types/note.md"\n}\n---\n\n# C\n',
        encoding="utf-8",
    )
    shared = tmp_path / "kb" / "types" / "my-type.md"
    shared.parent.mkdir(parents=True)
    shared.write_text("---\ntype: kb/types/type-spec.md\nname: my-type\n---\n", encoding="utf-8")
    (notes / "d.md").write_text(
        "---\ndescription: Project-shared type keeps its path\ntype: kb/types/my-type.md\n---\n\n# D\n",
        encoding="utf-8",
    )
    schema = tmp_path / "kb" / "reports" / "types" / "old-report.schema.yaml"
    schema.parent.mkdir(parents=True)
    schema.write_text('allOf:\n  - $ref: "../../types/note.schema.yaml"\n', encoding="utf-8")

    report = init_project(tmp_path)

    assert "type: note\n" in (notes / "a.md").read_text(encoding="utf-8")
    assert "- kb/types/note.md stays as prose" in (notes / "a.md").read_text(encoding="utf-8")
    assert "type: definition\n" in (notes / "b.md").read_text(encoding="utf-8")
    assert '"type": "note"' in (notes / "c.md").read_text(encoding="utf-8")
    assert "type: kb/types/my-type.md" in (notes / "d.md").read_text(encoding="utf-8")
    assert "type: type-spec" in shared.read_text(encoding="utf-8")
    assert '$ref: "commonplace:types/note.schema.yaml"' in schema.read_text(encoding="utf-8")
    assert set(report.rewritten_type_pointers) == {
        Path("kb/notes/a.md"),
        Path("kb/notes/b.md"),
        Path("kb/notes/c.md"),
        Path("kb/types/my-type.md"),
        Path("kb/reports/types/old-report.schema.yaml"),
    }


def test_init_project_leaves_foreign_skill_directories_alone(tmp_path: Path) -> None:
    dest = tmp_path / ".claude" / "skills" / "cp-skill-write"
    dest.mkdir(parents=True)
    (dest / "SKILL.md").write_text("runtime-specific skill", encoding="utf-8")
    (dest / "extra.md").write_text("not from the library", encoding="utf-8")

    report = init_project(tmp_path)

    assert Path(".claude/skills/cp-skill-write") in report.skipped_foreign
    assert (dest / "SKILL.md").read_text(encoding="utf-8") == "runtime-specific skill"


def test_commands_warn_when_outputs_are_stale(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    init_project(tmp_path)
    (tmp_path / library.ROUTING).write_text("old", encoding="utf-8")
    monkeypatch.chdir(tmp_path / "kb")

    library.checks_library(lambda: None)()

    err = capsys.readouterr().err
    assert "rerun commonplace-init" in err
    assert "stale:" in err


def test_init_project_satisfies_collection_landing_invariant(tmp_path: Path) -> None:
    init_project(tmp_path)

    assert is_collection_dir(tmp_path / "kb" / "sources")
    assert is_collection_dir(tmp_path / "kb" / "reports")

    results = validate_collection_landings(repo_root=tmp_path)

    assert results.fails == []
    assert any("collection landings: all" in line for line in results.passes)


def test_every_project_collection_the_template_routes_to_is_scaffolded(
    tmp_path: Path,
) -> None:
    # The template tells agents to read a routed collection's COLLECTION.md
    # before writing there, so each routed project path must ship one.
    init_project(tmp_path)
    template = (tmp_path / "AGENTS.md.template").read_text(encoding="utf-8")
    routed = re.findall(r"^\| `(kb/[^`]+)/` \|", template, flags=re.MULTILINE)

    assert routed
    missing = [path for path in routed if not is_collection_dir(tmp_path / path)]
    assert missing == []


def test_init_project_seeds_quote_or_snapshot_source_contract(tmp_path: Path) -> None:
    init_project(tmp_path)

    contract = (tmp_path / "kb" / "sources" / "COLLECTION.md").read_text(
        encoding="utf-8"
    )
    normalized_contract = " ".join(contract.split())

    assert "## Quotes in ingest reports" in contract
    assert "No source quotes have been retained yet." in contract
    assert "Never change an existing ingest's `snapshot_sha256`." in contract
    assert "exact marker `(snapshot required)`" in contract
    assert "never silently falls back from an unmarked link" in normalized_contract


def test_init_project_preserves_source_collection_heads(tmp_path: Path) -> None:
    init_project(tmp_path)
    collection = tmp_path / "kb" / "sources" / "COLLECTION.md"
    landing = tmp_path / "kb" / "sources" / "README.md"
    collection.write_text("project source contract\n", encoding="utf-8")
    landing.write_text("project source landing\n", encoding="utf-8")

    rerun = init_project(tmp_path)

    assert rerun.created == []
    assert Path("kb/sources/COLLECTION.md") in rerun.preserved_different
    assert Path("kb/sources/README.md") in rerun.preserved_different
    assert collection.read_text(encoding="utf-8") == "project source contract\n"
    assert landing.read_text(encoding="utf-8") == "project source landing\n"


def test_init_project_resolves_templates(tmp_path: Path) -> None:
    init_project(tmp_path, name="myproject")

    assert not (tmp_path / ".envrc").exists()

    # AGENTS.md.template has project name filled in
    agents = tmp_path / "AGENTS.md.template"
    text = agents.read_text(encoding="utf-8")
    assert "myproject" in text
    assert "{{project_name}}" not in text
    assert "## Vocabulary" in text
    assert "Terms needed to understand the project" in text
    assert "Call `commonplace-*` commands by bare name" in text
    assert "user-level `llm-commonplace` uv tool installation" in text
    assert ".venv" not in text

    assert not (tmp_path / "qmd-collections.yml").exists()


def test_init_project_defaults_name_to_directory(tmp_path: Path) -> None:
    init_project(tmp_path)

    agents = tmp_path / "AGENTS.md.template"
    text = agents.read_text(encoding="utf-8")
    assert tmp_path.name in text


def test_init_project_preserves_existing_files(tmp_path: Path) -> None:
    init_project(tmp_path)

    collection = tmp_path / "kb" / "instructions" / "COLLECTION.md"
    collection.write_text("custom content", encoding="utf-8")

    rerun = init_project(tmp_path)
    assert rerun.created == []
    assert Path("kb/instructions/COLLECTION.md") in rerun.preserved_different
    assert collection.read_text(encoding="utf-8") == "custom content"


def test_init_project_reports_identical_existing_files(tmp_path: Path) -> None:
    init_project(tmp_path)

    rerun = init_project(tmp_path)

    assert Path("kb/instructions/COLLECTION.md") in rerun.preserved_identical
    assert rerun.preserved_different == []


def test_init_project_treats_raw_template_source_as_matching(tmp_path: Path) -> None:
    raw_template = (REPO_ROOT / "AGENTS.md.template").read_text(encoding="utf-8")
    (tmp_path / "AGENTS.md.template").write_text(raw_template, encoding="utf-8")

    report = init_project(tmp_path)

    assert Path("AGENTS.md.template") in report.preserved_identical
    assert Path("AGENTS.md.template") not in report.preserved_different


def test_main_reports_preserved_file_statuses(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    init_project(tmp_path)
    (tmp_path / "kb" / "instructions" / "COLLECTION.md").write_text(
        "custom content",
        encoding="utf-8",
    )

    exit_code = main(["--root", str(tmp_path), "--name", "myproject"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Preserved existing files already matching scaffold:" in captured.out
    assert "Preserved existing files differing from current scaffold output:" in captured.out
    assert "- kb/instructions/COLLECTION.md" in captured.out


def test_main_does_not_imply_manual_edits_for_template_name_drift(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    init_project(tmp_path, name="custom-name")

    exit_code = main(["--root", str(tmp_path)])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Preserved existing files differing from current scaffold output:" in captured.out
    assert "- AGENTS.md.template" in captured.out
    assert "local changes" not in captured.out


def test_installation_warnings_report_missing_package_commands(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        init_project_module,
        "_installed_command_names",
        lambda: ("commonplace-init", "commonplace-validate"),
    )
    monkeypatch.setattr(
        init_project_module.shutil,
        "which",
        lambda name: "/tool/bin/commonplace-init" if name == "commonplace-init" else None,
    )
    monkeypatch.setattr(init_project_module, "_uv_tool_bin", lambda: None)

    lines = installation_warnings()

    assert any("commonplace-validate" in line and "not on PATH" in line for line in lines)
    assert any("uv tool update-shell" in line for line in lines)


def test_installation_warnings_report_missing_uv(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(init_project_module.shutil, "which", lambda _: None)
    monkeypatch.setattr(init_project_module, "_installed_command_names", lambda: ())
    monkeypatch.setattr(init_project_module, "_uv_tool_bin", lambda: None)

    lines = installation_warnings()

    assert any("uv is not on PATH" in line for line in lines)


def test_installation_warnings_report_shadowing_commands(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        init_project_module,
        "_installed_command_names",
        lambda: ("commonplace-validate",),
    )
    monkeypatch.setattr(
        init_project_module.shutil,
        "which",
        lambda _: "/project/.venv/bin/commonplace-validate",
    )
    monkeypatch.setattr(
        init_project_module, "_uv_tool_bin", lambda: Path("/user/uv-tool-bin")
    )

    lines = installation_warnings()

    assert any("resolve outside uv's tool executable directory" in line for line in lines)
    assert any("do not use uv tool install --force" in line for line in lines)


def test_installation_warnings_empty_for_healthy_tool_install(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        init_project_module,
        "_installed_command_names",
        lambda: ("commonplace-validate",),
    )
    monkeypatch.setattr(
        init_project_module.shutil,
        "which",
        lambda _: "/user/uv-tool-bin/commonplace-validate",
    )
    monkeypatch.setattr(
        init_project_module, "_uv_tool_bin", lambda: Path("/user/uv-tool-bin")
    )

    assert installation_warnings() == []

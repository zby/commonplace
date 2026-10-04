from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import pytest

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

REPO_ROOT = Path(__file__).resolve().parents[3]


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
        Path("kb/tags"),
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
        Path("kb/tags/COLLECTION.md"),
        Path("kb/tags/README.md"),
        Path("kb/sources/COLLECTION.md"),
        Path("kb/sources/README.md"),
        Path("kb/work/COLLECTION.md"),
        Path("kb/work/README.md"),
        Path("kb/reports/COLLECTION.md"),
        Path("kb/reports/README.md"),
        Path("kb/reports/.gitignore"),
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


def test_init_and_check_resolve_the_library_from_the_project_root(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """CI runs init from the checkout and --check from inside the project.

    The library is resolved from the project being initialized, not from the
    working directory, so both invocations compare against the same root.
    """
    monkeypatch.delenv(library.LIBRARY_ENV, raising=False)
    library_kb = library.library_root(Path.cwd())
    # Another checkout: the same library under a different path.
    other = tmp_path / "other-checkout"
    (other / "src" / "commonplace").mkdir(parents=True)
    (other / "kb").symlink_to(library_kb)
    (other / "pyproject.toml").write_text('[project]\nname = "llm-commonplace"\n', encoding="utf-8")
    project = tmp_path / "project"

    monkeypatch.chdir(other)
    init_project(project, name="project")
    routing = (project / library.ROUTING).read_text(encoding="utf-8")
    assert str(library_kb) in routing
    assert str(other / "kb") not in routing

    monkeypatch.chdir(project)
    assert [item.status for item in init_project_module.check_project(project)] == ["ok"] * len(
        init_project_module.check_project(project)
    )


def test_init_project_preserves_existing_library_and_skill_files(tmp_path: Path) -> None:
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

    before = {path: path.read_bytes() for path in tmp_path.rglob("*") if path.is_file()}

    report = init_project(tmp_path)

    assert all(path.read_bytes() == content for path, content in before.items())
    assert report.removed == []
    assert Path(".claude/skills/cp-skill-validate") in report.skipped_foreign
    assert not (old_skill / library.STUB_MARKER).exists()


def test_init_project_preserves_symlinked_skill_directories(tmp_path: Path) -> None:
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


def test_init_project_preserves_existing_kb_content_and_snapshot_pins(tmp_path: Path) -> None:
    import hashlib

    snapshot = b"---\ntype: kb/sources/types/snapshot.md\n---\n# Captured source\n"
    checksum = hashlib.sha256(snapshot).hexdigest()
    existing = {
        "kb/notes/note.md": b"---\ntype: note\n---\n# Note\n",
        "kb/notes/types/custom.schema.yaml": b"properties:\n  type:\n    const: kb/notes/types/custom.md\n",
        "kb/reports/types/custom.schema.yaml": b'allOf:\n  - $ref: "../../types/note.schema.yaml"\n',
        "kb/reports/state/report.md": b"---\ntype: kb/reports/types/full-pass-report.md\n---\n# Report\n",
        "kb/reports/retained/report.md": b"---\ntype: note\n---\n# Retained report\n",
        "kb/sources/.snapshots/source.md": snapshot,
        "kb/sources/source.ingest.md": (
            "---\ntype: ./types/ingest-report.md\n"
            f"snapshot_sha256: {checksum}\noriginal_snapshot_sha256: {checksum}\n---\n# Ingest\n"
        ).encode(),
    }
    for rel, content in existing.items():
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)

    init_project(tmp_path)
    init_project(tmp_path)

    assert {rel: (tmp_path / rel).read_bytes() for rel in existing} == existing


def test_check_reports_a_project_copy_of_a_global_type_as_a_collision(tmp_path: Path) -> None:
    init_project(tmp_path)
    copy = tmp_path / "kb" / "types" / "note.md"
    copy.parent.mkdir(parents=True)
    shutil.copy2(library.library_root() / "types" / "note.md", copy)

    statuses = init_project_module.check_project(tmp_path)

    assert ("collision", copy) in [(item.status, item.path) for item in statuses]


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


def test_a_bare_output_directory_is_not_an_initialized_project(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    # Analysis worktrees live under the same directory without any init.
    (tmp_path / ".commonplace" / "worktrees").mkdir(parents=True)
    assert library.find_project(tmp_path / ".commonplace" / "worktrees") is None
    library.warn_if_stale(tmp_path)
    assert capsys.readouterr().err == ""
    init_project(tmp_path)
    assert library.find_project(tmp_path / ".commonplace" / "worktrees") == tmp_path

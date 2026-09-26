from __future__ import annotations

import json
import os
import shutil
import subprocess
from datetime import UTC, datetime
from pathlib import Path

import pytest

from commonplace.cli import validate_notes
from commonplace.lib import validation
from commonplace.lib.naming import MAX_NOTE_SLUG_LENGTH
from commonplace.lib.snapshot import snapshot_sha256

pytestmark = pytest.mark.usefixtures("tmp_library")

REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURES_ROOT = Path(__file__).resolve().parent / "fixtures" / "schemas"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def write_type_spec(
    root: Path,
    rel_path: str,
    *,
    name: str,
    schema: str | None,
) -> Path:
    schema_value = "null" if schema is None else schema
    return write(
        root / rel_path,
        f"""---
type: types/type-spec.md
name: {name}
description: Type spec for {name}
schema: {schema_value}
---

# {name}
""",
    )


def copy_repo_file(tmp_path: Path, rel_path: str) -> Path:
    """Copy one committed repository file into the same place under tmp_path."""
    dest = tmp_path / rel_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(REPO_ROOT / rel_path, dest)
    return dest


def install_schema_tree(tmp_path: Path, tree_name: str) -> None:
    """Copy a prebuilt schema tree (fixtures/schemas/<tree_name>/) into tmp_path.

    Trees mirror the kb/ layout so each file lands at its expected location.
    """
    src = FIXTURES_ROOT / tree_name
    for path in src.rglob("*.yaml"):
        dest = tmp_path / path.relative_to(src)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, dest)


def configure_temp_repo(tmp_path: Path) -> Path:
    install_schema_tree(tmp_path, "flat")
    write(tmp_path / "kb" / "notes" / "COLLECTION.md", "# Notes collection\n")
    write_type_spec(
        tmp_path,
        "kb/types/note.md",
        name="note",
        schema="kb/types/note.schema.yaml",
    )
    write_type_spec(
        tmp_path,
        "kb/notes/types/structured-claim.md",
        name="structured-claim",
        schema="kb/notes/types/structured-claim.schema.yaml",
    )
    return tmp_path / "kb" / "notes"


def configure_tag_readme_repo(tmp_path: Path) -> Path:
    notes = configure_temp_repo(tmp_path)
    copy_repo_file(tmp_path, "kb/types/note-base.schema.yaml")
    copy_repo_file(tmp_path, "kb/types/tag-readme.schema.yaml")
    write_type_spec(
        tmp_path,
        "kb/types/tag-readme.md",
        name="tag-readme",
        schema="kb/types/tag-readme.schema.yaml",
    )
    write(
        tmp_path / "kb" / "tags" / "COLLECTION.md",
        "---\nparticipating: [notes]\n---\n\n# Tags\n",
    )
    return notes


def configure_type_spec_repo(tmp_path: Path) -> None:
    write(tmp_path / "kb" / "notes" / "COLLECTION.md", "# Notes collection\n")
    copy_repo_file(tmp_path, "kb/types/type-spec.schema.yaml")
    write_type_spec(
        tmp_path,
        "kb/types/type-spec.md",
        name="type-spec",
        schema="kb/types/type-spec.schema.yaml",
    )


def configure_snapshot_repo(tmp_path: Path) -> None:
    copy_repo_file(tmp_path, "kb/types/snapshot.schema.yaml")
    write_type_spec(
        tmp_path,
        "kb/types/snapshot.md",
        name="snapshot",
        schema="kb/types/snapshot.schema.yaml",
    )


def configure_sources_collection(tmp_path: Path) -> Path:
    sources = tmp_path / "kb" / "sources"
    write(sources / "COLLECTION.md", "# Sources\n")
    return sources


def configure_orphan_snapshot_sources(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A sources collection with one text file and one uncatalogued snapshot."""
    sources = configure_sources_collection(tmp_path)
    write(sources / "scratch.md", "Visible source work.\n")
    write(sources / ".snapshots" / "orphan.md", "uncatalogued bytes\n")
    monkeypatch.chdir(tmp_path)


def type_labelled_findings(results: validation.CheckResults, name: str) -> list[str]:
    return [
        finding
        for findings in (results.passes, results.warns, results.fails, results.infos)
        for finding in findings
        if finding.startswith(f"[type: {name}]")
    ]


def test_text_file_has_no_structural_requirements(tmp_path: Path) -> None:
    note = write(tmp_path / "raw-capture.md", "# Raw capture\n\nJust text.\n")

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.note_type == "text"
    assert results.fails == []
    assert any("no frontmatter" in item for item in results.passes)


def test_imperative_type_rules_dispatch_by_path_not_bare_name(tmp_path: Path) -> None:
    notes = configure_tag_readme_repo(tmp_path)
    write_type_spec(
        tmp_path,
        "kb/notes/types/tag-readme.md",
        name="tag-readme",
        schema=None,
    )
    local = write(
        notes / "same-name-local-type.md",
        """---
description: Local type that deliberately shares a framework type name
type: notes/types/tag-readme.md
---

# Same-name local type
""",
    )
    framework = write(
        tmp_path / "kb" / "tags" / "topic-README.md",
        """---
description: Curated head of the framework tag-readme type, whose imperative rules run
type: types/tag-readme.md
---

# Topic
""",
    )

    local_results = validation.validate_note(local, repo_root=tmp_path)
    framework_results = validation.validate_note(framework, repo_root=tmp_path)

    assert local_results.note_type == "tag-readme"
    assert type_labelled_findings(local_results, "tag-readme") == []
    # Positive control: the same label does appear when the framework type runs.
    assert framework_results.note_type == "tag-readme"
    assert type_labelled_findings(framework_results, "tag-readme") != []


def test_source_snapshot_requires_h1_as_first_nonblank_body_line(
    tmp_path: Path,
) -> None:
    configure_snapshot_repo(tmp_path)
    snapshot = write(
        tmp_path / "kb" / "sources" / "sample.md",
        """---
source: https://example.com/article
captured: "2026-04-19"
capture: web-fetch
type: types/snapshot.md
---

Captured text before the title.

# Accidental later heading
""",
    )

    results = validation.validate_note(snapshot, repo_root=tmp_path)

    assert any(
        "snapshot structure: first nonblank body line must be an H1 title" in item
        for item in results.fails
    )


def test_link_validation_checks_local_targets_and_skips_code_and_external(
    tmp_path: Path,
) -> None:
    configure_temp_repo(tmp_path)
    write(tmp_path / "target.txt", "Target\n")
    (tmp_path / "existing-dir").mkdir()
    note = write(
        tmp_path / "note.md",
        """---
description: A note with resolving, missing, code-span, and external links so link health checks each kind
type: types/note.md
traits: []
---

# Link validation note

Existing file: [target](./target.txt)
Existing file with fragment and query: [target details](./target.txt?mode=brief#details)
Existing directory: [directory](./existing-dir/)
Missing note: [missing](./missing.md)
Missing directory: [missing directory](./missing-dir/)
Missing non-md file: [missing text](./missing.txt)
Anchor-only link: [heading](#heading)
External link: [site](https://example.com/foo.md)
External scheme: [mail](mailto:person@example.com)
Protocol-relative URL: [cdn](//example.com/file.txt)

`[inline-code](./ignored.md)`

```md
[fenced](./also-ignored.md)
```
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert all(
        "link health: all local relative links resolve" not in item
        for item in results.passes
    )
    for missing in ("./missing.md", "./missing-dir/", "./missing.txt"):
        assert any(
            f"link health: missing target {missing}" in item for item in results.warns
        )
    for skipped in ("target.txt", "existing-dir", "#heading", "ignored.md", "example.com"):
        assert all(skipped not in item for item in results.warns)


def test_link_health_and_inbound_detection_share_url_resolution(tmp_path: Path) -> None:
    notes = configure_temp_repo(tmp_path)
    source = write(
        notes / "source.md",
        """---
description: Source note exercising normalized local and external Markdown link targets
type: types/note.md
traits: []
---

# Source

[Encoded target](./target%20name.md?mode=brief#details)
[Uppercase external scheme](HTTPS://example.com/external.md)
[Self](./source.md#local)
""",
    )
    target = write(
        notes / "target name.md",
        """---
description: Target note whose filename requires percent decoding during link resolution
type: types/note.md
traits: []
---

# Target
""",
    )

    results = validation.validate_note(source, repo_root=tmp_path)
    run = validation.ValidationRun(
        repo_root=tmp_path,
        paths=(source, target),
        collection=notes,
    )
    inbound = run.inbound_info((source, target))

    assert any(
        "link health: all local relative links resolve" in item
        for item in results.passes
    )
    assert results.warns == []
    assert inbound[source.resolve()] is False
    assert inbound[target.resolve()] is True


@pytest.mark.parametrize(
    ("filename", "frontmatter", "expected_type"),
    [
        (
            "source.md",
            (
                "---\ndescription: Library note linking to a retired proposal that must "
                "stay outside the live knowledge graph\ntype: types/note.md\n"
                "traits: []\n---\n\n"
            ),
            "note",
        ),
        ("README.md", "", "text"),
    ],
)
def test_library_artifact_cannot_link_to_archived_proposal(
    tmp_path: Path, filename: str, frontmatter: str, expected_type: str
) -> None:
    notes = configure_temp_repo(tmp_path)
    archived = write(
        tmp_path / "kb/reference/proposals/archive/retired.md",
        "# Retired proposal\n",
    )
    note = write(
        notes / filename,
        f"{frontmatter}# Source\n\n[Retired proposal]({os.path.relpath(archived, notes)})\n",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.note_type == expected_type
    assert any(
        "proposal archive boundary: library artifact links to archived proposal"
        in item
        for item in results.fails
    )


def test_proposal_archive_boundary_ignores_links_between_archived_files(
    tmp_path: Path,
) -> None:
    configure_temp_repo(tmp_path)
    write(tmp_path / "kb" / "reference" / "COLLECTION.md", "# Reference collection\n")
    archive = tmp_path / "kb" / "reference" / "proposals" / "archive"
    write(archive / "older.md", "# Older\n")
    newer = write(
        archive / "newer.md",
        "---\ndescription: An archived proposal that cites its archived sibling for texture\ntype: types/note.md\n---\n\n# Newer\n\nSee [older](./older.md).\n",
    )

    results = validation.validate_note(newer, repo_root=tmp_path)

    assert not any("archive boundary" in f for f in results.fails)


def test_proposal_archive_boundary_allows_readme_and_workshop_links(
    tmp_path: Path,
) -> None:
    notes = configure_temp_repo(tmp_path)
    archive = tmp_path / "kb/reference/proposals/archive"
    archive_readme = write(archive / "README.md", "# Proposal archive\n")
    archived = write(archive / "retired.md", "# Retired proposal\n")
    library_note = write(
        notes / "source.md",
        f"""---
description: Library note entering the proposal archive through its permitted reader-facing README
type: types/note.md
traits: []
---

# Source

[Archive instructions]({os.path.relpath(archive_readme, notes)})
""",
    )
    work = tmp_path / "kb/work"
    write(work / "COLLECTION.md", "# Workshop collection\n")
    workshop_note = write(
        work / "audit.md",
        f"# Audit\n\n[Retired proposal]({os.path.relpath(archived, work)})\n",
    )
    write(
        archive_readme,
        "# Proposal archive\n\n[Retired proposal](./retired.md)\n",
    )

    for path in (library_note, workshop_note, archive_readme):
        results = validation.validate_note(path, repo_root=tmp_path)
        assert results.fails == []


def test_non_path_frontmatter_type_fails_validation(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
    note = write(
        notes_root / "invalid-type.md",
        """---
description: A bare frontmatter type is a retired form, so it must be rejected with the path to use
type: spec
---

# Invalid type value
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.note_type == "unknown"
    assert any(
        "use `type: types/spec.md`" in item
        for item in results.fails
    )


def test_peer_collection_local_type_fails_validation(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
    write(tmp_path / "kb" / "reference" / "COLLECTION.md", "# Reference\n")
    write_type_spec(
        tmp_path,
        "kb/reference/types/adr.md",
        name="adr",
        schema=None,
    )
    note = write(
        notes_root / "wrong-local-type.md",
        """---
description: Peer collection local types should fail deterministic validation
type: reference/types/adr.md
---

# Wrong local type
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.note_type == "unknown"
    assert any(
        "kb/reference/types/adr.md is not eligible in collection kb/notes" in item
        for item in results.fails
    )


def test_type_spec_validation_resolves_its_own_declared_schema(tmp_path: Path) -> None:
    configure_type_spec_repo(tmp_path)
    type_spec = write_type_spec(
        tmp_path,
        "kb/notes/types/local.md",
        name="local",
        schema="kb/notes/types/missing.schema.yaml",
    )

    results = validation.validate_note(type_spec, repo_root=tmp_path)

    assert any(
        "[type: type-spec] type definition: "
        "notes/types/local.md: schema file is missing" in failure
        for failure in results.fails
    )


def test_type_spec_validation_accepts_explicitly_schema_less_type(
    tmp_path: Path,
) -> None:
    configure_type_spec_repo(tmp_path)
    type_spec = write_type_spec(
        tmp_path,
        "kb/notes/types/local.md",
        name="local",
        schema=None,
    )

    results = validation.validate_note(type_spec, repo_root=tmp_path)

    assert results.fails == []
    assert any(
        "[type: type-spec] type definition: schema is explicitly null" in item
        for item in results.passes
    )


def test_type_spec_validation_rejects_tags(tmp_path: Path) -> None:
    configure_type_spec_repo(tmp_path)
    type_spec = write(
        tmp_path / "kb" / "notes" / "types" / "local.md",
        """---
type: types/type-spec.md
name: local
description: Type spec for local
schema: null
tags: [learning-theory]
---

# local
""",
    )

    results = validation.validate_note(type_spec, repo_root=tmp_path)

    assert any("[schema]" in failure and "tags" in failure for failure in results.fails)


@pytest.mark.parametrize(
    ("content", "expected_pass", "expected_warn"),
    [
        (
            (
                "Retrieval latency dominates at scale.\n\n"
                "> p95 retrieval latency was 340ms, 6x the generation step\n"
                "> --- `src/memory/store.py` @ `abc123`\n"
            ),
            "quote-anchored citations: 1 well-formed",
            None,
        ),
        (
            (
                "> p95 retrieval latency was 340ms\n"
                "> --- [src/memory/store.py]"
                "(https://github.com/org/repo/blob/abc123/src/memory/store.py)\n"
            ),
            "quote-anchored citations: 1 well-formed",
            None,
        ),
        (
            "> p95 retrieval latency was 340ms\n> --- the documentation\n",
            None,
            "names no source",
        ),
        ("Some prose.\n\n> --- `src/memory/store.py`\n", None, "no quoted text above"),
    ],
)
def test_quote_citation_shape(
    content: str, expected_pass: str | None, expected_warn: str | None
) -> None:
    results = validation.CheckResults(note_type="agent-memory-system-review")

    validation.validate_quote_citations(results, content)

    if expected_pass is None:
        assert any(expected_warn in item for item in results.warns)
    else:
        assert any(expected_pass in item for item in results.passes)
        assert results.warns == []


def test_title_length_over_limit_fails_validation(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
    title = "A" * 101
    note = write(
        notes_root / "short-slug.md",
        f"""---
description: Note with an overly long title so the validator should fail deterministically on title length
type: types/note.md
traits: []
---

# {title}
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert any(
        "title: 101 chars exceeds limit of 100" in item for item in results.fails
    )


def test_filename_slug_length_over_limit_fails_validation(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
    overlong_slug = "a" * (MAX_NOTE_SLUG_LENGTH + 1)
    note = write(
        notes_root / f"{overlong_slug}.md",
        """---
description: Note with an overly long slug so the validator should fail deterministically on filename length
type: types/note.md
traits: []
---

# Short title
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    expected = (
        f"filename slug: {MAX_NOTE_SLUG_LENGTH + 1} chars exceeds limit of "
        f"{MAX_NOTE_SLUG_LENGTH}"
    )
    assert any(expected in item for item in results.fails)


def test_git_ignored_artifact_is_exempt_from_authored_length_limits(
    tmp_path: Path,
) -> None:
    notes_root = configure_temp_repo(tmp_path)
    ignored_dir = notes_root / "ignored"
    write(tmp_path / ".gitignore", "kb/notes/ignored/\n")
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    overlong_slug = "a" * (MAX_NOTE_SLUG_LENGTH + 1)
    title = "A" * 101
    note = write(
        ignored_dir / f"{overlong_slug}.md",
        f"""---
description: Ignored local artifact whose source-derived title and filename may exceed authored library limits
type: types/note.md
traits: []
---

# {title}
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.fails == []
    assert any(
        "title: 101 chars (git-ignored artifact; authored-artifact limit not applied)"
        in item
        for item in results.passes
    )
    expected_slug = (
        f"filename slug: {MAX_NOTE_SLUG_LENGTH + 1} chars "
        "(git-ignored artifact; authored-artifact limit not applied)"
    )
    assert any(expected_slug in item for item in results.passes)


def test_connect_report_derived_slug_is_exempt_from_note_limit(tmp_path: Path) -> None:
    configure_temp_repo(tmp_path)
    write(tmp_path / "kb" / "reports" / "COLLECTION.md", "# Reports collection\n")
    copy_repo_file(tmp_path, "kb/types/connect-report.md")
    copy_repo_file(tmp_path, "kb/types/connect-report.schema.yaml")
    source_slug = "a" * MAX_NOTE_SLUG_LENGTH
    report = write(
        tmp_path
        / "kb"
        / "reports"
        / "cache"
        / "connect"
        / "notes"
        / f"{source_slug}.connect.md",
        """---
description: Derived connection report whose filename preserves a valid source artifact slug
type: types/connect-report.md
---

# Connection report
""",
    )

    results = validation.validate_note(report, repo_root=tmp_path)

    derived_slug_length = MAX_NOTE_SLUG_LENGTH + len(".connect")
    # The global connect-report schema also applies; only the slug rule is under test.
    assert not any("filename slug" in item for item in results.fails)
    expected = (
        f"filename slug: {derived_slug_length} chars "
        "(derived connect-report name; authored-artifact limit not applied)"
    )
    assert any(expected in item for item in results.passes)


def test_recent_target_uses_mtime_and_target_lookup(tmp_path: Path) -> None:
    notes_root = tmp_path / "kb" / "notes"
    write(notes_root / "COLLECTION.md", "# Notes collection\n")
    today_note = write(
        notes_root / "today.md",
        """---
description: Note modified today so recent target resolution should find it deterministically
type: types/note.md
traits: []
---

# Today note
""",
    )
    old_note = write(
        notes_root / "old.md",
        """---
description: Older note that should not be picked up by recent target resolution in deterministic validation
type: types/note.md
traits: []
---

# Old note
""",
    )
    old_ts = datetime(2020, 1, 1, tzinfo=UTC).timestamp()
    old_note.touch()
    today_note.touch()
    os.utime(old_note, (old_ts, old_ts))

    recent = validate_notes.resolve_validation_target("recent", repo_root=tmp_path)

    assert today_note.resolve() in recent.paths
    assert old_note.resolve() not in recent.paths
    assert recent.collection is None


def test_notes_target_scans_only_notes_collection(tmp_path: Path) -> None:
    write(tmp_path / "kb" / "notes" / "COLLECTION.md", "# Notes collection\n")
    write(tmp_path / "kb" / "reports" / "COLLECTION.md", "# Reports collection\n")
    note = write(
        tmp_path / "kb" / "notes" / "note.md",
        """---
description: Note in the notes collection
type: types/note.md
traits: []
---

# Note
""",
    )
    report = write(
        tmp_path / "kb" / "reports" / "retained" / "report.md",
        """---
description: Report outside the notes collection
type: types/note.md
traits: []
---

# Report
""",
    )
    local_type = write(
        tmp_path / "kb" / "notes" / "types" / "local.md",
        "# Local type\n",
    )

    notes = validate_notes.resolve_validation_target("notes", repo_root=tmp_path)

    assert note in notes.paths
    assert local_type in notes.paths
    assert report not in notes.paths
    assert notes.collection == (tmp_path / "kb" / "notes").resolve()


def test_types_target_scans_all_type_spec_directories(tmp_path: Path) -> None:
    global_type = write(tmp_path / "kb" / "types" / "note.md", "# Note type\n")
    local_type = write(
        tmp_path / "kb" / "notes" / "types" / "structured-claim.md",
        "# Structured claim type\n",
    )
    write(tmp_path / "kb" / "types" / "text.md", "# Text\n")
    template = write(
        tmp_path / "kb" / "notes" / "types" / "example.template.md",
        "# Template\n",
    )

    target = validate_notes.resolve_validation_target("types", repo_root=tmp_path)

    assert target.paths == (
        template,
        local_type,
        global_type,
    )
    assert target.collection is None


def test_note_target_also_validates_marked_tag_readmes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    notes = configure_tag_readme_repo(tmp_path)
    write(
        notes / "tagged-note.md",
        """---
description: "Tagged note with enough metadata to validate cleanly by itself"
type: types/note.md
tags: [kb-design, unmarked]
---

# Tagged note
""",
    )
    write(
        tmp_path / "kb" / "tags" / "kb-design-README.md",
        """---
description: "Complete curated head for the kb-design tag"
type: types/tag-readme.md
complete: true
---

# kb-design

Orientation paragraph.
""",
    )
    write(
        tmp_path / "kb" / "tags" / "unmarked-README.md",
        """---
description: "Selective curated head for the unmarked tag"
type: types/tag-readme.md
---

# unmarked

Orientation paragraph.
""",
    )
    monkeypatch.chdir(tmp_path)

    exit_code = validate_notes.main(["--full", "kb/notes/tagged-note.md"])
    output = capsys.readouterr().out

    assert exit_code == 1
    assert "=== VALIDATION: tagged-note.md ===" in output
    assert "=== VALIDATION: kb-design-README.md ===" in output
    assert "=== VALIDATION: unmarked-README.md ===" not in output
    assert "complete mark: missing entry for kb/notes/tagged-note.md" in output
    assert "=== BATCH INFO ===" not in output


def test_bulk_scopes_are_rejected(tmp_path: Path) -> None:
    (tmp_path / "kb").mkdir()
    (tmp_path / "kb" / "notes").mkdir()

    for target in ("all", "kb", "kb/"):
        with pytest.raises(ValueError):
            validate_notes.resolve_validation_target(target, repo_root=tmp_path)


def test_lifecycle_target_emits_stable_json_diagnostics(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    write(tmp_path / "kb/work/README.md", "# Work\n")
    write(tmp_path / "kb/work/unframed/scratch.md", "Scratch\n")
    monkeypatch.chdir(tmp_path)

    exit_code = validate_notes.main(["--json", "lifecycle"])
    payload = json.loads(capsys.readouterr().out)

    assert exit_code == 1
    assert payload["schema"] == "commonplace.validation.v1"
    assert payload["status"] == "failed"
    assert [item["id"] for item in payload["diagnostics"]] == [
        "lifecycle.workshop.unregistered",
        "lifecycle.workshop.missing-framing",
    ]


def test_collection_directory_targets_scan_that_collection(tmp_path: Path) -> None:
    configure_temp_repo(tmp_path)
    write(
        tmp_path / "kb" / "agent-memory-systems" / "COLLECTION.md",
        "# Agent memory systems\n",
    )
    collection_note = write(
        tmp_path / "kb" / "agent-memory-systems" / "index.md",
        """---
description: Agent memory systems index note
type: types/note.md
traits: []
---

# Agent Memory Systems
""",
    )
    review_note = write(
        tmp_path / "kb" / "agent-memory-systems" / "reviews" / "agent-r.md",
        """---
description: Agent R review note
type: types/note.md
traits: []
---

# Agent R
""",
    )
    template = write(
        tmp_path / "kb" / "agent-memory-systems" / "types" / "review.template.md",
        """---
description: Template that should not be validated as collection content
type: types/note.md
---

# Template
""",
    )
    local_type = write(
        tmp_path / "kb" / "agent-memory-systems" / "types" / "review.md",
        "# Review type\n",
    )
    other_note = write(
        tmp_path / "kb" / "reports" / "retained" / "report.md",
        """---
description: Report outside the target collection
type: types/note.md
traits: []
---

# Report
""",
    )

    bare_collection = validate_notes.resolve_validation_target(
        "agent-memory-systems", repo_root=tmp_path
    )
    repo_relative_dir = validate_notes.resolve_validation_target(
        "kb/agent-memory-systems", repo_root=tmp_path
    )

    assert bare_collection == repo_relative_dir
    assert collection_note in bare_collection.paths
    assert review_note in bare_collection.paths
    assert local_type in bare_collection.paths
    assert template in bare_collection.paths
    assert other_note not in bare_collection.paths
    assert bare_collection.collection == (
        tmp_path / "kb" / "agent-memory-systems"
    )


def test_directory_without_collection_file_is_not_a_validation_scope(
    tmp_path: Path,
) -> None:
    configure_temp_repo(tmp_path)
    write(
        tmp_path / "kb" / "tasks" / "report.md",
        """---
description: Report in a support directory without collection conventions
type: types/note.md
traits: []
---

# Report
""",
    )

    with pytest.raises(ValueError, match="not a KB collection"):
        validate_notes.resolve_validation_target("kb/tasks", repo_root=tmp_path)


def test_validate_collection_structure_flags_nested_collection(tmp_path: Path) -> None:
    configure_temp_repo(tmp_path)
    write(
        tmp_path / "kb" / "notes" / "definitions" / "COLLECTION.md", "# Definitions\n"
    )

    failures = validation.validate_collection_structure(
        tmp_path / "kb" / "notes",
        repo_root=tmp_path,
    )

    assert failures == [
        (
            tmp_path / "kb" / "notes" / "definitions" / "COLLECTION.md",
            "nested COLLECTION.md: kb/notes/definitions/COLLECTION.md is inside collection kb/notes",
        )
    ]


def test_validate_collection_structure_allows_namespace_collections(
    tmp_path: Path,
) -> None:
    collection = tmp_path / "kb" / "commonplace" / "notes"
    write(collection / "COLLECTION.md", "# Shipped notes\n")

    failures = validation.validate_collection_structure(
        collection, repo_root=tmp_path
    )

    assert failures == []


def test_source_snapshot_cache_warns_about_redundant_alternate_copy(
    tmp_path: Path,
) -> None:
    sources = configure_sources_collection(tmp_path)
    expected = write(sources / ".snapshots" / "source.md", "same bytes\n")
    duplicate = write(sources / ".snapshots" / "adapter-name.md", "same bytes\n")
    write(
        sources / "source.ingest.md",
        f"---\nsnapshot_sha256: {snapshot_sha256(expected)}\n---\n",
    )

    warnings = validation.validate_source_snapshot_cache(
        sources, repo_root=tmp_path
    )

    assert warnings == [
        (
            duplicate,
            (
                "unpaired local snapshot: no same-stem ingest; its checksum "
                "duplicates the valid name-paired snapshot for "
                "kb/sources/source.ingest.md"
            ),
        )
    ]


def test_source_collection_validation_prints_local_snapshot_warning(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    configure_orphan_snapshot_sources(tmp_path, monkeypatch)

    exit_code = validate_notes.main(["sources"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "VALIDATION WARNING" in output
    assert "1 warnings across 1 subjects" in output
    assert "validation.collection-warning.unpaired-local-snapshot" in output
    assert (
        "kb/sources/.snapshots/orphan.md: unpaired local snapshot: no same-stem "
        "ingest and no ingest matches its source URL or checksum"
    ) not in output
    assert (
        "kb/sources/.snapshots/orphan.md | unpaired local snapshot: no same-stem "
        "ingest and no ingest matches its source URL or checksum"
    ) in output


def test_validation_json_is_compact_and_structured(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    configure_orphan_snapshot_sources(tmp_path, monkeypatch)

    exit_code = validate_notes.main(["--json", "sources"])
    payload = json.loads(capsys.readouterr().out)

    assert exit_code == 0
    assert payload["schema"] == "commonplace.validation.v1"
    assert payload["status"] == "warning"
    assert payload["summary"] == {
        "failing_subjects": 0,
        "failures": 0,
        "files_analysed": 1,
        "text_files": 1,
        "warning_subjects": 1,
        "warnings": 1,
    }
    assert payload["diagnostics"] == [
        {
            "id": "validation.collection-warning.unpaired-local-snapshot",
            "reason": (
                "unpaired local snapshot: no same-stem ingest and no ingest "
                "matches its source URL or checksum"
            ),
            "severity": "warning",
            "subject": "kb/sources/.snapshots/orphan.md",
        }
    ]
    assert payload["analysed_artifacts"] == [
        {
            "failures": 0,
            "path": "kb/sources/scratch.md",
            "type": "text",
            "warnings": 0,
        }
    ]
    assert payload["details_command"] == "commonplace-validate --full sources"


def test_validation_json_output_matches_stdout_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsysbinary: pytest.CaptureFixture[bytes],
) -> None:
    sources = configure_sources_collection(tmp_path)
    write(sources / "scratch.md", "Visible source work.\n")
    receipt = tmp_path / "validation.json"
    monkeypatch.chdir(tmp_path)

    exit_code = validate_notes.main(
        ["--json", "--output", receipt.as_posix(), "sources"]
    )
    stdout = capsysbinary.readouterr().out

    assert exit_code == 0
    assert receipt.read_bytes() == stdout
    assert json.loads(stdout)["status"] == "success"


def test_validation_json_identifies_one_typed_external_artifact(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    configure_temp_repo(tmp_path)
    result = tmp_path / "result.md"
    result.write_text(
        """---
description: "A typed note outside a collection"
type: types/note.md
tags: []
---

# External result
""",
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)

    exit_code = validate_notes.main(["--json", str(result)])
    payload = json.loads(capsys.readouterr().out)

    assert exit_code == 0
    assert payload["summary"]["files_analysed"] == 1
    assert payload["summary"]["text_files"] == 0
    assert len(payload["analysed_artifacts"]) == 1
    assert payload["analysed_artifacts"][0] == {
        "failures": 0,
        "path": "result.md",
        "type": "note",
        "warnings": payload["summary"]["warnings"],
    }


def test_source_snapshot_cache_reports_same_url_as_related_observation(
    tmp_path: Path,
) -> None:
    sources = configure_sources_collection(tmp_path)
    related = write(
        sources / ".snapshots" / "older-name.md",
        "---\nsource: https://example.com/article\n---\n\nOlder bytes.\n",
    )
    write(
        sources / "current.ingest.md",
        "---\nsource: https://example.com/article\n"
        f"snapshot_sha256: {'1' * 64}\n---\n",
    )

    warnings = validation.validate_source_snapshot_cache(
        sources, repo_root=tmp_path
    )

    assert warnings == [
        (
            related,
            (
                "unpaired local snapshot: no same-stem ingest; its source URL "
                "matches kb/sources/current.ingest.md, but no matching ingest "
                "records these exact bytes"
            ),
        )
    ]


def test_source_snapshot_cache_recognizes_derived_original_by_checksum(
    tmp_path: Path,
) -> None:
    sources = configure_sources_collection(tmp_path)
    original = write(
        sources / ".snapshots" / "article.md",
        "---\nsource: https://example.com/article\n---\n\nOriginal bytes.\n",
    )
    translated = write(
        sources / ".snapshots" / "article.en.md",
        "---\nsource: https://example.com/article\n---\n\nTranslated bytes.\n",
    )
    write(
        sources / "article.en.ingest.md",
        "---\nsource: https://example.com/article\n"
        f"snapshot_sha256: {snapshot_sha256(translated)}\n"
        f"original_snapshot_sha256: {snapshot_sha256(original)}\n---\n",
    )

    warnings = validation.validate_source_snapshot_cache(
        sources, repo_root=tmp_path
    )

    assert warnings == []

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import pytest

from commonplace.cli import validate_notes
from commonplace.lib import validation
from commonplace.lib.naming import MAX_NOTE_SLUG_LENGTH

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
type: kb/types/type-spec.md
name: {name}
description: Type spec for {name}
schema: {schema_value}
---

# {name}
""",
    )


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
    write_type_spec(
        tmp_path,
        "kb/types/tag-readme.md",
        name="tag-readme",
        schema="kb/types/tag-readme.schema.yaml",
    )
    write(
        tmp_path / "kb" / "types" / "tag-readme.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
required:
  - frontmatter
properties:
  frontmatter:
    type: object
    required:
      - description
      - type
      - index_source
      - index_key
    properties:
      type:
        const: kb/types/tag-readme.md
      index_source:
        const: tag
      index_key:
        type: string
      complete:
        type: boolean
      covered_by:
        type: array
        items:
          type: string
      user-verified:
        const: true
      status: false
    additionalProperties: true
""",
    )
    return notes


def configure_type_spec_repo(tmp_path: Path) -> None:
    notes = tmp_path / "kb" / "notes"
    write(notes / "COLLECTION.md", "# Notes collection\n")
    write(
        tmp_path / "kb" / "types" / "type-spec.schema.yaml",
        (Path.cwd() / "kb" / "types" / "type-spec.schema.yaml").read_text(
            encoding="utf-8"
        ),
    )
    write_type_spec(
        tmp_path,
        "kb/types/type-spec.md",
        name="type-spec",
        schema="kb/types/type-spec.schema.yaml",
    )


def test_text_file_has_no_structural_requirements(tmp_path: Path) -> None:
    note = write(tmp_path / "raw-capture.md", "# Raw capture\n\nJust text.\n")

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.note_type == "text"
    assert results.fails == []
    assert any("no frontmatter" in item for item in results.passes)


def test_imperative_type_rules_dispatch_by_path_not_bare_name(tmp_path: Path) -> None:
    configure_temp_repo(tmp_path)
    write_type_spec(
        tmp_path,
        "kb/notes/types/tag-readme.md",
        name="tag-readme",
        schema=None,
    )
    note = write(
        tmp_path / "kb" / "notes" / "same-name-local-type.md",
        """---
description: Local type that deliberately shares a framework type name
type: kb/notes/types/tag-readme.md
---

# Same-name local type
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.note_type == "tag-readme"
    assert not any(
        finding.startswith("[type: tag-readme]")
        for findings in (results.passes, results.warns, results.fails, results.infos)
        for finding in findings
    )


def test_source_snapshot_validates_without_description(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "sources" / "types" / "snapshot.schema.yaml",
        (Path.cwd() / "kb" / "sources" / "types" / "snapshot.schema.yaml").read_text(
            encoding="utf-8"
        ),
    )
    write_type_spec(
        tmp_path,
        "kb/sources/types/snapshot.md",
        name="snapshot",
        schema="kb/sources/types/snapshot.schema.yaml",
    )
    snapshot = write(
        tmp_path / "kb" / "sources" / "sample.md",
        """---
source: https://example.com/article
captured: "2026-04-19"
capture: web-fetch
capture_scope: full-source
genre: conceptual-essay
type: kb/sources/types/snapshot.md
---

# Sample

Captured text.
""",
    )

    results = validation.validate_note(snapshot, repo_root=tmp_path)

    assert results.note_type == "snapshot"
    assert results.fails == []
    assert any(
        "type schema: snapshot requirements satisfied" in item
        for item in results.passes
    )


def test_source_snapshot_allows_genre_to_be_omitted(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "sources" / "types" / "snapshot.schema.yaml",
        (Path.cwd() / "kb" / "sources" / "types" / "snapshot.schema.yaml").read_text(
            encoding="utf-8"
        ),
    )
    write_type_spec(
        tmp_path,
        "kb/sources/types/snapshot.md",
        name="snapshot",
        schema="kb/sources/types/snapshot.schema.yaml",
    )
    snapshot = write(
        tmp_path / "kb" / "sources" / "sample.md",
        """---
source: https://example.com/article
captured: "2026-04-19"
capture: web-fetch
type: kb/sources/types/snapshot.md
---

# Sample

Captured text.
""",
    )

    results = validation.validate_note(snapshot, repo_root=tmp_path)

    assert results.note_type == "snapshot"
    assert results.fails == []


def test_source_snapshot_off_list_genre_warns_not_fails(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "sources" / "types" / "snapshot.schema.yaml",
        (Path.cwd() / "kb" / "sources" / "types" / "snapshot.schema.yaml").read_text(
            encoding="utf-8"
        ),
    )
    write_type_spec(
        tmp_path,
        "kb/sources/types/snapshot.md",
        name="snapshot",
        schema="kb/sources/types/snapshot.schema.yaml",
    )
    snapshot = write(
        tmp_path / "kb" / "sources" / "sample.md",
        """---
source: https://example.com/article
captured: "2026-04-19"
capture: web-fetch
genre: podcast-transcript
type: kb/sources/types/snapshot.md
---

# Sample

Captured text.
""",
    )

    results = validation.validate_note(snapshot, repo_root=tmp_path)

    assert results.note_type == "snapshot"
    assert results.fails == []
    assert any("genre" in item for item in results.warns)


def test_source_snapshot_requires_h1_as_first_nonblank_body_line(
    tmp_path: Path,
) -> None:
    write(
        tmp_path / "kb" / "sources" / "types" / "snapshot.schema.yaml",
        (Path.cwd() / "kb" / "sources" / "types" / "snapshot.schema.yaml").read_text(
            encoding="utf-8"
        ),
    )
    write_type_spec(
        tmp_path,
        "kb/sources/types/snapshot.md",
        name="snapshot",
        schema="kb/sources/types/snapshot.schema.yaml",
    )
    snapshot = write(
        tmp_path / "kb" / "sources" / "sample.md",
        """---
source: https://example.com/article
captured: "2026-04-19"
capture: web-fetch
type: kb/sources/types/snapshot.md
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


def configure_ingest_report_repo(tmp_path: Path) -> None:
    for name in ("note-base.schema.yaml", "note.schema.yaml"):
        write(
            tmp_path / "kb" / "types" / name,
            (Path.cwd() / "kb" / "types" / name).read_text(encoding="utf-8"),
        )
    write(
        tmp_path / "kb" / "sources" / "types" / "ingest-report.schema.yaml",
        (
            Path.cwd() / "kb" / "sources" / "types" / "ingest-report.schema.yaml"
        ).read_text(encoding="utf-8"),
    )
    write_type_spec(
        tmp_path,
        "kb/sources/types/ingest-report.md",
        name="ingest-report",
        schema="kb/sources/types/ingest-report.schema.yaml",
    )


def code_grounded_ingest(
    *,
    include_heading: bool,
    secondary_sources: str | None = None,
) -> str:
    headings = "\n## Code Grounding\n\nStatic source inspection only.\n" if include_heading else ""
    if secondary_sources is None:
        secondary_sources = """secondary_sources:
  - role: implementation
    source: https://github.com/example/system/commit/0123456789abcdef0123456789abcdef01234567
  - role: implementation
    source: https://github.com/example/second/commit/89abcdef0123456789abcdef0123456789abcdef
"""
    return f"""---
description: Code-grounded analysis of a paper and its released implementation
source: https://arxiv.org/abs/2608.12345v1
captured: "2026-08-18"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
ingested: "2026-08-18"
type: kb/sources/types/ingest-report.md
domains: [agents, evaluation]
{secondary_sources.rstrip()}
---

# Ingest: Paper

## Classification

Scientific paper.

## Summary

Summary.
{headings}
## Quotes

No source quotes have been retained yet.

## Connections Found

Connections.

## Extractable Value

1. Value. [quick-win]

## Limitations (our opinion)

Limitations.

## Recommended Next Action

File as a reference.
"""


def test_code_grounded_ingest_requires_code_grounding_section(tmp_path: Path) -> None:
    configure_ingest_report_repo(tmp_path)
    ingest = write(
        tmp_path / "kb" / "sources" / "paper.ingest.md",
        code_grounded_ingest(include_heading=False),
    )

    results = validation.validate_note(ingest, repo_root=tmp_path)

    assert any("missing '## Code Grounding'" in item for item in results.fails)


def test_code_grounded_ingest_accepts_multiple_pinned_repositories(
    tmp_path: Path,
) -> None:
    configure_ingest_report_repo(tmp_path)
    ingest = write(
        tmp_path / "kb" / "sources" / "paper.ingest.md",
        code_grounded_ingest(include_heading=True),
    )

    results = validation.validate_note(ingest, repo_root=tmp_path)

    assert results.fails == []
    assert any(
        "type schema: ingest-report requirements satisfied" in item
        for item in results.passes
    )


def test_ordinary_ingest_accepts_no_secondary_sources(tmp_path: Path) -> None:
    configure_ingest_report_repo(tmp_path)
    content = code_grounded_ingest(
        include_heading=False,
        secondary_sources="",
    )
    ingest = write(tmp_path / "kb" / "sources" / "paper.ingest.md", content)

    results = validation.validate_note(ingest, repo_root=tmp_path)

    assert results.fails == []


@pytest.mark.parametrize(
    ("secondary_sources", "expected"),
    [
        ("secondary_sources: []", "should be non-empty"),
        (
            """secondary_sources:
  - role: evidence
    source: https://github.com/example/system/commit/0123456789abcdef0123456789abcdef01234567""",
            "'implementation' was expected",
        ),
        (
            """secondary_sources:
  - role: implementation
    source: https://github.com/example/system""",
            "does not match",
        ),
        (
            """secondary_sources:
  - role: implementation
    source: https://github.com/example/system/commit/0123456789abcdef0123456789abcdef01234567
    checkout: related-systems/example--system""",
            "Additional properties are not allowed",
        ),
        (
            """secondary_sources:
  - role: implementation
    source: https://github.com/example/system/commit/0123456789abcdef0123456789abcdef01234567
  - role: implementation
    source: https://github.com/example/system/commit/0123456789abcdef0123456789abcdef01234567""",
            "has non-unique elements",
        ),
    ],
)
def test_ingest_rejects_invalid_secondary_source_shapes(
    tmp_path: Path,
    secondary_sources: str,
    expected: str,
) -> None:
    configure_ingest_report_repo(tmp_path)
    ingest = write(
        tmp_path / "kb" / "sources" / "paper.ingest.md",
        code_grounded_ingest(
            include_heading=True,
            secondary_sources=secondary_sources,
        ),
    )

    results = validation.validate_note(ingest, repo_root=tmp_path)

    assert any(expected in item for item in results.fails), results.fails


@pytest.mark.parametrize("retired_field", ["source_snapshot: paper.md", "code_revisions: [old]"])
def test_ingest_rejects_retired_source_fields(
    tmp_path: Path,
    retired_field: str,
) -> None:
    configure_ingest_report_repo(tmp_path)
    content = code_grounded_ingest(include_heading=True).replace(
        "domains: [agents, evaluation]",
        f"domains: [agents, evaluation]\n{retired_field}",
    )
    ingest = write(tmp_path / "kb" / "sources" / "paper.ingest.md", content)

    results = validation.validate_note(ingest, repo_root=tmp_path)

    assert any("False schema does not allow" in item for item in results.fails)


def test_ingest_off_list_genre_warns_not_fails(tmp_path: Path) -> None:
    configure_ingest_report_repo(tmp_path)
    content = code_grounded_ingest(include_heading=True).replace(
        "genre: scientific-paper", "genre: podcast-transcript"
    )
    ingest = write(tmp_path / "kb" / "sources" / "paper.ingest.md", content)

    results = validation.validate_note(ingest, repo_root=tmp_path)

    assert results.fails == []
    assert any("genre" in item for item in results.warns)


@pytest.mark.parametrize(
    ("old", "new", "expected"),
    [
        (
            "source: https://arxiv.org/abs/2608.12345v1",
            "source: arxiv:2608.12345v1",
            "does not match",
        ),
        (
            'captured: "2026-08-18"',
            'captured: "not-a-date"',
            "captured",
        ),
        (
            "snapshot_sha256: 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
            "snapshot_sha256: ABCD",
            "does not match",
        ),
    ],
)
def test_ingest_rejects_invalid_primary_source_anchor(
    tmp_path: Path,
    old: str,
    new: str,
    expected: str,
) -> None:
    configure_ingest_report_repo(tmp_path)
    content = code_grounded_ingest(include_heading=True).replace(old, new)
    ingest = write(tmp_path / "kb" / "sources" / "paper.ingest.md", content)

    results = validation.validate_note(ingest, repo_root=tmp_path)

    assert any(expected in item for item in results.fails), results.fails


@pytest.mark.parametrize(
    ("description_line", "expected"),
    [
        ("", "'description' is a required property"),
        ("description:", "frontmatter.description: None is not of type 'string'"),
        ('description: ""', "frontmatter.description: '' should be non-empty"),
        ("description: '   '", "frontmatter.description: '   ' does not match"),
        (
            "description: [not, a, string]",
            "frontmatter.description: ['not', 'a', 'string'] is not of type 'string'",
        ),
    ],
)
def test_note_description_must_be_present_non_empty_text(
    tmp_path: Path, description_line: str, expected: str
) -> None:
    configure_temp_repo(tmp_path)
    frontmatter_lines = [
        line for line in [description_line, "type: kb/types/note.md"] if line
    ]
    note = write(
        tmp_path / "broken.md",
        "---\n"
        + "\n".join(frontmatter_lines)
        + """\n---

# Broken note
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.note_type == "note"
    assert any(expected in failure for failure in results.fails)


@pytest.mark.parametrize(
    ("description", "expected"),
    [
        ("Short but non-empty", "description should be at least 50 characters"),
        (
            "Long description "
            + "with enough repeated words to exceed the upper bound " * 5,
            "description should be at most 250 characters",
        ),
    ],
)
def test_note_description_length_outside_style_band_warns(
    tmp_path: Path, description: str, expected: str
) -> None:
    configure_temp_repo(tmp_path)
    note = write(
        tmp_path / "description-length.md",
        f"""---
description: {description}
type: kb/types/note.md
---

# Description length
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.note_type == "note"
    assert results.fails == []
    assert any(f"frontmatter.description: {expected}" in item for item in results.warns)


def test_note_description_between_old_and_new_upper_bound_does_not_warn(
    tmp_path: Path,
) -> None:
    configure_temp_repo(tmp_path)
    description = "x" * 225
    note = write(
        tmp_path / "description-inside-style-band.md",
        f"""---
description: {description}
type: kb/types/note.md
---

# Description inside style band
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.fails == []
    assert not any("frontmatter.description" in item for item in results.warns)


def test_link_validation_skips_code_and_external_urls(tmp_path: Path) -> None:
    configure_temp_repo(tmp_path)
    target = write(tmp_path / "target.md", "# Target\n")
    note = write(
        tmp_path / "note.md",
        f"""---
description: A note with one real missing link and links that should be ignored by deterministic validation
type: kb/types/note.md
traits: []
---

# Link validation note

Real link: [target](./{target.name})
Missing link: [missing](./missing.md)
External link: [site](https://example.com/foo.md)

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
    assert any(
        "link health: missing target ./missing.md" in item for item in results.warns
    )
    assert all("ignored.md" not in item for item in results.warns)
    assert all("example.com" not in item for item in results.warns)


def test_link_validation_checks_all_relative_targets(tmp_path: Path) -> None:
    configure_temp_repo(tmp_path)
    write(tmp_path / "target.txt", "Target\n")
    (tmp_path / "existing-dir").mkdir()
    note = write(
        tmp_path / "note.md",
        """---
description: A note with local links to files and directories so link health checks all relative targets
type: kb/types/note.md
traits: []
---

# Link validation note

Existing file: [target](./target.txt)
Existing file with fragment and query: [target details](./target.txt?mode=brief#details)
Existing directory: [directory](./existing-dir/)
Missing directory: [missing directory](./missing-dir/)
Missing non-md file: [missing text](./missing.txt)
Anchor-only link: [heading](#heading)
External scheme: [mail](mailto:person@example.com)
Protocol-relative URL: [cdn](//example.com/file.txt)
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert all(
        "link health: all local relative links resolve" not in item
        for item in results.passes
    )
    assert any(
        "link health: missing target ./missing-dir/" in item for item in results.warns
    )
    assert any(
        "link health: missing target ./missing.txt" in item for item in results.warns
    )
    assert all("target.txt" not in item for item in results.warns)
    assert all("existing-dir" not in item for item in results.warns)
    assert all("#heading" not in item for item in results.warns)
    assert all("person@example.com" not in item for item in results.warns)
    assert all("example.com" not in item for item in results.warns)


def test_link_health_and_inbound_detection_share_url_resolution(tmp_path: Path) -> None:
    notes = configure_temp_repo(tmp_path)
    source = write(
        notes / "source.md",
        """---
description: Source note exercising normalized local and external Markdown link targets
type: kb/types/note.md
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
type: kb/types/note.md
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


def test_library_artifact_cannot_link_to_archived_proposal(tmp_path: Path) -> None:
    notes = configure_temp_repo(tmp_path)
    archived = write(
        tmp_path / "kb/reference/proposals/archive/retired.md",
        "# Retired proposal\n",
    )
    note = write(
        notes / "source.md",
        f"""---
description: Library note linking to a retired proposal that must stay outside the live knowledge graph
type: kb/types/note.md
traits: []
---

# Source

[Retired proposal]({os.path.relpath(archived, notes)})
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert any(
        "proposal archive boundary: library artifact links to archived proposal"
        in item
        for item in results.fails
    )


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
type: kb/types/note.md
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


def test_bare_library_text_cannot_link_to_archived_proposal(tmp_path: Path) -> None:
    notes = configure_temp_repo(tmp_path)
    archived = write(
        tmp_path / "kb/reference/proposals/archive/retired.md",
        "# Retired proposal\n",
    )
    readme = write(
        notes / "README.md",
        f"# Notes\n\n[Retired proposal]({os.path.relpath(archived, notes)})\n",
    )

    results = validation.validate_note(readme, repo_root=tmp_path)

    assert results.note_type == "text"
    assert any("proposal archive boundary" in item for item in results.fails)


def test_structured_claim_requires_evidence_and_reasoning(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
    note = write(
        notes_root / "claim.md",
        """---
description: Structured claim missing one required section so the validator should fail deterministically
type: kb/notes/types/structured-claim.md
traits: []
---

# Claims need support

## Evidence

Some evidence.
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    # Schema violations fail by default unless the constraint opts down to warn.
    assert any("missing '## Reasoning'" in item for item in results.fails)


def test_non_path_frontmatter_type_fails_validation(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
    note = write(
        notes_root / "invalid-type.md",
        """---
description: Non-path frontmatter type should be rejected by the current path-valued contract
type: spec
---

# Invalid type value
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.note_type == "unknown"
    assert any(
        "frontmatter.type: must start with kb/ or be file-relative (./ or ../): spec"
        in item
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
type: kb/reference/types/adr.md
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
        "kb/notes/types/local.md: schema file is missing" in failure
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


def configure_agent_memory_review_type(tmp_path: Path) -> Path:
    configure_temp_repo(tmp_path)
    reviews_root = tmp_path / "kb" / "agent-memory-systems"
    write(reviews_root / "COLLECTION.md", "# Agent memory systems\n")
    write(
        tmp_path
        / "kb"
        / "agent-memory-systems"
        / "types"
        / "agent-memory-system-review.schema.yaml",
        (
            Path.cwd()
            / "kb"
            / "agent-memory-systems"
            / "types"
            / "agent-memory-system-review.schema.yaml"
        ).read_text(encoding="utf-8"),
    )
    write_type_spec(
        tmp_path,
        "kb/agent-memory-systems/types/agent-memory-system-review.md",
        name="agent-memory-system-review",
        schema="kb/agent-memory-systems/types/agent-memory-system-review.schema.yaml",
    )
    return reviews_root


def test_agent_memory_review_fails_when_last_checked_missing(tmp_path: Path) -> None:
    reviews_root = configure_agent_memory_review_type(tmp_path)
    note = write(
        reviews_root / "system.md",
        """---
description: Related system note missing the review freshness field so the structural validator should flag it
type: kb/agent-memory-systems/types/agent-memory-system-review.md
---

# System

## Core Ideas

Idea.

## Comparison with Our System

Comparison.

## Borrowable Ideas

Borrow.

## Curiosity Pass

Curiosity.

## What to Watch

Watch.
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert any(
        "frontmatter: 'last-checked' is a required property" in item
        for item in results.fails
    )


def test_agent_memory_review_accepts_stable_review_without_transfer_sections(
    tmp_path: Path,
) -> None:
    reviews_root = configure_agent_memory_review_type(tmp_path)
    note = write(
        reviews_root / "system.md",
        """---
description: "Ontology-normalized external memory system with explicit write and read-back mechanisms"
type: kb/agent-memory-systems/types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-08-30"
---

# System

## Core Ideas

The system frontloads a bounded project map before each run.

## Artifact analysis

**Storage substrate:** `files` — retained Markdown files.

**Representational form:** `natural-language` — prose consumed as context.

**Lineage:** `authored` — a maintainer writes the files.

**Behavioral authority:** `knowledge` — the agent receives advisory context.

## Write side

**Write agency:** `manual` — maintainers edit the files.

## Read-back

**Read-back:** `pull` — the agent requests a relevant file.

## Curiosity Pass

The frontloading mapping applies only to the generated project map.
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.fails == []


def test_agent_memory_review_trace_learning_tag_requires_subsection(
    tmp_path: Path,
) -> None:
    reviews_root = configure_agent_memory_review_type(tmp_path)
    note = write(
        reviews_root / "system.md",
        """---
description: "Trace-learning review whose missing evidence subsection must fail the structural contract"
type: kb/agent-memory-systems/types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-08-30"
---

# System

## Core Ideas

The system learns from tool traces.

## Artifact analysis

**Storage substrate:** `files` — retained files.

**Representational form:** `natural-language` — prose lessons.

**Lineage:** `trace-extracted` — lessons come from tool traces.

**Behavioral authority:** `knowledge` — lessons return as advice.

## Write side

**Write agency:** `automatic` — a scheduled job writes lessons.

**Curation operations:** `none` — it only acquires new lessons.

## Read-back

**Read-back:** `pull` — the agent requests lessons.

## Curiosity Pass

The source does not establish behavioral activation.
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert any("### Trace-learning" in item for item in results.fails)


def test_agent_memory_review_trace_learning_subsection_requires_tag(
    tmp_path: Path,
) -> None:
    reviews_root = configure_agent_memory_review_type(tmp_path)
    note = write(
        reviews_root / "system.md",
        """---
description: "Trace-learning review whose missing classification tag must fail the structural contract"
type: kb/agent-memory-systems/types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-08-30"
---

# System

## Core Ideas

The system learns from tool traces.

## Artifact analysis

**Storage substrate:** `files` — retained files.
**Representational form:** `natural-language` — lessons are text.
**Lineage:** `trace-extracted` — lessons come from tool traces.
**Behavioral authority:** `knowledge` — later agents read the lessons.

## Write side

**Write agency:** `automatic` — the learner writes lessons.

### Trace-learning

**Trace source:** `tool-traces` — completed tool calls.
**Learning scope:** `per-project` — lessons stay in one project.
**Learning timing:** `offline` — learning runs after the session.
**Distilled form:** `natural-language` — lessons are text.

## Read-back

**Read-back:** `pull` — the agent requests lessons.

## Curiosity Pass

The source does not establish behavioral activation.
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert any("frontmatter: 'tags' is a required property" in item for item in results.fails)


def test_quote_citation_shape_passes_when_well_formed() -> None:
    results = validation.CheckResults(note_type="agent-memory-system-review")
    content = (
        "Retrieval latency dominates at scale.\n\n"
        "> p95 retrieval latency was 340ms, 6x the generation step\n"
        "> --- `src/memory/store.py` @ `abc123`\n"
    )

    validation.validate_quote_citations(results, content)

    assert any(
        "quote-anchored citations: 1 well-formed" in item for item in results.passes
    )
    assert results.warns == []


def test_quote_citation_shape_accepts_commit_pinned_blob_url() -> None:
    results = validation.CheckResults(note_type="agent-memory-system-review")
    content = (
        "> p95 retrieval latency was 340ms\n"
        "> --- [src/memory/store.py](https://github.com/org/repo/blob/abc123/src/memory/store.py)\n"
    )

    validation.validate_quote_citations(results, content)

    assert any("1 well-formed" in item for item in results.passes)
    assert results.warns == []


def test_quote_citation_shape_warns_when_attribution_names_no_source() -> None:
    results = validation.CheckResults(note_type="agent-memory-system-review")
    content = "> p95 retrieval latency was 340ms\n> --- the documentation\n"

    validation.validate_quote_citations(results, content)

    assert any("names no source" in item for item in results.warns)


def test_quote_citation_shape_warns_when_no_quote_above_attribution() -> None:
    results = validation.CheckResults(note_type="agent-memory-system-review")
    content = "Some prose.\n\n> --- `src/memory/store.py`\n"

    validation.validate_quote_citations(results, content)

    assert any("no quoted text above" in item for item in results.warns)


@pytest.mark.parametrize(
    ("extra_frontmatter", "should_pass"),
    [
        ("", True),
        ("user-verified: true\n", True),
        ("user-verified: false\n", False),
        ("status: current\n", False),
    ],
)
def test_note_user_verification_schema_boundary(
    tmp_path: Path, extra_frontmatter: str, should_pass: bool
) -> None:
    notes_root = configure_temp_repo(tmp_path)
    note = write(
        notes_root / "verification.md",
        f"""---
description: Note exercising the committed user verification schema boundary
type: kb/types/note.md
{extra_frontmatter}---

# Verification boundary
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert (results.fails == []) is should_pass


def test_tag_readme_rejects_global_status(tmp_path: Path) -> None:
    notes_root = configure_tag_readme_repo(tmp_path)
    readme = write(
        notes_root / "topic-README.md",
        """---
description: Curated head exercising the direct note-base descendant boundary
type: kb/types/tag-readme.md
index_source: tag
index_key: topic
status: current
---

# Topic
""",
    )

    results = validation.validate_note(readme, repo_root=tmp_path)

    assert any(
        "False schema does not allow 'current'" in failure for failure in results.fails
    )


def test_adr_status_uses_type_specific_enum_from_note_base(tmp_path: Path) -> None:
    notes_root = tmp_path / "kb" / "notes"
    install_schema_tree(tmp_path, "adr")
    write_type_spec(
        tmp_path,
        "kb/notes/types/adr.md",
        name="adr",
        schema="kb/notes/types/adr.schema.yaml",
    )
    note = write(
        notes_root / "decision.md",
        """---
description: ADR with custom lifecycle status values that should validate independently of note status
type: kb/notes/types/adr.md
status: accepted
---

# Decision

## Context

Context.

## Decision

Decision.

## Consequences

Consequences.
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.fails == []
    assert all("status" not in warning for warning in results.warns)


def test_instruction_type_accepts_review_gate_metadata(tmp_path: Path) -> None:
    install_schema_tree(tmp_path, "instruction")
    write_type_spec(
        tmp_path,
        "kb/types/instruction.md",
        name="instruction",
        schema="kb/types/instruction.schema.yaml",
    )
    gate = write(
        tmp_path / "kb" / "instructions" / "review-gates" / "prose" / "sample.md",
        """---
gate_id: prose/sample
name: Sample
description: Sample review gate for validating instruction metadata
type: kb/types/instruction.md
lens: prose
watches: [body]
staleness: changed
---

# Sample

## Failure mode

The prose fails in a sample way.

## Test

Check the sample condition.
""",
    )

    results = validation.validate_note(gate, repo_root=tmp_path)

    assert results.fails == []
    assert results.warns == []
    assert any(
        "type schema: instruction requirements satisfied" in item
        for item in results.passes
    )


def test_title_length_over_limit_fails_validation(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
    title = "A" * 101
    note = write(
        notes_root / "short-slug.md",
        f"""---
description: Note with an overly long title so the validator should fail deterministically on title length
type: kb/types/note.md
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
type: kb/types/note.md
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
type: kb/types/note.md
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
    write_type_spec(
        tmp_path,
        "kb/reports/types/connect-report.md",
        name="connect-report",
        schema="kb/types/note.schema.yaml",
    )
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
type: kb/reports/types/connect-report.md
---

# Connection report
""",
    )

    results = validation.validate_note(report, repo_root=tmp_path)

    derived_slug_length = MAX_NOTE_SLUG_LENGTH + len(".connect")
    assert results.fails == []
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
type: kb/types/note.md
traits: []
---

# Today note
""",
    )
    old_note = write(
        notes_root / "old.md",
        """---
description: Older note that should not be picked up by recent target resolution in deterministic validation
type: kb/types/note.md
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
type: kb/types/note.md
traits: []
---

# Note
""",
    )
    report = write(
        tmp_path / "kb" / "reports" / "retained" / "report.md",
        """---
description: Report outside the notes collection
type: kb/types/note.md
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
type: kb/types/note.md
tags: [kb-design, unmarked]
---

# Tagged note
""",
    )
    write(
        notes / "kb-design-README.md",
        """---
description: "Complete curated head for the kb-design tag"
type: kb/types/tag-readme.md
index_source: tag
index_key: kb-design
complete: true
---

# kb-design

Orientation paragraph.
""",
    )
    write(
        notes / "unmarked-README.md",
        """---
description: "Selective curated head for the unmarked tag"
type: kb/types/tag-readme.md
index_source: tag
index_key: unmarked
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
type: kb/types/note.md
traits: []
---

# Agent Memory Systems
""",
    )
    review_note = write(
        tmp_path / "kb" / "agent-memory-systems" / "reviews" / "agent-r.md",
        """---
description: Agent R review note
type: kb/types/note.md
traits: []
---

# Agent R
""",
    )
    template = write(
        tmp_path / "kb" / "agent-memory-systems" / "types" / "review.template.md",
        """---
description: Template that should not be validated as collection content
type: kb/types/note.md
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
type: kb/types/note.md
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
type: kb/types/note.md
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
    from commonplace.lib.snapshot import snapshot_sha256

    sources = tmp_path / "kb" / "sources"
    write(sources / "COLLECTION.md", "# Sources\n")
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
    sources = tmp_path / "kb" / "sources"
    write(sources / "COLLECTION.md", "# Sources\n")
    write(sources / "scratch.md", "Visible source work.\n")
    write(sources / ".snapshots" / "orphan.md", "uncatalogued bytes\n")
    monkeypatch.chdir(tmp_path)

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
    sources = tmp_path / "kb" / "sources"
    write(sources / "COLLECTION.md", "# Sources\n")
    write(sources / "scratch.md", "Visible source work.\n")
    write(sources / ".snapshots" / "orphan.md", "uncatalogued bytes\n")
    monkeypatch.chdir(tmp_path)

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
    assert payload["details_command"] == "commonplace-validate --full sources"


def test_source_snapshot_cache_reports_same_url_as_related_observation(
    tmp_path: Path,
) -> None:
    sources = tmp_path / "kb" / "sources"
    write(sources / "COLLECTION.md", "# Sources\n")
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


def test_source_snapshot_cache_recognizes_checksumless_legacy_ingest_by_url(
    tmp_path: Path,
) -> None:
    sources = tmp_path / "kb" / "sources"
    write(sources / "COLLECTION.md", "# Sources\n")
    related = write(
        sources / ".snapshots" / "capture-name.md",
        "---\nsource: https://example.com/legacy\n---\n\nLegacy bytes.\n",
    )
    write(
        sources / "legacy.ingest.md",
        "---\nsource: https://example.com/legacy\n---\n",
    )

    warnings = validation.validate_source_snapshot_cache(
        sources, repo_root=tmp_path
    )

    assert warnings == [
        (
            related,
            (
                "unpaired local snapshot: no same-stem ingest; its source URL "
                "matches legacy ingest kb/sources/legacy.ingest.md, which records "
                "no snapshot_sha256"
            ),
        )
    ]


def test_source_snapshot_cache_recognizes_derived_original_by_checksum(
    tmp_path: Path,
) -> None:
    from commonplace.lib.snapshot import snapshot_sha256

    sources = tmp_path / "kb" / "sources"
    write(sources / "COLLECTION.md", "# Sources\n")
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

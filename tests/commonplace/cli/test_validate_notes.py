from __future__ import annotations

import os
import shutil
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path


SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import pytest  # noqa: E402

from jsonschema.exceptions import ValidationError  # noqa: E402

from commonplace.cli import validate_notes  # noqa: E402
from commonplace.lib import project_paths, validation  # noqa: E402
from commonplace.lib.naming import MAX_NOTE_SLUG_LENGTH  # noqa: E402


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
captured: 2026-04-19
capture: web-fetch
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


def test_source_snapshot_requires_genre(tmp_path: Path) -> None:
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
captured: 2026-04-19
capture: web-fetch
type: kb/sources/types/snapshot.md
---

# Sample

Captured text.
""",
    )

    results = validation.validate_note(snapshot, repo_root=tmp_path)

    assert results.note_type == "snapshot"
    assert any("'genre' is a required property" in item for item in results.fails)


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
captured: 2026-04-19
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
            + "with enough repeated words to exceed the upper bound " * 4,
            "description should be at most 200 characters",
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


def test_bare_enum_frontmatter_type_fails_validation(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
    note = write(
        notes_root / "legacy.md",
        """---
description: Legacy enum-typed note should be rejected after path-valued type migration
type: spec
---

# Legacy note
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.note_type == "unknown"
    assert any(
        "frontmatter.type: must start with kb/ or be file-relative (./ or ../): spec"
        in item
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


def test_agent_memory_review_fails_when_last_checked_missing(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
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
    note = write(
        notes_root / "system.md",
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


def test_schema_violation_fails_by_default() -> None:
    # No severity on the failing subschema → the default applies: a broken
    # constraint blocks (the schema is the contract).
    error = ValidationError(
        "'x' is a required property",
        validator="required",
        schema={"required": ["x"]},
        path=["frontmatter"],
    )

    severity, _ = validation._schema_error_message(error)

    assert severity == "fail"


def test_schema_constraint_can_opt_down_to_warn() -> None:
    # `severity: warn` on the failing subschema downgrades just that constraint,
    # keyed by its stable ruleId.
    error = ValidationError(
        "[] is too short",
        validator="minItems",
        schema={
            "type": "array",
            "minItems": 3,
            "ruleId": "min-items-example",
            "severity": "warn",
        },
        path=["links"],
    )

    severity, _ = validation._schema_error_message(error)

    assert severity == "warn"


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


def test_connect_report_derived_slug_is_exempt_from_note_limit(tmp_path: Path) -> None:
    configure_temp_repo(tmp_path)
    write_type_spec(
        tmp_path,
        "kb/reports/types/connect-report.md",
        name="connect-report",
        schema="kb/types/note.schema.yaml",
    )
    source_slug = "a" * MAX_NOTE_SLUG_LENGTH
    report = write(
        tmp_path / "kb" / "reports" / "connect" / "notes" / f"{source_slug}.connect.md",
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


def test_list_kb_note_paths_skips_nested_git_repos(tmp_path: Path) -> None:
    notes_root = tmp_path / "kb" / "notes"
    write(notes_root / "COLLECTION.md", "# Notes collection\n")
    write(
        notes_root / "kept.md",
        """---
description: Kept note with enough description text to satisfy structural validation
type: kb/types/note.md
traits: []
---

# Kept note
""",
    )
    nested_repo = notes_root / "related-systems" / "napkin"
    nested_repo.mkdir(parents=True, exist_ok=True)
    (nested_repo / ".git").mkdir()
    write(
        nested_repo / "ignored.md",
        """---
description: This note lives under a cloned repo and should be skipped by batch validation path discovery
type: kb/types/note.md
traits: []
---

# Ignored note
""",
    )

    discovered = project_paths.list_kb_note_paths(tmp_path)

    assert notes_root / "kept.md" in discovered
    assert nested_repo / "ignored.md" not in discovered


def test_list_kb_note_paths_includes_visible_type_directory_markdown(
    tmp_path: Path,
) -> None:
    notes_root = tmp_path / "kb" / "notes"
    write(notes_root / "COLLECTION.md", "# Notes collection\n")
    write(
        notes_root / "real.md",
        """---
description: Real note that should be picked up by batch validation
type: kb/types/note.md
traits: []
---

# Real note
""",
    )
    write(
        notes_root / "types" / "adr.template.md",
        """---
description: Template skeleton for authoring ADRs, not a knowledge artifact
type: kb/notes/types/adr.md
---

# {NNN}-{decision-title}
""",
    )
    write(
        notes_root / "types" / "adr.instructions.md",
        "# ADR Instructions\n\nUse an ADR for a concrete architectural decision.\n",
    )
    write(
        notes_root / "collection" / "types" / "nested.template.md",
        """---
description: Template nested deeper in the tree under a collection-local types directory
type: collection-item
---

# Template
""",
    )

    discovered = project_paths.list_kb_note_paths(tmp_path)

    assert notes_root / "real.md" in discovered
    assert notes_root / "types" / "adr.template.md" in discovered
    assert notes_root / "types" / "adr.instructions.md" in discovered
    assert notes_root / "collection" / "types" / "nested.template.md" in discovered


def test_list_kb_note_paths_skips_replaced_archives(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "agent-memory-systems" / "COLLECTION.md",
        "# Agent memory systems\n",
    )
    reviews_root = tmp_path / "kb" / "agent-memory-systems" / "reviews"
    current = write(
        reviews_root / "napkin.md",
        """---
description: Current review of napkin as an agent-memory-system
type: kb/agent-memory-systems/types/agent-memory-system-review.md
last-checked: "2026-04-20"
---

# Napkin
""",
    )
    archive = write(
        reviews_root / "napkin.replaced.2026-04-12.md",
        """---
description: Archived review of napkin superseded on 2026-04-12
type: kb/agent-memory-systems/types/agent-memory-system-review.md
last-checked: "2026-04-12"
---

# Napkin (replaced)
""",
    )

    discovered = project_paths.list_kb_note_paths(tmp_path)

    assert current in discovered
    assert archive not in discovered


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
    old_ts = datetime(2020, 1, 1).timestamp()
    old_note.touch()
    today_note.touch()
    os.utime(old_note, (old_ts, old_ts))

    recent = validate_notes.resolve_validation_target("recent", repo_root=tmp_path)

    assert today_note.resolve() in recent.paths
    assert old_note.resolve() not in recent.paths
    assert recent.collection is None


def test_notes_target_scans_only_notes_collection(tmp_path: Path) -> None:
    write(tmp_path / "kb" / "notes" / "COLLECTION.md", "# Notes collection\n")
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
        tmp_path / "kb" / "reports" / "report.md",
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
    legacy_template = write(
        tmp_path / "kb" / "notes" / "types" / "legacy.template.md",
        "# Template\n",
    )

    target = validate_notes.resolve_validation_target("types", repo_root=tmp_path)

    assert target.paths == (
        legacy_template,
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

    exit_code = validate_notes.main(["kb/notes/tagged-note.md"])
    output = capsys.readouterr().out

    assert exit_code == 1
    assert "=== VALIDATION: tagged-note.md ===" in output
    assert "=== VALIDATION: kb-design-README.md ===" in output
    assert "=== VALIDATION: unmarked-README.md ===" not in output
    assert "complete mark: missing entry for kb/notes/tagged-note.md" in output
    assert "=== BATCH INFO ===" not in output


def test_validation_run_parses_collection_artifacts_once_and_reuses_indexes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    notes = configure_tag_readme_repo(tmp_path)

    def tagged(name: str, tags: str) -> Path:
        return write(
            notes / f"{name}.md",
            f"""---
description: {name.title()} note in the validation-run cache fixture
type: kb/types/note.md
tags: [{tags}]
---

# {name.title()}
""",
        )

    def complete_head(tag: str, members: tuple[str, ...]) -> Path:
        links = "\n".join(
            f"- [{member.title()}](./{member}.md) — member" for member in members
        )
        return write(
            notes / f"{tag}-README.md",
            f"""---
description: Complete curated head for {tag}
type: kb/types/tag-readme.md
index_source: tag
index_key: {tag}
complete: true
---

# {tag.title()}

{links}
""",
        )

    first = tagged("first", "alpha, beta")
    second = tagged("second", "alpha")
    alpha = complete_head("alpha", ("first", "second"))
    beta = complete_head("beta", ("first",))
    paths = tuple(project_paths.list_collection_note_paths(notes))
    selected = {path.resolve() for path in paths}
    reads: Counter[Path] = Counter()
    original_read_text = Path.read_text

    def counting_read_text(path: Path, *args: object, **kwargs: object) -> str:
        resolved = path.resolve()
        if resolved in selected:
            reads[resolved] += 1
        return original_read_text(path, *args, **kwargs)

    monkeypatch.setattr(Path, "read_text", counting_read_text)

    run = validation.ValidationRun(
        repo_root=tmp_path,
        paths=paths,
        collection=notes,
    )
    outcome = run.evaluate()

    assert outcome.paths == paths
    assert set(outcome.results) == selected
    assert {first, second, alpha, beta} <= set(outcome.results)
    assert all(reads[path.resolve()] == 1 for path in paths)
    collection_index = run.collection_index(notes)
    assert collection_index is run.collection_index(notes)
    assert {path for path, _title, _description in collection_index.tag_index_entries} == {
        alpha,
        beta,
    }
    assert not outcome.collection_structure


def test_bulk_scopes_are_rejected(tmp_path: Path) -> None:
    (tmp_path / "kb").mkdir()
    (tmp_path / "kb" / "notes").mkdir()

    for target in ("all", "kb", "kb/"):
        with pytest.raises(ValueError):
            validate_notes.resolve_validation_target(target, repo_root=tmp_path)


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
        tmp_path / "kb" / "reports" / "report.md",
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
        tmp_path / "kb" / "reports" / "report.md",
        """---
description: Report in a support directory without collection conventions
type: kb/types/note.md
traits: []
---

# Report
""",
    )

    with pytest.raises(ValueError, match="not a KB collection"):
        validate_notes.resolve_validation_target("kb/reports", repo_root=tmp_path)


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

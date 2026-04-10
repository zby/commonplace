from __future__ import annotations

import os
import sys
from datetime import datetime
from pathlib import Path


SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.cli import validate_notes
from commonplace.lib import validation


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def configure_temp_repo(tmp_path: Path) -> Path:
    notes_root = tmp_path / "kb" / "notes"
    write(
        tmp_path / "kb" / "types" / "note.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
required:
  - frontmatter
  - body
  - headings
  - links
  - body_dates
properties:
  frontmatter:
    type: object
    required:
      - description
      - type
    properties:
      description:
        type: string
        minLength: 1
      type:
        type: string
      status:
        enum:
          - seedling
          - current
          - speculative
          - outdated
      traits:
        type: array
        items:
          type: string
    additionalProperties: true
  body:
    type: string
  headings:
    type: array
    items:
      type: string
  links:
    type: array
    items:
      type: string
  body_dates:
    type: array
    items:
      type: string
      format: date
""",
    )
    write(
        tmp_path / "kb" / "notes" / "types" / "structured-claim.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
allOf:
  - $ref: "../../types/note.schema.yaml"
  - type: object
    properties:
      frontmatter:
        type: object
        required:
          - description
          - type
        properties:
          type:
            const: structured-claim
        additionalProperties: true
      headings:
        type: array
        allOf:
          - contains:
              const: "## Evidence"
          - contains:
              const: "## Reasoning"
""",
    )
    write(
        tmp_path / "kb" / "notes" / "types" / "spec.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
allOf:
  - $ref: "../../types/note.schema.yaml"
  - type: object
    properties:
      frontmatter:
        type: object
        required:
          - description
          - type
        properties:
          type:
            const: spec
        additionalProperties: true
      headings:
        type: array
        anyOf:
          - contains:
              const: "## Design"
          - contains:
              const: "## Implementation"
""",
    )
    write(
        tmp_path / "kb" / "notes" / "types" / "related-system.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
allOf:
  - $ref: "../../types/note.schema.yaml"
  - type: object
    properties:
      frontmatter:
        type: object
        required:
          - description
          - type
          - last-checked
        properties:
          type:
            const: related-system
          last-checked:
            type: string
            format: date
        additionalProperties: true
      headings:
        type: array
        allOf:
          - contains:
              const: "## Core Ideas"
          - contains:
              const: "## Comparison with Our System"
          - contains:
              const: "## Borrowable Ideas"
          - contains:
              const: "## Curiosity Pass"
          - contains:
              const: "## What to Watch"
""",
    )
    return notes_root


def test_text_file_has_no_structural_requirements(tmp_path: Path) -> None:
    note = write(tmp_path / "raw-capture.md", "# Raw capture\n\nJust text.\n")

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.note_type == "text"
    assert results.fails == []
    assert any("no frontmatter" in item for item in results.passes)


def test_duplicate_frontmatter_keys_follow_yaml_last_value_wins(tmp_path: Path) -> None:
    configure_temp_repo(tmp_path)
    note = write(
        tmp_path / "broken.md",
        """---
description: first
description: second
type: note
---

# Broken note
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert results.note_type == "note"
    assert results.fails == []
    assert all("description" not in warning for warning in results.warns)


def test_link_validation_skips_code_and_external_urls(tmp_path: Path) -> None:
    configure_temp_repo(tmp_path)
    target = write(tmp_path / "target.md", "# Target\n")
    note = write(
        tmp_path / "note.md",
        f"""---
description: A note with one real missing link and links that should be ignored by deterministic validation
type: note
traits: []
status: current
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

    assert "link health: all relative markdown links resolve" not in results.passes
    assert "link health: missing target ./missing.md" in results.warns
    assert all("ignored.md" not in item for item in results.warns)
    assert all("example.com" not in item for item in results.warns)


def test_structured_claim_requires_evidence_and_reasoning(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
    note = write(
        notes_root / "claim.md",
        """---
description: Structured claim missing one required section so the validator should warn deterministically
type: structured-claim
traits: []
status: current
---

# Claims need support

## Evidence

Some evidence.
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert any("missing '## Reasoning'" in item for item in results.warns)


def test_spec_accepts_design_or_implementation_heading(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
    note = write(
        notes_root / "spec.md",
        """---
description: Spec note with one structural section so the resolver-backed validator should preserve legacy any-of behavior
type: spec
status: current
---

# Spec note

## Design

Design details.
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert all("Design" not in item and "Implementation" not in item for item in results.warns)
    assert all("headings" not in item for item in results.warns)


def test_related_system_warns_when_last_checked_missing(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
    note = write(
        notes_root / "system.md",
        """---
description: Related system note missing the review freshness field so the structural validator should flag it
type: related-system
status: current
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

    assert "frontmatter: 'last-checked' is a required property" in results.warns


def test_adr_status_uses_type_specific_enum_from_note_base(tmp_path: Path) -> None:
    notes_root = tmp_path / "kb" / "notes"
    write(
        tmp_path / "kb" / "types" / "note-base.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
required:
  - frontmatter
  - body
  - headings
  - links
  - body_dates
properties:
  frontmatter:
    type: object
    required:
      - description
      - type
    properties:
      description:
        type: string
        minLength: 1
      type:
        type: string
      status:
        type: string
    additionalProperties: true
  body:
    type: string
  headings:
    type: array
    items:
      type: string
  links:
    type: array
    items:
      type: string
  body_dates:
    type: array
    items:
      type: string
      format: date
""",
    )
    write(
        tmp_path / "kb" / "types" / "note.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
allOf:
  - $ref: "./note-base.schema.yaml"
  - type: object
    properties:
      frontmatter:
        type: object
        properties:
          status:
            enum:
              - seedling
              - current
              - speculative
              - outdated
        additionalProperties: true
""",
    )
    write(
        tmp_path / "kb" / "notes" / "types" / "adr.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
allOf:
  - $ref: "../../types/note-base.schema.yaml"
  - type: object
    properties:
      frontmatter:
        type: object
        required:
          - description
          - type
        properties:
          type:
            const: adr
          status:
            enum:
              - proposed
              - accepted
              - superseded
              - deprecated
        additionalProperties: true
      headings:
        type: array
        allOf:
          - contains:
              const: "## Context"
          - contains:
              const: "## Decision"
          - contains:
              const: "## Consequences"
""",
    )
    note = write(
        notes_root / "decision.md",
        """---
description: ADR with custom lifecycle status values that should validate independently of note status
type: adr
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


def test_title_length_over_limit_fails_validation(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
    title = "A" * 101
    note = write(
        notes_root / "short-slug.md",
        f"""---
description: Note with an overly long title so the validator should fail deterministically on title length
type: note
traits: []
status: current
---

# {title}
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert "title: 101 chars exceeds limit of 100" in results.fails


def test_filename_slug_length_over_limit_fails_validation(tmp_path: Path) -> None:
    notes_root = configure_temp_repo(tmp_path)
    overlong_slug = "a" * 101
    note = write(
        notes_root / f"{overlong_slug}.md",
        """---
description: Note with an overly long slug so the validator should fail deterministically on filename length
type: note
traits: []
status: current
---

# Short title
""",
    )

    results = validation.validate_note(note, repo_root=tmp_path)

    assert "filename slug: 101 chars exceeds limit of 100" in results.fails


def test_list_kb_note_paths_skips_nested_git_repos(tmp_path: Path) -> None:
    notes_root = tmp_path / "kb" / "notes"
    write(
        notes_root / "kept.md",
        """---
description: Kept note with enough description text to satisfy the deterministic validator heuristics well enough
type: note
traits: []
status: current
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
type: note
traits: []
status: current
---

# Ignored note
""",
    )

    discovered = validation.list_kb_note_paths(notes_root)

    assert notes_root / "kept.md" in discovered
    assert nested_repo / "ignored.md" not in discovered


def test_list_kb_note_paths_skips_type_definitions(tmp_path: Path) -> None:
    notes_root = tmp_path / "kb" / "notes"
    write(
        notes_root / "real.md",
        """---
description: Real note that should be picked up by batch validation
type: note
traits: []
status: current
---

# Real note
""",
    )
    write(
        notes_root / "types" / "adr.template.md",
        """---
description: Template skeleton for authoring ADRs, not a knowledge artifact
type: adr
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

    discovered = validation.list_kb_note_paths(notes_root)

    assert notes_root / "real.md" in discovered
    assert notes_root / "types" / "adr.template.md" not in discovered
    assert notes_root / "types" / "adr.instructions.md" not in discovered
    assert notes_root / "collection" / "types" / "nested.template.md" not in discovered


def test_recent_target_uses_mtime_and_target_lookup(tmp_path: Path) -> None:
    notes_root = tmp_path / "kb" / "notes"
    today_note = write(
        notes_root / "today.md",
        """---
description: Note modified today so recent target resolution should find it deterministically
type: note
traits: []
status: current
---

# Today note
""",
    )
    old_note = write(
        notes_root / "old.md",
        """---
description: Older note that should not be picked up by recent target resolution in deterministic validation
type: note
traits: []
status: current
---

# Old note
""",
    )
    old_ts = datetime(2020, 1, 1).timestamp()
    old_note.touch()
    today_note.touch()
    os.utime(old_note, (old_ts, old_ts))

    recent = validate_notes.resolve_targets("recent", repo_root=tmp_path, notes_root=notes_root)

    assert today_note.resolve() in recent
    assert old_note.resolve() not in recent

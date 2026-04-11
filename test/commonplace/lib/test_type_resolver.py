from __future__ import annotations

import sys
from pathlib import Path


SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.lib import type_resolver


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_root_note_profile_is_loaded_from_yaml(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "types" / "note.schema.yaml",
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
    additionalProperties: true
""",
    )
    note = write(
        tmp_path / "kb" / "notes" / "sample.md",
        """---
description: Sample
type: note
---

# Sample
""",
    )

    profile = type_resolver.resolve_type(note, {"description": "Sample", "type": "note"}, repo_root=tmp_path)

    assert profile.resolved_type == "note"
    assert profile.definition_path == tmp_path / "kb" / "types" / "note.schema.yaml"


def test_collection_definition_extends_note_profile(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "types" / "note.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
required:
  - frontmatter
  - headings
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
    additionalProperties: true
  headings:
    type: array
    items:
      type: string
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
    note = write(
        tmp_path / "kb" / "notes" / "claim.md",
        """---
description: Sample
type: structured-claim
---

# Claim
""",
    )

    profile = type_resolver.resolve_type(note, {"description": "Sample", "type": "structured-claim"}, repo_root=tmp_path)

    assert profile.resolved_type == "structured-claim"
    assert profile.definition_path == tmp_path / "kb" / "notes" / "types" / "structured-claim.schema.yaml"


def test_missing_type_definition_falls_back_to_note(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "types" / "note.schema.yaml",
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
    properties:
      description:
        type: string
        minLength: 1
      type:
        type: string
      status:
        enum:
          - seedling
    additionalProperties: true
""",
    )
    note = write(
        tmp_path / "kb" / "notes" / "sample.md",
        """---
description: Sample
type: unknown-type
---

# Sample
""",
    )

    profile = type_resolver.resolve_type(note, {"description": "Sample", "type": "unknown-type"}, repo_root=tmp_path)

    assert profile.resolved_type == "note"
    assert profile.definition_path == tmp_path / "kb" / "types" / "note.schema.yaml"


def test_workshop_scope_overrides_collection_and_root(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "types" / "note.schema.yaml",
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
    properties:
      description:
        type: string
        minLength: 1
      type:
        type: string
      status:
        enum:
          - current
    additionalProperties: true
""",
    )
    write(
        tmp_path / "kb" / "work" / "types" / "memo.schema.yaml",
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
          - collection-field
        properties:
          type:
            const: memo
        additionalProperties: true
""",
    )
    write(
        tmp_path / "kb" / "work" / "demo" / "types" / "memo.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
allOf:
  - $ref: "../../../types/note.schema.yaml"
  - type: object
    properties:
      frontmatter:
        type: object
        required:
          - description
          - type
          - workshop-field
        properties:
          type:
            const: memo
        additionalProperties: true
""",
    )
    note = write(
        tmp_path / "kb" / "work" / "demo" / "note.md",
        """---
description: Workshop note
type: memo
---

# Demo
""",
    )

    profile = type_resolver.resolve_type(note, {"description": "Workshop note", "type": "memo"}, repo_root=tmp_path)

    assert profile.resolved_type == "memo"
    assert profile.definition_path == tmp_path / "kb" / "work" / "demo" / "types" / "memo.schema.yaml"


def test_text_without_frontmatter_resolves_to_text_profile(tmp_path: Path) -> None:
    note = write(tmp_path / "kb" / "notes" / "raw.md", "# Raw\n")

    profile = type_resolver.resolve_type(note, None, repo_root=tmp_path)

    assert profile.resolved_type == "text"
    assert profile.definition_path is None


def test_reports_collection_type_definition_extends_note_profile(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "types" / "note.schema.yaml",
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
    properties:
      description:
        type: string
        minLength: 1
      type:
        type: string
    additionalProperties: true
""",
    )
    write(
        tmp_path / "kb" / "reports" / "types" / "connect-report.schema.yaml",
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
          - source
        properties:
          type:
            const: connect-report
        additionalProperties: true
""",
    )
    report = write(
        tmp_path / "kb" / "reports" / "connect" / "sample.connect.md",
        """---
description: Sample
type: connect-report
source: kb/notes/sample.md
---

# Sample
""",
    )

    profile = type_resolver.resolve_type(report, {"description": "Sample", "type": "connect-report"}, repo_root=tmp_path)

    assert profile.resolved_type == "connect-report"
    assert profile.definition_path == tmp_path / "kb" / "reports" / "types" / "connect-report.schema.yaml"


def test_type_specific_status_enum_overrides_note_status_via_base_schema(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "types" / "note-base.schema.yaml",
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
    properties:
      description:
        type: string
        minLength: 1
      type:
        type: string
      status:
        type: string
    additionalProperties: true
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
""",
    )
    note = write(
        tmp_path / "kb" / "notes" / "decision.md",
        """---
description: Decision
type: adr
status: accepted
---

# Decision
""",
    )

    profile = type_resolver.resolve_type(note, {"description": "Decision", "type": "adr"}, repo_root=tmp_path)

    assert profile.resolved_type == "adr"
    assert profile.definition_path == tmp_path / "kb" / "notes" / "types" / "adr.schema.yaml"

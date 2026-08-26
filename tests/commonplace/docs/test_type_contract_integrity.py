"""Keep authored type guidance aligned with executable schemas."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from commonplace.lib.naming import MAX_INGEST_SNAPSHOT_SLUG_LENGTH

REPO_ROOT = Path(__file__).resolve().parents[3]

TEXT_PROMOTION_GUIDANCE = (
    Path("README.md"),
    Path("kb/types/text.md"),
    Path("kb/reference/README.md"),
    Path("kb/notes/convert-still-requires-semantic-description.md"),
    Path("kb/notes/directory-scoped-types-are-cheaper-than-global-types.md"),
    Path("kb/notes/type-system-enforces-metadata-that-navigation-depends-on.md"),
    Path("kb/notes/why-notes-have-types.md"),
    Path("kb/notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md"),
)

RETIRED_TEXT_PROMOTION_WORDING = (
    "add frontmatter and it becomes a `note`",
    "at least a `description`",
    "becomes a `note` by adding frontmatter",
    "description as the only required field",
    "description is the only required field",
    "frontmatter without a description is structurally complete",
    "has frontmatter with description",
    "raw capture → add frontmatter (`note`)",
    "the file never moves or gets copied",
    "`type: note`",
)
RETIRED_BARE_NOTE_YAML = re.compile(r"(?m)^\s*type:\s*note\s*(?:#.*)?$")


def test_text_promotion_requires_complete_note_frontmatter() -> None:
    schema = yaml.safe_load(
        (REPO_ROOT / "kb/types/note-base.schema.yaml").read_text(encoding="utf-8")
    )
    required_fields = set(schema["properties"]["frontmatter"]["required"])
    expected_markers = {
        "description": "`description`",
        "type": "`type: kb/types/note.md`",
    }

    assert required_fields == set(expected_markers), (
        "note frontmatter requirements changed; update the text-promotion contract"
    )

    text_contract = (REPO_ROOT / "kb/types/text.md").read_text(encoding="utf-8")
    promotion = text_contract.split("## Promotion", maxsplit=1)[1]
    missing = [
        field for field, marker in expected_markers.items() if marker not in promotion
    ]
    assert missing == [], f"text promotion omits required note fields: {missing}"

    skill = (REPO_ROOT / "kb/instructions/cp-skill-convert/SKILL.md").read_text(
        encoding="utf-8"
    )
    template_block = (
        skill.split("#### Step 3: Generate frontmatter", maxsplit=1)[1]
        .split("```yaml", maxsplit=1)[1]
        .split("```", maxsplit=1)[0]
    )
    template = yaml.safe_load(
        "\n".join(line for line in template_block.splitlines() if line.strip() != "---")
    )
    assert required_fields <= set(template), (
        "convert template omits schema-required note frontmatter"
    )
    assert template["type"] == "kb/types/note.md"
    assert template["traits"] == []
    assert template["tags"] == []
    assert "user-verified" not in template


def test_current_text_promotion_guidance_avoids_retired_shortcuts() -> None:
    occurrences: list[str] = []
    for relative_path in TEXT_PROMOTION_GUIDANCE:
        content = (REPO_ROOT / relative_path).read_text(encoding="utf-8").casefold()
        occurrences.extend(
            f"{relative_path}: {wording}"
            for wording in RETIRED_TEXT_PROMOTION_WORDING
            if wording.casefold() in content
        )
        if RETIRED_BARE_NOTE_YAML.search(content):
            occurrences.append(f"{relative_path}: bare YAML type: note")

    assert occurrences == [], "retired text-promotion guidance remains:\n" + "\n".join(
        occurrences
    )


def test_snapshot_type_pointer_matches_schema() -> None:
    schema = yaml.safe_load(
        (REPO_ROOT / "kb/sources/types/snapshot.schema.yaml").read_text(
            encoding="utf-8"
        )
    )
    expected_pointer = schema["properties"]["frontmatter"]["properties"]["type"][
        "const"
    ]
    contract = (REPO_ROOT / "kb/sources/types/snapshot.md").read_text(
        encoding="utf-8"
    )
    metadata = contract.split("## Metadata", maxsplit=1)[1].split(
        "## Genre", maxsplit=1
    )[0]

    assert f"`type: {expected_pointer}`" in metadata
    assert "`type: snapshot`" not in metadata

    collection_contract = (REPO_ROOT / "kb/sources/COLLECTION.md").read_text(
        encoding="utf-8"
    )
    assert "## Type eligibility" in collection_contract
    assert f"| `snapshot` | `{expected_pointer}` |" not in collection_contract

    snapshot_skill = (
        REPO_ROOT / "kb/instructions/cp-skill-snapshot-web/SKILL.md"
    ).read_text(encoding="utf-8")
    assert f"supplies `{expected_pointer}` as the type" in snapshot_skill
    assert f"type: {expected_pointer}" in snapshot_skill
    assert "Types menu" not in snapshot_skill


def test_ingest_owns_durable_source_and_snapshot_anchor() -> None:
    ingest_schema = yaml.safe_load(
        (REPO_ROOT / "kb/sources/types/ingest-report.schema.yaml").read_text(
            encoding="utf-8"
        )
    )
    ingest_contract = (REPO_ROOT / "kb/sources/types/ingest-report.md").read_text(
        encoding="utf-8"
    )
    snapshot_schema = yaml.safe_load(
        (REPO_ROOT / "kb/sources/types/snapshot.schema.yaml").read_text(
            encoding="utf-8"
        )
    )

    ingest_fields = ingest_schema["allOf"][1]["properties"]["frontmatter"]
    required = set(ingest_fields["required"])
    assert {
        "source",
        "captured",
        "capture",
        "genre",
        "snapshot_sha256",
    } <= required
    assert ingest_fields["properties"]["source_snapshot"] is False
    assert ingest_fields["properties"]["code_revisions"] is False
    assert "secondary_sources" in ingest_fields["properties"]
    assert "`kb/sources/.snapshots/`" in ingest_contract

    snapshot_required = set(snapshot_schema["properties"]["frontmatter"]["required"])
    assert "genre" not in snapshot_required

    snapshot_frontmatter = snapshot_schema["properties"]["frontmatter"]
    snapshot_scopes = set(
        snapshot_frontmatter["properties"]["capture_scope"]["enum"]
    )
    ingest_scopes = set(ingest_fields["properties"]["capture_scope"]["enum"])
    assert snapshot_scopes == {
        "full-source",
        "partial-source",
        "abstract",
        "excerpt",
    }
    assert ingest_scopes == snapshot_scopes
    assert "capture_scope" not in snapshot_required
    assert "capture_scope" not in required
    assert "`capture_scope`" in ingest_contract


def test_snapshot_and_ingest_skills_budget_the_derived_filename() -> None:
    snapshot_skill = (
        REPO_ROOT / "kb/instructions/cp-skill-snapshot-web/SKILL.md"
    ).read_text(encoding="utf-8")
    ingest_skill = (
        REPO_ROOT / "kb/instructions/cp-skill-ingest/SKILL.md"
    ).read_text(encoding="utf-8")

    assert f"max {MAX_INGEST_SNAPSHOT_SLUG_LENGTH} chars" in snapshot_skill
    assert "Before connection discovery" in ingest_skill
    assert "stem (`<slug>.ingest`) to be at most 70 characters" in ingest_skill

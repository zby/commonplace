"""Keep authored type guidance aligned with executable schemas."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from commonplace.lib import frontmatter
from commonplace.lib.naming import MAX_INGEST_SNAPSHOT_SLUG_LENGTH
from commonplace.lib.type_resolver import validate_type_path

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

TYPE_EXAMPLE_GUIDANCE = (
    Path("kb/notes/agent-statelessness-means-the-context-engine-should-inject-context.md"),
    Path("kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured.md"),
    Path("kb/notes/document-types-should-be-verifiable.md"),
    Path("kb/notes/title-as-claim-enables-traversal-as-reasoning.md"),
    Path("kb/notes/why-directories-despite-their-costs.md"),
    Path("kb/reference/collections-and-types.md"),
    Path("kb/types/note.md"),
)

# This example is explicitly an ADR under kb/reference/adr/, so its
# file-relative pointer resolves from that illustrated artifact location.
TYPE_EXAMPLE_SOURCE_CONTEXTS = {
    (
        Path("kb/reference/collections-and-types.md"),
        "../types/adr.md",
    ): Path("kb/reference/adr/example.md"),
}

TYPE_LOCAL_STATUS_VALUES = {
    "kb/articles/types/article.md": {
        "draft",
        "working-paper",
        "published",
        "superseded",
        "withdrawn",
    },
    "kb/reference/types/adr.md": {"accepted", "superseded", "deprecated"},
}

FENCED_EXAMPLE = re.compile(
    r"(?ms)^```(?P<language>yaml|markdown)\s*\n(?P<body>.*?)^```\s*$"
)


def _active_kb_markdown_paths() -> tuple[Path, ...]:
    paths: list[Path] = []
    for path in (REPO_ROOT / "kb").rglob("*.md"):
        relative_path = path.relative_to(REPO_ROOT)
        # Workshops and generated reports retain experiments, captured prompts,
        # and immutable pre-migration copies. They are evidence, not current
        # artifact contracts or authoring guidance.
        if relative_path.is_relative_to(Path("kb/work")):
            continue
        if relative_path.is_relative_to(Path("kb/reports")):
            continue
        if ".snapshots" in relative_path.parts:
            continue
        paths.append(relative_path)
    return tuple(sorted(paths))


def _canonical_type_path(relative_path: Path, value: object) -> str:
    canonical, resolved = validate_type_path(
        value,
        repo_root=REPO_ROOT,
        source_file=REPO_ROOT / relative_path,
    )
    assert resolved.is_file(), f"{relative_path}: missing type spec {canonical}"
    return canonical


def _example_frontmatter(block: str, language: str) -> dict[str, object] | None:
    if block.startswith("---\n"):
        parsed = frontmatter.parse(block)
        assert parsed.ok, parsed.errors
        return parsed.data
    if language == "yaml":
        parsed = yaml.safe_load(block)
        return parsed if isinstance(parsed, dict) else None
    return None


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


def test_note_contract_matches_the_global_frontmatter_schema() -> None:
    base_schema = yaml.safe_load(
        (REPO_ROOT / "kb/types/note-base.schema.yaml").read_text(encoding="utf-8")
    )
    frontmatter_schema = base_schema["properties"]["frontmatter"]
    required_fields = set(frontmatter_schema["required"])
    shared_fields = set(frontmatter_schema["properties"])

    assert required_fields == {"description", "type"}
    assert shared_fields == {
        "description",
        "type",
        "traits",
        "tags",
        "user-verified",
    }
    assert "status" not in shared_fields

    note_schema = yaml.safe_load(
        (REPO_ROOT / "kb/types/note.schema.yaml").read_text(encoding="utf-8")
    )
    note_fields = note_schema["allOf"][1]["properties"]["frontmatter"][
        "properties"
    ]
    assert note_fields["status"] is False

    note_contract = (REPO_ROOT / "kb/types/note.md").read_text(encoding="utf-8")
    table = note_contract.split("## Frontmatter", maxsplit=1)[1].split(
        "## Description", maxsplit=1
    )[0]
    rows: dict[str, tuple[str, str]] = {}
    for line in table.splitlines():
        if not line.startswith("| `"):
            continue
        field, required, use = (cell.strip() for cell in line.strip("|").split("|"))
        rows[field.strip("`")] = (required, use)

    assert set(rows) == shared_fields
    assert {field for field, (required, _) in rows.items() if required == "Yes"} == (
        required_fields
    )
    assert rows["type"][1] == "`kb/types/note.md`"


def test_status_frontmatter_is_confined_to_specialized_type_contracts() -> None:
    observed_types: set[str] = set()
    violations: list[str] = []

    for relative_path in _active_kb_markdown_paths():
        content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
        parsed = frontmatter.parse(content)
        assert parsed.ok, f"{relative_path}: {parsed.errors}"
        if "status" not in parsed.data:
            continue

        type_path = _canonical_type_path(relative_path, parsed.data.get("type"))
        observed_types.add(type_path)
        allowed_values = TYPE_LOCAL_STATUS_VALUES.get(type_path)
        status = parsed.data["status"]
        if allowed_values is None or status not in allowed_values:
            violations.append(f"{relative_path}: {type_path} status={status!r}")

    assert violations == [], "non-local status frontmatter remains:\n" + "\n".join(
        violations
    )
    assert observed_types == set(TYPE_LOCAL_STATUS_VALUES)


def test_active_frontmatter_types_are_paths() -> None:
    for relative_path in _active_kb_markdown_paths():
        content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
        parsed = frontmatter.parse(content)
        assert parsed.ok, f"{relative_path}: {parsed.errors}"
        if not parsed.data:
            continue
        assert "type" in parsed.data, f"{relative_path}: frontmatter.type is missing"
        _canonical_type_path(relative_path, parsed.data["type"])


def test_current_type_examples_use_path_values() -> None:
    checked: list[str] = []
    for relative_path in TYPE_EXAMPLE_GUIDANCE:
        content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
        for match in FENCED_EXAMPLE.finditer(content):
            metadata = _example_frontmatter(
                match.group("body"), match.group("language")
            )
            if not metadata or "type" not in metadata:
                continue
            example_type = metadata["type"]
            assert isinstance(example_type, str), (
                f"{relative_path}: example type must be a string"
            )
            source_context = TYPE_EXAMPLE_SOURCE_CONTEXTS.get(
                (relative_path, example_type), relative_path
            )
            canonical = _canonical_type_path(source_context, example_type)
            checked.append(f"{relative_path}: {canonical}")

    assert checked, "no path-valued type examples were checked"


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

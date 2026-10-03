"""Keep authored type guidance aligned with executable schemas."""

from __future__ import annotations

from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.lib.project_paths import iter_validation_markdown_files
from commonplace.lib.type_resolver import validate_type_path

REPO_ROOT = Path(__file__).resolve().parents[3]

TYPE_LOCAL_STATUS_VALUES = {
    "articles/types/article.md": {
        "draft",
        "working-paper",
        "published",
        "superseded",
        "withdrawn",
    },
    "reference/types/adr.md": {"accepted", "superseded", "deprecated"},
}

def _active_kb_markdown_paths() -> tuple[Path, ...]:
    paths: list[Path] = []
    for path in iter_validation_markdown_files(REPO_ROOT / "kb"):
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

"""Contract tests for the committed type schemas.

Each test validates a sample document against a real schema under kb/, through
the validator's schema step, so a schema edit that changes what a type accepts
fails here. Validator code paths are tested in tests/commonplace/validation/.
"""

from __future__ import annotations

import pytest

from commonplace.lib.note_parser import parse_document
from commonplace.lib.type_resolver import resolve_type_definition
from commonplace.lib.validation import CheckResults, ParsedNote, apply_schema_validation
from tests.commonplace.validation_helpers import REPO_ROOT

SNAPSHOT = "kb/types/snapshot.md"
INGEST = "kb/types/ingest-report.md"


def check(type_path: str, text: str) -> CheckResults:
    """Run only the schema step for text declared as type_path."""
    document, error = parse_document(text)
    assert error is None, error
    assert document is not None
    profile = resolve_type_definition(REPO_ROOT / type_path, repo_root=REPO_ROOT)
    results = CheckResults(note_type=profile.type_name)
    apply_schema_validation(
        results,
        ParsedNote(
            path=REPO_ROOT / "sample.md",
            content=text,
            note_type=profile.type_name,
            profile=profile,
            document=document,
        ),
    )
    return results


def note(frontmatter: str, body: str = "# Sample\n") -> str:
    return f"---\n{frontmatter.strip()}\n---\n\n{body}"


def assert_fails_with(results: CheckResults, expected: str) -> None:
    assert any(expected in item for item in results.fails), results.fails


# --- sources ----------------------------------------------------------------


def test_source_snapshot_validates_without_optional_fields() -> None:
    results = check(
        SNAPSHOT,
        note(
            "source: https://example.com/article\n"
            'captured: "2026-04-19"\n'
            "capture: web-fetch\n"
            f"type: {SNAPSHOT}",
            "# Sample\n\nCaptured text.\n",
        ),
    )

    assert results.fails == []
    assert any("snapshot requirements satisfied" in item for item in results.passes)


CHECKSUM = "0123456789abcdef" * 4
COMMIT = "https://github.com/example/system/commit/0123456789abcdef0123456789abcdef01234567"
ONE_REPOSITORY = f"secondary_sources:\n  - role: implementation\n    source: {COMMIT}"
TWO_REPOSITORIES = (
    f"{ONE_REPOSITORY}\n  - role: implementation\n"
    "    source: https://github.com/example/second/commit/89abcdef0123456789abcdef0123456789abcdef"
)


def ingest(*, code_grounding: bool = True, secondary_sources: str = TWO_REPOSITORIES) -> str:
    grounding = "\n## Code Grounding\n\nStatic source inspection only.\n" if code_grounding else ""
    return note(
        f"""description: Code-grounded analysis of a paper and its released implementation
source: https://arxiv.org/abs/2608.12345v1
captured: "2026-08-18"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: {CHECKSUM}
ingested: "2026-08-18"
type: {INGEST}
domains: [agents, evaluation]
{secondary_sources}""",
        f"""# Ingest: Paper

## Classification

Scientific paper.

## Summary

Summary.
{grounding}
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
""",
    )


@pytest.mark.parametrize(
    "text",
    [ingest(), ingest(code_grounding=False, secondary_sources="")],
    ids=["code-grounded", "ordinary"],
)
def test_ingest_accepts_valid_reports(text: str) -> None:
    results = check(INGEST, text)

    assert results.fails == []
    assert any("ingest-report requirements satisfied" in item for item in results.passes)


def test_code_grounded_ingest_requires_code_grounding_section() -> None:
    assert_fails_with(check(INGEST, ingest(code_grounding=False)), "missing '## Code Grounding'")


@pytest.mark.parametrize(
    ("secondary_sources", "expected"),
    [
        (
            f"secondary_sources:\n  - role: evidence\n    source: {COMMIT}",
            "'implementation' was expected",
        ),
        (
            "secondary_sources:\n  - role: implementation\n    source: https://github.com/example/system",
            "does not match",
        ),
    ],
    ids=["wrong-role", "unpinned"],
)
def test_ingest_rejects_invalid_secondary_sources(
    secondary_sources: str, expected: str
) -> None:
    assert_fails_with(check(INGEST, ingest(secondary_sources=secondary_sources)), expected)


def test_ingest_rejects_invalid_primary_source_anchor() -> None:
    text = ingest()
    old = f"snapshot_sha256: {CHECKSUM}"
    assert old in text

    assert_fails_with(check(INGEST, text.replace(old, "snapshot_sha256: ABCD")), "does not match")

"""Contract tests for the committed type schemas.

Each test validates a sample document against a real schema under kb/, through
the validator's schema step, so a schema edit that changes what a type accepts
fails here. Validator code paths are tested in tests/commonplace/cli/.
"""

from __future__ import annotations

import pytest

from commonplace.lib.note_parser import parse_document
from commonplace.lib.type_resolver import resolve_type_definition
from commonplace.lib.validation import CheckResults, ParsedNote, apply_schema_validation
from tests.commonplace.validation_helpers import REPO_ROOT

NOTE = "kb/types/note.md"
SNAPSHOT = "kb/sources/types/snapshot.md"
INGEST = "kb/sources/types/ingest-report.md"
STRUCTURED_CLAIM = "kb/notes/types/structured-claim.md"
ADR = "kb/reference/types/adr.md"
AGENT_MEMORY_REVIEW = "kb/agent-memory-systems/types/agent-memory-system-review.md"


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


# --- note -------------------------------------------------------------------

NOTE_DESCRIPTION = "A sample note description long enough to sit inside the style band"


@pytest.mark.parametrize(
    ("description_line", "expected"),
    [
        ("", "'description' is a required property"),
        ("description:", "frontmatter.description: None is not of type 'string'"),
        ("description: '   '", "frontmatter.description: '   ' does not match"),
    ],
    ids=["missing", "null", "whitespace"],
)
def test_note_description_must_be_non_empty_text(
    description_line: str, expected: str
) -> None:
    results = check(NOTE, note(f"{description_line}\ntype: {NOTE}"))

    assert_fails_with(results, expected)


@pytest.mark.parametrize(
    ("description", "expected"),
    [
        ("Short but non-empty", "description should be at least 50 characters"),
        ("x" * 251, "description should be at most 250 characters"),
        ("x" * 225, None),
    ],
    ids=["too-short", "too-long", "inside-band"],
)
def test_note_description_length_band_only_warns(
    description: str, expected: str | None
) -> None:
    results = check(NOTE, note(f"description: {description}\ntype: {NOTE}"))

    assert results.fails == []
    warns = [item for item in results.warns if "frontmatter.description" in item]
    if expected is None:
        assert warns == []
    else:
        assert any(f"frontmatter.description: {expected}" in item for item in warns)


@pytest.mark.parametrize(
    ("extra", "should_pass"),
    [
        ("", True),
        ("user-verified: true", True),
        ("user-verified: false", False),
        ("status: current", False),
    ],
)
def test_note_user_verification_and_status_boundary(
    extra: str, should_pass: bool
) -> None:
    results = check(NOTE, note(f"description: {NOTE_DESCRIPTION}\ntype: {NOTE}\n{extra}"))

    assert (results.fails == []) is should_pass


# --- structured claim and ADR -----------------------------------------------


def test_structured_claim_requires_evidence_and_reasoning() -> None:
    results = check(
        STRUCTURED_CLAIM,
        note(
            f"description: {NOTE_DESCRIPTION}\ntype: {STRUCTURED_CLAIM}",
            "# Claims need support\n\n## Evidence\n\nSome evidence.\n",
        ),
    )

    assert_fails_with(results, "missing '## Reasoning'")


@pytest.mark.parametrize(("status", "should_pass"), [("accepted", True), ("current", False)])
def test_adr_status_uses_its_own_enum(status: str, should_pass: bool) -> None:
    results = check(
        ADR,
        note(
            f"description: {NOTE_DESCRIPTION}\ntype: {ADR}\nstatus: {status}",
            "# Decision\n\n## Context\n\nC.\n\n## Decision\n\nD.\n\n## Consequences\n\nQ.\n",
        ),
    )

    assert (results.fails == []) is should_pass


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
        ("secondary_sources: []", "should be non-empty"),
        (
            f"secondary_sources:\n  - role: evidence\n    source: {COMMIT}",
            "'implementation' was expected",
        ),
        (
            "secondary_sources:\n  - role: implementation\n    source: https://github.com/example/system",
            "does not match",
        ),
        (
            f"{ONE_REPOSITORY}\n    checkout: related-systems/example--system",
            "Additional properties are not allowed",
        ),
        (
            f"{ONE_REPOSITORY}\n  - role: implementation\n    source: {COMMIT}",
            "has non-unique elements",
        ),
    ],
    ids=["empty", "wrong-role", "unpinned", "extra-key", "duplicate"],
)
def test_ingest_rejects_invalid_secondary_sources(
    secondary_sources: str, expected: str
) -> None:
    assert_fails_with(check(INGEST, ingest(secondary_sources=secondary_sources)), expected)


@pytest.mark.parametrize(
    ("old", "new", "expected"),
    [
        (
            "source: https://arxiv.org/abs/2608.12345v1",
            "source: arxiv:2608.12345v1",
            "does not match",
        ),
        ('captured: "2026-08-18"', 'captured: "not-a-date"', "captured"),
        (f"snapshot_sha256: {CHECKSUM}", "snapshot_sha256: ABCD", "does not match"),
    ],
    ids=["source-not-url", "captured-not-date", "checksum-not-hex"],
)
def test_ingest_rejects_invalid_primary_source_anchor(
    old: str, new: str, expected: str
) -> None:
    text = ingest()
    assert old in text

    assert_fails_with(check(INGEST, text.replace(old, new)), expected)


@pytest.mark.parametrize("retired_field", ["source_snapshot: paper.md", "code_revisions: [old]"])
def test_ingest_rejects_retired_source_fields(retired_field: str) -> None:
    text = ingest().replace(
        "domains: [agents, evaluation]", f"domains: [agents, evaluation]\n{retired_field}"
    )

    assert_fails_with(check(INGEST, text), "False schema does not allow")


# --- agent-memory system review ---------------------------------------------

TRACE_LEARNING_SUBSECTION = """
### Trace-learning

**Trace source:** `tool-traces` — completed tool calls.
**Learning scope:** `per-project` — lessons stay in one project.
**Learning timing:** `offline` — learning runs after the session.
**Distilled form:** `natural-language` — lessons are text.
"""


def review(
    *, last_checked: bool = True, tags: str | None = None, trace_subsection: bool = False
) -> str:
    frontmatter = (
        'description: "External memory system with explicit write and read-back mechanisms"\n'
        f"type: {AGENT_MEMORY_REVIEW}\n"
        "source-tier: code-grounded"
    )
    if last_checked:
        frontmatter += '\nlast-checked: "2026-08-30"'
    if tags is not None:
        frontmatter += f"\ntags: {tags}"
    return note(
        frontmatter,
        f"""# System

## Core Ideas

The system learns from tool traces.

## Artifact analysis

**Storage substrate:** `files` — retained files.
**Representational form:** `natural-language` — lessons are text.
**Lineage:** `trace-extracted` — lessons come from tool traces.
**Behavioral authority:** `knowledge` — later agents read the lessons.

## Write side

**Write agency:** `automatic` — the learner writes lessons.
{TRACE_LEARNING_SUBSECTION if trace_subsection else ""}
## Read-back

**Read-back:** `pull` — the agent requests lessons.

## Curiosity Pass

The source does not establish behavioral activation.
""",
    )


@pytest.mark.parametrize(
    "text",
    [review(), review(tags="[trace-learning]", trace_subsection=True)],
    ids=["stable", "trace-learning"],
)
def test_agent_memory_review_accepts_valid_reviews(text: str) -> None:
    assert check(AGENT_MEMORY_REVIEW, text).fails == []


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        (review(last_checked=False), "'last-checked' is a required property"),
        (review(tags="[trace-learning]"), "missing '### Trace-learning'"),
        (review(trace_subsection=True), "'tags' is a required property"),
    ],
    ids=["no-last-checked", "tag-without-subsection", "subsection-without-tag"],
)
def test_agent_memory_review_rejects_invalid_reviews(text: str, expected: str) -> None:
    assert_fails_with(check(AGENT_MEMORY_REVIEW, text), expected)

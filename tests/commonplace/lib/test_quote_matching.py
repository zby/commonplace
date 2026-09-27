from pathlib import Path

import pytest

from commonplace.lib.agentic_analysis import SourceIdentity, _verify_quote_anchors
from commonplace.lib.hashing import content_sha256_for_text
from commonplace.lib.quote_matching import match_quote, parse_blockquotes
from commonplace.lib.quote_verification import parse_prose_citations, verify_content
from commonplace.lib.validation import CheckResults, validate_ingest_quotes


@pytest.mark.parametrize(
    ("quote", "source", "ranges", "count", "passed"),
    [
        ("one", "one\ntwo", (), 1, True),
        ("one", "one\none", (), 2, False),
        ("one", "one\none", ((2, 2),), 1, True),
        ("one", "one\ntwo", ((2, 2),), 0, False),
        ("one", "one\none", ((1, 2),), 2, False),
        ("one two", "one\n  two", ((1, 2),), 1, True),
        ("one two", "one\ntwo", ((1, 1),), 0, False),
        ("one two", "one\nignored\ntwo", ((1, 1), (3, 3)), 0, False),
        ("one", "one\ntwo", ((1, 1), (1, 2)), 1, True),
        ("ana", "banana", (), 2, False),
        ("one", "one one", ((1, 1),), 2, False),
    ],
)
def test_occurrences_and_containment(quote, source, ranges, count, passed):
    result = match_quote(quote, source, kind="code", ranges=ranges)
    assert result.count == count
    assert result.matched is passed
    if count > 1:
        assert f"{count} times" in result.error


@pytest.mark.parametrize("ranges", [((0, 1),), ((2, 1),), ((1, 3),)])
def test_invalid_bounds(ranges):
    assert "outside" in match_quote("one", "one\ntwo", kind="code", ranges=ranges).error


def test_normalization_preserves_code_operators():
    assert match_quote("value", "**value**", kind="prose").matched
    assert not match_quote("a b", "a ** b", kind="code").matched
    assert not match_quote("a b", "a __ b", kind="code").matched
    assert match_quote("a ** b", "a  **\nb", kind="code").matched


def test_regions_do_not_manufacture_a_quote():
    assert not match_quote("one two", ["one", "two"], kind="prose").matched


def test_parsers_share_record_and_blockquote_ranges():
    block = parse_blockquotes(
        "> one\n> two\n> --- `doc.md:2-3` @ `sha256:abc` — locator"
    )[0]
    prose = parse_prose_citations('"one two" ([source](doc.md), verbatim).')[0]
    assert type(block) is type(prose)
    assert block.quote == "one\ntwo"
    assert block.source == "doc.md"
    assert block.ranges == ((2, 3),)
    assert block.version == "sha256:abc"
    assert prose.version is None and prose.ranges == ()


def test_fenced_attributions_are_examples():
    assert not parse_blockquotes("```markdown\n> example\n> --- `doc.md` @ `abc`\n```")


@pytest.mark.parametrize("quote", ["one two", "Section title", "doc.md", "two three"])
def test_notes_only_match_retained_bodies(tmp_path, quote):
    source = tmp_path / "source.ingest.md"
    source.write_text(
        "## Quotes\n\n> one\n> two\n> --- `doc.md` @ `abc` — Section title\n\n> three\n> --- `doc.md` @ `abc`\n"
    )
    result = verify_content(
        f'"{quote}" ([source](source.ingest.md), verbatim).', tmp_path / "note.md"
    )[0]
    assert (result.status == "match") is (quote == "one two")


@pytest.mark.parametrize(
    ("body", "expected"), [("one", True), ("one\none", False), ("other", False)]
)
def test_three_verifiers_agree_on_same_quote_and_region(tmp_path: Path, body, expected):
    digest = content_sha256_for_text(body)
    snapshot = tmp_path / "kb/sources/.snapshots/source.md"
    snapshot.parent.mkdir(parents=True)
    snapshot.write_text(body)
    attributed = f"> one\n> --- `kb/sources/.snapshots/source.md` @ `sha256:{digest}`\n"
    content = f"---\nsnapshot_sha256: {digest}\n---\n## Quotes\n\n{attributed}"
    checks = CheckResults(note_type="ingest-report")
    validate_ingest_quotes(checks, content, snapshot.parent.parent / "source.ingest.md")
    assert (not checks.fails) is expected
    _, failures = _verify_quote_anchors(
        attributed, source=SourceIdentity("capture", "doc", digest, snapshot, digest)
    )
    assert (not failures) is expected
    kb_source = tmp_path / "source.md"
    kb_source.write_text(body)
    result = verify_content(
        '"one" ([source](source.md), verbatim).', tmp_path / "note.md"
    )[0]
    assert (result.status == "match") is expected


def test_wrong_capture_binding_is_source_error(tmp_path):
    snapshot = tmp_path / "source.md"
    snapshot.write_text("one")
    _, failures = _verify_quote_anchors(
        "> one\n> --- `source.md` @ `sha256:wrong`",
        source=SourceIdentity(
            "capture", "doc", "capture", snapshot, content_sha256_for_text("one")
        ),
    )
    assert "source error" in failures[0]
    assert "does not occur" not in failures[0]


@pytest.mark.parametrize("source,genre,expected", [
    ("https://github.com/example/repo", "tool-announcement", "code"),
    ("https://custom.example/repo", "code-repository", "code"),
    ("https://example.com/paper.pdf", "scientific-paper", "prose"),
])
def test_ingest_normalization_uses_source_kind(source, genre, expected):
    from commonplace.lib.validation import ingest_normalization

    assert ingest_normalization(f"---\nsource: {source}\ngenre: {genre}\n---\n") == expected

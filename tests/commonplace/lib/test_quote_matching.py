from pathlib import Path

import pytest

from commonplace.lib.hashing import content_sha256_for_text
from commonplace.lib.quote_grounding import CapturePin, GitPin, resolve_citations
from commonplace.lib.quote_matching import match_quote, parse_blockquotes
from commonplace.lib.quote_verification import verify_content
from commonplace.lib.validation import CheckResults, validate_ingest_quotes


@pytest.mark.parametrize(
    ("quote", "source", "ranges", "count", "passed"),
    [
        ("one", "one\ntwo", (), 1, True),
        ("one", "one\none", (), 2, False),
        ("one", "one\none", ((2, 2),), 1, True),
        ("one", "one\ntwo", ((2, 2),), 0, False),
        ("one two", "one\n  two", ((1, 2),), 1, True),
        ("one two", "one\ntwo", ((1, 1),), 0, False),
        ("one two", "one\nignored\ntwo", ((1, 1), (3, 3)), 0, False),
        ("one", "one\ntwo", ((1, 1), (1, 2)), 1, True),
        ("ana", "banana", (), 2, False),
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
    resolutions = resolve_citations(
        parse_blockquotes(attributed), CapturePin("doc", digest, snapshot, digest), kind="code"
    )
    assert (resolutions[0].status == "match") is expected
    kb_source = tmp_path / "source.md"
    kb_source.write_text(body)
    result = verify_content(
        '"one" ([source](source.md), verbatim).', tmp_path / "note.md"
    )[0]
    assert (result.status == "match") is expected


def test_wrong_capture_binding_is_source_error(tmp_path):
    snapshot = tmp_path / "source.md"
    snapshot.write_text("one")
    result, = resolve_citations(
        parse_blockquotes("> one\n> --- `source.md` @ `sha256:wrong`"),
        CapturePin("doc", "capture", snapshot, content_sha256_for_text("one")),
        kind="code",
    )
    assert result.status == "mismatch"
    assert "source error" in result.detail
    assert "does not occur" not in result.detail


def test_inline_backticks_do_not_hide_later_fabricated_quote(tmp_path):
    snapshot = tmp_path / "source.md"
    snapshot.write_text("real quote")
    digest = content_sha256_for_text("real quote")
    attribution = f"> --- `{snapshot}` @ `sha256:{digest}`\n"
    content = "> real quote\n" + attribution + "\n```example```\n\n> fabricated\n" + attribution
    resolutions = resolve_citations(
        parse_blockquotes(content), CapturePin("doc", digest, snapshot, digest), kind="code"
    )
    assert [result.status for result in resolutions] == ["match", "mismatch"]
    assert "does not occur" in resolutions[1].detail


def test_malformed_attribution_url_is_a_diagnostic(tmp_path):
    from commonplace.lib.validation import validate_quote_citations

    content = "> quote\n> --- [source](https://[broken)\n"
    citation = parse_blockquotes(content)[0]
    assert "invalid attribution URL" in citation.error
    checks = CheckResults(note_type="agentic-system-analysis-result")
    validate_quote_citations(checks, content)
    assert any("invalid attribution URL" in message for message in checks.warns)
    result, = resolve_citations(
        parse_blockquotes(content), GitPin("https://github.com/a/b", "abc", tmp_path),
        kind="code",
    )
    assert result.status == "mismatch" and "source error" in result.detail


@pytest.mark.parametrize("wrapper", ["{}", "<{}>", "[source]({})", "`{}`"])
def test_structural_and_source_checks_accept_registered_urls(tmp_path, wrapper):
    from commonplace.lib.validation import validate_quote_citations

    source = tmp_path / "snapshot.md"
    source.write_text("one")
    digest = content_sha256_for_text("one")
    identity = "https://example.com/source"
    content = "> one\n> --- " + wrapper.format(identity) + "\n"
    results = CheckResults(note_type="agentic-system-analysis-result")
    validate_quote_citations(results, content)
    assert not results.warns
    result, = resolve_citations(
        parse_blockquotes(content), CapturePin(identity, "capture", source, digest), kind="code",
    )
    assert result.status == "match"


@pytest.mark.parametrize("attribution", ["[source](README.md)"])
def test_structural_validation_reports_missing_parsed_source(attribution):
    from commonplace.lib.validation import validate_quote_citations

    results = CheckResults(note_type="agentic-system-analysis-result")
    validate_quote_citations(results, "> quote\n> --- " + attribution + "\n")
    assert any("expected a source path in backticks or source URL" in message for message in results.warns)


@pytest.mark.parametrize("source,genre", [
    ("https://github.com/example/repo", "tool-announcement"),
    ("https://example.com/repo", "code-repository"),
])
@pytest.mark.parametrize("quote,expected", [("return a b", "mismatch"), ("return a ** b", "match")])
def test_notes_preserve_repository_ingest_operators(tmp_path, source, genre, quote, expected):
    ingest = tmp_path / "source.ingest.md"
    ingest.write_text(
        f"---\nsource: {source}\ngenre: {genre}\n---\n## Quotes\n\n"
        "> return a ** b\n> --- `snapshot.md` @ `sha256:abc`\n"
    )
    results = verify_content(f'"{quote}" ([source](source.ingest.md), verbatim).', tmp_path / "note.md")
    assert results[0].status == expected


@pytest.mark.parametrize("attribution,expected", [
    ("[source](https://example.com/paper)", True),
    ("[unrelated](https://example.com/other)", False),
    ("`source.md`", True),
    ("`source.md` @ `sha256:{digest}`", True),
    ("`wrong.md` @ `sha256:{digest}`", False),
    ("`source.md` @ `sha256:wrong`", False),
])
def test_capture_attribution_identifies_registered_source(tmp_path, attribution, expected):
    snapshot = tmp_path / "source.md"
    snapshot.write_text("quote")
    digest = content_sha256_for_text("quote")
    result, = resolve_citations(
        parse_blockquotes("> quote\n> --- " + attribution.format(digest=digest)),
        CapturePin("https://example.com/paper", "capture", snapshot, digest), kind="code",
    )
    assert (result.status == "match") is expected

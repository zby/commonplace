from hashlib import sha256

import pytest

from commonplace.lib.agentic_analysis import SourceIdentity, _verify_quote_anchors
from commonplace.lib.quote_generation import (
    generate_quote_batch,
    generate_quotes,
    quote_occurrences,
    render_quote,
)
from commonplace.lib.quote_matching import (
    match_quote,
    normalize_text,
    parse_blockquotes,
)


@pytest.mark.parametrize(
    "text,source,count",
    [
        ("one", "one\none\none", 3),
        ("one", "one one", 2),
        ("ana", "banana", 2),
        ("x", "xx", 2),
        ("one two", "one\n\t two\n", 1),
        ("* a ** b", "header\r\n * a ** b\r\nend", 1),
        ("café", "café\ncafé", 2),
        ("word", "word\vword", 2),
        ("not present", "original source", 0),
    ],
)
def test_every_occurrence_yields_source_text_with_a_unique_derived_range(
    text, source, count
):
    occurrences = quote_occurrences(text, source)
    assert len(occurrences) == count
    for occurrence in occurrences:
        assert (
            occurrence.text == source[occurrence.start_offset : occurrence.end_offset]
        )
        assert normalize_text(text, "code") in normalize_text(occurrence.text, "code")
        citation = parse_blockquotes(
            render_quote(occurrence, path="source.md", version="abc")
        )[0]
        assert citation.error is None
        assert match_quote(
            citation.quote, source, kind="code", ranges=citation.ranges
        ).matched


def test_same_line_alternatives_preserve_each_distinct_occurrence():
    candidates = quote_occurrences("one", "one one")
    assert [candidate.text for candidate in candidates] == ["one o", "e one"]
    assert len({(c.start_offset, c.end_offset) for c in candidates}) == 2


@pytest.mark.parametrize("text", ["", " \n\t"])
def test_empty_selection_is_rejected(text):
    with pytest.raises(ValueError, match="empty"):
        quote_occurrences(text, "source")


def test_capture_generation_preserves_text_and_uses_frozen_identity(
    tmp_path, monkeypatch
):
    snapshot = tmp_path / "source.md"
    snapshot.write_text(" * repeated\n * repeated\n")
    digest = sha256(snapshot.read_bytes()).hexdigest()
    source = SourceIdentity(
        "capture", "https://example.com/doc", "capture", snapshot, digest
    )

    # Construction must not dispatch a quote checker after locating the text.
    def no_validation(*args, **kwargs):
        pytest.fail("generation called a quotation validator")

    with monkeypatch.context() as context:
        context.setattr("commonplace.lib.quote_matching.match_quote", no_validation)
        context.setattr(
            "commonplace.lib.agentic_analysis._verify_quote_anchors", no_validation
        )
        result = generate_quotes("* repeated", source=source)
    assert [c["start_line"] for c in result["occurrences"]] == [1, 2]
    for candidate in result["occurrences"]:
        assert "sha256:" + digest in candidate["citation"]
        assert not _verify_quote_anchors(candidate["citation"], source=source)[1]
    snapshot.write_text("changed source")
    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        generate_quotes("changed source", source=source)


def test_generation_does_not_clean_up_comment_markers(tmp_path):
    snapshot = tmp_path / "source.md"
    snapshot.write_text(" * first line\n * second line\n")
    source = SourceIdentity(
        "capture", "doc", "capture", snapshot, sha256(snapshot.read_bytes()).hexdigest()
    )
    with pytest.raises(ValueError, match="does not occur"):
        generate_quotes("first line\nsecond line", source=source)


def test_unrepresentable_attribution_delimiter_is_explicit(tmp_path):
    snapshot = tmp_path / "source.md"
    snapshot.write_text("before\n--- source\nafter")
    source = SourceIdentity(
        "capture", "doc", "capture", snapshot, sha256(snapshot.read_bytes()).hexdigest()
    )
    with pytest.raises(ValueError, match="cannot be represented"):
        generate_quotes(snapshot.read_text(), source=source)


@pytest.mark.parametrize("count", [1, 2, 10, 11])
def test_generation_output_and_ambiguity_limit(tmp_path, count):
    snapshot = tmp_path / "source.md"
    snapshot.write_text("selected passage\n" * count)
    source = SourceIdentity(
        "capture", "doc", "capture", snapshot, sha256(snapshot.read_bytes()).hexdigest()
    )
    if count > 10:
        with pytest.raises(
            ValueError, match="more than 10 occurrences; choose a longer quote"
        ):
            generate_quotes("selected passage", source=source)
        return
    result = generate_quotes("selected passage", source=source)
    if count == 1:
        assert isinstance(result, str)
        assert result.startswith("> selected passage\n> --- ")
        assert len(parse_blockquotes(result)) == 1
    else:
        assert list(result) == ["occurrences"]
        assert [entry["occurrence"] for entry in result["occurrences"]] == list(
            range(1, count + 1)
        )
        assert [entry["start_line"] for entry in result["occurrences"]] == list(
            range(1, count + 1)
        )


def test_occurrence_limit_counts_overlapping_matches():
    with pytest.raises(ValueError, match="more than 10 occurrences"):
        quote_occurrences("aa", "a" * 12)


def capture_source(tmp_path, text):
    snapshot = tmp_path / "source.md"
    snapshot.write_text(text)
    return SourceIdentity(
        "capture", "doc", "capture", snapshot, sha256(snapshot.read_bytes()).hexdigest()
    )


def test_batch_resolves_each_key_independently(tmp_path):
    source = capture_source(tmp_path, "unique line\nrepeated\nrepeated\n")
    results = generate_quote_batch(
        [
            {"key": "one", "text": "unique line"},
            {"key": "two", "text": "repeated", "source_path": None},
            {"key": "missing", "text": "absent text"},
            {"key": "bad", "text": 7},
        ],
        source=source,
    )
    assert list(results) == ["one", "two", "missing", "bad"]
    assert results["one"]["status"] == "citation"
    assert results["one"]["citation"] == generate_quotes("unique line", source=source)
    assert results["two"]["status"] == "candidates"
    assert [c["start_line"] for c in results["two"]["occurrences"]] == [2, 3]
    assert results["missing"] == {
        "status": "error", "error": "requested text does not occur in the frozen source",
    }
    assert results["bad"] == {"status": "error", "error": "text must be a string"}


@pytest.mark.parametrize(
    "selections,message",
    [
        ([], "nonempty JSON list"),
        ({"key": "x", "text": "y"}, "nonempty JSON list"),
        (["text"], "not a JSON object"),
        ([{"text": "unique"}], "nonempty string key"),
        ([{"key": "", "text": "unique"}], "nonempty string key"),
        ([{"key": "a", "text": "unique"}, {"key": "a", "text": "unique"}], "not unique"),
    ],
)
def test_malformed_batch_is_rejected_as_a_whole(tmp_path, selections, message):
    source = capture_source(tmp_path, "unique\n")
    with pytest.raises(ValueError, match=message):
        generate_quote_batch(selections, source=source)


def test_batch_source_path_rules_follow_the_source_kind(tmp_path):
    source = capture_source(tmp_path, "unique\n")
    results = generate_quote_batch(
        [{"key": "a", "text": "unique", "source_path": "README.md"}], source=source
    )
    assert results["a"]["status"] == "error"
    assert "omit --source-path" in results["a"]["error"]

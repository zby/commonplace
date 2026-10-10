"""Occurrence diagnostics preserve the passage and only propose checked ranges."""
from dataclasses import replace
from hashlib import sha256

import pytest

from commonplace.lib.quote_generation import MAX_QUOTE_OCCURRENCES, quote_occurrences
from commonplace.lib.quote_grounding import CapturePin, GitPin, resolve_citations
from commonplace.lib.quote_matching import (
    match_quote,
    normalize_text,
    parse_blockquotes,
)


@pytest.mark.parametrize("text,source,count", [
    ("one", "one\none\none", 3), ("one", "one one", 2),
    ("ana", "banana", 2), ("one two", "one\n\t two\n", 1),
    ("* a ** b", "header\r\n * a ** b\r\nend", 1),
    ("café", "café\ncafé", 2), ("word", "word\vword", 2),
    ("not present", "original source", 0),
])
def test_occurrences_are_exact_source_substrings_without_context_expansion(text, source, count):
    occurrences = quote_occurrences(text, source)
    assert len(occurrences) == count
    for occurrence in occurrences:
        assert occurrence.text == source[occurrence.start_offset:occurrence.end_offset]
        assert normalize_text(text, "code") == normalize_text(occurrence.text, "code")


def capture(tmp_path, text):
    path = tmp_path / "capture.md"
    path.write_text(text)
    return CapturePin("https://example.com/doc", "capture", path, sha256(path.read_bytes()).hexdigest())


def block(source, text, suffix=""):
    return "\n".join("> " + line for line in text.splitlines()) + f"\n> --- `{source.file}{suffix}`\n"


def test_unique_path_only_quote_and_whitespace_pass(tmp_path):
    source = capture(tmp_path, "original\n    passage\n")
    result, = resolve_citations(parse_blockquotes(block(source, "original passage")), source, kind="code")
    assert result.status == "match"
    complete = block(source, "original passage", ":1-2").rstrip() + f" @ `sha256:{source.checksum}`\n"
    result, = resolve_citations(parse_blockquotes(complete), source, kind="code")
    assert result.status == "match"
    result, = resolve_citations(parse_blockquotes(complete.replace(source.checksum, "0" * 64)), source, kind="code")
    assert result.status == "mismatch"


def test_not_found_never_proposes_repair_and_rechecks_claim(tmp_path):
    source = capture(tmp_path, 'write("\\n")')
    result, = resolve_citations(parse_blockquotes(block(source, 'write("\\\\n")')), source, kind="code")
    assert result.status == "mismatch"
    assert "quotation not found" in result.detail
    assert "recheck the claim" in result.detail
    assert "candidate" not in result.detail and "paste attribution" not in result.detail


def test_several_ambiguous_quotes_offer_ranges_that_pass(tmp_path):
    source = capture(tmp_path, "first\nrepeated\nsecond\nrepeated\nother\nother\n")
    results = resolve_citations(
        parse_blockquotes(block(source, "repeated") + "\n" + block(source, "other")), source, kind="code",
    )
    assert len(results) == 2
    assert all(result.status == "mismatch" for result in results)
    assert all("candidate 1" in result.detail and "candidate 2" in result.detail for result in results)
    assert f"> --- `{source.file}:2-2`" in results[0].detail
    result, = resolve_citations(parse_blockquotes(block(source, "repeated", ":2-2")), source, kind="code")
    assert result.status == "match"
    result, = resolve_citations(parse_blockquotes(block(source, "repeated", ":1-1")), source, kind="code")
    assert result.status == "mismatch"


def test_same_line_ambiguity_requires_longer_passage(tmp_path):
    source = capture(tmp_path, "one one")
    result, = resolve_citations(parse_blockquotes(block(source, "one")), source, kind="code")
    assert result.status == "mismatch"
    assert "lengthen the quotation" in result.detail
    assert "candidate 1" in result.detail and "candidate 2" in result.detail
    assert "paste attribution" not in result.detail
    assert not match_quote("one", "one one", kind="code", ranges=((1, 1),)).matched
    result, = resolve_citations(parse_blockquotes(block(source, "one one")), source, kind="code")
    assert result.status == "match"


def test_limit_and_checked_range_apply_to_eligible_region(tmp_path):
    source = capture(tmp_path, "repeated\n" * (MAX_QUOTE_OCCURRENCES + 1))
    result, = resolve_citations(parse_blockquotes(block(source, "repeated")), source, kind="code")
    assert result.status == "mismatch"
    assert "expand the quotation" in result.detail and "no candidates proposed" in result.detail
    assert "candidate 1" not in result.detail
    result, = resolve_citations(parse_blockquotes(block(source, "repeated", ":3-3")), source, kind="code")
    assert result.status == "match"
    result, = resolve_citations(parse_blockquotes(block(source, "repeated", ":3-4")), source, kind="code")
    assert result.status == "mismatch"
    assert "paste attribution" in result.detail


def test_capture_path_and_hash_are_checked_even_without_version(tmp_path):
    source = capture(tmp_path, "original")
    result, = resolve_citations(
        parse_blockquotes(block(source, "original").replace("capture.md", "wrong.md")), source, kind="code",
    )
    assert result.status == "mismatch"
    result, = resolve_citations(parse_blockquotes(block(source, "original")), source, kind="code")
    assert result.status == "match"
    source.file.write_text("changed")
    # A pin caches its verified bytes; a new verification needs a fresh pin.
    result, = resolve_citations(parse_blockquotes(block(source, "changed")), replace(source), kind="code")
    assert result.status == "unverified"
    assert "source unavailable" in result.detail and "SHA-256 mismatch" in result.detail


def test_missing_git_checkout_is_unverified(tmp_path):
    source = GitPin("https://github.com/example/repo", "abc", tmp_path / "missing")
    result, = resolve_citations(parse_blockquotes("> quote\n> --- `README.md`"), source, kind="code")
    assert result.status == "unverified"
    assert "source unavailable" in result.detail and "directory does not exist" in result.detail


def test_registered_capture_url_candidates_propose_its_path(tmp_path):
    source = capture(tmp_path, "repeated\nrepeated\n")
    result, = resolve_citations(parse_blockquotes(f"> repeated\n> --- {source.identity}\n"), source, kind="code")
    assert result.status == "mismatch"
    assert f"> --- `{source.file}:1-1`" in result.detail
    result, = resolve_citations(parse_blockquotes(block(source, "repeated", ":1-1")), source, kind="code")
    assert result.status == "match"


def test_overlapping_ranges_do_not_duplicate_diagnostic_candidates(tmp_path):
    source = capture(tmp_path, "repeated\nrepeated\n")
    result, = resolve_citations(parse_blockquotes(block(source, "repeated", ":1-2,1-2")), source, kind="code")
    assert result.status == "mismatch"
    assert "candidate 1" in result.detail and "candidate 2" in result.detail
    assert "candidate 3" not in result.detail


def test_fenced_examples_and_ordinary_blockquotes_are_not_quotations(tmp_path):
    source = capture(tmp_path, "source")
    text = '> ordinary blockquote\n\n```text\n> absent\n> --- `capture.md`\n```\n'
    assert parse_blockquotes(text) == ()
    assert resolve_citations(parse_blockquotes(text), source, kind="code") == []

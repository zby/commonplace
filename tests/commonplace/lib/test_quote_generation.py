"""Occurrence diagnostics preserve the passage and only propose checked ranges."""
from hashlib import sha256

import pytest

from commonplace.lib.agentic_analysis import SourceIdentity, verify_quote_anchors
from commonplace.lib.quote_generation import MAX_QUOTE_OCCURRENCES, quote_occurrences
from commonplace.lib.quote_matching import match_quote, normalize_text


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
    return SourceIdentity("capture", "https://example.com/doc", "capture", path, sha256(path.read_bytes()).hexdigest())


def block(source, text, suffix=""):
    return "\n".join("> " + line for line in text.splitlines()) + f"\n> --- `{source.path}{suffix}`\n"


def test_unique_path_only_quote_and_whitespace_pass(tmp_path):
    source = capture(tmp_path, "original\n    passage\n")
    assert not verify_quote_anchors(block(source, "original passage"), source=source)[1]
    complete = block(source, "original passage", ":1-2").rstrip() + f" @ `sha256:{source.expected_sha256}`\n"
    assert not verify_quote_anchors(complete, source=source)[1]
    assert verify_quote_anchors(complete.replace(source.expected_sha256, "0" * 64), source=source)[1]


def test_not_found_never_proposes_repair_and_rechecks_claim(tmp_path):
    source = capture(tmp_path, 'write("\\n")')
    _, errors = verify_quote_anchors(block(source, 'write("\\\\n")'), source=source)
    assert "quotation not found" in errors[0]
    assert "recheck the claim" in errors[0]
    assert "candidate" not in errors[0] and "paste attribution" not in errors[0]


def test_several_ambiguous_quotes_offer_ranges_that_pass(tmp_path):
    source = capture(tmp_path, "first\nrepeated\nsecond\nrepeated\nother\nother\n")
    _, errors = verify_quote_anchors(block(source, "repeated") + "\n" + block(source, "other"), source=source)
    assert len(errors) == 2
    assert all("candidate 1" in error and "candidate 2" in error for error in errors)
    assert f"> --- `{source.path}:2-2`" in errors[0]
    assert not verify_quote_anchors(block(source, "repeated", ":2-2"), source=source)[1]
    assert verify_quote_anchors(block(source, "repeated", ":1-1"), source=source)[1]


def test_same_line_ambiguity_requires_longer_passage(tmp_path):
    source = capture(tmp_path, "one one")
    _, errors = verify_quote_anchors(block(source, "one"), source=source)
    assert "lengthen the quotation" in errors[0]
    assert "candidate 1" in errors[0] and "candidate 2" in errors[0]
    assert "paste attribution" not in errors[0]
    assert not match_quote("one", "one one", kind="code", ranges=((1, 1),)).matched
    assert not verify_quote_anchors(block(source, "one one"), source=source)[1]


def test_limit_and_checked_range_apply_to_eligible_region(tmp_path):
    source = capture(tmp_path, "repeated\n" * (MAX_QUOTE_OCCURRENCES + 1))
    _, errors = verify_quote_anchors(block(source, "repeated"), source=source)
    assert "expand the quotation" in errors[0] and "no candidates proposed" in errors[0]
    assert "candidate 1" not in errors[0]
    assert not verify_quote_anchors(block(source, "repeated", ":3-3"), source=source)[1]
    _, errors = verify_quote_anchors(block(source, "repeated", ":3-4"), source=source)
    assert "paste attribution" in errors[0]


def test_capture_path_and_hash_are_checked_even_without_version(tmp_path):
    source = capture(tmp_path, "original")
    assert verify_quote_anchors(block(source, "original").replace("capture.md", "wrong.md"), source=source)[1]
    source.path.write_text("changed")
    assert verify_quote_anchors(block(source, "changed"), source=source)[1]


def test_registered_capture_url_candidates_propose_its_path(tmp_path):
    source = capture(tmp_path, "repeated\nrepeated\n")
    _, errors = verify_quote_anchors(f"> repeated\n> --- {source.identity}\n", source=source)
    assert f"> --- `{source.path}:1-1`" in errors[0]
    assert not verify_quote_anchors(block(source, "repeated", ":1-1"), source=source)[1]


def test_overlapping_ranges_do_not_duplicate_diagnostic_candidates(tmp_path):
    source = capture(tmp_path, "repeated\nrepeated\n")
    _, errors = verify_quote_anchors(block(source, "repeated", ":1-2,1-2"), source=source)
    assert "candidate 1" in errors[0] and "candidate 2" in errors[0]
    assert "candidate 3" not in errors[0]


def test_fenced_examples_and_ordinary_blockquotes_are_not_quotations(tmp_path):
    source = capture(tmp_path, "source")
    text = '> ordinary blockquote\n\n```text\n> absent\n> --- `capture.md`\n```\n'
    assert verify_quote_anchors(text, source=source) == ([], [])

"""Tests for the reusable quote-verification prototype."""

from pathlib import Path

from scripts.verify_quotes import normalize_text, verify_note


def _write_pair(tmp_path: Path, note_body: str, source_body: str) -> Path:
    notes = tmp_path / "notes"
    sources = tmp_path / "sources"
    notes.mkdir()
    sources.mkdir()
    (sources / "source.md").write_text(source_body, encoding="utf-8")
    note = notes / "note.md"
    note.write_text(note_body, encoding="utf-8")
    return note


def test_normalize_text_folds_capture_typography_and_whitespace():
    assert normalize_text("  “one\n two” … it’s  ") == '"one two" ... it\'s'


def test_verifies_citation_marker(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        'The source says "quoted words here" '
        '([Source](../sources/source.md), Abstract, verbatim).',
        "The source has quoted\nwords here in its abstract.",
    )

    results = verify_note(note)

    assert [result.status for result in results] == ["match"]


def test_verifies_marker_before_quote(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        'The conclusion, verbatim: “quoted words here” '
        '([Source](../sources/source.md), Abstract).',
        "The source has quoted words here in its abstract.",
    )

    assert [result.status for result in verify_note(note)] == ["match"]


def test_mismatch_is_reported(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        'The source says "words not in source" '
        '([Source](../sources/source.md), Abstract, verbatim).',
        "Different text.",
    )

    assert [result.status for result in verify_note(note)] == ["mismatch"]


def test_explicitly_non_verbatim_prose_is_not_a_candidate(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        'The snapshot does not carry this passage verbatim, but summarizes it as '
        '"an own-words rendering" ([Source](../sources/source.md), paraphrase layer).',
        "Different text.",
    )

    assert verify_note(note) == []


def test_unlinked_mentions_are_out_of_scope(tmp_path: Path):
    note = tmp_path / "note.md"
    note.write_text('The source says "quoted words" (Abstract, verbatim).', encoding="utf-8")

    assert verify_note(note) == []


def test_quotes_in_markdown_link_labels_are_ignored(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        'The conclusion is "quoted words" '
        '([Source, "A title"](../sources/source.md), verbatim).',
        "quoted words",
    )

    results = verify_note(note)

    assert [result.quote for result in results] == ["quoted words"]


def test_quotes_in_citation_locators_are_ignored(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        'The conclusion is "quoted words" '
        '([Source](../sources/source.md), "Notable claims", verbatim).',
        "# Notable claims\n\nquoted words",
    )

    results = verify_note(note)

    assert [result.quote for result in results] == ["quoted words"]


def test_marker_does_not_cross_a_sentence_boundary(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        'The paraphrase calls this "own words." The conclusion is "quoted words" '
        '([Source](../sources/source.md), verbatim).',
        "quoted words",
    )

    results = verify_note(note)

    assert [result.quote for result in results] == ["quoted words"]


def test_quoted_title_in_bold_lead_in_is_not_a_candidate(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        '**Paper (2020, "A title"):** "quoted words" '
        '([Source](../sources/source.md), verbatim).',
        "quoted words",
    )

    results = verify_note(note)

    assert [result.quote for result in results] == ["quoted words"]


def test_terminal_punctuation_does_not_separate_blockquote_attribution(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        '> "A complete quoted sentence."\n'
        '> ([Source](../sources/source.md), verbatim)',
        "A complete quoted sentence.",
    )

    assert [result.status for result in verify_note(note)] == ["match"]


def test_distant_verbatim_discussion_does_not_create_unresolved_candidate(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        'The paper calls this "a paraphrase" '
        '([Source](../sources/source.md), summary). A direct verbatim statement follows later.',
        "Different text.",
    )

    assert verify_note(note) == []


def test_verbatim_citation_without_quotation_is_unresolved(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        "The source makes the claim "
        "([Source](../sources/source.md), Abstract, verbatim).",
        "The source makes the claim.",
    )

    results = verify_note(note)

    assert [result.status for result in results] == ["unresolved"]


def test_blockquote_and_following_citation_paragraph_are_paired(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        '> "A complete quoted sentence."\n\n'
        '([Source](../sources/source.md), Abstract, verbatim).',
        "A complete quoted sentence.",
    )

    assert [result.status for result in verify_note(note)] == ["match"]


def test_missing_linked_source_is_unresolved(tmp_path: Path):
    notes = tmp_path / "notes"
    notes.mkdir()
    note = notes / "note.md"
    note.write_text(
        'The source says "quoted words" '
        '([Missing](../sources/missing.md), verbatim).',
        encoding="utf-8",
    )

    results = verify_note(note)

    assert [result.status for result in results] == ["unresolved"]

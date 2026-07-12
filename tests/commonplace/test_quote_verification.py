"""Tests for verbatim-quote verification and its validator integration."""

from pathlib import Path

from commonplace.lib.quote_verification import normalize_text, verify_note
from commonplace.lib.validation import CheckResults, validate_verbatim_quotes


def _check(note: Path) -> CheckResults:
    results = CheckResults(note_type="note")
    validate_verbatim_quotes(results, note.read_text(encoding="utf-8"), note)
    return results


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


# --- validator integration ---------------------------------------------------


def test_validator_fails_a_false_verbatim_claim(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        'It says "words never written" '
        "([Source](../sources/source.md), Abstract, verbatim).",
        "The source says something else entirely.",
    )

    results = _check(note)

    assert any("verbatim quote: not found" in fail for fail in results.fails)
    assert not results.warns


def test_validator_passes_a_true_verbatim_claim(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        'It says "quoted words here" '
        "([Source](../sources/source.md), Abstract, verbatim).",
        "The source has quoted words here in its abstract.",
    )

    results = _check(note)

    assert not results.fails
    assert any("1 resolve against their cited sources" in p for p in results.passes)


def test_validator_stays_silent_on_unresolved_where_the_convention_is_unused(tmp_path: Path):
    """A KB that never adopted the convention must not be warned at.

    An unpaired verbatim citation is an `unresolved` candidate. Warning on it
    unconditionally would fire in every KB that only *writes about* the
    convention without adopting it, and a check that cries wolf teaches authors
    to ignore it — the failure this check exists to prevent. So `unresolved` is
    reported only alongside at least one resolvable verbatim quote.
    """
    note = _write_pair(
        tmp_path,
        "The source makes the claim "
        "([Source](../sources/source.md), Abstract, verbatim).",
        "The source makes the claim.",
    )

    assert [r.status for r in verify_note(note)] == ["unresolved"]

    results = _check(note)

    assert not results.fails
    assert not results.warns


def test_validator_warns_on_unresolved_only_where_the_convention_is_used(tmp_path: Path):
    """One resolvable verbatim quote proves the note uses the convention, so its
    unpaired verbatim citations become visible coverage gaps rather than noise."""
    note = _write_pair(
        tmp_path,
        'It says "quoted words here" '
        "([Source](../sources/source.md), Abstract, verbatim).\n\n"
        "The figure is reported as 4.7 "
        "([Source](../sources/source.md), Table 1, verbatim).",
        "The source has quoted words here in its abstract.",
    )

    results = _check(note)

    assert not results.fails
    assert any("verbatim quote:" in warn for warn in results.warns)


def test_validator_is_inert_on_notes_with_no_verbatim_marker(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        'A plain note quoting "quoted words here" from [Source](../sources/source.md).',
        "The source has quoted words here in its abstract.",
    )

    results = _check(note)

    assert not results.fails
    assert not results.warns
    assert not results.passes


def test_fenced_code_demonstrating_the_convention_is_not_a_claim(tmp_path: Path):
    """A fence *showing* the convention is not asserting it.

    Documentation, type specs, and ADRs all contain worked examples of a
    verbatim citation. Scanning them reports a false mismatch against whatever
    source the example happens to link. Code fences are neutralized through the
    shared parser primitive, so this check and link health agree on what counts
    as code.
    """
    note = _write_pair(
        tmp_path,
        "Write a verbatim citation like this:\n\n"
        "```markdown\n"
        'The paper says "an example quote never in the source" '
        "([Source](../sources/source.md), Abstract, verbatim).\n"
        "```\n\n"
        "That is the whole convention.",
        "Real source text, containing nothing from the example.",
    )

    assert verify_note(note) == []
    results = _check(note)
    assert not results.fails
    assert not results.warns


def test_line_numbers_survive_a_preceding_code_fence(tmp_path: Path):
    """Blanking rather than deleting is what keeps reported line numbers true."""
    note = _write_pair(
        tmp_path,
        "Intro.\n\n```python\nx = 1\ny = 2\n```\n\n"
        'The source says "quoted words here" '
        "([Source](../sources/source.md), Abstract, verbatim).",
        "The source has quoted words here in its abstract.",
    )

    results = verify_note(note)

    assert [r.status for r in results] == ["match"]
    assert results[0].line == 8

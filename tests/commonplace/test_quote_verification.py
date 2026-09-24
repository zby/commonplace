"""Tests for verbatim-quote verification and its validator integration."""

from pathlib import Path

import pytest

from commonplace.lib.hashing import content_sha256_for_text
from commonplace.lib.quote_verification import (
    ingest_quotes_section,
    normalize_text,
    verify_content,
    verify_note,
)
from commonplace.lib.validation import (
    CheckResults,
    validate_ingest_quotes,
    validate_ingest_snapshot_pairing,
    validate_verbatim_quotes,
)


def _check(note: Path) -> CheckResults:
    results = CheckResults(note_type="note")
    validate_verbatim_quotes(
        results, verify_content(note.read_text(encoding="utf-8"), note)
    )
    return results


def _write_pair(
    tmp_path: Path, note_body: str, source_body: str, source_name: str = "source.md"
) -> Path:
    notes = tmp_path / "notes"
    sources = tmp_path / "sources"
    notes.mkdir()
    sources.mkdir()
    (sources / source_name).write_text(source_body, encoding="utf-8")
    note = notes / "note.md"
    note.write_text(note_body, encoding="utf-8")
    return note


_INGEST_WITH_SUMMARY_PHRASE = (
    "## Summary\n\n"
    "The paper argues that shorter contexts help.\n\n"
    "## Quotes\n\n"
    "- **Source extract (verbatim):** an unrelated retained passage\n"
    "  - **Source location:** Section 1.\n"
)

_INGEST_WITH_QUOTED_PHRASE = (
    "## Summary\n\n"
    "Analysis prose that does not repeat the passage.\n\n"
    "## Quotes\n\n"
    "- **Source extract (verbatim):** shorter contexts help\n"
    "  - **Source location:** Section 1.\n"
)


def test_normalize_text_folds_capture_typography_and_whitespace():
    assert normalize_text("  “one\n two” … it’s  ") == '"one two" ... it\'s'


@pytest.mark.parametrize(
    "body, source_body, source_name",
    [
        pytest.param(
            'The conclusion, verbatim: “quoted words here” '
            '([Source](../sources/source.md), Abstract).',
            "The source has quoted words here in its abstract.",
            "source.md",
            id="marker-before-quote",
        ),
        pytest.param(
            '> "A complete quoted sentence."\n'
            '> ([Source](../sources/source.md), verbatim)',
            "A complete quoted sentence.",
            "source.md",
            id="terminal-punctuation-in-blockquote-attribution",
        ),
        pytest.param(
            '> "A complete quoted sentence."\n\n'
            '([Source](../sources/source.md), Abstract, verbatim).',
            "A complete quoted sentence.",
            "source.md",
            id="blockquote-then-citation-paragraph",
        ),
        pytest.param(
            'The paper says "shorter contexts help" '
            "([Ingest](../sources/src.ingest.md), Section 1, verbatim).",
            _INGEST_WITH_QUOTED_PHRASE,
            "src.ingest.md",
            id="ingest-quotes-section",
        ),
        pytest.param(
            'The paper says "shorter contexts help" '
            "([Source](../sources/source.md), Summary, verbatim).",
            "## Summary\n\nThe paper argues that shorter contexts help.\n",
            "source.md",
            id="non-ingest-source-anywhere-in-file",
        ),
    ],
)
def test_single_verbatim_quote_matches(
    tmp_path: Path, body: str, source_body: str, source_name: str
):
    note = _write_pair(tmp_path, body, source_body, source_name)

    assert [result.status for result in verify_note(note)] == ["match"]


@pytest.mark.parametrize(
    "body",
    [
        pytest.param(
            'The snapshot does not carry this passage verbatim, but summarizes it as '
            '"an own-words rendering" ([Source](../sources/source.md), paraphrase layer).',
            id="explicitly-non-verbatim-prose",
        ),
        pytest.param(
            'The source says "quoted words" (Abstract, verbatim).',
            id="unlinked-mention",
        ),
        pytest.param(
            'The paper calls this "a paraphrase" '
            '([Source](../sources/source.md), summary). '
            "A direct verbatim statement follows later.",
            id="distant-verbatim-discussion",
        ),
    ],
)
def test_no_verbatim_candidate(tmp_path: Path, body: str):
    note = _write_pair(tmp_path, body, "Different text.")

    assert verify_note(note) == []


@pytest.mark.parametrize(
    "body, source_body",
    [
        pytest.param(
            'The conclusion is "quoted words" '
            '([Source, "A title"](../sources/source.md), verbatim).',
            "quoted words",
            id="quote-in-link-label",
        ),
        pytest.param(
            'The conclusion is "quoted words" '
            '([Source](../sources/source.md), "Notable claims", verbatim).',
            "# Notable claims\n\nquoted words",
            id="quote-in-citation-locator",
        ),
        pytest.param(
            'The paraphrase calls this "own words." The conclusion is "quoted words" '
            '([Source](../sources/source.md), verbatim).',
            "quoted words",
            id="marker-does-not-cross-sentence-boundary",
        ),
        pytest.param(
            '**Paper (2020, "A title"):** "quoted words" '
            '([Source](../sources/source.md), verbatim).',
            "quoted words",
            id="quoted-title-in-bold-lead-in",
        ),
    ],
)
def test_distractor_quotes_are_not_candidates(
    tmp_path: Path, body: str, source_body: str
):
    note = _write_pair(tmp_path, body, source_body)

    assert [result.quote for result in verify_note(note)] == ["quoted words"]


@pytest.mark.parametrize(
    "body, quote",
    [
        (
            (
                'Earlier context ([Source](../sources/source.md)); '
                'verbatim: "quoted words" [Source](../sources/source.md) '
                '(additional context).'
            ),
            "quoted words",
        ),
        (
            (
                'The source says "a (conservative) estimate" '
                '[Source](../sources/source.md), verbatim; '
                'compare ([Other](../sources/other.md)).'
            ),
            "a (conservative) estimate",
        ),
        (
            (
                'The source says "Ŝ(E) is bounded" '
                '[Source](../sources/source.md), verbatim; '
                'compare ([Other](../sources/other.md)).'
            ),
            "Ŝ(E) is bounded",
        ),
        (
            (
                'The conclusion is "quoted words" '
                '([Source](../sources/source.md), section 2 (discussion), '
                '"Locator title", verbatim).'
            ),
            "quoted words",
        ),
        (
            (
                'The source says "an unmatched ( in the source" '
                '[Source](../sources/source.md), verbatim; '
                'compare ([Other](../sources/other.md)).'
            ),
            "an unmatched ( in the source",
        ),
    ],
)
def test_citation_parentheses_do_not_hide_or_misattribute_quotes(
    tmp_path: Path, body: str, quote: str
):
    note = _write_pair(tmp_path, body, quote)
    (tmp_path / "sources" / "other.md").write_text("Unrelated text.", encoding="utf-8")

    results = verify_note(note)

    assert [(result.status, result.quote, result.source) for result in results] == [
        ("match", quote, (tmp_path / "sources" / "source.md").resolve())
    ]


@pytest.mark.parametrize("quote", ["a (conservative) estimate", "Ŝ(E) is bounded"])
def test_parenthesis_in_quote_does_not_hide_the_next_quote(tmp_path: Path, quote: str):
    note = _write_pair(
        tmp_path,
        f'The source says "{quote}" [Source](../sources/source.md), verbatim; '
        'also "another claim" [Other](../sources/other.md), verbatim (discussion).',
        quote,
    )
    other = tmp_path / "sources" / "other.md"
    other.write_text("another claim", encoding="utf-8")

    results = verify_note(note)

    assert [(result.status, result.quote, result.source) for result in results] == [
        ("match", quote, (tmp_path / "sources" / "source.md").resolve()),
        ("match", "another claim", other.resolve()),
    ]


def test_verbatim_citation_without_quotation_is_unresolved(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        "The source makes the claim "
        "([Source](../sources/source.md), Abstract, verbatim).",
        "The source makes the claim.",
    )

    results = verify_note(note)

    assert [result.status for result in results] == ["unresolved"]


def test_missing_linked_source_is_unresolved(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        'The source says "quoted words" '
        '([Missing](../sources/missing.md), verbatim).',
        "",
    )

    results = verify_note(note)

    assert [result.status for result in results] == ["unresolved"]


@pytest.mark.parametrize(
    "ingest_body",
    [
        pytest.param(_INGEST_WITH_SUMMARY_PHRASE, id="phrase-only-in-analysis"),
        pytest.param(
            "## Summary\n\nThe paper argues that shorter contexts help.\n",
            id="no-quotes-section",
        ),
    ],
)
def test_ingest_analysis_prose_does_not_satisfy_a_verbatim_quote(
    tmp_path: Path, ingest_body: str
):
    """An ingest's own analysis is not source support (ADR 073)."""
    note = _write_pair(
        tmp_path,
        'The paper says "shorter contexts help" '
        "([Ingest](../sources/src.ingest.md), Summary, verbatim).",
        ingest_body,
        "src.ingest.md",
    )

    results = verify_note(note)

    assert [result.status for result in results] == ["mismatch"]
    assert results[0].detail == (
        "normalized quotation does not occur in the linked ingest's Quotes section"
    )


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


class TestIngestQuoteValidation:
    """`Source extract (verbatim)` resolves against the ingest's pinned snapshot.

    Conditional on retention: `kb/sources/.snapshots/` is gitignored, so a fresh
    clone has the checksum but not the bytes. Absent snapshot is silence.
    """

    @staticmethod
    def _ingest(
        tmp_path,
        extract: str | None,
        *,
        snapshot: str | None,
        sha: str | None = None,
        snapshot_name: str = "src.md",
        source: str | None = None,
    ):
        sources = tmp_path / "kb" / "sources"
        (sources / ".snapshots").mkdir(parents=True)
        body = snapshot if snapshot is not None else ""
        digest = sha if sha is not None else content_sha256_for_text(body)
        if snapshot is not None:
            (sources / ".snapshots" / snapshot_name).write_text(
                body, encoding="utf-8"
            )
        quotes = (
            "No source quotes have been retained yet.\n"
            if extract is None
            else f"- **Source extract (verbatim):** {extract}\n"
        )
        source_line = f"source: {source}\n" if source is not None else ""
        ingest = sources / "src.ingest.md"
        ingest.write_text(
            f"---\n{source_line}snapshot_sha256: {digest}\n---\n\n"
            f"## Quotes\n\n{quotes}",
            encoding="utf-8",
        )
        return ingest

    def _run(self, ingest):
        results = CheckResults(note_type="ingest-report")
        validate_ingest_quotes(results, ingest.read_text(encoding="utf-8"), ingest)
        return results

    def _run_pairing(self, ingest):
        results = CheckResults(note_type="ingest-report")
        validate_ingest_snapshot_pairing(
            results, ingest.read_text(encoding="utf-8"), ingest
        )
        return results

    def test_extract_present_in_snapshot_passes(self, tmp_path):
        ingest = self._ingest(tmp_path, "the exact words", snapshot="here are the exact words indeed")
        results = self._run(ingest)
        assert not results.fails
        assert any("resolve against the pinned snapshot" in p for p in results.passes)

    def test_extract_absent_from_snapshot_fails(self, tmp_path):
        ingest = self._ingest(tmp_path, "words never written", snapshot="something else entirely")
        results = self._run(ingest)
        assert any("not found in the checksum-verified snapshot" in f for f in results.fails)

    def test_extract_spanning_wrapped_lines_passes(self, tmp_path):
        """Normalization collapses whitespace, so a quote may cross a wrapped line."""
        ingest = self._ingest(tmp_path, "one continuous sentence", snapshot="one continuous\nsentence")
        results = self._run(ingest)
        assert not results.fails

    def test_populated_quotes_reject_stale_global_empty_claim(self, tmp_path):
        ingest = self._ingest(
            tmp_path,
            "the exact words",
            snapshot="here are the exact words indeed",
        )
        ingest.write_text(
            ingest.read_text(encoding="utf-8")
            + "\n## Recommended Next Action\n\n"
            + "No source quotes have been retained yet.\n",
            encoding="utf-8",
        )

        results = self._run(ingest)

        assert any(
            "populated Quotes section conflicts" in item for item in results.fails
        )

    def test_populated_quotes_warn_on_snapshot_required_marker(self, tmp_path):
        ingest = self._ingest(
            tmp_path,
            "the exact words",
            snapshot="here are the exact words indeed",
        )
        ingest.write_text(
            ingest.read_text(encoding="utf-8")
            + "\n## Recommended Next Action\n\n"
            + "Use this ingest as (snapshot required) for the broader claim.\n",
            encoding="utf-8",
        )

        results = self._run(ingest)

        assert not results.fails
        assert any(
            "verify the marker still names a claim" in item
            for item in results.warns
        )

    def test_missing_snapshot_is_silent(self, tmp_path):
        ingest = self._ingest(tmp_path, "anything at all", snapshot=None, sha="0" * 64)
        results = self._run(ingest)
        assert not results.fails and not results.warns and not results.passes

    def test_snapshot_disagreeing_with_checksum_warns_without_failing(self, tmp_path):
        ingest = self._ingest(tmp_path, "absent text", snapshot="other bytes", sha="1" * 64)
        results = self._run_pairing(ingest)
        assert not results.fails
        assert any("does not match snapshot_sha256" in w for w in results.warns)

    def test_checksum_locates_differently_named_snapshot_with_empty_quotes(
        self, tmp_path
    ):
        ingest = self._ingest(
            tmp_path,
            None,
            snapshot="the exact retained bytes",
            snapshot_name="adapter-derived-name.md",
        )

        results = self._run_pairing(ingest)

        assert not results.fails
        assert results.warns == [
            (
                "snapshot pairing: expected .snapshots/src.md is absent; "
                "snapshot_sha256 locates the exact recorded bytes at "
                ".snapshots/adapter-derived-name.md"
            )
        ]

    def test_absent_snapshot_without_exact_local_match_remains_silent(self, tmp_path):
        ingest = self._ingest(tmp_path, None, snapshot=None, sha="2" * 64)

        results = self._run_pairing(ingest)

        assert not results.warns

    def test_matching_checksum_with_different_source_url_warns(self, tmp_path):
        ingest = self._ingest(
            tmp_path,
            None,
            snapshot="---\nsource: https://example.com/capture\n---\n\nBytes.\n",
            source="https://example.com/other",
        )

        results = self._run_pairing(ingest)

        assert results.warns == [
            (
                "snapshot pairing: .snapshots/src.md matches snapshot_sha256 "
                "but its source URL differs from the ingest"
            )
        ]

    def test_missing_expected_snapshot_reports_same_url_as_different_bytes(
        self, tmp_path
    ):
        ingest = self._ingest(
            tmp_path,
            None,
            snapshot="---\nsource: https://example.com/article\n---\n\nNew bytes.\n",
            snapshot_name="capture-name.md",
            sha="1" * 64,
            source="https://example.com/article",
        )

        results = self._run_pairing(ingest)

        assert results.warns == [
            (
                "snapshot pairing: expected .snapshots/src.md is absent; its "
                "source URL matches .snapshots/capture-name.md, but "
                "snapshot_sha256 identifies different bytes"
            )
        ]

    def test_instruction_showing_the_template_is_not_checked(self, tmp_path):
        """Only a tracked ingest asserts an extract; docs merely display one."""
        doc = tmp_path / "ground-source-dependent-claims.md"
        doc.write_text(
            "## Quotes\n\n- **Source extract (verbatim):** <exact supporting content>\n",
            encoding="utf-8",
        )
        results = CheckResults(note_type="instruction")
        validate_ingest_quotes(results, doc.read_text(encoding="utf-8"), doc)
        assert not results.fails and not results.warns and not results.passes


def test_marker_word_inside_a_link_target_is_not_a_citation(tmp_path: Path):
    note = _write_pair(
        tmp_path,
        "The validator fails a note on a mismatch "
        "([ADR 046](./046-verbatim-quotes-are-validated.md)), so the marker is load-bearing.",
        "",
    )
    (note.parent / "046-verbatim-quotes-are-validated.md").write_text(
        "An ADR.", encoding="utf-8"
    )

    assert verify_note(note) == []


def test_ingest_quotes_section_stops_at_the_next_h2():
    content = "## Quotes\n\nretained passage\n\n## Recommended Next Action\n\nlater prose\n"

    section = ingest_quotes_section(content)

    assert "retained passage" in section
    assert "later prose" not in section

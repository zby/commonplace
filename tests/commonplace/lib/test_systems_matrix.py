from __future__ import annotations

from pathlib import Path

from commonplace.lib import systems_matrix as sm

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def parse(text: str, review_file: str = "reviews/x.md", tier: str = "code-grounded"):
    return sm.parse_review_text(text, review_file, tier)


def test_zikkaron_fixture_full_new_format() -> None:
    """A real review converted to the full new format parses to the expected one-hot row."""
    text = (FIXTURES_DIR / "zikkaron_review.md").read_text(encoding="utf-8")
    row, flags = parse(text, "kb/agent-memory-systems/reviews/Zikkaron.md")

    assert row["system_name"] == "Zikkaron"
    assert row["storage_substrate"] == "sqlite"
    assert row["trace_learning"] == "yes"

    # representational form one-hot + derived component list
    assert (
        row["form_natural_language"],
        row["form_symbolic"],
        row["form_parametric"],
    ) == ("1", "1", "1")
    assert row["representational_form"] == "natural-language;symbolic;parametric"

    # lineage + behavioral authority (artifact analysis)
    assert (row["lin_authored"], row["lin_imported"], row["lin_trace_extracted"]) == ("1", "1", "1")
    assert row["auth_knowledge"] == "1" and row["auth_enforcement"] == "1" and row["auth_learning"] == "1"

    # read-back direction one-hot + signal + faithfulness
    assert (row["read_back_direction"], row["rb_pull"], row["rb_push"]) == ("both", "1", "1")
    assert row["sig_coarse"] == "1" and row["sig_identifier"] == "1"
    assert row["sig_inferred_lexical"] == "1" and row["sig_inferred_embedding"] == "1"
    assert row["sig_inferred_judgment"] == "0"
    assert row["rb_faithfulness_tested"] == "no"

    # write side: agency (both) + curation operations one-hot
    assert (row["wa_manual"], row["wa_automatic"]) == ("1", "1")
    assert row["op_consolidate"] == "1" and row["op_dedup"] == "1"
    assert row["op_evolve"] == "1" and row["op_decay"] == "1" and row["op_promote"] == "1"
    assert row["op_synthesize"] == "0" and row["op_invalidate"] == "0"

    # trace axes
    assert row["ts_tool_traces"] == "1" and row["ts_event_streams"] == "1"
    assert row["df_natural_language"] == "1"
    assert row["df_symbolic"] == "1" and row["df_parametric"] == "1"

    assert flags == []


def test_pull_only_skips_push_and_keeps_universal_axes() -> None:
    text = (
        "# Pully\n\n"
        "## Artifact analysis\n\n"
        "**Storage substrate:** `files` — x\n"
        "**Representational form:** `natural-language` — x\n"
        "**Lineage:** `authored` — x\n"
        "**Behavioral authority:** `knowledge` — x\n"
        "\n## Write side\n\n"
        "**Write agency:** `manual` — edits through the authoring channel\n"
        "\n## Read-back\n\n"
        "**Read-back:** `pull` — agent must call search\n"
    )
    row, flags = parse(text)
    assert (row["rb_pull"], row["rb_push"]) == ("1", "0")
    # write agency is universal; manual-only -> curation operations not applicable
    assert (row["wa_manual"], row["wa_automatic"]) == ("1", "0")
    assert row["op_consolidate"] == ""  # blank, not flagged
    # push-only axes left blank (not applicable), not flagged
    assert row["sig_coarse"] == ""
    assert row["rb_faithfulness_tested"] == ""
    # universal axes set
    assert row["form_natural_language"] == "1"
    assert row["lin_authored"] == "1" and row["auth_knowledge"] == "1"
    # trace axes blank (not trace-learning)
    assert row["ts_tool_traces"] == ""
    assert flags == []


def test_trace_axes_only_apply_to_trace_learning() -> None:
    base = (
        "# Sys\n\n"
        "## Artifact analysis\n\n"
        "**Storage substrate:** `files` — x\n"
        "**Representational form:** `natural-language` — x\n"
        "**Lineage:** `authored` — x\n"
        "**Behavioral authority:** `knowledge` — x\n"
        "\n## Write side\n\n"
        "**Write agency:** `manual` — x\n"
        "\n## Read-back\n\n"
        "**Read-back:** `pull` — x\n"
    )
    row, flags = parse(base)  # no trace-learning tag
    assert row["ls_per_task"] == ""  # blank, not flagged
    assert not any("Trace source" in f for f in flags)


def test_missing_applicable_tokens_are_flagged() -> None:
    text = (
        "# Bare\ntags: [trace-learning]\n\n"
        "## Artifact analysis\n\n"
        "**Storage substrate:** `files` — x\n"
        "\n## Write side\n\n"
        "\n## Read-back\n\n"
        "**Read-back:** `push` — pushes stuff\n"
    )
    _row, flags = parse(text)
    # universal + push + trace axes all flagged as missing
    assert "Representational form: missing lead token" in flags
    assert "Lineage: missing lead token" in flags
    assert "Behavioral authority: missing lead token" in flags
    assert "Read-back signal: missing lead token" in flags
    assert "Trace source: missing lead token" in flags
    assert "Write agency: missing lead token" in flags
    assert "Faithfulness tested: missing lead token" in flags


def test_not_determinable_marks_applicable_axis_assessed_unknown() -> None:
    text = (
        "# Pushy\ntags: [trace-learning]\n\n"
        "## Artifact analysis\n\n"
        "**Storage substrate:** `files` — x\n"
        "**Representational form:** `natural-language` — x\n"
        "**Lineage:** `authored` — x\n"
        "**Behavioral authority:** `knowledge` — x\n"
        "\n## Write side\n\n"
        "**Write agency:** `not-determinable` — the review cannot tell\n"
        "**Trace source:** `not-determinable` — the review says traces are used but not which kind\n"
        "**Learning scope:** `cross-task` — x\n"
        "**Learning timing:** `offline` — x\n"
        "**Distilled form:** `natural-language` — x\n"
        "\n## Read-back\n\n"
        "**Read-back:** `push` — pushes stuff\n"
        "**Read-back signal:** `not-determinable` — push exists but the review does not identify the selector\n"
        "**Faithfulness tested:** `not-determinable` — the review does not say whether ablations exist\n"
    )
    row, flags = parse(text)
    assert row["ts_session_logs"] == "" and row["ts_tool_traces"] == ""
    assert row["sig_coarse"] == "" and row["sig_identifier"] == ""
    assert row["rb_faithfulness_tested"] == ""
    assert flags == []


def test_not_determinable_cannot_be_mixed_with_controlled_values() -> None:
    text = (
        "# MixedUnknown\n\n"
        "## Artifact analysis\n\n"
        "**Storage substrate:** `files` — x\n"
        "**Representational form:** `natural-language` `not-determinable` — x\n"
        "**Lineage:** `authored` — x\n"
        "**Behavioral authority:** `knowledge` — x\n"
        "\n## Write side\n\n"
        "**Write agency:** `manual` — x\n"
        "\n## Read-back\n\n"
        "**Read-back:** `pull` — x\n"
    )
    row, flags = parse(text)
    assert row["form_natural_language"] == "1"
    assert "Representational form: `not-determinable` cannot be mixed with controlled values" in flags


def test_curation_none_sets_assessed_absent_zeros_without_flag() -> None:
    # automatic writes but no curation: `none` records 0 across the axis, no flag
    text = (
        "# Acquisitive\n\n"
        "## Artifact analysis\n\n"
        "**Storage substrate:** `files` — x\n"
        "**Representational form:** `natural-language` — x\n"
        "**Lineage:** `imported` — x\n"
        "**Behavioral authority:** `knowledge` — x\n"
        "\n## Write side\n\n"
        "**Write agency:** `manual` `automatic` — auto-extracts, no curation\n"
        "**Curation operations:** `none` — only acquisition, nothing over stored memory\n"
        "\n## Read-back\n\n"
        "**Read-back:** `pull` — x\n"
    )
    row, flags = parse(text)
    assert row["op_consolidate"] == "0" and row["op_dedup"] == "0"
    assert row["op_promote"] == "0" and row["op_synthesize"] == "0"
    assert flags == []


def test_curation_none_cannot_be_mixed_with_controlled_values() -> None:
    text = (
        "# MixedNone\n\n"
        "## Artifact analysis\n\n"
        "**Storage substrate:** `files` — x\n"
        "**Representational form:** `natural-language` — x\n"
        "**Lineage:** `authored` — x\n"
        "**Behavioral authority:** `knowledge` — x\n"
        "\n## Write side\n\n"
        "**Write agency:** `automatic` — x\n"
        "**Curation operations:** `dedup` `none` — x\n"
        "\n## Read-back\n\n"
        "**Read-back:** `pull` — x\n"
    )
    _row, flags = parse(text)
    assert "Curation operations: `none` cannot be mixed with controlled values" in flags


def test_off_vocab_single_token_flagged() -> None:
    row, flags = parse("# X\n\n## Read-back\n\n**Read-back:** `sometimes` — off vocab\n")
    assert "read_back_direction: off-vocab `sometimes`" in flags
    assert row["rb_pull"] == "" and row["rb_push"] == ""


def test_corpus_shaped_natural_language_only_form_is_not_dropped() -> None:
    text = (
        "# Textual\n\n"
        "## Artifact analysis\n\n"
        "- **Storage substrate:** `files` — Markdown files\n"
        "- **Representational form:** `natural-language` — Notes and guidance are text.\n"
        "- **Lineage:** `authored` — Written directly.\n"
        "- **Behavioral authority:** `knowledge` `instruction` — Read by agents.\n"
        "\n## Write side\n\n"
        "**Write agency:** `manual` — Maintainers edit files.\n"
        "\n## Read-back\n\n"
        "**Read-back:** `pull` — Agents open the files.\n"
    )
    row, flags = parse(text)

    assert row["form_natural_language"] == "1"
    assert row["form_symbolic"] == "0" and row["form_parametric"] == "0"
    assert row["representational_form"] == "natural-language"
    assert flags == []


def test_corpus_shaped_mixed_form_retains_natural_language_component() -> None:
    text = (
        "# Mixed\n\n"
        "## Artifact analysis\n\n"
        "- **Storage substrate:** `files` — Markdown files\n"
        "- **Representational form:** `natural-language` `symbolic` — Text plus frontmatter.\n"
        "- **Lineage:** `authored` — Written directly.\n"
        "- **Behavioral authority:** `knowledge` `routing` — Content advises; fields route.\n"
        "\n## Write side\n\n"
        "**Write agency:** `manual` — Maintainers edit files.\n"
        "\n## Read-back\n\n"
        "**Read-back:** `pull` — Agents open the files.\n"
    )
    row, flags = parse(text)

    assert row["form_natural_language"] == "1" and row["form_symbolic"] == "1"
    assert row["form_parametric"] == "0"
    assert row["representational_form"] == "natural-language;symbolic"
    assert flags == []


def test_legacy_sections_cannot_supply_authoritative_matrix_values() -> None:
    text = (
        "# Scoped\n\n"
        "## Comparison with Our System\n\n"
        "**Storage substrate:** `sqlite` — a legacy comparison value\n"
        "**Read-back:** `push` — a legacy comparison value\n"
        "\n## Artifact analysis\n\n"
        "**Storage substrate:** `files` — the source-grounded value\n"
        "**Representational form:** `natural-language` — x\n"
        "**Lineage:** `authored` — x\n"
        "**Behavioral authority:** `knowledge` — x\n"
        "\n## Write side\n\n"
        "**Write agency:** `manual` — x\n"
        "\n## Read-back\n\n"
        "**Read-back:** `pull` — the source-grounded value\n"
    )

    row, flags = parse(text)

    assert row["storage_substrate"] == "files"
    assert row["read_back_direction"] == "pull"
    assert flags == []


def test_backticked_rationale_terms_are_not_controlled_values() -> None:
    text = (
        "# Rationale\n\n"
        "## Artifact analysis\n\n"
        "**Storage substrate:** `files` — x\n"
        "**Representational form:** `natural-language` — x\n"
        "**Lineage:** `authored` — x\n"
        "**Behavioral authority:** `knowledge` — x\n"
        "\n## Write side\n\n"
        "**Write agency:** `automatic` — x\n"
        "**Curation operations:** `evolve` — The system implements neither `none` nor `invalidate`.\n"
        "\n## Read-back\n\n"
        "**Read-back:** `pull` — x\n"
    )

    row, flags = parse(text)

    assert row["op_evolve"] == "1"
    assert row["op_invalidate"] == "0"
    assert flags == []

#!/usr/bin/env python3
"""Compatibility wrappers for multi-note single-gate review protocol helpers."""

from __future__ import annotations

from typing import Sequence

from commonplace.review.protocol.parser import (
    extract_gate_sweep_reviews as _extract_gate_sweep_reviews,
    rewrite_gate_sweep_result_footers as _rewrite_gate_sweep_result_footers,
)
from commonplace.review.protocol.prompt import GateSweepNoteTarget, render_sweep_prompt


def build_gate_sweep_prompt(
    *,
    gate_id: str,
    gate_text: str,
    notes: Sequence[GateSweepNoteTarget],
    gate_path: str | None = None,
) -> str:
    return render_sweep_prompt(
        gate_id=gate_id,
        gate_text=gate_text,
        notes=notes,
        gate_path=gate_path,
    )


def extract_gate_sweep_reviews(
    bundle_markdown: str,
    *,
    gate_id: str,
    expected_note_paths: Sequence[str],
) -> dict[str, str]:
    return _extract_gate_sweep_reviews(
        bundle_markdown,
        gate_id=gate_id,
        expected_note_paths=expected_note_paths,
    )


def rewrite_gate_sweep_result_footers(
    bundle_markdown: str,
    *,
    gate_id: str,
    parsed_reviews: dict[str, str],
) -> str:
    return _rewrite_gate_sweep_result_footers(
        bundle_markdown,
        gate_id=gate_id,
        parsed_reviews=parsed_reviews,
    )


__all__ = [
    "GateSweepNoteTarget",
    "build_gate_sweep_prompt",
    "extract_gate_sweep_reviews",
    "rewrite_gate_sweep_result_footers",
]

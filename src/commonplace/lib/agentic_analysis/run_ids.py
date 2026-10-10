"""The analysis's identifier grammars: full Git commits and run IDs.

A run ID is `AAS-<date>-<source-slug>-<preparation-token>-<nn>`. An
incumbent written by an earlier method may carry an older run-ID form, so
archiving accepts any `AAS-` name.
"""

from __future__ import annotations

import re


def is_commit(value: object) -> bool:
    """Whether ``value`` is a full 40-hex Git commit."""
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}", value) is not None


def run_id(date: str, slug: str, token: str, number: int) -> str:
    """The run ID for a run of this source slug and preparation token."""
    return f"AAS-{date}-{slug}-{token}-{number:02d}"


def is_run_id(value: str, *, token: str, slug: str | None = None) -> bool:
    """Whether ``value`` is a run ID of this preparation token, and of ``slug`` when given."""
    source = re.escape(slug) if slug is not None else "[a-z0-9-]+"
    return re.fullmatch(rf"AAS-\d{{4}}-\d{{2}}-\d{{2}}-{source}-{re.escape(token)}-\d{{2}}", value) is not None


def run_token(value: str) -> str:
    """The preparation token a run ID carries."""
    return value.rsplit("-", 2)[-2]


def is_archived_run_id(value: object) -> bool:
    """Whether ``value`` names an incumbent run, under any method's run-ID form."""
    return isinstance(value, str) and re.fullmatch(r"AAS-[a-zA-Z0-9-]+", value) is not None

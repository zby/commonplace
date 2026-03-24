"""Parse and validate KB frontmatter.

Frontmatter sits between ``---`` delimiters at the start of a markdown
file.  This module defines the *only* grammar the KB recognises — a
strict subset of YAML chosen so that a stdlib-only parser is correct by
construction.

Grammar
-------

::

    frontmatter  := "---\\n" line* "---\\n"
    line         := key ":" SP value NL
    key          := [a-z][a-z0-9_-]*
    value        := inline_list | quoted_string | unquoted_scalar
    inline_list  := "[" ( item ( "," item )* )? "]"
    item         := quoted_string | unquoted_item
    unquoted_item:= [^,\\]"']+          (trimmed)
    quoted_string:= '"' [^"]* '"'  |  "'" [^']* "'"
    unquoted_scalar := .+               (trimmed; must not start with [ or {)

Rules:

* All keys are top-level — no nesting, no indentation.
* No block-style lists (``- item``), multi-line scalars (``|``, ``>``),
  anchors (``&``/``*``), or explicit YAML tags (``!!``).
* Duplicate keys are errors.
* An empty value (key with nothing after the colon) yields ``""``.
* Unquoted scalars that look like common types are coerced:
  ``true``/``false`` → bool, digit-only strings → int.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Public types
# ---------------------------------------------------------------------------

@dataclass
class FrontmatterResult:
    """Parsed frontmatter with optional diagnostics."""

    data: dict[str, Any] = field(default_factory=dict)
    raw: str = ""
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


# ---------------------------------------------------------------------------
# Internals
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\n(.*?)\n---(?:\n|$)", re.DOTALL)
_LINE_RE = re.compile(r"^([a-z][a-z0-9_-]*)\s*:\s*(.*)$")
_BOOL_MAP = {"true": True, "false": False}
_UNSUPPORTED_SCALAR_PREFIXES = ("{", "&", "*", "!!", "|", ">")


def _parse_inline_list(raw: str) -> list[str]:
    """Parse ``[a, b, c]`` into a list of stripped strings."""
    inner = raw[1:-1]  # strip [ ]
    if not inner.strip():
        return []

    items: list[str] = []
    part_chars: list[str] = []
    quote_char: str | None = None

    for char in inner:
        if quote_char:
            if char == quote_char:
                quote_char = None
            part_chars.append(char)
            continue

        if char in ('"', "'"):
            quote_char = char
            part_chars.append(char)
            continue

        if char == ",":
            part = "".join(part_chars).strip()
            if len(part) >= 2 and part[0] == part[-1] and part[0] in ('"', "'"):
                part = part[1:-1]
            items.append(part)
            part_chars = []
            continue

        part_chars.append(char)

    if quote_char:
        raise ValueError("unterminated quoted string in inline list")

    part = "".join(part_chars).strip()
    if len(part) >= 2 and part[0] == part[-1] and part[0] in ('"', "'"):
        part = part[1:-1]
    if part or inner.endswith(","):
        part = part.strip()
        items.append(part)

    return items


def _coerce_scalar(raw: str) -> Any:
    """Coerce an unquoted scalar to a Python type."""
    if not raw:
        return ""
    low = raw.lower()
    if low in _BOOL_MAP:
        return _BOOL_MAP[low]
    if raw.isdigit():
        return int(raw)
    return raw


def _parse_value(raw: str) -> Any:
    """Parse a single frontmatter value."""
    raw = raw.strip()
    if not raw:
        return ""
    # Quoted string
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in ('"', "'"):
        return raw[1:-1]
    # Inline list
    if raw.startswith("[") and raw.endswith("]"):
        return _parse_inline_list(raw)
    if raw.startswith(_UNSUPPORTED_SCALAR_PREFIXES):
        raise ValueError(f"unsupported YAML syntax: {raw}")
    return _coerce_scalar(raw)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def extract_raw(content: str) -> str | None:
    """Return the raw frontmatter text (between delimiters) or None."""
    m = _FM_RE.match(content)
    return m.group(1) if m else None


def parse(content: str) -> FrontmatterResult:
    """Parse frontmatter from markdown *content*.

    Returns a ``FrontmatterResult`` whose ``.data`` dict contains the
    parsed key/value pairs.  Structural violations are collected in
    ``.errors`` — the parser is lenient (best-effort) so that downstream
    code can report all issues rather than stopping at the first one.
    """
    raw = extract_raw(content)
    if raw is None:
        return FrontmatterResult()

    result = FrontmatterResult(raw=raw)
    seen_keys: set[str] = set()

    for lineno, line in enumerate(raw.splitlines(), start=1):
        if not line.strip():
            continue

        m = _LINE_RE.match(line)
        if not m:
            result.errors.append(
                f"line {lineno}: does not match 'key: value' pattern: {line!r}"
            )
            continue

        key, val_raw = m.group(1), m.group(2)

        if key in seen_keys:
            result.errors.append(f"line {lineno}: duplicate key '{key}'")
            continue
        seen_keys.add(key)

        try:
            result.data[key] = _parse_value(val_raw)
        except ValueError as exc:
            result.errors.append(f"line {lineno}: {exc}")

    return result


def strip(content: str) -> str:
    """Return *content* with the frontmatter block removed."""
    return re.sub(r"^---\n.*?\n---(?:\n|$)", "", content, count=1, flags=re.DOTALL)

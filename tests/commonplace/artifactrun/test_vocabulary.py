"""The registered words reach code by ADR 116's spelling rule (ADR 116's drift test).

The register is the workshop glossary while the workshop is open. Each row's
Code cell is `—` for a prose-only word, `derived` when a spelling of the word
must exist in the package, or the one recorded exception spelling. The test
checks spelling only; whether a new word is the right word stays a judgment.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
GLOSSARY = ROOT / "kb/work/workflow-requirements/glossary.md"
PACKAGE = [
    *sorted((ROOT / "src/commonplace/artifactrun").glob("*.py")),
    *sorted((ROOT / "src/commonplace/lib/agentic_analysis").glob("*.py")),
    ROOT / "src/commonplace/lib/directory_layout.py",
    ROOT / "src/commonplace/cli/run.py",
    ROOT / "src/commonplace/cli/analysis.py",
]
SUFFIXES = ("ments", "ment", "ances", "ance", "ences", "ence", "ions", "ion", "ings", "ing",
            "als", "al", "ed", "es", "s", "e")


def stem(word: str) -> str:
    """Inflections of one stem are one word: judge, judged and judgment."""
    for suffix in SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            return word[: -len(suffix)]
    return word


def components(identifier: str) -> list[str]:
    """An identifier's words, split at underscores, hyphens and case changes."""
    return [piece.lower() for part in re.split(r"[_\-]", identifier)
            for piece in re.findall(r"[A-Z]?[a-z0-9]+|[A-Z]+(?![a-z])", part)]


def package_identifiers() -> set[str]:
    """Names, keys and strings in the engine and the analysis package."""
    return {token for path in PACKAGE
            for token in re.findall(r"[A-Za-z_][A-Za-z0-9_\-]*", path.read_text(encoding="utf-8"))}


def spells(word: str, identifier: str) -> bool:
    """Whether the identifier spells the word: snake, kebab or collapsed CamelCase, by stem, beside qualifiers."""
    parts = [part for part in re.split(r"[ \-]", word.lower()) if part]
    stems = [stem(part) for part in parts]
    words = [stem(piece) for piece in components(identifier)]
    if stem("".join(parts)) in words:
        return True
    return any(words[i:i + len(stems)] == stems for i in range(len(words) - len(stems) + 1))


def derives(word: str, identifiers: set[str]) -> bool:
    """A word, or a multiword word beside its qualifier (`condition` for run condition), has a spelling."""
    parts = word.split()
    candidates = [word] + ([" ".join(parts[1:]), " ".join(parts[:-1])] if len(parts) > 1 else [])
    return any(spells(candidate, identifier) for candidate in candidates for identifier in identifiers)


def register() -> list[tuple[str, str]]:
    """Every glossary row's Word and Code cells, from each table headed `| Concept | Word | Code |`."""
    rows, in_table = [], False
    for line in GLOSSARY.read_text(encoding="utf-8").splitlines():
        if line.startswith("| Concept | Word | Code |"):
            in_table = True
            continue
        if not line.startswith("|"):
            in_table = False
            continue
        if in_table and not line.startswith("|---"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            rows.append((cells[1], cells[2]))
    return rows


def test_the_register_is_read():
    rows = register()
    assert rows and any(code == "derived" for _, code in rows)
    malformed = [word for word, code in rows if code not in ("—", "derived") and not re.fullmatch(r"`[^`\s]+`", code)]
    assert not malformed, f"{malformed}: a Code cell is —, derived or one backticked spelling"


@pytest.mark.parametrize("word,code", [row for row in register() if row[1] != "—"], ids=lambda value: str(value))
def test_each_registered_word_reaches_code_by_its_spelling(word, code):
    identifiers = package_identifiers()
    if code == "derived":
        missing = [each.strip() for each in word.split(",") if not derives(each.strip(), identifiers)]
        assert not missing, f"{missing}: no spelling in the package; rename the code or record an exception"
    else:
        exception = code.strip("`")
        assert code.startswith("`") and code.endswith("`"), f"{word}: Code must be —, derived or `<spelling>`"
        assert exception in identifiers or any(path.stem == exception or path.parent.name == exception
                                                for path in PACKAGE), f"{word}: exception {exception} is absent"


@pytest.mark.parametrize("word,identifier,expected", [
    ("hand-out", "Handout", True),
    ("judgment", "judged", True),
    ("acceptance", "accepted", True),
    ("start", "start_run", True),
    ("max attempts", "max-attempts", True),
    ("attempt result", "AttemptResult", True),
    ("handed input", "address", False),
])
def test_the_spelling_rule(word, identifier, expected):
    assert derives(word, {identifier}) is expected

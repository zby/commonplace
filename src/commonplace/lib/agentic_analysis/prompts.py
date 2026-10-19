"""The worker prompt's bindings and the plan's prompt section.

A worker's prompt is the instruction to follow, `name = value` lines and the
prompt section rendered from those values (ADR 117). The layout contributes
the role's identity sources, citations and, for a verifier, the roles it
verifies; the workflow contributes the run's parameters, the reads and the
output paths.
"""

from __future__ import annotations

import re
from collections.abc import Mapping

from commonplace.lib.directory_layout import RUN, Layout
from commonplace.lib.note_parser import parse_document

PLACEHOLDER = re.compile(r"\{([^{}]*)\}")
ABSENT_LINE = "absent"
"""The value the prompt prints for an optional input that is missing."""
CONDITION = re.compile(r"\[([A-Za-z0-9][A-Za-z0-9_-]*)\]")


def layout_bindings(layout: Layout, role: str) -> dict[str, str]:
    """The layout's facts about `role` as prompt bindings.

    `identity` names the fields the role repeats and from which roles, or
    from `run` for fields that must equal the run's values,
    `cites` the roles its references may resolve in, and, for a verifying
    role only, `verifies` the roles its verdict settles.
    """
    declared = layout.roles[role]
    sources = [(source.role, source.fields) for source in declared.identity]
    sources += [(RUN, declared.run_identity)] if declared.run_identity else []
    bindings = {"identity": "; ".join(f"{source}: {', '.join(fields)}" for source, fields in sources) or "none",
                "cites": ", ".join(declared.cites) or "none"}
    if declared.verifies:
        bindings["verifies"] = ", ".join(declared.verifies)
    return bindings


def render_prompt_section(text: str, bindings: Mapping[str, str]) -> str:
    """The plan's prompt section filled from the prompt's own bindings.

    Frontmatter is dropped. A paragraph whose first line is `[<name>]` is
    kept, without that line, only when the prompt binds `<name>` to a value
    other than `absent`. Every `{<name>}` is that variable's value; an
    unknown name raises KeyError.
    """
    document, _ = parse_document(text)
    body = document.body if document is not None else text
    paragraphs = []
    for paragraph in body.strip().split("\n\n"):
        first, _, rest = paragraph.partition("\n")
        condition = CONDITION.fullmatch(first.strip())
        if condition:
            if bindings.get(condition.group(1), ABSENT_LINE) == ABSENT_LINE:
                continue
            paragraph = rest
        paragraphs.append(paragraph)
    return PLACEHOLDER.sub(lambda match: bindings[match.group(1)], "\n\n".join(paragraphs))

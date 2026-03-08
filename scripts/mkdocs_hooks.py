"""MkDocs hook: inject note metadata (status, type) below the first heading."""

import re


def on_page_markdown(markdown: str, page, **kwargs) -> str:
    meta = page.meta
    if not meta:
        return markdown

    status = meta.get("status")
    note_type = meta.get("type")
    if not status and not note_type:
        return markdown

    parts = []
    if note_type:
        parts.append(f"**Type:** {note_type}")
    if status:
        parts.append(f"**Status:** {status}")
    badge_line = " · ".join(parts)

    # Insert after the first heading
    return re.sub(
        r"(^# .+\n)",
        rf"\1\n{badge_line}\n",
        markdown,
        count=1,
        flags=re.MULTILINE,
    )

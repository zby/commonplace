# Small changes

Changes of one or two lines are not staged as file copies (operator direction, 2026-09-25). They live as exact search-and-replace pairs in [`migrations/90_small_edits.py`](./migrations/90_small_edits.py), each with the file, the old and new text, and the reason. `apply.py` runs it last, and it stops if a pair no longer matches exactly once, so the pair can be rebased. Read that file for the list.

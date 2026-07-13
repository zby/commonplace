"""Content hashing for artifact versions.

One artifact version is the SHA-256 of a file's UTF-8 text. Review freshness
hashes note and criterion text with it; packet-owned captures hash their
start-state text with it and compare against the live artifact before a
guarded transition. It lives in `lib` rather than `review` because a version
guard is not review machinery.

Hash the decoded text, never the raw bytes: a caller that has text in hand
(a capture already read into memory) and a caller that has only a path must
agree on the version of the same content.
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


def content_sha256_for_text(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def file_content_sha256(path: Path) -> str:
    return content_sha256_for_text(path.read_text(encoding="utf-8"))

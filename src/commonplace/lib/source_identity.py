"""One normalized form for a source identity (a repository URL or other name)."""

from __future__ import annotations

from urllib.parse import urlsplit, urlunsplit


def normalize_source_identity(identity: str) -> str:
    """One form of a source identity: surrounding whitespace, a trailing ``/``
    and a trailing ``.git`` removed, and a URL's scheme and host lowercased.

    It decides only between forms of one identity, not whether two different
    URLs name one repository.
    """
    value = identity.strip().rstrip("/").removesuffix(".git")
    parts = urlsplit(value)
    if not (parts.scheme and parts.netloc):
        return value
    user, at, host = parts.netloc.rpartition("@")
    return urlunsplit(parts._replace(netloc=f"{user}{at}{host.lower()}"))

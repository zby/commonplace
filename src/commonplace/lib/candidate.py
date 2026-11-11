"""Draft outside the library, publish only what was accepted.

A workflow that replaces a library artifact writes its draft, the candidate, in
an ignored working directory. The artifact at the destination, the incumbent,
stays untouched while the candidate is drafted, checked and repaired, so a
failed or abandoned run needs no restoration. Two operations make that safe:

- ``validate_at_destination`` judges candidate bytes as if they were already at
  the destination, so links and name-paired files resolve from the real path.
- ``publish_candidate`` copies the candidate to the destination only if the
  incumbent is still the one the work started from.

Working-directory layout and acceptance rules belong to each workflow.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from commonplace.lib.snapshot import snapshot_sha256
from commonplace.lib.validation import CheckResults, ValidationRun


class PublicationRefused(Exception):
    """The destination was left as it was."""


def exact_sha256(path: Path) -> str | None:
    """Lowercase SHA-256 of a file's exact bytes, or None when it does not exist."""
    return snapshot_sha256(path) if path.is_file() else None


def validate_at_destination(
    candidate: bytes, destination: Path, *, repo_root: Path
) -> CheckResults | None:
    """Validate candidate bytes in place of the destination's content, without writing."""
    destination = destination.resolve()
    outcome = ValidationRun(
        repo_root=repo_root,
        paths=(destination,),
        content_overrides={destination: candidate},
    ).evaluate()
    return outcome.results.get(destination)


def publish_candidate(
    candidate: Path, destination: Path, *, expected_incumbent_sha256: str | None
) -> str:
    """Copy the candidate over the destination and return the published hash.

    ``expected_incumbent_sha256`` is the destination's hash when the work
    began, or None when the destination did not exist. A destination that
    changed since then is not overwritten: the candidate was drafted and
    checked against a different incumbent.
    """
    current = exact_sha256(destination)
    if current != expected_incumbent_sha256:
        before = expected_incumbent_sha256 or "no file"
        raise PublicationRefused(
            f"{destination} changed since the work began "
            f"(expected {before}, found {current or 'no file'})"
        )
    candidate_sha256 = exact_sha256(candidate)
    if candidate_sha256 is None:
        raise PublicationRefused(f"candidate {candidate} does not exist")
    shutil.copyfile(candidate, destination)
    published = exact_sha256(destination)
    if published != candidate_sha256:
        raise PublicationRefused(
            f"{destination} hashes to {published} after the copy, expected {candidate_sha256}"
        )
    return candidate_sha256

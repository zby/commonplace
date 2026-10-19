"""The analysis's code-job handlers for the artifact-run engine.

These are the engine-facing adapters: each reads its ``CodeAttempt`` and
calls the plain-value function of the same name, which is the domain code.
Later extractions add their adapters here.
"""

from __future__ import annotations

import json

from commonplace.artifactrun import CodeAttempt
from commonplace.artifactrun.handlers import criterion_bytes
from commonplace.lib.agentic_analysis import opening, publication

# The engine finds a handler's reset hook as its sibling ``reset_<handler>``.
reset_publish_analysis = publication.reset_publish_analysis


def open_analysis(attempt: CodeAttempt) -> dict[str, bytes]:
    return {"metadata": opening.open_analysis(
        attempt.parameters, attempt.read("worker-profiles"), attempt.run_dir, attempt.library,
    )}


def acquire_analysis(attempt: CodeAttempt) -> dict[str, bytes]:
    return {"source": opening.acquire_analysis(attempt.read("metadata"), attempt.run_dir)}


def _members(attempt: CodeAttempt, *, overview: bool) -> dict[str, bytes]:
    """The present role members by role, with or without the overview."""
    return {role: data for role in attempt.layout.roles
            if (overview or role != "overview") and (data := attempt.read(role)) is not None}


def _provenance(attempt: CodeAttempt, members: dict[str, bytes]) -> dict[str, publication.Provenance]:
    """Each model member's producer record, which must be its filler's model attempt."""
    provenance = {}
    for role in members:
        if role == "overview":
            continue  # Code-written, never a model worker.
        data = attempt.read(f"{role}-attempt")
        if data is None:
            raise ValueError(f"{role} producer attempt requires a declared present input")
        record = json.loads(data)
        if not isinstance(record, dict):
            raise TypeError(f"{role} producer attempt must be an object")
        filler = attempt.filler(role)
        digest = record.get("outputs", {}).get(filler.outputs[0])
        if record.get("kind") != "model" or record.get("job") != filler.name or not isinstance(digest, str):
            raise ValueError(f"{role} provenance does not identify its completed output")
        # The engine records only the worker-reported model; the adapter goes with the engine.
        provenance[role] = publication.Provenance(model=record.get("worker_model"), output_sha256=digest)
    return provenance


def assemble_analysis(attempt: CodeAttempt) -> dict[str, bytes]:
    members = _members(attempt, overview=False)
    overview, manifest = publication.assemble_analysis(
        members, metadata=attempt.read("metadata"), source=attempt.read("source"),
        provenance=_provenance(attempt, members), layout=attempt.layout, type_spec=attempt.type_spec,
        criteria=criterion_bytes(attempt), run_dir=attempt.run_dir,
    )
    scope = tuple(relation for origin, partner, relation in attempt.relations
                  if "overview" in (origin, partner)
                  and (partner if origin == "overview" else origin) in members)
    attempt.judge("overview", outcome="accepted", scope=scope)
    return {"overview": overview, "manifest": manifest}


def publish_analysis(attempt: CodeAttempt) -> dict[str, bytes]:
    # Reading the pinned inputs is a preliminary check like publication's own.
    with publication.preliminary_checks(attempt.run_dir):
        members = _members(attempt, overview=True)
        pinned = {"metadata": attempt.read("metadata"), "source": attempt.read("source"),
                  "provenance": _provenance(attempt, members), "manifest": attempt.read("manifest"),
                  "criteria": criterion_bytes(attempt)}
    return {"receipt": publication.publish_analysis(
        members, **pinned, layout=attempt.layout, type_spec=attempt.type_spec,
        run_dir=attempt.run_dir, library=attempt.library,
    )}

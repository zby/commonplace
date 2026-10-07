"""Opt-in migration skeleton for the analysis job set, not a live workflow.

Build a declaration against the shipped analysis contracts without modifying
those contracts or dispatching workers. All code jobs fail closed. This lets
contract tests exercise the real graph before opening/acquisition, checks,
verdict application, run-state projection and publication are ported.

The eventual declaration belongs beside the job instructions. This builder
only supplies absolute file addresses for a caller-selected library and run;
it neither allocates a run nor substitutes for the engine's scheduler.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from commonplace.lib.agentic_set import SET_TYPE
from commonplace.lib.directory_layout import Layout, parse_layout
from commonplace.lib.note_parser import parse_document

METHOD = "agentic-system-analyses/instructions/analyse-agentic-system/jobs"
REPORTS = ("runtime", "memory", "epistemic")
RECORDS = (*REPORTS, "reconciliation")
MODEL_ROLES = {
    "boundary": "boundary",
    "runtime": "runtime",
    "memory": "memory",
    "epistemic": "epistemic",
    "reconcile": "reconciliation",
    "verify": "record-verification",
    "profile": "memory-profile",
    "verify-profile": "profile-verification",
    "synthesize": "synthesis",
    "verify-synthesis": "synthesis-verification",
}
PRIMARY = {
    "boundary": "boundary", "runtime": "report", "memory": "report", "epistemic": "report",
    "reconcile": "reconciliation", "verify": "verification", "profile": "profile",
    "verify-profile": "verification", "synthesize": "synthesis", "verify-synthesis": "verification",
}
HANDLER = "commonplace.lib.agentic_job_set.unported"


def unported(_attempt):
    """Never turn a migration placeholder into a successful attempt."""
    raise NotImplementedError(
        "analysis job-set migration skeleton: code handlers are not ported; "
        "do not launch workers or publish from this declaration"
    )


def _layout(library: Path) -> Layout:
    document, error = parse_document((library / SET_TYPE).read_text(encoding="utf-8"))
    if document is None or error:
        raise ValueError(f"cannot read analysis set type: {error}")
    return parse_layout(document.frontmatter["layout"], where=SET_TYPE)


def declaration(library: Path, run_dir: Path) -> str:
    """Return the proposed graph as YAML, with explicitly selected file bases.

    This is a contract skeleton, not permission to use the current worker
    instructions with new-engine hand-outs. In particular, correction rounds,
    untracked runtime context, disposition gating and verdict relations still
    need the changes reported by :func:`contract_gaps`.
    """
    library, run_dir = library.resolve(), run_dir.resolve()
    layout = _layout(library)
    jobs = []

    def address(kind, source, required=True, **extra):
        return {"address": kind, "source": source, "required": required, **extra}

    def file(path):
        return address("file", str(path))

    def member(role, required=True):
        return address("member", role, required)

    def output(name, key=None, required=True):
        return address("output", f"{name}:{key or PRIMARY[name]}", required)

    def code(name, inputs, outputs=(), role=None):
        job = {"name": name, "kind": "code", "handler": HANDLER,
               "inputs": inputs, "outputs": list(outputs)}
        if role is not None:
            job["role"] = role
        jobs.append(job)

    def verified(role, verifier):
        return address("judgment", role, relation=f"{verifier}:cites:{role}", outcome="accepted")

    def model(name, inputs, bound=3):
        role = MODEL_ROLES[name]
        contracts = {
            "instruction": file(library / METHOD / f"{name}.md"),
            "worker-rules": file(library / METHOD / "worker-rules.md"),
            "collection": file(library / "agentic-system-analyses/COLLECTION.md"),
            "member-type": file(library / layout.roles[role].type),
            "set-type": file(library / SET_TYPE),
            "sources-contract": file(library / "agentic-system-analyses/instructions/agentic-analysis-sources.md"),
            "records-contract": file(library / "agentic-system-analyses/instructions/agentic-analysis-records.md"),
            "boundary-contract": file(library / "agentic-system-analyses/instructions/agentic-analysis-boundary.md"),
        }
        judged_roles = RECORDS if name in ("reconcile", "verify") else ()
        if name == "verify-profile":
            judged_roles = ("memory-profile",)
        elif name == "verify-synthesis":
            judged_roles = ("synthesis",)
        contracts.update({f"{other}-type": file(library / layout.roles[other].type) for other in judged_roles})
        outputs = [PRIMARY[name], *(["answers"] if name in REPORTS else [])]
        jobs.append({
            "name": name, "kind": "model", "role": role, "instruction": "instruction",
            "bound": bound, "outputs": outputs,
            "inputs": {**contracts, **inputs, "refusal": address("refusal", name, False)},
            "parameters": {"system": "{param:system}", "run-state": "{run}/run-state.md",
                           "validation-set": "{set}", "validation-member": layout.path(role)},
        })

    def check(name):
        role = MODEL_ROLES[name]
        partners = {source.role for source in layout.roles[role].identity}
        partners.update(layout.roles[role].cites)
        partners.discard(role)
        inputs = {
            "candidate": output(name),
            "metadata": address("output", "open:metadata"),
            "producer-attempt": address("attempt", name),
            "answered-refusal": address("handed", "producer-attempt:refusal", False),
            "member-type": file(library / layout.roles[role].type),
            "set-type": file(library / SET_TYPE),
            **{partner: member(partner, partner == "boundary") for partner in sorted(partners)},
        }
        if name == "boundary":
            inputs["source"] = address("output", "acquire:source")
        if name in REPORTS:
            inputs["answers"] = output(name, "answers", False)
        code(f"check-{name}", inputs)

    def apply(name):
        role = MODEL_ROLES[name]
        model_job = next(job for job in jobs if job["name"] == name)
        seen = [key for key, spec in model_job["inputs"].items() if spec["address"] == "member"]
        code(f"apply-{name}", {
            "candidate": output(name),
            "verifier-attempt": address("attempt", name),
            "member-type": file(library / layout.roles[role].type),
            "set-type": file(library / SET_TYPE),
            **{f"{subject}-seen": address("handed", f"verifier-attempt:{subject}") for subject in seen},
        })

    code("open", {"request": file(run_dir / "run.json")}, ["metadata"])
    code("acquire", {"metadata": address("output", "open:metadata")}, ["source"])
    model("boundary", {"opening": address("output", "open:metadata"),
                       "source": address("output", "acquire:source")}, bound=2)
    check("boundary")
    for name in REPORTS:
        model(name, {"boundary": member("boundary")})
        check(name)
    model("reconcile", {role: member(role) for role in ("boundary", *REPORTS)})
    check("reconcile")
    model("verify", {**{role: member(role) for role in ("boundary", *RECORDS)},
                     **{f"{name}-answers": output(name, "answers", False) for name in REPORTS}})
    apply("verify")
    gates = {f"{role}-verified": verified(role, "record-verification") for role in RECORDS}
    model("profile", {**{role: member(role) for role in ("boundary", *RECORDS)}, **gates})
    check("profile")
    model("verify-profile", {**{role: member(role) for role in ("boundary", *RECORDS)},
                             "profile": member("memory-profile")})
    apply("verify-profile")
    model("synthesize", {
        **{role: member(role) for role in ("boundary", *RECORDS, "memory-profile",
                                         "record-verification", "profile-verification")},
        **gates, "profile-verified": verified("memory-profile", "profile-verification"),
    }, bound=2)
    check("synthesize")
    model("verify-synthesis", {role: member(role) for role in (
        "boundary", *RECORDS, "synthesis", "record-verification", "profile-verification",
    )}, bound=2)
    apply("verify-synthesis")
    # Coverage can be held by an acceptance at either end. These optional
    # records are currency inputs, not an all-required readiness gate: a
    # non-complete disposition has fewer relations. The eventual handlers
    # must enforce whole-set coverage before assembly/publication.
    coverage = {}
    for origin, spec in layout.roles.items():
        relations = [("cites", partner) for partner in spec.cites]
        relations += [("identity", source.role) for source in spec.identity]
        for kind, partner in relations:
            if origin == partner:
                continue
            for subject in (origin, partner):
                coverage[f"coverage-{origin}-{kind}-{partner}-{subject}"] = address(
                    "judgment", subject, False, relation=f"{origin}:{kind}:{partner}", outcome="accepted",
                )
    common = {"metadata": address("output", "open:metadata"),
              "set-type": file(library / SET_TYPE)}
    code("assemble", {
        **common, "overview-type": file(library / layout.roles["overview"].type),
        **{role: member(role, role == "boundary") for role in layout.roles if role != "overview"},
        **{key: spec for key, spec in coverage.items() if not key.startswith("coverage-overview-")},
    }, ["overview"], "overview")
    code("publish", {
        **common, "manifest": file(run_dir / "set/ARTIFACT.yaml"),
        **{role: member(role, role in ("boundary", "overview")) for role in layout.roles}, **coverage,
    })
    return yaml.safe_dump({"type_spec": SET_TYPE, "jobs": jobs}, sort_keys=False)


def contract_gaps(library: Path) -> tuple[str, ...]:
    """Name adoption blockers visible in the shipped layout, not engine defects."""
    layout = _layout(library)
    gaps = [
        "working set path: consumers use output/, the new engine uses set/",
        "worker protocol: port read-first ordering, input names, round/requests/answers and previous-output parameters",
        "runtime context: order the first memory/epistemic jobs without making runtime a rerun trigger",
        "run-state: project new-engine attempts/stops and uncertain external effects",
        "publication: gate on holding acceptances, preserve incumbent checks and effect recovery",
        "handlers: opening/acquisition, member checks, verdict application and assembly remain unported",
        "check criteria: declare schema/shared-contract dependency closure for validators",
        "coverage: assembly/publication handlers must enforce disposition-dependent whole-set coverage",
        "memory provenance: implement the workflow check promised by the set type or remove the promise",
    ]
    if layout.required.by_role != "boundary":
        gaps.append("disposition: the layout discriminator must be available before overview assembly")
    for verifier, subjects in (
        ("record-verification", RECORDS),
        ("profile-verification", ("memory-profile",)),
        ("synthesis-verification", ("synthesis",)),
    ):
        for subject in subjects:
            if subject not in layout.roles[verifier].cites:
                gaps.append(f"missing verdict relation: {verifier}:cites:{subject}")
    gaps.append("set relations: decide how overview amendment-index and synthesis limit checks enter coverage")
    return tuple(gaps)

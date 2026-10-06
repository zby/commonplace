"""The analyse-agentic-system workflow as a code-scheduled definition.

Start a run with

    commonplace-workflow start commonplace.lib.agentic_workflow:AnalyseAgenticSystem \\
        --param system=<name> --param source-identity=<identity> \\
        --param source=<the caller's source input>

from the prepared worktree root. `start` allocates the run ID,
AAS-<date>-<system slug>-<worktree token>-<nn> (the slug from the source
identity's last path segment, or the system name), creates the run directory under
`kb/agentic-system-analyses/state/`, and prints it; the run ID is the directory's
name. Each job's task is an instruction file under
`kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs/`, declared as an
input, so a change to it reopens the job. The job split
is defined by those job instructions and their declared dependencies.

Opening, acquisition and publication are effects: opening records values
that cannot be reproduced (the method commit, the run date, the incumbent's
digest), acquisition freezes a GitHub source's checkout outside the run, and
publication changes the repository outside the run. Everything else code does
is replayed from the run's files in every step.
"""

from __future__ import annotations

import datetime
import difflib
import json
import os
import re
import subprocess
import sys
from collections import Counter
from collections.abc import Callable, Mapping, Sequence
from dataclasses import replace
from functools import partial
from hashlib import sha256
from pathlib import Path
from typing import Any

import yaml
from jsonschema import FormatChecker

from commonplace.lib.agentic_analysis import (
    parse_agentic_analysis_run_state,
    verify_quote_anchors,
)
from commonplace.lib.agentic_checkout import freeze_checkout, github_checkout_path
from commonplace.lib.agentic_finalize import build_manifest
from commonplace.lib.agentic_publication import (
    PublicationSpec,
    atomic_write,
    inspect_destination,
    publish_publication,
    require_publishable_worktree,
    require_running_package_unchanged,
)
from commonplace.lib.agentic_records import (
    amendment_index,
    declared_ids,
    record_declaration,
    record_references,
    section,
    set_record_errors,
    source_register_ids,
    source_register_rows,
    value_amendments,
)
from commonplace.lib.agentic_set import (
    OUTPUT_DIR,
    OVERVIEW_NAME,
    RECORD_MEMBER_NAMES,
    RETAINED_ROOT,
    RUN_ID,
    normalize_source_identity,
    source_slug,
)
from commonplace.lib.analysis_worktree import preparation_for
from commonplace.lib.note_parser import parse_document
from commonplace.lib.quote_matching import ranged_prose_anchors
from commonplace.lib.validation import agentic_set_member_link_failures, validate_note
from commonplace.workflow import (
    Blocked,
    Done,
    Job,
    Launch,
    Recognition,
    StepResult,
    StopRun,
    Uncertain,
    Workflow,
)

JOBS = "kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs"
STATE_ROOT = Path("kb/agentic-system-analyses/state")
OVERVIEW_TYPE = "agentic-system-analyses/types/agentic-system-analysis-overview.md"
RUN_STATE_TYPE = "agentic-system-analyses/types/agentic-system-analysis-run-state.md"
# Shared contracts and member types, relative to the job instructions.
# Analysts load shared definitions plus their own member type. Only jobs
# judging records need the analyst types and reconciliation type.
TYPES = "../../../types"
BOUNDARY_CONTRACT = "../../agentic-analysis-boundary.md"
SOURCES_CONTRACT = "../../agentic-analysis-sources.md"
RECORDS_CONTRACT = "../../agentic-analysis-records.md"
OVERVIEW_CONTRACT = f"{TYPES}/agentic-system-analysis-overview.md"
RUNTIME_CONTRACT = f"{TYPES}/agentic-system-runtime-report.md"
PROFILE_CONTRACT = f"{TYPES}/agent-memory-profile.md"
MEMORY_CONTRACT = f"{TYPES}/agent-memory-analysis-report.md"
EPISTEMIC_CONTRACT = f"{TYPES}/agentic-system-epistemic-report.md"
RECONCILIATION_CONTRACT = f"{TYPES}/agentic-system-reconciliation-report.md"
VERIFICATION_CONTRACT = f"{TYPES}/agentic-system-verification.md"
SYNTHESIS_CONTRACT = f"{TYPES}/agentic-system-synthesis.md"
VERIFICATION_TYPE = "agentic-system-analyses/types/agentic-system-verification.md"
RECORD_CONTRACTS = (
    SOURCES_CONTRACT,
    RECORDS_CONTRACT,
    RUNTIME_CONTRACT,
    MEMORY_CONTRACT,
    EPISTEMIC_CONTRACT,
    RECONCILIATION_CONTRACT,
)
SYNTHESIS_CONTRACTS = (SOURCES_CONTRACT, RECORDS_CONTRACT, OVERVIEW_CONTRACT, SYNTHESIS_CONTRACT)

OPENING = "opening.json"
RUN_METADATA = "run-metadata.json"
FROZEN_SOURCE = "source.json"
BOUNDARY = "boundary.md"
RUN_STATE = "run-state.md"
RUNTIME = f"{OUTPUT_DIR}/runtime.md"
MEMORY = f"{OUTPUT_DIR}/memory.md"
PROFILE = f"{OUTPUT_DIR}/memory-profile.md"
EPISTEMIC = f"{OUTPUT_DIR}/epistemic.md"
RECONCILIATION = f"{OUTPUT_DIR}/reconciliation.md"
OVERVIEW = f"{OUTPUT_DIR}/{OVERVIEW_NAME}"
MANIFEST = f"{OUTPUT_DIR}/ARTIFACT.yaml"

DISPOSITIONS = ("complete", "blocked", "out-of-scope")
BOUNDARY_FIELDS = (
    "target-class",
    "boundary-kind",
    "reviewed-boundary",
    "analysis-cutoff",
    "evidence-tier",
)
SOURCE_FIELDS = ("kind", "identity", "revision", "path", "sha256")
ANALYST_SPECS: dict[str, dict[str, Any]] = {
    "runtime": {"prefix": "RT-", "contract": RUNTIME_CONTRACT, "reads": ()},
    "memory": {"prefix": "MEM-", "contract": MEMORY_CONTRACT, "reads": ("runtime",)},
    "epistemic": {"prefix": "EPI-", "contract": EPISTEMIC_CONTRACT, "reads": ("runtime",)},
}
"""The analysts: the ID prefix each declares, the type its report follows,
and the analysts whose reports it reads in its first round. `reads` also
orders the work: an analyst runs after the analysts it reads."""
ANALYSTS = tuple(ANALYST_SPECS)
ADDRESSEES = (*ANALYSTS, "reconciliation")
"""Who a record-verification blocker can be addressed to."""
CURRENT = {"runtime": RUNTIME, "memory": MEMORY, "epistemic": EPISTEMIC}
"""Where the current version of each analyst report is in the output set."""
DECLARING = {spec["prefix"]: member for member, spec in ANALYST_SPECS.items()}
ANSWERS_NAME = "answers.md"
"""What a correcting analyst writes beside its report, in its job workspace."""
READ_BATCH_BYTES = 24 * 1024
"""Shared byte budget for input batches and line ranges.

Keep below the harness's tool-result delivery limit, leaving room for wrappers.
Change this constant to tune both grouping and range hints together. Workers
must still recover actual truncation; the budget is not a delivery guarantee.
"""


def reading_batches(paths: Sequence[str]) -> list[list[str]]:
    """Suggest bounded reads without copying files or changing dependencies.

    Oversized or not-yet-produced inputs are read separately, in ranges.
    """
    batches: list[list[str]] = []
    batch: list[str] = []
    size = 0
    for path in paths:
        file = Path(path)
        count = file.stat().st_size if file.is_file() else READ_BATCH_BYTES + 1
        if batch and size + count > READ_BATCH_BYTES:
            batches.append(batch)
            batch, size = [], 0
        if count > READ_BATCH_BYTES:
            batches.append([f"{path} — read in bounded ranges"])
        else:
            batch.append(path)
            size += count
    if batch:
        batches.append(batch)
    return batches


def reading_ranges(path: Path) -> list[tuple[int, int]]:
    """Line ranges fitting the read budget; an oversized line stands alone."""
    ranges = []
    start = 1
    size = 0
    end = 0
    with path.open("rb") as source:
        for end, line in enumerate(source, 1):
            if size and size + len(line) > READ_BATCH_BYTES:
                ranges.append((start, end - 1))
                start, size = end, 0
            size += len(line)
    if end:
        ranges.append((start, end))
    return ranges


def report(member: str, round_: int) -> str:
    """One version of an analyst report. Versions are never overwritten."""
    return f"{member}-report-{round_}.md"


def requests(member: str, round_: int) -> str:
    """The blockers one analyst answers in a correction round, with the
    records they cite from other reports."""
    return f"{member}-requests-{round_}.md"


def answers(member: str, round_: int) -> str:
    """The analyst's answers to the blockers that version responds to."""
    return f"{member}-answers-{round_}.md"


def changes(member: str, round_: int) -> str:
    """The text difference between a version and its predecessor."""
    return f"{member}-changes-{round_}.md"


def reconciliation(round_: int) -> str:
    return f"reconcile-{round_}.md"


def round_file(kind: str, round_: int) -> str:
    """One round's check, verification or synthesis output."""
    return f"{kind}-{round_}.md"


# Reading job outputs


def split(text: str) -> tuple[dict[str, Any], str]:
    """Frontmatter and body of a Markdown file; ValueError when it does not parse."""
    document, error = parse_document(text)
    if error is not None or document is None:
        raise ValueError(error or "cannot parse the file")
    return dict(document.frontmatter or {}), document.body


def headings(body: str, level: int) -> list[str]:
    marker = "#" * level
    return re.findall(rf"(?m)^{marker} (.+?)[ \t]*$", body)


def subsection(body: str, title: str) -> str:
    """The text under one level-three heading, or empty when it is absent."""
    match = re.search(rf"(?ms)^### {re.escape(title)}[ \t]*\n(.*?)(?=^##+ |\Z)", body)
    return match[1].strip() if match else ""


def require_sections(body: str, level: int, wanted: Sequence[str]) -> list[str]:
    present = headings(body, level)
    marker = "#" * level
    refusals = [
        f"missing section `{marker} {title}`"
        for title in wanted
        if title not in present
    ]
    refusals += [
        f"section `{marker} {title}` is empty"
        for title in wanted
        if title in present
        and not (
            section(body, title) if level == 2 else subsection(body, title)
        ).strip()
    ]
    return refusals


def overview_enums(repo_root: Path) -> dict[str, list[Any]]:
    """The allowed values of the boundary fields, from the overview schema."""
    schema = yaml.safe_load(
        (repo_root / "kb/agentic-system-analyses/types/agentic-system-analysis-overview.schema.yaml").read_text(
            encoding="utf-8"
        )
    )
    found: dict[str, list[Any]] = {}

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            properties = node.get("properties")
            if isinstance(properties, dict):
                for name, spec in properties.items():
                    if (
                        name in BOUNDARY_FIELDS
                        and isinstance(spec, dict)
                        and "enum" in spec
                    ):
                        found.setdefault(name, list(spec["enum"]))
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(schema)
    return found


def boundary_refusals(
    path: Path, *, enums: dict[str, list[Any]], identity: str,
    frozen: dict[str, Any] | None = None,
) -> list[str]:
    try:
        fields, body = split(path.read_text(encoding="utf-8"))
    except ValueError as error:
        return [f"boundary.md does not parse: {error}"]
    refusals = []
    expected = {"result-disposition", *BOUNDARY_FIELDS, "source"}
    if set(fields) != expected:
        refusals.append(
            "the frontmatter must have exactly these fields: "
            + ", ".join(sorted(expected))
        )
    disposition = fields.get("result-disposition")
    if disposition not in DISPOSITIONS:
        refusals.append(f"result-disposition must be one of {', '.join(DISPOSITIONS)}")
    for name, allowed in enums.items():
        value = fields.get(name)
        if value is not None and value not in allowed:
            refusals.append(
                f"{name} {value!r} is not one of the overview type's values; use one of {allowed!r}"
            )
    refusals += [
        f"{name} must be a quoted string or null, not {type(fields[name]).__name__}"
        for name in BOUNDARY_FIELDS
        if fields.get(name) is not None and not isinstance(fields[name], str)
    ]
    cutoff = fields.get("analysis-cutoff")
    if isinstance(cutoff, str) and not FormatChecker().conforms(cutoff, "date"):
        refusals.append("analysis-cutoff must be a valid quoted YYYY-MM-DD date")
    source = fields.get("source")
    if source is not None and (
        not isinstance(source, dict) or set(source) != set(SOURCE_FIELDS)
    ):
        refusals.append(
            "source must be null or a mapping of " + ", ".join(SOURCE_FIELDS)
        )
    elif source is not None:
        if source.get("identity") != identity:
            refusals.append(
                f"source.identity must be `{identity}`, the run's source identity"
            )
        if frozen is not None and (
            source != frozen or fields.get("reviewed-boundary") != frozen["revision"]
        ):
            refusals.append(
                "source must be exactly the checkout code froze, and reviewed-boundary "
                f"its commit `{frozen['revision']}`: {json.dumps(frozen)}"
            )
        refusals += frozen_source_refusals(source)
        refusals += source_register_refusals(body, source=frozen or source)
    wanted = ["Boundary and evidence", "Source register"]
    if disposition == "complete":
        missing = [
            name for name in (*BOUNDARY_FIELDS, "source") if fields.get(name) is None
        ]
        if missing:
            refusals.append("a complete disposition needs " + ", ".join(missing))
    elif disposition in DISPOSITIONS:
        wanted.append("Not reached")
    refusals += require_sections(body, 2, wanted)
    refusals += [
        f"duplicate source declaration: {identifier}; keep one row per source ID "
        "and separate evidence layers and scopes within that row"
        for identifier, count in Counter(source_register_ids(body)).items() if count > 1
    ]
    return refusals


def source_register_refusals(body: str, *, source: dict[str, Any]) -> list[str]:
    """The register declares the source whose identity the run can verify."""
    rows = source_register_rows(body)
    expected = tuple(str(source.get(field) or "") for field in ("kind", "identity", "revision"))
    refusals = [
        f"source register: {row[0]} needs all eight columns from the boundary contract"
        for row in rows if len(row) != 8
    ]
    if not any(
        len(row) == 8 and tuple(cell.strip("`") for cell in row[1:4]) == expected
        for row in rows
    ):
        refusals.append(
            "source register must declare the frozen source in a SRC-* row: "
            f"kind `{expected[0]}`, identity `{expected[1]}`, revision or capture `{expected[2]}`"
        )
    return refusals


def frozen_source_refusals(source: dict[str, Any]) -> list[str]:
    """The frozen source is what later jobs read: a Git checkout whose files
    are exactly the recorded commit's, or a capture file with its digest."""
    path = Path(str(source.get("path") or ""))
    if not path.is_absolute():
        return ["source.path must be the absolute path of the frozen source"]
    if source.get("kind") == "capture":
        if not path.is_file():
            return [f"source.path {path} is not a file"]
        if source.get("sha256") != digest(path):
            return [f"source.sha256 must be the SHA-256 of the capture file: expected {digest(path)}"]
        return []
    revision = str(source.get("revision") or "")
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        return ["source.revision must be a full 40-hex commit"]

    def git(*args: str) -> str | None:
        result = subprocess.run(
            ["git", "-C", str(path), *args],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout if result.returncode == 0 else None

    head = git("rev-parse", "HEAD") if path.is_dir() else None
    if head is None:
        return [f"source.path {path} is not a Git checkout"]
    if head.strip() != revision:
        return [f"the checkout at {path} is not at source.revision"]
    if git("status", "--porcelain"):
        return [
            (
                f"the checkout at {path} does not hold exactly the commit's files; "
                "a clone made without checkout lists them all as deleted"
            )
        ]
    return []


def member_refusals(path: Path, *, repo_root: Path) -> list[str]:
    return list(validate_note(path, repo_root=repo_root).fails)


def refusal_rule(reason: str) -> str:
    """Stable rule names for advice and per-job measurements, not locations."""
    for phrase, rule in (
        ("quotation ambiguous", "quotation uniqueness"),
        ("quotation not found", "quotation occurrence"),
        ("quote-anchored citation", "quotation source"),
        ("unresolved record", "record reference"),
        ("identity", "member identity"),
        ("route fields", "route fields"),
        ("epistemic ledger", "epistemic ledger"),
        ("conclusion status", "conclusion status"),
        ("record", "record contract"),
        ("source", "source identity"),
        ("frontmatter", "frontmatter"),
        ("parse", "document parsing"),
    ):
        if phrase in reason:
            return rule
    return "job contract"


def actionable_refusals(validator: Callable[[Path], Sequence[str]], path: Path) -> list[str]:
    """Address the same mechanical findings to either caller, never edit output."""
    try:
        reasons = validator(path)
    except (OSError, ValueError, KeyError) as error:
        reasons = [f"validation input: {error}; correct malformed output or report a missing supplied input to the coordinator"]
    repairs = {
        "unresolved record": "check the named declaration and use its full ID; reconsider the reference if no declaration supports it",
        "duplicate": "keep one declaration or field per identity; give distinct records distinct names",
        "missing field": "supply the named field in that record with an answer or an explicit reason it is uninspected or inapplicable",
        "empty field": "supply a substantive answer in the named field",
        "does not match": "replace the named identity field with the expected run value shown",
        "invalid value": "write exactly one listed value in each named field, with no trailing punctuation or added text",
        "invalid route function": "use a registered route function, or 'other — description'",
        "invalid architectural status": "use a registered architectural status from the epistemic contract",
        "structural failures require": "write the supplied structural failures as explicit blockers",
    }
    findings = []
    # An identical reason repeated adds nothing the analyst can act on.
    for reason, count in Counter(reasons).items():
        if count > 1:
            reason += f" ({count} identical findings)"
        repair = next((value for key, value in repairs.items() if key in reason),
                      "correct the named field, section or citation to satisfy the stated rule and the supplied job/type contract")
        rule = refusal_rule(reason)
        findings.append(f"{path.name}: rule {rule}: {reason}\nRepair: {repair}")
    return findings


def set_bodies(
    *, boundary: Path, reconciled: Path | None = None, **members: Path
) -> dict[str, str]:
    """The bodies of the set these files make, by set name.

    The boundary supplies the overview's Source register, without requiring
    a rendered overview. Each member keyword names a file without its `.md`.
    """
    _, boundary_body = split(boundary.read_text(encoding="utf-8"))
    bodies = {OVERVIEW_NAME: boundary_body}
    if reconciled is not None:
        bodies["reconciliation.md"] = split(reconciled.read_text(encoding="utf-8"))[1]
    for name, path in members.items():
        bodies[f"{name}.md"] = split(path.read_text(encoding="utf-8"))[1]
    return bodies


def reference_refusals(bodies: Callable[[], dict[str, str]]) -> list[str]:
    """Every record the bodies cite is declared once among them."""
    try:
        found = bodies()
    except (ValueError, OSError) as error:
        return [f"a set document does not parse: {error}"]
    _, errors = set_record_errors(found)
    return errors


def pass_refusals(
    path: Path, *, repo_root: Path, run_state: Path, boundary: Path,
    declaration_prefix: str,
    bodies: Callable[[Path], dict[str, str]],
) -> list[str]:
    """The output of an analyst, which declares records: a valid member whose
    record references resolve against the set so far and whose quotations
    resolve against the frozen source."""
    refusals = member_refusals(path, repo_root=repo_root)
    refusals += reference_refusals(partial(bodies, path))
    try:
        # Read the run's identity and source without validating its published
        # artifact: a replay of a complete run passes through earlier report
        # versions in output/, which the final manifest does not pin.
        document, error = parse_document(run_state.read_text(encoding="utf-8"))
        if error is not None or document is None:
            raise ValueError(f"run state does not parse: {error}")
        state = parse_agentic_analysis_run_state(run_state, document, repo_root=repo_root)
        metadata, _ = split(path.read_text(encoding="utf-8"))
        boundary_fields, _ = split(boundary.read_text(encoding="utf-8"))
    except (ValueError, OSError) as error:
        return refusals + [str(error)]
    refusals += identity_refusals(metadata, run_id=state.run_id, boundary_fields=boundary_fields)
    wrong_prefix = [
        identifier for identifier in declared_ids(path.read_text(encoding="utf-8"))
        if not identifier.startswith(declaration_prefix)
    ]
    if wrong_prefix:
        refusals += [
            f"record declarations: this analyst must use {declaration_prefix}: "
            + ", ".join(wrong_prefix)
            + "; keep supplied IDs unchanged in references and annotations"
        ]
    source = state.source
    if source is None:
        return refusals + ["quotation checks require a registered frozen source; report the missing source to the coordinator"]
    _, failures = verify_quote_anchors(path.read_text(encoding="utf-8"), source=source)
    return refusals + failures


def identity_refusals(metadata: Mapping[str, Any], *, run_id: str, boundary_fields: Mapping[str, Any]) -> list[str]:
    """A set member names the run and the frozen boundary it belongs to."""
    identities = (("run-id", run_id), ("reviewed-boundary", boundary_fields.get("reviewed-boundary")))
    return [
        f"member identity: {field} {metadata.get(field)!r} does not match {expected!r}"
        for field, expected in identities if metadata.get(field) != expected
    ]


def reconcile_refusals(
    path: Path,
    *,
    repo_root: Path,
    run_id: str,
    boundary: Path,
    runtime: Path,
    report: Path,
    epistemic: Path,
) -> list[str]:
    """A valid reconciliation member of this run, with no value amendment, and
    every record it cites declared in the set it will make."""
    refusals = member_refusals(path, repo_root=repo_root)
    try:
        metadata, body = split(path.read_text(encoding="utf-8"))
        boundary_fields, _ = split(boundary.read_text(encoding="utf-8"))
    except (ValueError, OSError) as error:
        return refusals + [str(error)]
    refusals += identity_refusals(metadata, run_id=run_id, boundary_fields=boundary_fields)
    refusals.extend(
        "value amendment: reconciliation states connections between reports and does "
        "not replace a record's value; describe the disagreement with both records and "
        "their evidence, or use `Amendment: <ID> is superseded by <IDs>` for an "
        f"identity judgment: {line[:120]}"
        for line in value_amendments(body)
    )
    refusals.extend(source_anchor_refusals(body))
    return refusals + reference_refusals(
        partial(
            set_bodies,
            boundary=boundary,
            reconciled=path,
            runtime=runtime,
            memory=report,
            epistemic=epistemic,
        )
    )


def blocker_entries(blockers: str) -> list[str]:
    """The first line of each blocker in a `### Blockers` list."""
    return [line for line in blockers.splitlines() if line.startswith("- ")]


def blocker_addressees(blockers: str) -> list[str]:
    """Who each blocker is addressed to, in order; empty for one without an
    addressee. Code routes corrections by this word, not by the blocker's prose."""
    found = []
    for line in blocker_entries(blockers):
        match = re.match(r"- ([a-z]+): \S", line)
        found.append(match[1] if match and match[1] in ADDRESSEES else "")
    return found


def addressee_refusals(blockers: str) -> list[str]:
    return [
        "blocker addressee: start each blocker with `runtime:`, `memory:`, `epistemic:` "
        "or `reconciliation:`, naming the one report whose text must change; write a "
        f"blocker that concerns two reports as two blockers: {line[:120]}"
        for line, addressee in zip(blocker_entries(blockers), blocker_addressees(blockers), strict=True)
        if not addressee
    ]


def correction_refusals(
    path: Path, *, member: str, previous: Path, packet: Path,
) -> list[str]:
    """A corrected report keeps its predecessor's records and answers every
    blocker addressed to it, by a correction or a reason for declining."""
    text = path.read_text(encoding="utf-8")
    dropped = sorted(
        set(declared_ids(previous.read_text(encoding="utf-8"))) - set(declared_ids(text))
    )
    refusals = []
    if dropped:
        refusals.append(
            "record declarations: a corrected report keeps every record its predecessor "
            "declared, because other reports cite them: " + ", ".join(dropped)
            + "; keep the declaration and correct its finding"
        )
    wanted = len(blocker_entries(section(packet.read_text(encoding="utf-8"), "Blockers")))
    answers_path = path.parent / ANSWERS_NAME
    if not answers_path.is_file():
        return [*refusals, (
            f"correction answers: write {ANSWERS_NAME} beside the report, with one "
            "`- corrected: ...` or `- declined: ...` entry per blocker addressed to this report"
        )]
    entries = [line for line in answers_path.read_text(encoding="utf-8").splitlines() if line.startswith("- ")]
    malformed = [line for line in entries if re.match(r"- (corrected|declined): \S", line) is None]
    if malformed or len(entries) != wanted:
        refusals.append(
            f"correction answers: {ANSWERS_NAME} needs exactly {wanted} entries, one per "
            f"blocker addressed to the {member} report, each starting `- corrected: ` or "
            f"`- declined: `; found {len(entries)}"
            + (f", malformed: {malformed[0][:80]}" if malformed else "")
        )
    elif (any(line.startswith("- corrected:") for line in entries)
            and path.read_bytes() == previous.read_bytes()):
        refusals.append(
            "correction answers: an entry says corrected but the report is identical to "
            "its predecessor; change the report or decline the blocker with a reason"
        )
    return refusals


def blocker_texts(blockers: str) -> list[str]:
    """Each blocker with its continuation lines."""
    entries: list[str] = []
    for line in blockers.splitlines():
        if line.startswith("- "):
            entries.append(line)
        elif entries and line.strip():
            entries[-1] += "\n" + line
    return entries


def render_requests(
    member: str, verification: str, blockers: str, bodies: Mapping[str, str],
) -> str:
    """What one analyst needs to answer its blockers: the blockers addressed
    to it, and the current declaration of every record they cite from another
    report, cut by ID. The analyst reads these fragments, not the reports."""
    own = [
        text for text, addressee in zip(blocker_texts(blockers), blocker_addressees(blockers), strict=True)
        if addressee == member
    ]
    cited = []
    for identifier in sorted(record_references("\n".join(own))):
        declaring = DECLARING.get(identifier.split("-", 1)[0] + "-")
        if declaring is None or declaring == member:
            continue
        declaration = record_declaration(bodies[declaring], identifier)
        if declaration is not None:
            cited.append(f"From the {declaring} report:\n\n{declaration}")
    return (
        f"# Correction requests for the {member} report\n\n"
        f"The record verification `{verification}` addressed these blockers to this report.\n\n"
        "## Blockers\n\n" + "\n".join(own) + "\n\n"
        "## Cited records from other reports\n\n"
        + ("\n".join(cited) if cited else "none\n")
    )


def render_changes(member: str, previous: str, current: str, old: str, new: str) -> str:
    """What changed between two versions, for readers judging a correction."""
    lines = list(difflib.unified_diff(
        previous.splitlines(), current.splitlines(), fromfile=old, tofile=new, lineterm="",
    ))
    if not lines:
        return f"# Changes to the {member} report\n\nNone: `{new}` is identical to `{old}`.\n"
    # Report text can contain fences; the diff stays data inside a longer one.
    fence = "`" * max(3, 1 + max((len(run) for run in re.findall(r"`+", "\n".join(lines))), default=0))
    return (
        f"# Changes to the {member} report\n\n"
        "Code computed this difference. It shows which lines changed, not whether a "
        "change is right or whether unchanged text is still supported.\n\n"
        f"{fence}diff\n" + "\n".join(lines) + f"\n{fence}\n"
    )


def blockers_refusals(blockers: str) -> list[str]:
    """Blockers are exactly `none`, or a Markdown list: every non-blank line
    starts an entry with `- ` or continues one with indentation."""
    if blockers == "none":
        return []
    lines = [line for line in blockers.splitlines() if line.strip()]
    if lines and lines[0].startswith("- ") and all(
        line.startswith(("- ", " ", "\t")) for line in lines
    ):
        return []
    return [
        (
            "`### Blockers` must be exactly `none` or a Markdown list whose "
            "entries start with `- `"
        )
    ]


def source_anchor_refusals(text: str) -> list[str]:
    return [
        f"source anchor at line {line}: {anchor} carries a line range; cite the path"
        for line, anchor in ranged_prose_anchors(text)
    ]


def synthesis_refusals(
    path: Path, *, repo_root: Path, run_id: str, boundary: Path,
    bodies: Callable[[Path], dict[str, str]],
) -> list[str]:
    """A valid synthesis of this run whose links resolve from the overview."""
    refusals = member_refusals(path, repo_root=repo_root)
    text = path.read_text(encoding="utf-8")
    document, error = parse_document(text)
    if error or document is None:
        return refusals + [f"synthesis does not parse: {error}"]
    try:
        boundary_fields, _ = split(boundary.read_text(encoding="utf-8"))
    except (ValueError, OSError) as error:
        return refusals + [str(error)]
    refusals += identity_refusals(dict(document.frontmatter or {}), run_id=run_id, boundary_fields=boundary_fields)
    # Synthesis is written beside output/, then assembled into overview.md.
    refusals += agentic_set_member_link_failures(path.parent / OUTPUT_DIR / OVERVIEW_NAME, document.links)
    return refusals + reference_refusals(partial(bodies, path))


def verification_refusals(
    path: Path, *, repo_root: Path, run_id: str, boundary: Path, verifies: str,
) -> list[str]:
    """A valid verification of this run and stage, with well-formed blockers."""
    refusals = member_refusals(path, repo_root=repo_root)
    try:
        metadata, body = split(path.read_text(encoding="utf-8"))
        boundary_fields, _ = split(boundary.read_text(encoding="utf-8"))
    except (ValueError, OSError) as error:
        return refusals + [str(error)]
    refusals += identity_refusals(metadata, run_id=run_id, boundary_fields=boundary_fields)
    if metadata.get("verifies") != verifies:
        refusals.append(f"member identity: verifies {metadata.get('verifies')!r} does not match {verifies!r}")
    return refusals + blockers_refusals(section(body, "Blockers").strip())


def verified(verification: str) -> str:
    """A verification's account, for the overview."""
    return section(split(verification)[1], "Verification").strip()


def one_line(text: str) -> str:
    return " ".join(text.split())



def write_file(path: Path, text: str) -> None:
    """Replace a file whole, so an interrupted write leaves the old bytes or
    none, never a fragment a later replay would parse."""
    atomic_write(path, text.encode("utf-8"))


def dump_frontmatter(fields: dict[str, Any], body: str) -> str:
    serialized = yaml.safe_dump(fields, sort_keys=False, allow_unicode=True, width=1000)
    return f"---\n{serialized}---\n\n{body.strip()}\n"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


# The definition


class AnalyseAgenticSystem(Workflow):
    """Analyse one external agentic system at one frozen evidence boundary.

    Parameters: `system` (the name the caller gave), `source-identity` (the
    stable identity of the source), `source` (the caller's source input, as
    given), and optionally `review-path` and `source-revision`. For a GitHub
    identity, code freezes the checkout before the boundary job: at
    `source-revision` when given, and otherwise at the tip of the default
    branch.

    Jobs: `boundary`; the analysts of ANALYST_SPECS as `<member>-0`, each
    after the analysts it reads; then rounds of `reconcile-<n>` and
    `verify-<n>`. A verification's blockers name the reports that must
    change; code cuts each named analyst a request packet and runs it again
    as `<member>-<n>` before the next round.
    Profile classification and synthesis follow, each independently verified.
    Code renders the accepted overview.

    Every version of an analyst report stays in the run directory as
    `<member>-report-<n>.md`. `output/` holds the current version at each
    point of the definition, so a replay rewrites it in the same order.
    """

    correction_rounds = 2
    """How many reconciliation rounds may follow the first. Each follows a
    verification that named blockers; analysts named there correct in between."""
    synthesis_correction_rounds = 1
    profile_correction_rounds = 1

    def __init__(self, params=None) -> None:
        super().__init__(params)
        # The one form of the source identity that the run slug, destination
        # inspection, the boundary and publication use.
        self.source_identity = normalize_source_identity(
            str(self.params["source-identity"])
        )
        self.job_destinations: dict[str, Path] = {}
        self.source_revision = self.params.get("source-revision")
        self._checking = False
        if self.source_revision is not None and (
            not isinstance(self.source_revision, str)
            or re.fullmatch(r"[0-9a-f]{40}", self.source_revision) is None
        ):
            raise ValueError("source-revision must be a full 40-hex Git commit")
        self.checkout = github_checkout_path(self.source_identity)
        if self.source_revision is not None and self.checkout is None:
            raise ValueError("source-revision requires a GitHub repository identity")

    def run_location(self, base: Path) -> tuple[str, str]:
        """`AAS-<today>-<slug>-<worktree token>` under analysis state.

        The slug is the last path segment of the source identity when it is a
        URL, such as the repository name of a GitHub URL, so reruns of a system
        keep one review path whatever the system is called; otherwise it is the
        system parameter.
        """
        token = preparation_for(base)["token"]
        slug = source_slug(self.source_identity, str(self.params["system"]))
        today = datetime.datetime.now(datetime.UTC).date().isoformat()
        return STATE_ROOT.as_posix(), f"AAS-{today}-{slug}-{token}"

    def run(self, ctx) -> None:
        run_dir = ctx.run_dir
        repo_root = self.repo_root(run_dir)
        self.run_id = run_dir.name
        self.jobs_dir = repo_root / JOBS
        self.repo = repo_root

        ctx.effect(
            "open",
            partial(self.open, run_dir),
            recognize=partial(self.recognize_file, run_dir / OPENING),
        )
        opening = json.loads((run_dir / OPENING).read_text(encoding="utf-8"))
        write_file(run_dir / RUN_METADATA, json.dumps({key: opening[key] for key in ("inputs-commit", "run-date")}) + "\n")
        self.write_run_state(run_dir, opening, {})

        frozen = None
        if self.checkout is not None:
            ctx.effect(
                "acquire",
                partial(self.acquire, run_dir),
                recognize=partial(self.recognize_file, run_dir / FROZEN_SOURCE),
            )
            frozen = json.loads((run_dir / FROZEN_SOURCE).read_text(encoding="utf-8"))
            self.write_run_state(run_dir, opening, {"source": frozen})

        enums = overview_enums(repo_root)
        self.run_job(ctx, self.boundary_job(run_dir, enums, frozen))
        fields, boundary_body = split((run_dir / BOUNDARY).read_text(encoding="utf-8"))
        self.write_run_state(run_dir, opening, fields)

        if fields["result-disposition"] != "complete":
            self.close_without_analysis(run_dir, opening, fields, boundary_body)
            return

        (run_dir / OUTPUT_DIR).mkdir(exist_ok=True)
        versions = dict.fromkeys(ANALYSTS, 0)
        self.run_analysts(ctx, run_dir, ANALYSTS, versions)

        round_ = 0
        corrected: tuple[str, ...] = ()
        while True:
            self.run_job(ctx, self.reconcile_job(run_dir, round_, versions, corrected))
            verification = self.close_round(ctx, run_dir, fields, round_, versions, corrected)
            blockers = section(split(verification)[1], "Blockers").strip()
            if blockers == "none":
                break
            if round_ >= self.correction_rounds:
                raise StopRun(
                    "the record verification of the last round names blockers: "
                    + blockers
                )
            addressed = blocker_addressees(blockers)
            corrected = tuple(member for member in ANALYSTS if member in addressed)
            versions = {member: version + (member in corrected) for member, version in versions.items()}
            self.run_analysts(ctx, run_dir, corrected, versions, requests_from=round_)
            round_ += 1

        for profile_round in range(self.profile_correction_rounds + 1):
            self.run_job(ctx, self.profile_job(run_dir, profile_round))
            self.run_job(ctx, self.profile_verification_job(run_dir, profile_round))
            profile_verification = (run_dir / round_file("profile-verification", profile_round)).read_text(encoding="utf-8")
            blockers = section(split(profile_verification)[1], "Blockers").strip()
            if blockers == "none":
                break
            if profile_round == self.profile_correction_rounds:
                raise StopRun("the profile verification of the last round names blockers: " + blockers)
        atomic_write(run_dir / PROFILE, (run_dir / round_file("profile", profile_round)).read_bytes())

        for synthesis_round in range(self.synthesis_correction_rounds + 1):
            self.run_job(ctx, self.synthesis_job(run_dir, synthesis_round))
            self.run_job(ctx, self.synthesis_verification_job(run_dir, synthesis_round))
            synthesis_verification = (run_dir / round_file("synthesis-verification", synthesis_round)).read_text(encoding="utf-8")
            blockers = section(split(synthesis_verification)[1], "Blockers").strip()
            if blockers == "none":
                break
            if synthesis_round == self.synthesis_correction_rounds:
                raise StopRun("the synthesis verification of the last round names blockers: " + blockers)

        self.assemble(run_dir, opening, fields, boundary_body, synthesis_round,
                      verification, profile_verification, synthesis_verification)
        self.validate_set(run_dir)

        spec = PublicationSpec(
            repo_root=repo_root,
            run_state_path=run_dir / RUN_STATE,
            generated_candidate_path=run_dir / OVERVIEW,
            generated_destination=opening["review-path"],
            expected_incumbent_sha256=opening["expected-incumbent-sha256"],
        )
        ctx.effect(
            "publish",
            partial(self.publish, spec),
            inputs=(OVERVIEW, MANIFEST),
            recognize=partial(self.recognize_publication, spec),
        )

    # Jobs

    def acceptance_job(self, run_dir: Path, name: str) -> Job:
        """Obtain a job's existing validator without replay or file writes.

        Job constructors own the contexts at both call sites. This builds only
        the job value, without rendering its prompt or making its workspace.
        """
        self.repo = self.repo_root(run_dir)
        self.run_id = run_dir.name
        self.jobs_dir = self.repo / JOBS
        self._checking = True
        try:
            if name == "boundary":
                frozen_path = run_dir / FROZEN_SOURCE
                frozen = json.loads(frozen_path.read_text()) if frozen_path.exists() else None
                return self.boundary_job(run_dir, overview_enums(self.repo), frozen)
            if name == "profile":
                return self.profile_job(run_dir, 0)
            if name == "verify-profile":
                return self.profile_verification_job(run_dir, 0)
            if name == "synthesize":
                return self.synthesis_job(run_dir, 0)
            if name == "verify-synthesis":
                return self.synthesis_verification_job(run_dir, 0)
            match = re.fullmatch(r"(runtime|memory|epistemic|reconcile|verify|profile|verify-profile|synthesize|verify-synthesis)-(\d+)", name)
            if match is None:
                raise ValueError(f"unknown analysis job {name!r}; use the supplied job name")
            kind, round_ = match[1], int(match[2])
            if kind in ANALYSTS:
                return self.analyst_job(run_dir, kind, round_)
            if kind == "reconcile":
                # The round number does not say which versions the job was
                # given. Its supplied invocation does.
                supplied = self.supplied(run_dir, name)
                versions = {member: self.supplied_round(name, supplied, member, "report") for member in ANALYSTS}
                return self.reconcile_job(run_dir, round_, versions, ())
            if kind == "verify":
                text = (run_dir / round_file("set-check", round_)).read_text()
                failures = [line[2:] for line in text.splitlines() if line.startswith("- ")]
                return self.verification_job(run_dir, round_, dict.fromkeys(ANALYSTS, 0), (), validator=partial(self.record_verification_refusals, run_dir, failures=failures))
            constructors = {
                "profile": self.profile_job,
                "verify-profile": self.profile_verification_job,
                "synthesize": self.synthesis_job,
                "verify-synthesis": self.synthesis_verification_job,
            }
            return constructors[kind](run_dir, round_)
        finally:
            self._checking = False

    @staticmethod
    def supplied(run_dir: Path, name: str) -> dict[str, str]:
        """The `key = value` lines of the invocation a job was handed."""
        prompt = (run_dir / "workflow-state/jobs" / name / "prompt.md").read_text()
        invocation = prompt.split("\n## Input reading batches", 1)[0]
        return dict(re.findall(r"(?m)^([a-z-]+) = (.+)$", invocation))

    @staticmethod
    def supplied_round(name: str, supplied: Mapping[str, str], key: str, kind: str) -> int:
        """The round in a supplied `<...>-<kind>-<n>.md` or `<kind>-<n>.md` path."""
        found = re.search(rf"(?:^|-){kind}-(\d+)\.md$", Path(supplied.get(key, "")).name)
        if found is None:
            raise ValueError(f"{name}: missing supplied {key} input; report the invocation to the coordinator")
        return int(found[1])

    def run_analysts(
        self, ctx, run_dir: Path, members: Sequence[str], versions: Mapping[str, int],
        requests_from: int | None = None,
    ) -> None:
        """Run analysts in dependency order: an analyst runs after the ones it
        reads, and analysts that do not read each other run in parallel.

        `versions` gives the version each named analyst produces; the first
        round produces version 0, a correction round the next number. A
        correction round answers the blockers of verification `requests_from`.
        """
        done: set[str] = set()
        remaining = [member for member in ANALYSTS if member in members]
        while remaining:
            ready = [
                member for member in remaining
                if all(read in done or read not in members for read in ANALYST_SPECS[member]["reads"])
            ]
            if not ready:
                raise ValueError(f"analysts read each other in a cycle: {remaining}")
            ctx.parallel(*(
                partial(self.run_analyst, ctx, run_dir, member, versions[member], requests_from)
                for member in ready
            ))
            done.update(ready)
            remaining = [member for member in remaining if member not in done]

    def run_analyst(
        self, ctx, run_dir: Path, member: str, round_: int, requests_from: int | None,
    ) -> None:
        """Run one analyst job, then make its report the current version.

        A correction round first gets its request packet, cut from the current
        reports; afterwards its answers and the text difference from its
        predecessor are kept for the next reconciler and verifier.
        """
        if round_:
            if requests_from is None:
                raise ValueError(f"{member}-{round_}: a correction round needs the verification it answers")
            verification = round_file("verification", requests_from)
            text = (run_dir / verification).read_text(encoding="utf-8")
            bodies = {
                other: split((run_dir / CURRENT[other]).read_text(encoding="utf-8"))[1]
                for other in ANALYSTS if other != member
            }
            self.replace(run_dir / requests(member, round_), render_requests(
                member, verification, section(split(text)[1], "Blockers").strip(), bodies,
            ).encode("utf-8"))
        job = self.analyst_job(run_dir, member, round_)
        self.run_job(ctx, job)
        destination = self.job_destinations[job.name]
        self.replace(run_dir / CURRENT[member], destination.read_bytes())
        if round_:
            self.replace(
                run_dir / answers(member, round_),
                (job.output_path(run_dir).parent / ANSWERS_NAME).read_bytes(),
            )
            old, new = report(member, round_ - 1), report(member, round_)
            self.replace(run_dir / changes(member, round_), render_changes(
                member, (run_dir / old).read_text(encoding="utf-8"),
                destination.read_text(encoding="utf-8"), old, new,
            ).encode("utf-8"))

    @staticmethod
    def replace(path: Path, content: bytes) -> None:
        """Write coordinator-owned bytes only when they differ, so a replay
        that changes nothing leaves the file alone."""
        if not path.is_file() or path.read_bytes() != content:
            atomic_write(path, content)

    def run_job(self, ctx, job: Job) -> None:
        """Expose a worker result to later jobs only after engine acceptance.

        Workers own their job directory; canonical run files and the assembled
        set remain coordinator-owned. Copying is replay-safe and byte-exact.
        """
        ctx.agent(job).wait()
        destination = self.job_destinations[job.name]
        content = job.output_path(ctx.run_dir).read_bytes()
        if not destination.is_file() or destination.read_bytes() != content:
            atomic_write(destination, content)

    def job(
        self,
        run_dir: Path,
        name: str,
        output: str,
        *,
        reads: Mapping[str, str],
        instruction: str | None = None,
        extra: Sequence[str] = (),
        parameters: Mapping[str, str] | None = None,
        source: str | None = None,
        validator: Callable[[Path], Sequence[str]] | None = None,
    ) -> Job:
        """Build the invocation from the same paths declared to the engine.

        Named reads are resolved once for both parameters and dependencies.
        Run state is a mutable command argument, not a file dependency.
        Worker outputs live in a per-job workspace. The supplied output path
        names the coordinator-owned accepted copy used by downstream readers.
        """
        run_dir = run_dir.resolve()
        validator = partial(actionable_refusals, validator) if validator is not None else None
        if self._checking:
            return Job(name=name, prompt="", output=f"jobs/{name}/{Path(output).name}", validator=validator)
        instruction = instruction or name
        method = [f"{instruction}.md", "../../../COLLECTION.md", "worker-rules.md"]
        method_paths = [str((self.jobs_dir / file).resolve()) for file in (*method, *extra)]
        input_paths = {key: str((run_dir / path).resolve()) for key, path in reads.items()}
        workspace = run_dir / "jobs" / name
        (workspace / "scratch").mkdir(parents=True, exist_ok=True)
        self.job_destinations[name] = run_dir / output
        job = Job(
            name=name,
            prompt="",
            output=f"jobs/{name}/{Path(output).name}",
            inputs=(*input_paths.values(), *method_paths),
            validator=validator,
            prompt_is_complete=True,
            launch={"fork_turns": "none"},
        )
        values = {
            "system": one_line(str(self.params["system"])),
            "run-id": run_dir.name,
            **(parameters or {}),
            "run-state": str(run_dir / RUN_STATE),
            "job": name,
            **self.command_path(run_dir),
            **input_paths,
            "output": str(job.output_path(run_dir)),
            "problem": str(job.problem_path(run_dir)),
            "workspace": str(workspace) + "/",
            "scratch": str(workspace / "scratch") + "/",
        }
        lines = [f"Follow {method_paths[0]} with:"]
        lines += [f"{key} = {value}" for key, value in values.items()]
        lines += ["", "read-first:", *(f"- {path}" for path in method_paths[1:])]
        lines += [
            "", "## Input reading batches", "",
            f"Read the named job instruction {method_paths[0]} before these reading batches.",
            "",
            ("Load inputs in these batches to avoid truncated reads. Use one tool "
            "call per batch, return the complete command result, and recover any "
            "truncation before continuing. Read oversized files in bounded ranges."),
        ]
        for title, paths in (("Read-first", method_paths[1:]), ("Task inputs", list(input_paths.values()))):
            lines += ["", f"{title}:"]
            lines += [f"{number}. " + ", ".join(batch)
                      for number, batch in enumerate(reading_batches(paths), 1)]
        oversized = [Path(path) for path in (*method_paths[1:], *input_paths.values())
                     if Path(path).is_file() and Path(path).stat().st_size > READ_BATCH_BYTES]
        if oversized:
            lines += ["", "Oversized-file ranges:",
                      ("Read each range in a separate tool call. A single oversized line "
                       "still needs a smaller read if delivery is truncated.")]
            for path in oversized:
                spans = "; ".join(f"{start}-{end}" for start, end in reading_ranges(path))
                lines.append(f"- {path}: lines {spans}")
        if source is not None:
            # Caller text stays data even when it contains fences or parameters.
            fence = "`" * max(3, 1 + max((len(run) for run in re.findall(r"`+", source)), default=0))
            lines += ["", "source:", fence, source, fence]
        return replace(job, prompt="\n".join(lines) + "\n")

    def boundary_job(
        self, run_dir: Path, enums: dict[str, list[Any]],
        frozen: dict[str, Any] | None = None,
    ) -> Job:
        frozen_parameters = {} if frozen is None else {
            "source-revision": frozen["revision"], "source-path": frozen["path"],
        }
        return self.job(
            run_dir,
            "boundary",
            BOUNDARY,
            reads={"opening": RUN_METADATA},
            extra=(BOUNDARY_CONTRACT, SOURCES_CONTRACT),
            parameters={
                "source-identity": one_line(self.source_identity),
                **frozen_parameters,
            },
            source=str(self.params["source"]),
            validator=partial(
                boundary_refusals, enums=enums, identity=self.source_identity,
                frozen=frozen,
            ),
        )

    def analyst_job(self, run_dir: Path, member: str, round_: int) -> Job:
        """One analyst job, `<member>-<round>`.

        The first round reads the boundary and the first version of each
        report the analyst depends on. A correction round reads the boundary,
        its own previous report and its request packet, and writes its
        answers beside the report. Citations resolve against the reports the
        analyst read, or in a correction round against every current report.
        """
        run_dir = run_dir.resolve()
        spec = ANALYST_SPECS[member]
        name = f"{member}-{round_}"
        reads = {"boundary": BOUNDARY}
        parameters = {"round": "correction" if round_ else "first"}
        if round_:
            reads.update({"previous-report": report(member, round_ - 1), "requests": requests(member, round_)})
            parameters["answers"] = str(run_dir / "jobs" / name / ANSWERS_NAME)
            cited = {other: run_dir / CURRENT[other] for other in ANALYSTS if other != member}
        else:
            reads.update({read: report(read, 0) for read in spec["reads"]})
            cited = {read: run_dir / CURRENT[read] for read in spec["reads"]}
        checks = [partial(
            pass_refusals,
            repo_root=self.repo,
            run_state=run_dir / RUN_STATE,
            boundary=run_dir / BOUNDARY,
            declaration_prefix=spec["prefix"],
            bodies=lambda path: set_bodies(boundary=run_dir / BOUNDARY, **cited, **{member: path}),
        )]
        if round_:
            checks.append(partial(
                correction_refusals, member=member,
                previous=run_dir / reads["previous-report"], packet=run_dir / reads["requests"],
            ))
        return self.job(
            run_dir, name, report(member, round_), reads=reads, instruction=member,
            extra=(SOURCES_CONTRACT, RECORDS_CONTRACT, spec["contract"]),
            parameters=parameters,
            validator=lambda path: [reason for check in checks for reason in check(path)],
        )

    @staticmethod
    def correction_reads(corrected: Sequence[str], versions: Mapping[str, int]) -> dict[str, str]:
        """What the last correction step produced, for the jobs that judge it."""
        reads = {}
        for member in corrected:
            reads[f"{member}-answers"] = answers(member, versions[member])
            reads[f"{member}-changes"] = changes(member, versions[member])
        return reads

    def reconcile_job(
        self, run_dir: Path, round_: int, versions: Mapping[str, int],
        corrected: Sequence[str],
    ) -> Job:
        reads = {"boundary": BOUNDARY, **{member: report(member, versions[member]) for member in ANALYSTS}}
        if round_ > 0:
            reads["previous-reconciliation"] = reconciliation(round_ - 1)
            reads.update({kind: round_file(kind, round_ - 1) for kind in ("verification", "set-check")})
            reads.update(self.correction_reads(corrected, versions))
        return self.job(
            run_dir,
            f"reconcile-{round_}",
            reconciliation(round_),
            reads=reads,
            instruction="reconcile",
            extra=RECORD_CONTRACTS,
            parameters={"round": "after-blockers" if round_ else "first"},
            validator=partial(
                reconcile_refusals,
                repo_root=self.repo,
                run_id=run_dir.name,
                boundary=run_dir / BOUNDARY,
                runtime=run_dir / reads["runtime"],
                report=run_dir / reads["memory"],
                epistemic=run_dir / reads["epistemic"],
            ),
        )

    def record_bodies(self, run_dir: Path, **extra: Path) -> dict[str, str]:
        return set_bodies(
            boundary=run_dir / BOUNDARY,
            reconciled=run_dir / RECONCILIATION,
            runtime=run_dir / RUNTIME,
            memory=run_dir / MEMORY,
            epistemic=run_dir / EPISTEMIC,
            **extra,
        )

    def record_check(self, run_dir: Path, fields: dict[str, Any]) -> list[str]:
        """Check records directly, before any public synthesis or overview exists."""
        failures = []
        for name in RECORD_MEMBER_NAMES:
            path = run_dir / OUTPUT_DIR / name
            failures.extend(f"{name}: {failure}" for failure in member_refusals(path, repo_root=self.repo))
            metadata, _ = split(path.read_text(encoding="utf-8"))
            for field, expected in (("run-id", self.run_id), ("reviewed-boundary", fields["reviewed-boundary"])):
                if metadata.get(field) != expected:
                    failures.append(f"{name}: {field} {metadata.get(field)!r} does not match the boundary; expected {expected!r}")
        failures.extend(reference_refusals(partial(self.record_bodies, run_dir)))
        return failures

    def close_round(
        self, ctx, run_dir: Path, fields: dict[str, Any], round_: int,
        versions: Mapping[str, int], corrected: Sequence[str],
    ) -> str:
        """Make the round's reports current, check the records, and independently judge them."""
        for member in ANALYSTS:
            self.replace(run_dir / CURRENT[member], (run_dir / report(member, versions[member])).read_bytes())
        self.replace(run_dir / RECONCILIATION, (run_dir / reconciliation(round_)).read_bytes())
        failures = self.record_check(run_dir, fields)
        write_file(run_dir / round_file("set-check", round_),
                   "# Record set check\n\n" + ("\n".join(f"- {failure}" for failure in failures) or "none") + "\n")
        self.run_job(ctx, self.verification_job(
            run_dir, round_, versions, corrected,
            validator=partial(self.record_verification_refusals, run_dir, failures=failures),
        ))
        return (run_dir / round_file("verification", round_)).read_text(encoding="utf-8")

    def verifier_refusals(self, run_dir: Path, verifies: str) -> Callable[[Path], list[str]]:
        return partial(
            verification_refusals, repo_root=self.repo, run_id=run_dir.name,
            boundary=run_dir / BOUNDARY, verifies=verifies,
        )

    def verification_job(
        self, run_dir: Path, round_: int, versions: Mapping[str, int],
        corrected: Sequence[str],
        *, validator: Callable[[Path], Sequence[str]] | None = None,
    ) -> Job:
        reads = {"boundary": BOUNDARY, "reconciliation": RECONCILIATION,
                 **{member: report(member, versions[member]) for member in ANALYSTS},
                 "set-check": round_file("set-check", round_)}
        if round_ > 0:
            reads["previous-verification"] = round_file("verification", round_ - 1)
            reads.update(self.correction_reads(corrected, versions))
        return self.job(
            run_dir, f"verify-{round_}", round_file("verification", round_),
            reads=reads, instruction="verify", extra=(*RECORD_CONTRACTS, VERIFICATION_CONTRACT),
            validator=validator, parameters={"round": "after-blockers" if round_ else "first"},
        )

    def record_verification_refusals(self, run_dir: Path, path: Path, *, failures: Sequence[str]) -> list[str]:
        refusals = self.verifier_refusals(run_dir, "records")(path)
        try:
            blockers = section(split(path.read_text(encoding="utf-8"))[1], "Blockers").strip()
        except ValueError:
            return refusals
        if failures and blockers == "none":
            refusals.append("structural failures require explicit blockers")
        if not blockers_refusals(blockers):
            refusals += addressee_refusals(blockers)
        return refusals + reference_refusals(partial(self.record_bodies, run_dir, verification=path))

    def profile_job(self, run_dir: Path, round_: int) -> Job:
        reads = {"boundary": BOUNDARY, "runtime": RUNTIME, "memory": MEMORY,
                 "epistemic": EPISTEMIC, "reconciliation": RECONCILIATION}
        if round_:
            reads.update({"previous-profile": round_file("profile", round_ - 1),
                          "verification": round_file("profile-verification", round_ - 1)})
        return self.job(
            run_dir, "profile" if round_ == 0 else f"profile-{round_}",
            round_file("profile", round_), reads=reads, instruction="profile",
            extra=(SOURCES_CONTRACT, RECORDS_CONTRACT, PROFILE_CONTRACT),
            parameters={"round": "after-blockers" if round_ else "first"},
            validator=partial(self.profile_refusals, run_dir),
        )

    def profile_refusals(self, run_dir: Path, path: Path) -> list[str]:
        refusals = member_refusals(path, repo_root=self.repo)
        metadata, _ = split(path.read_text(encoding="utf-8"))
        # Require the current write contract only at scheduled job acceptance.
        # Immutable set and finalization readers still interpret retained v1.
        comparison = metadata.get("memory-comparison")
        if (not isinstance(comparison, dict)
                or type(comparison.get("version")) is not int
                or comparison["version"] != 2):
            refusals.append("new workflow profiles require memory-comparison version: 2")
        if metadata.get("type") != "agentic-system-analyses/types/agent-memory-profile.md":
            refusals.append("profile frontmatter type must be agentic-system-analyses/types/agent-memory-profile.md")
        fields, _ = split((run_dir / BOUNDARY).read_text(encoding="utf-8"))
        for key, expected in (("run-id", self.run_id),
                              ("reviewed-boundary", fields["reviewed-boundary"]),
                              ("source-identity", self.source_identity)):
            if metadata.get(key) != expected:
                refusals.append(f"profile identity: {key} {metadata.get(key)!r} does not match the run's expected {expected!r}")
        return refusals + reference_refusals(partial(self.record_bodies, run_dir, profile=path))

    def profile_verification_job(self, run_dir: Path, round_: int) -> Job:
        return self.job(
            run_dir, "verify-profile" if round_ == 0 else f"verify-profile-{round_}",
            round_file("profile-verification", round_),
            reads={"profile": round_file("profile", round_), "boundary": BOUNDARY,
                   "runtime": RUNTIME, "memory": MEMORY, "epistemic": EPISTEMIC,
                   "reconciliation": RECONCILIATION},
            instruction="verify-profile",
            extra=(SOURCES_CONTRACT, RECORDS_CONTRACT, PROFILE_CONTRACT, VERIFICATION_CONTRACT),
            validator=partial(self.profile_verification_refusals, run_dir),
        )

    def profile_verification_refusals(self, run_dir: Path, path: Path) -> list[str]:
        return self.verifier_refusals(run_dir, "profile")(path) + reference_refusals(
            partial(self.record_bodies, run_dir, verification=path))

    def synthesis_job(self, run_dir: Path, round_: int) -> Job:
        reads = {"boundary": BOUNDARY, "runtime": RUNTIME, "memory": MEMORY,
                 "epistemic": EPISTEMIC, "reconciliation": RECONCILIATION}
        if round_:
            reads.update({"previous-synthesis": round_file("synthesis", round_ - 1),
                          "verification": round_file("synthesis-verification", round_ - 1)})
        return self.job(
            run_dir, "synthesize" if round_ == 0 else f"synthesize-{round_}",
            round_file("synthesis", round_), reads=reads, instruction="synthesize",
            extra=SYNTHESIS_CONTRACTS,
            parameters={"round": "after-blockers" if round_ else "first"},
            validator=partial(synthesis_refusals, repo_root=self.repo, run_id=run_dir.name,
                              boundary=run_dir / BOUNDARY,
                              bodies=lambda path: self.record_bodies(run_dir, synthesis=path)),
        )

    def synthesis_verification_job(self, run_dir: Path, round_: int) -> Job:
        return self.job(
            run_dir, "verify-synthesis" if round_ == 0 else f"verify-synthesis-{round_}",
            round_file("synthesis-verification", round_),
            reads={"synthesis": round_file("synthesis", round_), "boundary": BOUNDARY,
                   "runtime": RUNTIME, "memory": MEMORY, "epistemic": EPISTEMIC,
                   "reconciliation": RECONCILIATION},
            instruction="verify-synthesis", extra=(*SYNTHESIS_CONTRACTS, VERIFICATION_CONTRACT),
            validator=partial(self.synthesis_verification_refusals, run_dir, round_),
        )

    def synthesis_verification_refusals(self, run_dir: Path, round_: int, path: Path) -> list[str]:
        return self.verifier_refusals(run_dir, "synthesis")(path) + reference_refusals(
            partial(self.record_bodies, run_dir,
                    synthesis=run_dir / round_file("synthesis", round_), verification=path))

    # Steps that code executes

    @staticmethod
    def command_path(run_dir: Path) -> dict[str, str]:
        """Name the run's local command directory when this code runs from it.

        A worker launched by a session that began outside the run's checkout
        does not inherit that directory on PATH.
        """
        bin_dir = Path(sys.prefix) / ("Scripts" if os.name == "nt" else "bin")
        parents = run_dir.parents
        depth = len(STATE_ROOT.parts)
        if len(parents) <= depth or Path(sys.prefix).resolve() != (parents[depth] / ".venv").resolve():
            return {}
        return {"command-path": str(bin_dir) + "/"}

    @staticmethod
    def repo_root(run_dir: Path) -> Path:
        if not RUN_ID.fullmatch(run_dir.name):
            raise ValueError(
                f"{run_dir.name} is not a run ID of the form AAS-YYYY-MM-DD-slug-token-nn"
            )
        repo_root = run_dir.parents[len(STATE_ROOT.parts)]
        if repo_root / STATE_ROOT != run_dir.parent:
            raise ValueError(f"a run directory must be directly under {STATE_ROOT}")
        return repo_root

    def review_path(self) -> str:
        if "review-path" in self.params:
            raise ValueError("review-path is no longer a run parameter; publication uses the source slug")
        return (RETAINED_ROOT / source_slug(self.source_identity, str(self.params["system"])) / OVERVIEW_NAME).as_posix()

    def head(self) -> str:
        result = subprocess.run(
            ["git", "-C", str(self.repo), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()

    def check_opening(self, commit: str) -> None:
        require_publishable_worktree(self.repo)
        require_running_package_unchanged(commit)

    def inspect(self, destination: str) -> str:
        found = inspect_destination(
            repo_root=self.repo,
            generated_destination=destination,
            source_identity=self.source_identity,
        )
        return str(found["expected_incumbent_sha256"])

    def open(self, run_dir: Path) -> None:
        record_path = self.repo.with_name(self.repo.name + ".preparation.json")
        slug = source_slug(self.source_identity, str(self.params["system"]))
        tokenized = re.fullmatch(
            rf"AAS-\d{{4}}-\d{{2}}-\d{{2}}-{re.escape(slug)}-[0-9a-f]{{12}}-\d{{2}}",
            self.run_id,
        ) is not None
        if tokenized or record_path.exists():
            preparation = preparation_for(self.repo, require_token=tokenized)
            token = preparation.get("token")
            if token is not None and not re.fullmatch(
                rf"AAS-\d{{4}}-\d{{2}}-\d{{2}}-{re.escape(slug)}-{token}-\d{{2}}",
                self.run_id,
            ):
                raise ValueError("analysis run ID does not match the worktree preparation token")
        commit = self.head()
        if tokenized and preparation["commit"] != commit:
            raise ValueError("analysis worktree HEAD differs from its preparation commit")
        self.check_opening(commit)
        destination = self.review_path()
        record = {
            "inputs-commit": commit,
            "run-date": datetime.datetime.now(datetime.UTC).date().isoformat(),
            "review-path": destination,
            "expected-incumbent-sha256": self.inspect(destination),
        }
        write_file(run_dir / OPENING, json.dumps(record, indent=2) + "\n")

    def origin(self) -> str:
        """Where a missing checkout is cloned from, and the origin an existing
        one must have."""
        return self.source_identity

    def acquire(self, run_dir: Path) -> None:
        assert self.checkout is not None
        frozen = freeze_checkout(
            self.repo, self.checkout, identity=self.source_identity,
            origin=self.origin(), revision=self.source_revision,
        )
        write_file(run_dir / FROZEN_SOURCE, json.dumps(frozen, indent=2) + "\n")

    @staticmethod
    def recognize_file(path: Path) -> Recognition:
        return Recognition.COMPLETED if path.is_file() else Recognition.ABSENT

    def write_run_state(
        self,
        run_dir: Path,
        opening: dict[str, Any],
        fields: dict[str, Any],
        *,
        completion: dict[str, Any] | None = None,
    ) -> None:
        """Render the run state from the run's files. A complete state is left
        alone: publication wrote it, or it is this rendering's own result."""
        path = run_dir / RUN_STATE
        if path.is_file() and completion is None:
            current, _ = split(path.read_text(encoding="utf-8"))
            if current.get("run-status") == "complete":
                return
        frontmatter = {
            "type": RUN_STATE_TYPE,
            "description": f"Minimal completion state for {self.run_id}",
            "run-id": self.run_id,
            "system": str(self.params["system"]),
            "run-status": "running",
            "result-disposition": None,
            "source": fields.get("source"),
            "artifact": None,
            "generated-review": None,
            "failure": None,
        }
        outcome = "Running."
        if completion is not None:
            frontmatter.update(completion)
            outcome = (
                "Completed without publication: the overview's disposition is "
                + str(completion["result-disposition"])
                + "."
            )
        source = fields.get("source") or {}
        body = (
            f"# Agentic-system analysis run — {self.run_id}\n\n## Run\n\n"
            f"Target: {self.params['system']}. Source: {source.get('identity', 'not frozen')}"
            f" at {source.get('revision', 'no revision')}. Expected incumbent digest: "
            f"`{opening['expected-incumbent-sha256']}`.\n\n## Outcome\n\n{outcome}"
        )
        write_file(path, dump_frontmatter(frontmatter, body))

    def record_step_result(self, run_dir: Path, result: StepResult) -> None:
        """Project the last workflow outcome into the operator-facing run state."""
        path = run_dir / RUN_STATE
        if not path.is_file() or isinstance(result, Done):
            return
        fields, body = split(path.read_text(encoding="utf-8"))
        if fields.get("run-status") in ("complete", "failed"):
            return
        if isinstance(result, Uncertain):
            status = "uncertain"
            outcome = f"Uncertain effect {result.effect}: {result.detail}"
        elif isinstance(result, Blocked):
            status = "stopped" if any(block.permitted == "stop" for block in result.blocks) else "blocked"
            outcome = f"{status.capitalize()}: " + "; ".join(
                f"{block.subject}: {block.reason}" for block in result.blocks
            )
        elif isinstance(result, Launch):
            status = "running"
            outcome = "Running."
        else:
            raise TypeError(f"unknown step result: {result!r}")
        fields["run-status"] = status
        prefix, separator, _ = body.partition("## Outcome\n\n")
        if not separator:
            raise ValueError("run state has no Outcome section")
        write_file(path, dump_frontmatter(fields, prefix + separator + outcome))

    def assemble(
        self, run_dir: Path, opening: dict[str, Any], fields: dict[str, Any],
        boundary_body: str, round_: int, record_verification: str,
        profile_verification: str, synthesis_verification: str,
    ) -> None:
        """Render the final overview after all three independent checks pass."""
        write_file(run_dir / OVERVIEW, self.render_overview(
            run_dir, opening, fields, boundary_body, round_,
            record_verification, profile_verification, synthesis_verification,
        ))
        build_manifest(run_dir)

    def overview_frontmatter(
        self,
        opening: dict[str, Any],
        fields: dict[str, Any],
        description: str | None = None,
    ) -> dict[str, Any]:
        """The overview's frontmatter. A complete run's description is the
        synthesizer's; code writes the others."""
        disposition = fields["result-disposition"]
        boundary = fields.get("reviewed-boundary") or "no established boundary"
        return {
            "type": OVERVIEW_TYPE,
            "description": description
            or (
                f"Analysis of {self.params['system']} at {boundary}, with {disposition} disposition"
            ),
            "run-id": self.run_id,
            "system": str(self.params["system"]),
            "run-date": opening["run-date"],
            "result-disposition": disposition,
            **{name: fields.get(name) for name in BOUNDARY_FIELDS},
            "inputs-commit": opening["inputs-commit"],
        }

    def overview_body(self, boundary_body: str, rest: str) -> str:
        return (
            f"# {self.params['system']} agentic-system analysis\n\n"
            f"## Boundary and evidence\n\n{section(boundary_body, 'Boundary and evidence').strip()}\n\n"
            f"## Source register\n\n{section(boundary_body, 'Source register').strip()}\n\n"
            f"{rest.strip()}\n"
        )

    def validation_text(self, run_dir: Path) -> str:
        output = (run_dir / OUTPUT_DIR).relative_to(self.repo).as_posix()
        return (
            f"`commonplace-validate {output} --full` runs after the manifest is written, "
            "over every member, the manifest and the set's cross-member checks; code "
            "publishes only when it passes, and publication runs it again."
        )

    def render_overview(
        self, run_dir: Path, opening: dict[str, Any], fields: dict[str, Any],
        boundary_body: str, round_: int, record_verification: str,
        profile_verification: str, synthesis_verification: str,
    ) -> str:
        synthesis_fields, synthesis = split((run_dir / round_file("synthesis", round_)).read_text(encoding="utf-8"))
        index = amendment_index((run_dir / RECONCILIATION).read_text(encoding="utf-8"))
        rest = (
            f"## Bounded synthesis\n\n{section(synthesis, 'Bounded synthesis').strip()}\n\n"
            f"## Limitations\n\n{section(synthesis, 'Limitations').strip()}\n\n"
            "## Verification and blockers\n\n"
            f"### Record verification\n\n{verified(record_verification)}\n\n"
            f"### Profile verification\n\n{verified(profile_verification)}\n\n"
            f"### Synthesis verification\n\n{verified(synthesis_verification)}\n\n"
            f"### Deterministic validation\n\n{self.validation_text(run_dir)}\n\n"
            "### Blockers\n\nnone\n"
        )
        # Insert within the Source register regardless of the boundary's section order.
        boundary_with_index = re.sub(
            r"(?ms)^## Source register[ \t]*\n.*?(?=^## |\Z)",
            lambda match: match[0].rstrip() + "\n\n" + index + "\n\n",
            boundary_body,
            count=1,
        )
        return dump_frontmatter(
            self.overview_frontmatter(opening, fields, one_line(str(synthesis_fields["description"]))),
            self.overview_body(boundary_with_index, rest),
        )

    def close_without_analysis(
        self,
        run_dir: Path,
        opening: dict[str, Any],
        fields: dict[str, Any],
        boundary_body: str,
    ) -> None:
        """A blocked or out-of-scope run: an overview-only set, no publication."""
        reason = section(boundary_body, "Not reached").strip()
        not_reached = f"Not reached. {reason}"
        rest = (
            f"## Bounded synthesis\n\n{not_reached}\n\n"
            f"## Limitations\n\n{reason}\n\n"
            "## Verification and blockers\n\n"
            f"### Record verification\n\n{not_reached}\n\n"
            f"### Profile verification\n\n{not_reached}\n\n"
            f"### Synthesis verification\n\n{not_reached}\n\n"
            f"### Deterministic validation\n\n{self.validation_text(run_dir)}\n\n"
            f"### Blockers\n\n{reason}\n"
        )
        (run_dir / OUTPUT_DIR).mkdir(exist_ok=True)
        write_file(
            run_dir / OVERVIEW,
            dump_frontmatter(
                self.overview_frontmatter(opening, fields),
                self.overview_body(boundary_body, rest),
            ),
        )
        build_manifest(run_dir)
        self.validate_set(run_dir)
        manifest = run_dir / MANIFEST
        self.write_run_state(
            run_dir,
            opening,
            fields,
            completion={
                "run-status": "complete",
                "result-disposition": fields["result-disposition"],
                "artifact": {
                    "path": manifest.relative_to(self.repo).as_posix(),
                    "sha256": digest(manifest),
                },
            },
        )

    def validate_set(self, run_dir: Path) -> None:
        failures = validate_note(run_dir / OUTPUT_DIR, repo_root=self.repo).fails
        if failures:
            raise ValueError("the set does not validate:\n" + "\n".join(failures))

    # Publication

    def publish(self, spec: PublicationSpec) -> None:
        publish_publication(spec)

    def recognize_publication(self, spec: PublicationSpec) -> Recognition:
        state, _ = split(spec.run_state_path.read_text(encoding="utf-8"))
        candidate = digest(spec.generated_candidate_path)
        review = state.get("generated-review") or {}
        if state.get("run-status") == "complete" and review.get("sha256") == candidate:
            return Recognition.COMPLETED
        destination = spec.repo_root / spec.generated_destination
        current = digest(destination) if destination.is_file() else "absent"
        # A partial accepted set is an uncertain publication, even if its
        # overview still has the expected incumbent digest.
        retained = (spec.repo_root / spec.generated_destination).parent
        if (
            state.get("run-status") == "running"
            and current == spec.expected_incumbent_sha256
            and (spec.expected_incumbent_sha256 != "absent" or not retained.exists())
        ):
            if spec.expected_incumbent_sha256 != "absent":
                from commonplace.lib.agentic_set import current_analyses

                try:
                    current_analyses(spec.repo_root)
                except ValueError:
                    return Recognition.UNKNOWN
            return Recognition.ABSENT
        return Recognition.UNKNOWN

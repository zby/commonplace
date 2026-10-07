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

from commonplace.lib.agentic_checkout import freeze_checkout, github_checkout_path
from commonplace.lib.agentic_finalize import build_manifest, start_manifest
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
)
from commonplace.lib.agentic_set import (
    OUTPUT_DIR,
    RETAINED_ROOT,
    RUN_ID,
    SET_TYPE,
    analysis_layout,
    normalize_source_identity,
    record_prefix,
    source_slug,
)
from commonplace.lib.analysis_worktree import preparation_for
from commonplace.lib.directory_artifact import MANIFEST_NAME
from commonplace.lib.directory_layout import Finding
from commonplace.lib.note_parser import parse_document
from commonplace.lib.validation import (
    ValidationRun,
    validate_draft_at_slot,
    validate_note,
)
from commonplace.workflow.reading import (
    READ_BATCH_BYTES,
    reading_batches,
    reading_ranges,
)
from commonplace.workflow_legacy import (
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
BOUNDARY_TYPE = f"{TYPES}/agentic-system-boundary.md"
SOURCES_CONTRACT = "../../agentic-analysis-sources.md"
RECORDS_CONTRACT = "../../agentic-analysis-records.md"
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
SYNTHESIS_CONTRACTS = (SOURCES_CONTRACT, RECORDS_CONTRACT, SYNTHESIS_CONTRACT)

OPENING = "opening.json"
RUN_METADATA = "run-metadata.json"
FROZEN_SOURCE = "source.json"
RUN_STATE = "run-state.md"
MANIFEST = f"{OUTPUT_DIR}/{MANIFEST_NAME}"


def slot(role: str) -> str:
    """Where a set role's current document is, relative to the run directory."""
    return f"{OUTPUT_DIR}/{analysis_layout().path(role)}"


BOUNDARY_FIELDS = (
    "target-class",
    "boundary-kind",
    "reviewed-boundary",
    "analysis-cutoff",
    "evidence-tier",
)
ANALYST_SPECS: dict[str, dict[str, Any]] = {
    "runtime": {"contract": RUNTIME_CONTRACT, "reads": ()},
    "memory": {"contract": MEMORY_CONTRACT, "reads": ("runtime",)},
    "epistemic": {"contract": EPISTEMIC_CONTRACT, "reads": ("runtime",)},
}
"""The analysts: the type its report follows, and the analysts whose reports
it reads in its first round. `reads` also orders the work: an analyst runs
after the analysts it reads. The ID prefix each declares is its report
type's `record-prefix`."""
ANALYSTS = tuple(ANALYST_SPECS)
RECORD_ROLES = (*ANALYSTS, "reconciliation")
"""The set roles whose records the round-close check judges."""
LATER_ROLES = ("record-verification", "memory-profile", "profile-verification",
               "synthesis", "synthesis-verification", "overview")
"""The set roles written after the record rounds close."""
ADDRESSEES = (*ANALYSTS, "reconciliation")
"""Who a record-verification blocker can be addressed to."""
ANSWERS_NAME = "answers.md"
"""What a correcting analyst writes beside its report, in its job workspace."""
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


def boundary_refusals(
    path: Path, *, repo_root: Path, run_id: str, identity: str,
    frozen: dict[str, Any] | None = None,
) -> list[str]:
    """Invocation-only checks against run parameters and pinned source bytes."""
    refusals = []
    try:
        fields, _ = split(path.read_text(encoding="utf-8"))
    except ValueError:
        return refusals
    if fields.get("run-id") != run_id:
        refusals.append(f"member identity: run-id {fields.get('run-id')!r} does not match {run_id!r}")
    source = fields.get("source")
    if isinstance(source, dict):
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


def validation_reasons(validator: Callable[[Path], Sequence[str]], path: Path) -> list[str]:
    """Materialize raw reasons, including malformed-input refusals."""
    try:
        return list(validator(path))
    except (OSError, ValueError, KeyError) as error:
        return [f"validation input: {error}; correct malformed output or report a missing supplied input to the coordinator"]


def actionable_refusals(validator: Callable[[Path], Sequence[str]], path: Path) -> list[str]:
    """Address the same mechanical findings to either caller, never edit output."""
    reasons = validation_reasons(validator, path)
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
    # Preserve every set finding byte-for-byte, including repeated findings.
    # Only invocation residue is coalesced; it has no standalone caller.
    findings = [reason for reason in reasons if reason.startswith(SET_LABEL)]
    for reason, count in Counter(reason for reason in reasons if not reason.startswith(SET_LABEL)).items():
        if count > 1:
            reason += f" ({count} identical findings)"
        repair = next((value for key, value in repairs.items() if key in reason),
                      "correct the named field, section or citation to satisfy the stated rule and the supplied job/type contract")
        rule = refusal_rule(reason)
        findings.append(f"[job residue] {path.name}: rule {rule}: {reason}\nRepair: {repair}")
    return findings


SET_LABEL = "[set] "
"""Marks a refusal that is the set type's finding, as distinct from a workflow check."""
MEASUREMENTS = "acceptance-measurements"
"""Coordinator-owned, replay-safe judgments; outside both output and engine state."""


class SetRefusal(str):
    """Keep a finding's role beside its unchanged delivered text."""

    role: str | None

    def __new__(cls, finding: Finding):
        value = super().__new__(cls, SET_LABEL + finding.render())
        value.role = finding.role
        return value


def compare_selfcheck(
    measurement: Mapping[str, Any], *, candidate_sha256: str, findings: Sequence[str],
) -> bool | None:
    """Return disagreement, or None for different bytes.

    Supply the selfcheck's retained digest and rendered failing set findings
    (without the acceptance-only [set] label). Validation writes no log, so
    the coordinator must retain that observation separately. Same bytes do
    not establish same sibling/source context; a disagreement needs triage.
    """
    if candidate_sha256 != measurement["candidate-sha256"]:
        return None
    return list(findings) != [text.removeprefix(SET_LABEL) for text in measurement["set-findings"]]


def set_findings(
    run_dir: Path, *, repo_root: Path, role: str | None = None, candidate: Path | None = None,
) -> list[Finding]:
    """The working set's findings, as its type reports them, by role.

    With ``candidate``, its bytes stand at ``role``'s path; nothing is written
    to ``output/``. The manifest is read as the working one, so a replay over
    a finished, pinned set judges each step the same way the run first did.
    """
    output = run_dir / OUTPUT_DIR
    overrides: dict[Path, str | bytes] = {output / MANIFEST_NAME: yaml.safe_dump({"type": SET_TYPE})}
    if candidate is not None:
        assert role is not None
        return validate_draft_at_slot(
            output, analysis_layout().path(role), candidate, repo_root=repo_root,
        )
    return ValidationRun(repo_root, (), content_overrides=overrides).artifact_findings(output)


def set_role_refusals(path: Path, *, run_dir: Path, repo_root: Path, role: str) -> list[str]:
    """The set's findings for one role, with ``path`` as that role's document."""
    findings = set_findings(run_dir, repo_root=repo_root, role=role, candidate=path)
    return [SetRefusal(finding) for finding in findings
            if finding.role == role and not finding.absent and not finding.warn]


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
        declaring = next((analyst for analyst in ANALYSTS
                          if identifier.startswith(record_prefix(analyst))), None)
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
    given), `model` (the exact identifier of the model running the workers,
    recorded in the manifest), and optionally `effort` (its reasoning-effort
    setting) and `source-revision`. For a GitHub
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
    profile_correction_rounds = 2

    def __init__(self, params=None) -> None:
        super().__init__(params)
        # The one form of the source identity that the run slug, destination
        # inspection, the boundary and publication use.
        self.source_identity = normalize_source_identity(
            str(self.params["source-identity"])
        )
        self.job_destinations: dict[str, Path] = {}
        self.job_measurements: dict[str, dict[str, Any]] = {}
        model = self.params.get("model")
        if not isinstance(model, str) or not model.strip():
            raise ValueError(
                "model is required: the exact identifier of the model running this "
                "workflow's workers, such as claude-fable-5-1 or gpt-6.1-sol"
            )
        self.source_revision = self.params.get("source-revision")
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
        write_file(run_dir / RUN_METADATA, json.dumps({
            **{key: opening[key] for key in ("inputs-commit", "run-date")},
            **{key: str(self.params[key]) for key in ("model", "effort") if self.params.get(key)},
        }) + "\n")
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

        start_manifest(run_dir)
        self.run_job(ctx, self.boundary_job(run_dir, frozen))
        fields, _ = split((run_dir / slot("boundary")).read_text(encoding="utf-8"))
        self.write_run_state(run_dir, opening, fields)

        if fields["result-disposition"] != "complete":
            self.close_without_analysis(run_dir, opening, fields)
            return

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
            self.replace(run_dir / slot("memory-profile"), (run_dir / round_file("profile", profile_round)).read_bytes())
            self.run_job(ctx, self.profile_verification_job(run_dir, profile_round))
            self.replace(run_dir / slot("profile-verification"), (run_dir / round_file("profile-verification", profile_round)).read_bytes())
            profile_verification = (run_dir / round_file("profile-verification", profile_round)).read_text(encoding="utf-8")
            blockers = section(split(profile_verification)[1], "Blockers").strip()
            if blockers == "none":
                break
            if profile_round == self.profile_correction_rounds:
                raise StopRun("the profile verification of the last round names blockers: " + blockers)

        judged = (round_file("verification", round_), round_file("profile-verification", profile_round))
        for synthesis_round in range(self.synthesis_correction_rounds + 1):
            self.run_job(ctx, self.synthesis_job(run_dir, synthesis_round, judged))
            self.replace(run_dir / slot("synthesis"), (run_dir / round_file("synthesis", synthesis_round)).read_bytes())
            self.run_job(ctx, self.synthesis_verification_job(run_dir, synthesis_round, judged))
            self.replace(run_dir / slot("synthesis-verification"), (run_dir / round_file("synthesis-verification", synthesis_round)).read_bytes())
            synthesis_verification = (run_dir / round_file("synthesis-verification", synthesis_round)).read_text(encoding="utf-8")
            blockers = section(split(synthesis_verification)[1], "Blockers").strip()
            if blockers == "none":
                break
            if synthesis_round == self.synthesis_correction_rounds:
                raise StopRun("the synthesis verification of the last round names blockers: " + blockers)

        self.assemble(run_dir, opening, fields)
        self.validate_set(run_dir)

        spec = PublicationSpec(
            repo_root=repo_root,
            run_state_path=run_dir / RUN_STATE,
            generated_candidate_path=run_dir / slot("overview"),
            generated_destination=opening["review-path"],
            expected_incumbent_sha256=opening["expected-incumbent-sha256"],
        )
        ctx.effect(
            "publish",
            partial(self.publish, spec),
            inputs=(slot("overview"), MANIFEST),
            recognize=partial(self.recognize_publication, spec),
        )

    # Jobs

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
                other: split((run_dir / slot(other)).read_text(encoding="utf-8"))[1]
                for other in ANALYSTS if other != member
            }
            self.replace(run_dir / requests(member, round_), render_requests(
                member, verification, section(split(text)[1], "Blockers").strip(), bodies,
            ).encode("utf-8"))
        job = self.analyst_job(run_dir, member, round_)
        self.run_job(ctx, job)
        destination = self.job_destinations[job.name]
        self.replace(run_dir / slot(member), destination.read_bytes())
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
        # The validator only captures in memory. Persist from coordinator code
        # before wait ends a refused path, and before the engine moves its output.
        # Clear stale captures when no validator is called (missing output,
        # changed inputs, or a problem report).
        self.job_measurements.pop(job.name, None)
        handle = ctx.agent(job)
        measurement = self.job_measurements.pop(job.name, None)
        if measurement is not None:
            content = (json.dumps(measurement, sort_keys=True, indent=2) + "\n").encode("utf-8")
            key = sha256(content).hexdigest()
            self.replace(ctx.run_dir / MEASUREMENTS / job.name / f"{key}.json", content)
        handle.wait()
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
        role: str,
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
        validator = self.measured_validator(name, role, run_dir, validator) if validator is not None else None
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
            "validation-set": str(run_dir / OUTPUT_DIR),
            "validation-member": analysis_layout().path(role),
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

    def measured_validator(
        self, name: str, role: str, run_dir: Path,
        validator: Callable[[Path], Sequence[str]],
    ) -> Callable[[Path], list[str]]:
        """Capture exactly one validation's raw counts and delivered text, no IO writes.

        These are validator judgments, not engine acceptance or attempt history:
        the engine may refuse changed inputs without calling the validator.
        Content-addressed records retain changed judgments of the same bytes,
        but deliberately do not count identical replay observations as attempts.
        """
        def judge(path: Path) -> list[str]:
            candidate_sha256 = digest(path)
            reasons = validation_reasons(validator, path)
            rendered = actionable_refusals(lambda _: reasons, path)
            if digest(path) != candidate_sha256:
                raise ValueError("candidate bytes changed during validation")
            set_reasons = [reason for reason in reasons if reason.startswith(SET_LABEL)]
            roles = [getattr(reason, "role", None) for reason in set_reasons]
            self.job_measurements[name] = {
                "version": 1,
                "run-id": run_dir.name,
                "job": name,
                "role": role,
                "candidate-sha256": candidate_sha256,
                "findings": rendered,
                "set-findings": [reason for reason in rendered if reason.startswith(SET_LABEL)],
                "set-finding-roles": roles,
                "another-member-count": sum(found is not None and found != role for found in roles),
                "unattributed-set-finding-count": roles.count(None),
                "residue-rule-counts": dict(Counter(
                    refusal_rule(reason) for reason in reasons if not reason.startswith(SET_LABEL)
                )),
            }
            return rendered
        return judge

    def boundary_job(self, run_dir: Path, frozen: dict[str, Any] | None = None) -> Job:
        frozen_parameters = {} if frozen is None else {
            "source-revision": frozen["revision"], "source-path": frozen["path"],
        }
        return self.job(
            run_dir,
            "boundary",
            slot("boundary"),
            role="boundary", reads={"opening": RUN_METADATA},
            extra=(BOUNDARY_CONTRACT, SOURCES_CONTRACT, BOUNDARY_TYPE),
            parameters={
                "source-identity": one_line(self.source_identity),
                **frozen_parameters,
            },
            source=str(self.params["source"]),
            validator=lambda path: set_role_refusals(
                path, run_dir=run_dir, repo_root=self.repo, role="boundary",
            ) + boundary_refusals(
                path, repo_root=self.repo, run_id=run_dir.name,
                identity=self.source_identity, frozen=frozen,
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
        reads = {"boundary": slot("boundary")}
        parameters = {"round": "correction" if round_ else "first"}
        if round_:
            reads.update({"previous-report": report(member, round_ - 1), "requests": requests(member, round_)})
            parameters["answers"] = str(run_dir / "jobs" / name / ANSWERS_NAME)
        else:
            reads.update({read: report(read, 0) for read in spec["reads"]})
        checks = [partial(set_role_refusals, run_dir=run_dir, repo_root=self.repo, role=member)]
        if round_:
            checks.append(partial(
                correction_refusals, member=member,
                previous=run_dir / reads["previous-report"], packet=run_dir / reads["requests"],
            ))
        return self.job(
            run_dir, name, report(member, round_), role=member, reads=reads, instruction=member,
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
        reads = {"boundary": slot("boundary"), **{member: report(member, versions[member]) for member in ANALYSTS}}
        if round_ > 0:
            reads["previous-reconciliation"] = reconciliation(round_ - 1)
            reads.update({kind: round_file(kind, round_ - 1) for kind in ("verification", "set-check")})
            reads.update(self.correction_reads(corrected, versions))
        return self.job(
            run_dir,
            f"reconcile-{round_}",
            reconciliation(round_),
            role="reconciliation", reads=reads,
            instruction="reconcile",
            extra=RECORD_CONTRACTS,
            parameters={"round": "after-blockers" if round_ else "first"},
            validator=partial(set_role_refusals, run_dir=run_dir, repo_root=self.repo, role="reconciliation"),
        )

    def record_check(self, run_dir: Path) -> list[str]:
        """The round's whole-set check, before any profile or overview exists:
        each record member's own validation, then the working set's findings.

        Absent members are expected mid-run and dropped. Findings of the
        roles written after the rounds are dropped too: a replay finds the
        final profile and overview in place, and must write the same check
        the round first wrote.
        """
        output = run_dir / OUTPUT_DIR
        layout = analysis_layout()
        failures = []
        for role in RECORD_ROLES:
            name = layout.path(role)
            failures.extend(f"{name}: {failure}" for failure in member_refusals(output / name, repo_root=self.repo))
        failures.extend(
            SET_LABEL + finding.render() for finding in set_findings(run_dir, repo_root=self.repo)
            if not finding.absent and finding.role not in LATER_ROLES
        )
        return failures

    def close_round(
        self, ctx, run_dir: Path, fields: dict[str, Any], round_: int,
        versions: Mapping[str, int], corrected: Sequence[str],
    ) -> str:
        """Make the round's reports current, check the records, and independently judge them."""
        for member in ANALYSTS:
            self.replace(run_dir / slot(member), (run_dir / report(member, versions[member])).read_bytes())
        self.replace(run_dir / slot("reconciliation"), (run_dir / reconciliation(round_)).read_bytes())
        failures = self.record_check(run_dir)
        write_file(run_dir / round_file("set-check", round_),
                   "# Record set check\n\n" + ("\n".join(f"- {failure}" for failure in failures) or "none") + "\n")
        self.run_job(ctx, self.verification_job(
            run_dir, round_, versions, corrected,
            validator=partial(self.record_verification_refusals, run_dir, failures=failures),
        ))
        self.replace(run_dir / slot("record-verification"), (run_dir / round_file("verification", round_)).read_bytes())
        return (run_dir / round_file("verification", round_)).read_text(encoding="utf-8")

    def verifier_refusals(self, run_dir: Path, verifies: str) -> Callable[[Path], list[str]]:
        role = {"records": "record-verification", "profile": "profile-verification",
                "synthesis": "synthesis-verification"}[verifies]
        return partial(set_role_refusals, run_dir=run_dir, repo_root=self.repo, role=role)

    def verification_job(
        self, run_dir: Path, round_: int, versions: Mapping[str, int],
        corrected: Sequence[str],
        *, validator: Callable[[Path], Sequence[str]] | None = None,
    ) -> Job:
        reads = {"boundary": slot("boundary"), "reconciliation": slot("reconciliation"),
                 **{member: report(member, versions[member]) for member in ANALYSTS},
                 "set-check": round_file("set-check", round_)}
        if round_ > 0:
            reads["previous-verification"] = round_file("verification", round_ - 1)
            reads.update(self.correction_reads(corrected, versions))
        return self.job(
            run_dir, f"verify-{round_}", round_file("verification", round_),
            role="record-verification", reads=reads, instruction="verify",
            extra=(*RECORD_CONTRACTS, BOUNDARY_CONTRACT, VERIFICATION_CONTRACT),
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
        return refusals

    def profile_job(self, run_dir: Path, round_: int) -> Job:
        reads = {"boundary": slot("boundary"), "runtime": slot("runtime"), "memory": slot("memory"),
                 "epistemic": slot("epistemic"), "reconciliation": slot("reconciliation")}
        if round_:
            reads.update({"previous-profile": round_file("profile", round_ - 1),
                          "verification": round_file("profile-verification", round_ - 1)})
        return self.job(
            run_dir, "profile" if round_ == 0 else f"profile-{round_}",
            round_file("profile", round_), role="memory-profile", reads=reads, instruction="profile",
            extra=(SOURCES_CONTRACT, RECORDS_CONTRACT, PROFILE_CONTRACT),
            parameters={"round": "after-blockers" if round_ else "first"},
            validator=partial(self.profile_refusals, run_dir),
        )

    def profile_refusals(self, run_dir: Path, path: Path) -> list[str]:
        refusals = set_role_refusals(path, run_dir=run_dir, repo_root=self.repo, role="memory-profile")
        try:
            metadata, _ = split(path.read_text(encoding="utf-8"))
        except ValueError:
            return refusals
        # Require the current write contract only at scheduled job acceptance.
        # Immutable set and finalization readers still interpret retained v1.
        comparison = metadata.get("memory-comparison")
        if (not isinstance(comparison, dict)
                or type(comparison.get("version")) is not int
                or comparison["version"] != 2):
            refusals.append("new workflow profiles require memory-comparison version: 2")
        if metadata.get("source-identity") != self.source_identity:
            refusals.append(f"profile identity: source-identity {metadata.get('source-identity')!r} "
                            f"does not match the run's expected {self.source_identity!r}")
        return refusals

    def profile_verification_job(self, run_dir: Path, round_: int) -> Job:
        return self.job(
            run_dir, "verify-profile" if round_ == 0 else f"verify-profile-{round_}",
            round_file("profile-verification", round_), role="profile-verification",
            reads={"profile": round_file("profile", round_), "boundary": slot("boundary"),
                   "runtime": slot("runtime"), "memory": slot("memory"), "epistemic": slot("epistemic"),
                   "reconciliation": slot("reconciliation")},
            instruction="verify-profile",
            extra=(SOURCES_CONTRACT, RECORDS_CONTRACT, PROFILE_CONTRACT, VERIFICATION_CONTRACT),
            validator=partial(self.profile_verification_refusals, run_dir),
        )

    def profile_verification_refusals(self, run_dir: Path, path: Path) -> list[str]:
        return self.verifier_refusals(run_dir, "profile")(path)

    def synthesis_job(self, run_dir: Path, round_: int, judged: tuple[str, str] = ("", "")) -> Job:
        """The synthesizer reads the accepted members and the final record and
        profile verifications, whose limits its Limitations must carry."""
        reads = {"boundary": slot("boundary"), "runtime": slot("runtime"), "memory": slot("memory"),
                 "epistemic": slot("epistemic"), "reconciliation": slot("reconciliation"),
                 **self.judged_reads(judged)}
        if round_:
            reads.update({"previous-synthesis": round_file("synthesis", round_ - 1),
                          "verification": round_file("synthesis-verification", round_ - 1)})
        return self.job(
            run_dir, "synthesize" if round_ == 0 else f"synthesize-{round_}",
            round_file("synthesis", round_), role="synthesis", reads=reads, instruction="synthesize",
            extra=SYNTHESIS_CONTRACTS,
            parameters={"round": "after-blockers" if round_ else "first"},
            validator=partial(set_role_refusals, run_dir=run_dir, repo_root=self.repo, role="synthesis"),
        )

    @staticmethod
    def judged_reads(judged: tuple[str, str]) -> dict[str, str]:
        record, profile = judged
        return {**({"record-verification": record} if record else {}),
                **({"profile-verification": profile} if profile else {})}

    def synthesis_verification_job(self, run_dir: Path, round_: int, judged: tuple[str, str] = ("", "")) -> Job:
        return self.job(
            run_dir, "verify-synthesis" if round_ == 0 else f"verify-synthesis-{round_}",
            round_file("synthesis-verification", round_), role="synthesis-verification",
            reads={"synthesis": round_file("synthesis", round_), "boundary": slot("boundary"),
                   "runtime": slot("runtime"), "memory": slot("memory"), "epistemic": slot("epistemic"),
                   "reconciliation": slot("reconciliation"), **self.judged_reads(judged)},
            instruction="verify-synthesis", extra=(*SYNTHESIS_CONTRACTS, VERIFICATION_CONTRACT),
            validator=partial(self.synthesis_verification_refusals, run_dir, round_),
        )

    def synthesis_verification_refusals(self, run_dir: Path, round_: int, path: Path) -> list[str]:
        return self.verifier_refusals(run_dir, "synthesis")(path)

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
        return (RETAINED_ROOT / source_slug(self.source_identity, str(self.params["system"])) / analysis_layout().path("overview")).as_posix()

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
    ) -> None:
        """Render the final overview after all three independent checks pass."""
        self.replace(run_dir / slot("overview"), self.render_overview(
            run_dir, opening, fields,
        ).encode("utf-8"))
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

    def overview_body(self, run_dir: Path, fields: Mapping[str, Any], index: str) -> str:
        """Entry navigation only; authored accounts remain in their own slots."""
        members = "\n".join(
            f"- [{role.name.replace('-', ' ').capitalize()}](./{role.path})"
            for role in analysis_layout().roles.values()
            if role.name != "overview" and (run_dir / OUTPUT_DIR / role.path).is_file()
        )
        return (
            f"# {self.params['system']} agentic-system analysis\n\n"
            f"## Members\n\nDisposition: `{fields['result-disposition']}`.\n\n{members}\n\n"
            f"## Amendment index\n\n{index}\n\n"
            f"## Deterministic validation\n\n{self.validation_text(run_dir)}\n"
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
    ) -> str:
        synthesis_fields, _ = split((run_dir / slot("synthesis")).read_text(encoding="utf-8"))
        index = amendment_index((run_dir / slot("reconciliation")).read_text(encoding="utf-8"))
        return dump_frontmatter(
            self.overview_frontmatter(opening, fields, one_line(str(synthesis_fields["description"]))),
            self.overview_body(run_dir, fields, index),
        )

    def close_without_analysis(
        self,
        run_dir: Path,
        opening: dict[str, Any],
        fields: dict[str, Any],
    ) -> None:
        """A blocked or out-of-scope run: boundary and entry, no publication."""
        write_file(
            run_dir / slot("overview"),
            dump_frontmatter(
                self.overview_frontmatter(opening, fields),
                self.overview_body(run_dir, fields, "Amended or superseded records: none"),
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

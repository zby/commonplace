"""The analyse-agentic-system workflow as a code-scheduled definition.

Start a run with

    commonplace-workflow start commonplace.lib.agentic_workflow:AnalyseAgenticSystem \\
        --param system=<name> --param source-identity=<identity> \\
        --param source=<the caller's source input> [--param review-path=<path>]

from the repository root. `start` allocates the run ID, AAS-<date>-<system
slug>-<nn> (the slug from the source identity's last path segment, or
the system name), creates the run directory under kb/reports/state/agentic-system-
analysis/, and prints it; the run ID is the directory's name. Each
job's task is an instruction file under `kb/instructions/analyse-agentic-system/
jobs/`, declared as an input, so a change to it reopens the job. The job split
is recorded in `kb/work/analysis-offload-to-code/README.md`.

Opening and publication are effects: opening records values that cannot be
reproduced (the method commit, the run date, the incumbent's digest), and
publication changes the repository outside the run. Everything else code does
is replayed from the run's files in every step.
"""

from __future__ import annotations

import datetime
import json
import posixpath
import re
import subprocess
from collections.abc import Callable, Sequence
from functools import partial
from hashlib import sha256
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import yaml

from commonplace.lib.agentic_finalize import build_manifest
from commonplace.lib.agentic_publication import (
    PublicationSpec,
    atomic_write,
    inspect_destination,
    publish_publication,
    require_publishable_worktree,
    require_running_package_unchanged,
)
from commonplace.lib.agentic_records import section, set_record_errors
from commonplace.lib.agentic_set import (
    OUTPUT_DIR,
    OVERVIEW_NAME,
    RETAINED_ROOT,
    REVIEW_TYPE,
    REVIEWS_ROOT,
    RUN_ID,
    normalize_source_identity,
)
from commonplace.lib.note_parser import parse_document, replace_markdown_links
from commonplace.lib.validation import validate_note
from commonplace.workflow import Job, Recognition, StopRun, Workflow

JOBS = "kb/instructions/analyse-agentic-system/jobs"
STATE_ROOT = Path("kb/reports/state/agentic-system-analysis")
OVERVIEW_TYPE = "types/agentic-system-analysis-overview.md"
RUN_STATE_TYPE = "types/agentic-system-analysis-run-state.md"
# The set's contracts, relative to the job instructions. A job gets as
# declared inputs the type of every member it writes or judges, plus the
# overview type, which defines the conventions every member uses (record
# IDs, conclusion statuses, the set), so the jobs that produce and judge the
# same content load the same definitions.
TYPES = "../../../types"
OVERVIEW_CONTRACT = f"{TYPES}/agentic-system-analysis-overview.md"
RUNTIME_CONTRACT = f"{TYPES}/agentic-system-runtime-report.md"
MEMORY_CONTRACT = f"{TYPES}/agent-memory-analysis-report.md"
EPISTEMIC_CONTRACT = f"{TYPES}/agentic-system-epistemic-report.md"
SET_CONTRACTS = (
    OVERVIEW_CONTRACT,
    RUNTIME_CONTRACT,
    MEMORY_CONTRACT,
    EPISTEMIC_CONTRACT,
)

OPENING = "opening.json"
BOUNDARY = "boundary.md"
CANDIDATE = "review-candidate.md"
RUN_STATE = "run-state.md"
RUNTIME = f"{OUTPUT_DIR}/runtime.md"
MEMORY = f"{OUTPUT_DIR}/memory.md"
EPISTEMIC = f"{OUTPUT_DIR}/epistemic.md"
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
RETURNED = "Returned to the memory analyst"
DESCRIPTION_LENGTH = (50, 250)
"""The length the note schema expects of a description; the reconciliation's
description becomes the overview's and the review's."""


def memory_report(round_: int) -> str:
    return f"memory-report-{round_}.md"


def reconciliation(round_: int) -> str:
    return f"reconcile-{round_}.md"


def round_file(kind: str, round_: int) -> str:
    """A file one reconciliation round's closing writes: `overview-draft`,
    `set-check` or `verification`."""
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
        (repo_root / "kb/types/agentic-system-analysis-overview.schema.yaml").read_text(
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
    path: Path, *, enums: dict[str, list[Any]], identity: str
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
                f"{name} {value!r} is not one of the overview type's values"
            )
    refusals += [
        f"{name} must be a quoted string or null, not {type(fields[name]).__name__}"
        for name in BOUNDARY_FIELDS
        if fields.get(name) is not None and not isinstance(fields[name], str)
    ]
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
        refusals += frozen_source_refusals(source)
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
            return ["source.sha256 must be the SHA-256 of the capture file"]
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
        return [f"the checkout at {path} is not at source.revision; check it out"]
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


def set_bodies(
    *, boundary: Path, reconciled: Path | None = None, **members: Path
) -> dict[str, str]:
    """The bodies of the set these files make, by set name.

    The overview is the boundary's Boundary and evidence and Source register
    followed by the reconciliation's sections; each member keyword names a
    set member without its `.md`. ValueError when a file does not parse.
    """
    _, boundary_body = split(boundary.read_text(encoding="utf-8"))
    overview = boundary_body
    if reconciled is not None:
        overview += "\n" + reconciled.read_text(encoding="utf-8")
    bodies = {OVERVIEW_NAME: overview}
    for name, path in members.items():
        bodies[f"{name}.md"] = split(path.read_text(encoding="utf-8"))[1]
    return bodies


def reference_refusals(bodies: Callable[[], dict[str, str]]) -> list[str]:
    """Every record the bodies cite is declared once among them."""
    try:
        found = bodies()
    except ValueError as error:
        return [f"a set document does not parse: {error}"]
    _, errors = set_record_errors(found)
    return errors


def pass_refusals(
    path: Path, *, repo_root: Path, bodies: Callable[[Path], dict[str, str]]
) -> list[str]:
    """The output of an analyst, which declares records: a valid member whose
    citations resolve against the set so far, which ``bodies`` assembles
    around it."""
    return member_refusals(path, repo_root=repo_root) or reference_refusals(
        partial(bodies, path)
    )


def reconcile_refusals(
    path: Path,
    *,
    boundary: Path,
    runtime: Path,
    report: Path,
    epistemic: Path,
    may_return: bool,
) -> list[str]:
    """The reconciliation's sections, the description's length, the last-round
    rule, and every record it cites, amendments included, declared in the set
    it will make."""
    body = path.read_text(encoding="utf-8")
    refusals = require_sections(
        body, 2, ["Description", "Reconciliation", "Bounded synthesis", "Limitations"]
    )
    description = one_line(section(body, "Description"))
    shortest, longest = DESCRIPTION_LENGTH
    if description and not shortest <= len(description) <= longest:
        refusals.append(
            f"the `## Description` sentence has {len(description)} characters; "
            f"write {shortest} to {longest}"
        )
    returned = RETURNED in headings(body, 2)
    if returned and not may_return:
        refusals.append(
            f"this is the last round: remove `## {RETURNED}` and retain the conflicts "
            "as explicit uncertainty"
        )
    if refusals or returned:
        return refusals
    return reference_refusals(
        partial(
            set_bodies,
            boundary=boundary,
            reconciled=path,
            runtime=runtime,
            memory=report,
            epistemic=epistemic,
        )
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


def verification_refusals(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return require_sections(
        text, 3, ["Semantic verification", "Blockers"]
    ) or blockers_refusals(subsection(text, "Blockers"))


def one_line(text: str) -> str:
    return " ".join(text.split())


def retarget_links(text: str, *, set_dir: str, destination: str) -> str:
    """Rewrite the relative links of set text, which resolve inside the set
    directory, to resolve from ``destination`` into ``set_dir``. Absolute
    URLs and anchor-only links stay as they are."""
    base = posixpath.dirname(destination)

    def retarget(target: str) -> str:
        parts = urlsplit(target.strip())
        if parts.scheme or parts.netloc or not parts.path or parts.path.startswith("/"):
            return target
        path, rest = re.fullmatch(r"([^?#]*)(.*)", target.strip(), re.DOTALL).groups()
        joined = posixpath.normpath(posixpath.join(set_dir, path))
        return posixpath.relpath(joined, base) + rest

    return replace_markdown_links(text, retarget)


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
    given), and optionally `review-path`.

    Jobs: `boundary`; `runtime`; the `memory-<n>` and `epistemic` analysts;
    then rounds of `reconcile-<n>` and `verify-<n>`. Code renders the
    overview and the public review.
    """

    correction_rounds = 2
    """How many reconciliation rounds may follow the first, whether a round
    returned findings to the memory analyst or its verification named blockers."""

    def __init__(self, params=None) -> None:
        super().__init__(params)
        # The one form of the source identity that the run slug, destination
        # inspection, the boundary and publication use.
        self.source_identity = normalize_source_identity(
            str(self.params["source-identity"])
        )

    def run_location(self) -> tuple[str, str]:
        """`AAS-<today>-<slug>` under the analysis state directory.

        The slug is the last path segment of the source identity when it is a
        URL, such as the repository name of a GitHub URL, so reruns of a system
        keep one review path whatever the system is called; otherwise it is the
        system parameter.
        """
        identity = urlsplit(self.source_identity)
        segment = identity.path.rsplit("/", 1)[-1]
        name = segment if identity.scheme and identity.netloc and segment else ""
        name = name or str(self.params["system"])
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        if not slug:
            raise ValueError("neither the source identity nor the system names the run")
        today = datetime.datetime.now(datetime.UTC).date().isoformat()
        return STATE_ROOT.as_posix(), f"AAS-{today}-{slug}"

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
        self.write_run_state(run_dir, opening, {})

        enums = overview_enums(repo_root)
        ctx.agent(
            self.job(
                "boundary",
                BOUNDARY,
                reads=(OPENING,),
                extra=(OVERVIEW_CONTRACT,),
                validator=partial(
                    boundary_refusals, enums=enums, identity=self.source_identity
                ),
                note=(
                    f"The caller's source input: {self.params['source']}\n\n"
                    f"The run's source identity is `{self.source_identity}`. When "
                    "you freeze a source, write exactly this as `source.identity`."
                ),
            )
        ).wait()
        fields, boundary_body = split((run_dir / BOUNDARY).read_text(encoding="utf-8"))
        self.write_run_state(run_dir, opening, fields)

        if fields["result-disposition"] != "complete":
            self.close_without_analysis(run_dir, opening, fields, boundary_body)
            return

        (run_dir / OUTPUT_DIR).mkdir(exist_ok=True)
        ctx.agent(self.runtime_job(run_dir)).wait()
        ctx.parallel(
            lambda: ctx.agent(self.memory_job(run_dir, 0, 0)).wait(),
            lambda: ctx.agent(self.epistemic_job(run_dir)).wait(),
        )

        reconcile = 0
        memory = 0
        reason = None
        while True:
            last = reconcile >= self.correction_rounds
            ctx.agent(
                self.reconcile_job(run_dir, reconcile, memory, reason, not last)
            ).wait()
            text = (run_dir / reconciliation(reconcile)).read_text(encoding="utf-8")
            if RETURNED in headings(text, 2):
                memory += 1
                ctx.agent(self.memory_job(run_dir, memory, reconcile)).wait()
                reconcile += 1
                reason = "returned"
                continue
            verification = self.close_round(
                ctx, run_dir, opening, fields, boundary_body, reconcile, memory
            )
            blockers = subsection(verification, "Blockers")
            if blockers == "none":
                break
            if last:
                raise StopRun(
                    "the semantic verification of the last round names blockers: "
                    + blockers
                )
            reconcile += 1
            reason = "blockers"

        self.assemble(run_dir, opening, fields, boundary_body, reconcile, verification)
        self.validate_set(run_dir)
        self.write_candidate(run_dir, opening, fields)

        spec = PublicationSpec(
            repo_root=repo_root,
            run_state_path=run_dir / RUN_STATE,
            generated_candidate_path=run_dir / CANDIDATE,
            generated_destination=opening["review-path"],
            expected_incumbent_sha256=opening["expected-incumbent-sha256"],
        )
        ctx.effect(
            "publish",
            partial(self.publish, spec),
            inputs=(CANDIDATE, MANIFEST),
            recognize=partial(self.recognize_publication, spec),
        )

    # Jobs

    def job(
        self,
        name: str,
        output: str,
        *,
        reads: Sequence[str] = (),
        norms: bool = False,
        instruction: str | None = None,
        extra: Sequence[str] = (),
        note: str = "",
        validator: Callable[[Path], Sequence[str]] | None = None,
    ) -> Job:
        instruction = instruction or name
        method = [f"{instruction}.md", "worker-rules.md"]
        if norms:
            method.append("judging-norms.md")
        method_paths = [str(self.jobs_dir / file) for file in method]
        method_paths += [str((self.jobs_dir / path).resolve()) for path in extra]
        prompt = (
            f"You are the `{name}` job of the analyse-agentic-system run {self.run_id} "
            f"for the system {self.params['system']}. Follow `{JOBS}/{instruction}.md` "
            "and the other instruction files listed under Inputs; the remaining inputs "
            "are what you work from. The run's state is `run-state.md` in the run "
            f"directory. Your scratch directory is `scratch/{name}/` in the run "
            "directory; write intermediate files there and nowhere else."
        )
        if note:
            prompt += f"\n\n{note}"
        return Job(
            name=name,
            prompt=prompt,
            output=output,
            inputs=(*reads, *method_paths),
            validator=validator,
        )

    def runtime_job(self, run_dir: Path) -> Job:
        """The runtime analyst. Its member cites the boundary's sources and its
        own records."""
        return self.job(
            "runtime",
            RUNTIME,
            reads=(BOUNDARY,),
            norms=True,
            extra=(OVERVIEW_CONTRACT, RUNTIME_CONTRACT),
            validator=partial(
                pass_refusals,
                repo_root=self.repo,
                bodies=lambda path: set_bodies(
                    boundary=run_dir / BOUNDARY, runtime=path
                ),
            ),
        )

    def epistemic_job(self, run_dir: Path) -> Job:
        """The epistemic analyst. It runs beside the memory analyst, so its
        member cites the boundary's sources, the runtime member and its own
        records."""
        return self.job(
            "epistemic",
            EPISTEMIC,
            reads=(BOUNDARY, RUNTIME),
            norms=True,
            extra=(
                "../../analyse-external-system-epistemic-architecture.md",
                OVERVIEW_CONTRACT,
                EPISTEMIC_CONTRACT,
                RUNTIME_CONTRACT,
            ),
            validator=partial(
                pass_refusals,
                repo_root=self.repo,
                bodies=lambda path: set_bodies(
                    boundary=run_dir / BOUNDARY,
                    runtime=run_dir / RUNTIME,
                    epistemic=path,
                ),
            ),
        )

    def memory_job(self, run_dir: Path, round_: int, returned_by: int) -> Job:
        """One round of the memory analyst. Its report cites the boundary's
        sources, the runtime member and its own records; a correction round,
        which runs after the epistemic member exists, may cite that member too."""
        reads: tuple[str, ...] = (BOUNDARY, RUNTIME)
        note = "This is the first round."
        cited = {"runtime": run_dir / RUNTIME}
        if round_ > 0:
            reads += (EPISTEMIC, memory_report(round_ - 1), reconciliation(returned_by))
            note = (
                f"This is correction round {round_}: the previous report is "
                f"`{memory_report(round_ - 1)}` and the reconciliation that returned "
                f"findings is `{reconciliation(returned_by)}`."
            )
            cited["epistemic"] = run_dir / EPISTEMIC
        return self.job(
            f"memory-{round_}",
            memory_report(round_),
            reads=reads,
            instruction="memory",
            norms=True,
            extra=(
                "../../analyse-agent-memory.md",
                OVERVIEW_CONTRACT,
                MEMORY_CONTRACT,
                RUNTIME_CONTRACT,
            ),
            note=note,
            validator=partial(
                pass_refusals,
                repo_root=self.repo,
                bodies=lambda path: set_bodies(
                    boundary=run_dir / BOUNDARY, memory=path, **cited
                ),
            ),
        )

    def reconcile_job(
        self,
        run_dir: Path,
        round_: int,
        memory: int,
        reason: str | None,
        may_return: bool,
    ) -> Job:
        report = memory_report(memory)
        reads: tuple[str, ...] = (BOUNDARY, RUNTIME, report, EPISTEMIC)
        note = (
            f"This is reconciliation round {round_}. The memory report is `{report}`."
        )
        if round_ > 0:
            reads += (reconciliation(round_ - 1),)
            note += f" The previous reconciliation is `{reconciliation(round_ - 1)}`."
        if reason == "blockers":
            previous = round_ - 1
            reads += tuple(
                round_file(kind, previous) for kind in ("verification", "set-check")
            )
            note += (
                f" The verification of round {previous} named blockers: resolve each "
                f"one stated in `{round_file('verification', previous)}`."
            )
        note += (
            " This round may return findings to the memory analyst."
            if may_return
            else " This is the last round: it may not return findings."
        )
        return self.job(
            f"reconcile-{round_}",
            reconciliation(round_),
            reads=reads,
            instruction="reconcile",
            extra=SET_CONTRACTS,
            norms=True,
            note=note,
            validator=partial(
                reconcile_refusals,
                boundary=run_dir / BOUNDARY,
                runtime=run_dir / RUNTIME,
                report=run_dir / report,
                epistemic=run_dir / EPISTEMIC,
                may_return=may_return,
            ),
        )

    def close_round(
        self,
        ctx,
        run_dir: Path,
        opening: dict[str, Any],
        fields: dict[str, Any],
        boundary_body: str,
        round_: int,
        memory: int,
    ) -> str:
        """Assemble the set one reconciliation round makes, check it, and
        verify it. Returns the verification.

        The runtime and epistemic members are already in `output/`; the
        round's memory report goes there byte for byte as the memory member.
        """
        draft = round_file("overview-draft", round_)
        check = round_file("set-check", round_)
        verification = round_file("verification", round_)

        output = run_dir / OUTPUT_DIR
        atomic_write(run_dir / MEMORY, (run_dir / memory_report(memory)).read_bytes())
        overview = self.render_overview(
            run_dir, opening, fields, boundary_body, reconciliation(round_), None
        )
        write_file(run_dir / draft, overview)
        write_file(run_dir / OVERVIEW, overview)
        build_manifest(run_dir)
        failures = validate_note(output, repo_root=self.repo).fails
        write_file(
            run_dir / check,
            "# Set check\n\n"
            + ("\n".join(f"- {failure}" for failure in failures) or "none")
            + "\n",
        )

        ctx.agent(
            self.job(
                f"verify-{round_}",
                verification,
                reads=(draft, RUNTIME, memory_report(memory), EPISTEMIC, check),
                instruction="verify",
                extra=SET_CONTRACTS,
                norms=True,
                validator=partial(
                    self.verified_set_refusals,
                    run_dir,
                    opening,
                    fields,
                    boundary_body,
                    reconciliation(round_),
                    known=set(failures),
                ),
            )
        ).wait()
        return (run_dir / verification).read_text(encoding="utf-8")

    def verified_set_refusals(
        self,
        run_dir: Path,
        opening: dict[str, Any],
        fields: dict[str, Any],
        boundary_body: str,
        final: str,
        path: Path,
        *,
        known: set[str],
    ) -> list[str]:
        """The verification's form, and the set it completes: the overview
        with this verification must add no failure to those the set check
        already listed, which the verification reports as blockers."""
        text = path.read_text(encoding="utf-8")
        refusals = verification_refusals(path)
        if refusals:
            return refusals
        write_file(
            run_dir / OVERVIEW,
            self.render_overview(run_dir, opening, fields, boundary_body, final, text),
        )
        build_manifest(run_dir)
        failures = validate_note(run_dir / OUTPUT_DIR, repo_root=self.repo).fails
        return [
            f"the overview with this verification does not validate: {failure}"
            for failure in failures
            if failure not in known
        ]

    # Steps that code executes

    @staticmethod
    def repo_root(run_dir: Path) -> Path:
        if not RUN_ID.fullmatch(run_dir.name):
            raise ValueError(
                f"{run_dir.name} is not a run ID of the form AAS-YYYY-MM-DD-slug-nn"
            )
        repo_root = run_dir.parents[len(STATE_ROOT.parts)]
        if repo_root / STATE_ROOT != run_dir.parent:
            raise ValueError(f"a run directory must be directly under {STATE_ROOT}")
        return repo_root

    def review_path(self) -> str:
        if "review-path" in self.params:
            return str(self.params["review-path"])
        slug = self.run_id[len("AAS-YYYY-MM-DD-") : -len("-nn")]
        return f"{REVIEWS_ROOT}/{slug}.md"

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
        commit = self.head()
        self.check_opening(commit)
        destination = self.review_path()
        record = {
            "inputs-commit": commit,
            "run-date": datetime.datetime.now(datetime.UTC).date().isoformat(),
            "review-path": destination,
            "expected-incumbent-sha256": self.inspect(destination),
        }
        write_file(run_dir / OPENING, json.dumps(record, indent=2) + "\n")

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

    def assemble(
        self,
        run_dir: Path,
        opening: dict[str, Any],
        fields: dict[str, Any],
        boundary_body: str,
        round_: int,
        verification: str,
    ) -> None:
        """Complete the accepted round's set with the verified overview.

        The members are in `output/` from the round's closing, which copied
        its memory report there."""
        write_file(
            run_dir / OVERVIEW,
            self.render_overview(
                run_dir,
                opening,
                fields,
                boundary_body,
                reconciliation(round_),
                verification,
            ),
        )
        build_manifest(run_dir)

    def overview_frontmatter(
        self,
        opening: dict[str, Any],
        fields: dict[str, Any],
        description: str | None = None,
    ) -> dict[str, Any]:
        """The overview's frontmatter. A complete run's description is the
        reconciliation's; code writes the others."""
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
        self,
        run_dir: Path,
        opening: dict[str, Any],
        fields: dict[str, Any],
        boundary_body: str,
        final: str,
        verification: str | None,
    ) -> str:
        reconciled = (run_dir / final).read_text(encoding="utf-8")
        semantic = (
            subsection(verification, "Semantic verification")
            if verification is not None
            else "Written after this draft is checked."
        )
        blockers = (
            subsection(verification, "Blockers")
            if verification is not None
            else "Not checked yet."
        )
        rest = (
            f"## Reconciliation\n\n{section(reconciled, 'Reconciliation').strip()}\n\n"
            f"## Bounded synthesis\n\n{section(reconciled, 'Bounded synthesis').strip()}\n\n"
            f"## Limitations\n\n{section(reconciled, 'Limitations').strip()}\n\n"
            "## Verification and blockers\n\n"
            f"### Semantic verification\n\n{semantic}\n\n"
            f"### Deterministic validation\n\n{self.validation_text(run_dir)}\n\n"
            f"### Blockers\n\n{blockers}\n"
        )
        return dump_frontmatter(
            self.overview_frontmatter(
                opening, fields, one_line(section(reconciled, "Description"))
            ),
            self.overview_body(boundary_body, rest),
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
            f"## Reconciliation\n\n{not_reached}\n\n"
            f"## Bounded synthesis\n\n{not_reached}\n\n"
            f"## Limitations\n\n{reason}\n\n"
            "## Verification and blockers\n\n"
            f"### Semantic verification\n\n{not_reached}\n\n"
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

    def write_candidate(
        self, run_dir: Path, opening: dict[str, Any], fields: dict[str, Any]
    ) -> None:
        """Render the public review from the verified overview: its
        description, an evidence-basis line from the boundary, the Bounded
        synthesis and the Limitations, with the set's relative links pointing
        into the retained set."""
        overview, body = split((run_dir / OVERVIEW).read_text(encoding="utf-8"))
        source = fields["source"]
        retained = RETAINED_ROOT / self.run_id
        text = (
            f"# {self.params['system']}\n\n"
            f"Evidence basis: {fields['evidence-tier']} analysis of "
            f"`{source['identity']}` at `{fields['reviewed-boundary']}`, with an "
            f"analysis cutoff of {fields['analysis-cutoff']}.\n\n"
            f"{section(body, 'Bounded synthesis').strip()}\n\n"
            f"## Limitations\n\n{section(body, 'Limitations').strip()}\n"
        )
        frontmatter = {
            "type": REVIEW_TYPE,
            "description": overview["description"],
            "generated-by": "analyse-agentic-system",
            "analysis-run": self.run_id,
            "source-identity": source["identity"],
            "reviewed-revision": fields["reviewed-boundary"],
            "analysis-artifact": (retained / "ARTIFACT.yaml").as_posix(),
            "analysis-artifact-sha256": digest(run_dir / MANIFEST),
        }
        write_file(
            run_dir / CANDIDATE,
            dump_frontmatter(
                frontmatter,
                retarget_links(
                    text,
                    set_dir=retained.as_posix(),
                    destination=opening["review-path"],
                ),
            ),
        )

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
        # Publication writes the retained set before the review, and an
        # interrupted one leaves part of it: that is not "nothing happened".
        retained = spec.repo_root / RETAINED_ROOT / self.run_id
        if (
            state.get("run-status") == "running"
            and current == spec.expected_incumbent_sha256
            and not retained.exists()
        ):
            return Recognition.ABSENT
        return Recognition.UNKNOWN

"""The analyse-agentic-system workflow as a code-scheduled definition.

Start a run with

    commonplace-workflow start commonplace.lib.agentic_workflow:AnalyseAgenticSystem \\
        --param system=<name> --param source-identity=<identity> \\
        --param source=<the caller's source input> [--param review-path=<path>]

from the repository root. `start` allocates the run ID, AAS-<date>-<system
slug>-<nn>, creates the run directory under kb/reports/state/agentic-system-
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
import re
import subprocess
from collections.abc import Callable, Sequence
from functools import partial
from hashlib import sha256
from pathlib import Path
from typing import Any

import yaml

from commonplace.lib.agentic_finalize import (
    build_manifest,
    finalize_memory_report,
    render_finalization_summary,
)
from commonplace.lib.agentic_publication import (
    PublicationSpec,
    inspect_destination,
    publish_publication,
    require_publishable_worktree,
    require_running_package_unchanged,
)
from commonplace.lib.agentic_records import section, set_record_errors
from commonplace.lib.agentic_set import (
    LOCAL_INPUT_NAME,
    LOCAL_REPORT_NAME,
    OUTPUT_DIR,
    OVERVIEW_NAME,
    RETAINED_ROOT,
    REVIEW_TYPE,
    REVIEWS_ROOT,
    RUN_ID,
)
from commonplace.lib.note_parser import parse_document
from commonplace.lib.validation import validate_note
from commonplace.workflow import Job, Recognition, Workflow

JOBS = "kb/instructions/analyse-agentic-system/jobs"
STATE_ROOT = Path("kb/reports/state/agentic-system-analysis")
OVERVIEW_TYPE = "types/agentic-system-analysis-overview.md"
RUN_STATE_TYPE = "types/agentic-system-analysis-run-state.md"

OPENING = "opening.json"
BOUNDARY = "boundary.md"
SCOPING = "scoping.md"
EPISTEMIC_DRAFT = "epistemic-draft.md"
REVIEW_BODY = "review-body.md"
CANDIDATE = "review-candidate.md"
RUN_STATE = "run-state.md"
RUNTIME_DRAFT = "runtime-draft.md"
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
RETURNED = "Returned to the specialist"


def memory_report(round_: int) -> str:
    return f"memory-report-{round_}.md"


def reconciliation(round_: int) -> str:
    return f"reconcile-{round_}.md"


def round_file(kind: str, round_: int) -> str:
    """A file one reconciliation round's closing writes: `runtime-final`,
    `memory-final`, `epistemic-final`, `overview-draft`, `set-check` or
    `verification`."""
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


def boundary_refusals(path: Path, *, enums: dict[str, list[Any]]) -> list[str]:
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


def member_refusals(path: Path, *, repo_root: Path) -> list[str]:
    return list(validate_note(path, repo_root=repo_root).fails)


def reconcile_refusals(
    path: Path, *, report: Path, runtime: Path, may_return: bool
) -> list[str]:
    body = path.read_text(encoding="utf-8")
    refusals = require_sections(
        body, 2, ["Reconciliation", "Bounded synthesis", "Limitations"]
    )
    returned = RETURNED in headings(body, 2)
    if returned and not may_return:
        refusals.append(
            f"this is the last round: remove `## {RETURNED}` and retain the conflicts "
            "as explicit uncertainty"
        )
    if refusals or returned:
        return refusals
    try:
        _, runtime_body = split(runtime.read_text(encoding="utf-8"))
        finalize_memory_report(
            report.read_text(encoding="utf-8"),
            overview_body=body,
            runtime_body=runtime_body,
        )
    except ValueError as error:
        return [
            f"the memory report cannot be finalized from this reconciliation: {error}"
        ]
    return []


def runtime_final_refusals(
    path: Path,
    *,
    repo_root: Path,
    boundary: Path,
    reconciled: Path,
    report: Path,
    epistemic: Path,
) -> list[str]:
    """The runtime member, and every record the set will reference declared.

    The references are resolved as the assembled set will resolve them: the
    overview's Source register and reconciled sections, this member, the memory
    member finalized against it, and the epistemic draft's canonical IDs.
    """
    refusals = member_refusals(path, repo_root=repo_root)
    if refusals:
        return refusals
    try:
        _, runtime_body = split(path.read_text(encoding="utf-8"))
        _, boundary_body = split(boundary.read_text(encoding="utf-8"))
        reconciled_body = reconciled.read_text(encoding="utf-8")
        memory = finalize_memory_report(
            report.read_text(encoding="utf-8"),
            overview_body=reconciled_body,
            runtime_body=runtime_body,
        )
        _, memory_body = split(memory.text)
    except ValueError as error:
        return [f"the memory report cannot be finalized against this member: {error}"]
    returns = "## Returns to the coordinator"
    epistemic_body = epistemic.read_text(encoding="utf-8").split(returns)[0]
    _, errors = set_record_errors(
        {
            "overview.md": f"{boundary_body}\n{reconciled_body}",
            "runtime.md": runtime_body,
            "memory.md": memory_body,
            "epistemic.md": epistemic_body,
        }
    )
    return errors


def reference_refusals(
    path: Path,
    *,
    repo_root: Path,
    boundary: Path,
    reconciled: Path,
    runtime: Path,
    memory: Path,
) -> list[str]:
    """The epistemic member, and every record it cites declared in the set."""
    refusals = member_refusals(path, repo_root=repo_root)
    if refusals:
        return refusals
    try:
        bodies = {
            name: split(file.read_text(encoding="utf-8"))[1]
            for name, file in (
                ("runtime.md", runtime),
                ("memory.md", memory),
                ("epistemic.md", path),
            )
        }
        _, boundary_body = split(boundary.read_text(encoding="utf-8"))
    except ValueError as error:
        return [f"a set member does not parse: {error}"]
    bodies["overview.md"] = f"{boundary_body}\n{reconciled.read_text(encoding='utf-8')}"
    _, errors = set_record_errors(bodies)
    return errors


def review_body_refusals(path: Path) -> list[str]:
    try:
        fields, body = split(path.read_text(encoding="utf-8"))
    except ValueError as error:
        return [f"review-body.md does not parse: {error}"]
    refusals = []
    if (
        set(fields) != {"description"}
        or not str(fields.get("description") or "").strip()
    ):
        refusals.append("the frontmatter must have only a non-empty `description`")
    lines = body.strip().splitlines()
    if not lines or not lines[0].startswith("# "):
        refusals.append("the body must open with `# <System>`")
    if not any(line.startswith("Evidence basis:") for line in lines):
        refusals.append("the body needs one line starting `Evidence basis:`")
    return refusals


def dump_frontmatter(fields: dict[str, Any], body: str) -> str:
    serialized = yaml.safe_dump(fields, sort_keys=False, allow_unicode=True, width=1000)
    return f"---\n{serialized}---\n\n{body.strip()}\n"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


# The definition


class AnalyseAgenticSystem(Workflow):
    """Analyse one external agentic system at one frozen evidence boundary.

    Parameters: `system` (the name the caller gave), `source-identity` (the
    stable identity destination inspection uses), `source` (the caller's
    source input, as given), and optionally `review-path`.
    """

    correction_rounds = 2
    """How many reconciliation rounds may follow the first, whether a round
    returned findings to the specialist or its verification named blockers."""

    def run_location(self) -> tuple[str, str]:
        """`AAS-<today>-<system-slug>` under the analysis state directory."""
        slug = re.sub(r"[^a-z0-9]+", "-", str(self.params["system"]).lower()).strip("-")
        if not slug:
            raise ValueError("the system parameter gives no name for the run ID")
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
                validator=partial(boundary_refusals, enums=enums),
                note=f"The caller's source input: {self.params['source']}",
            )
        ).wait()
        fields, boundary_body = split((run_dir / BOUNDARY).read_text(encoding="utf-8"))
        self.write_run_state(run_dir, opening, fields)

        if fields["result-disposition"] != "complete":
            self.close_without_analysis(run_dir, opening, fields, boundary_body)
            return

        member = partial(member_refusals, repo_root=repo_root)
        ctx.agent(
            self.job(
                "runtime",
                RUNTIME_DRAFT,
                reads=(BOUNDARY,),
                norms=True,
                validator=member,
            )
        ).wait()
        ctx.agent(
            self.job(
                "scoping",
                SCOPING,
                reads=(BOUNDARY, RUNTIME_DRAFT),
                validator=lambda path: require_sections(
                    path.read_text(encoding="utf-8"),
                    3,
                    ["Memory/context scope", "Epistemic scope"],
                ),
            )
        ).wait()
        self.write_memory_input(run_dir, fields, boundary_body)

        ctx.parallel(
            lambda: ctx.agent(self.memory_job(0, 0, member)).wait(),
            lambda: ctx.agent(
                self.job(
                    "epistemic",
                    EPISTEMIC_DRAFT,
                    reads=(BOUNDARY, RUNTIME_DRAFT, SCOPING),
                    norms=True,
                    extra=("../../analyse-external-system-epistemic-architecture.md",),
                )
            ).wait(),
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
                ctx.agent(self.memory_job(memory, reconcile, member)).wait()
                reconcile += 1
                reason = "returned"
                continue
            verification = self.close_round(
                ctx, run_dir, opening, fields, boundary_body, reconcile, memory
            )
            blockers = subsection(verification, "Blockers")
            if blockers.lower().rstrip(".") == "none":
                break
            if last:
                raise ValueError(
                    "the semantic verification of the last round names blockers: "
                    + blockers
                )
            reconcile += 1
            reason = "blockers"

        self.assemble(
            run_dir, opening, fields, boundary_body, reconcile, memory, verification
        )
        self.validate_set(run_dir)

        ctx.agent(
            self.job(
                "review",
                REVIEW_BODY,
                reads=(OVERVIEW, RUNTIME, MEMORY, EPISTEMIC, MANIFEST),
                validator=review_body_refusals,
            )
        ).wait()
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

    def memory_job(
        self, round_: int, returned_by: int, member: Callable[[Path], list[str]]
    ) -> Job:
        reads: tuple[str, ...] = (LOCAL_INPUT_NAME,)
        note = "This is the first pass."
        if round_ > 0:
            reads += (memory_report(round_ - 1), reconciliation(returned_by))
            note = (
                f"This is correction round {round_}: the previous report is "
                f"`{memory_report(round_ - 1)}` and the reconciliation that returned "
                f"findings is `{reconciliation(returned_by)}`."
            )
        return self.job(
            f"memory-{round_}",
            memory_report(round_),
            reads=reads,
            instruction="memory",
            extra=("../../analyse-agent-memory.md",),
            note=note,
            validator=member,
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
        reads: tuple[str, ...] = (
            BOUNDARY,
            SCOPING,
            RUNTIME_DRAFT,
            report,
            EPISTEMIC_DRAFT,
        )
        note = (
            f"This is reconciliation round {round_}. The memory report is `{report}`."
        )
        if round_ > 0:
            reads += (reconciliation(round_ - 1),)
            note += f" The previous reconciliation is `{reconciliation(round_ - 1)}`."
        if reason == "blockers":
            previous = round_ - 1
            reads += tuple(
                round_file(kind, previous)
                for kind in (
                    "verification",
                    "set-check",
                    "runtime-final",
                    "epistemic-final",
                )
            )
            note += (
                f" The verification of round {previous} named blockers: resolve each "
                f"one stated in `{round_file('verification', previous)}`."
            )
        note += (
            " This round may return findings to the specialist."
            if may_return
            else " This is the last round: it may not return findings."
        )
        return self.job(
            f"reconcile-{round_}",
            reconciliation(round_),
            reads=reads,
            instruction="reconcile",
            norms=True,
            note=note,
            validator=partial(
                reconcile_refusals,
                report=run_dir / report,
                runtime=run_dir / RUNTIME_DRAFT,
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
        """Write the members of one reconciliation round, check the set they
        make, and verify it. Returns the verification."""
        reconciled = reconciliation(round_)
        report = memory_report(memory)
        runtime = round_file("runtime-final", round_)
        memory_final = round_file("memory-final", round_)
        epistemic = round_file("epistemic-final", round_)
        draft = round_file("overview-draft", round_)
        check = round_file("set-check", round_)
        verification = round_file("verification", round_)
        references = partial(
            reference_refusals,
            repo_root=self.repo,
            boundary=run_dir / BOUNDARY,
            reconciled=run_dir / reconciled,
        )

        ctx.agent(
            self.job(
                f"runtime-final-{round_}",
                runtime,
                reads=(BOUNDARY, RUNTIME_DRAFT, reconciled, report, EPISTEMIC_DRAFT),
                instruction="runtime-final",
                norms=True,
                validator=partial(
                    runtime_final_refusals,
                    repo_root=self.repo,
                    boundary=run_dir / BOUNDARY,
                    reconciled=run_dir / reconciled,
                    report=run_dir / report,
                    epistemic=run_dir / EPISTEMIC_DRAFT,
                ),
            )
        ).wait()
        summary = self.finalize(run_dir, memory, round_)
        ctx.agent(
            self.job(
                f"epistemic-final-{round_}",
                epistemic,
                reads=(EPISTEMIC_DRAFT, reconciled, runtime, memory_final),
                instruction="epistemic-final",
                validator=partial(
                    references,
                    runtime=run_dir / runtime,
                    memory=run_dir / memory_final,
                ),
            )
        ).wait()

        overview = self.render_overview(
            run_dir, opening, fields, boundary_body, reconciled, summary, None
        )
        (run_dir / draft).write_text(overview, encoding="utf-8")
        output = run_dir / OUTPUT_DIR
        output.mkdir(exist_ok=True)
        for source, target in (
            (runtime, RUNTIME),
            (memory_final, MEMORY),
            (epistemic, EPISTEMIC),
            (draft, OVERVIEW),
        ):
            (run_dir / target).write_bytes((run_dir / source).read_bytes())
        build_manifest(run_dir)
        failures = validate_note(output, repo_root=self.repo).fails
        (run_dir / check).write_text(
            "# Set check\n\n"
            + ("\n".join(f"- {failure}" for failure in failures) or "none")
            + "\n",
            encoding="utf-8",
        )

        ctx.agent(
            self.job(
                f"verify-{round_}",
                verification,
                reads=(draft, runtime, memory_final, epistemic, check),
                instruction="verify",
                norms=True,
                validator=lambda path: require_sections(
                    path.read_text(encoding="utf-8"),
                    3,
                    ["Semantic verification", "Blockers"],
                ),
            )
        ).wait()
        return (run_dir / verification).read_text(encoding="utf-8")

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
            source_identity=str(self.params["source-identity"]),
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
        (run_dir / OPENING).write_text(
            json.dumps(record, indent=2) + "\n", encoding="utf-8"
        )

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
        path.write_text(dump_frontmatter(frontmatter, body), encoding="utf-8")

    def write_memory_input(
        self, run_dir: Path, fields: dict[str, Any], boundary_body: str
    ) -> None:
        _, runtime_body = split((run_dir / RUNTIME_DRAFT).read_text(encoding="utf-8"))
        scope = subsection(
            (run_dir / SCOPING).read_text(encoding="utf-8"), "Memory/context scope"
        )
        source = yaml.safe_dump(fields["source"], sort_keys=False).strip()
        text = (
            f"# Memory specialist input — {self.run_id}\n\n"
            f"- Run: {self.run_id}\n- System: {self.params['system']}\n"
            f"- Reviewed boundary: {fields['reviewed-boundary']}\n"
            f"- Target class: {fields['target-class']}; boundary kind: {fields['boundary-kind']}\n\n"
            f"## Source\n\n```yaml\n{source}\n```\n\n"
            f"## Boundary and source register\n\n{boundary_body.strip()}\n\n"
            f"## Memory scope, depth, exclusions and question\n\n{scope}\n\n"
            "## Provisional canonical records\n\n"
            "The runtime member's records below are source-checkable seeds, not accepted "
            "conclusions. Route records carry the fields of the runtime report type's "
            "Routes records.\n\n"
            f"{runtime_body.strip()}\n"
        )
        (run_dir / LOCAL_INPUT_NAME).write_text(text, encoding="utf-8")

    def finalize(self, run_dir: Path, memory: int, round_: int) -> str:
        """Copy the memory report into place and write the round's memory member."""
        report = run_dir / LOCAL_REPORT_NAME
        report.write_bytes((run_dir / memory_report(memory)).read_bytes())
        body = (run_dir / reconciliation(round_)).read_text(encoding="utf-8")
        runtime = run_dir / round_file("runtime-final", round_)
        _, runtime_body = split(runtime.read_text(encoding="utf-8"))
        result = finalize_memory_report(
            report.read_text(encoding="utf-8"),
            overview_body=body,
            runtime_body=runtime_body,
        )
        (run_dir / round_file("memory-final", round_)).write_text(
            result.text, encoding="utf-8"
        )
        return render_finalization_summary(result)

    def assemble(
        self,
        run_dir: Path,
        opening: dict[str, Any],
        fields: dict[str, Any],
        boundary_body: str,
        round_: int,
        memory: int,
        verification: str,
    ) -> None:
        """Put the accepted round's members and the verified overview in `output/`."""
        summary = self.finalize(run_dir, memory, round_)
        for kind, target in (
            ("runtime-final", RUNTIME),
            ("memory-final", MEMORY),
            ("epistemic-final", EPISTEMIC),
        ):
            (run_dir / target).write_bytes(
                (run_dir / round_file(kind, round_)).read_bytes()
            )
        (run_dir / OVERVIEW).write_text(
            self.render_overview(
                run_dir,
                opening,
                fields,
                boundary_body,
                reconciliation(round_),
                summary,
                verification,
            ),
            encoding="utf-8",
        )
        build_manifest(run_dir)

    def overview_frontmatter(
        self, opening: dict[str, Any], fields: dict[str, Any]
    ) -> dict[str, Any]:
        disposition = fields["result-disposition"]
        boundary = fields.get("reviewed-boundary") or "no established boundary"
        return {
            "type": OVERVIEW_TYPE,
            "description": (
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
        summary: str,
        verification: str | None,
    ) -> str:
        scoping = (run_dir / SCOPING).read_text(encoding="utf-8")
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
            "## Lens scoping\n\n"
            f"### Memory/context scope\n\n{subsection(scoping, 'Memory/context scope')}\n\n"
            f"### Epistemic scope\n\n{subsection(scoping, 'Epistemic scope')}\n\n"
            f"## Reconciliation\n\n{section(reconciled, 'Reconciliation').strip()}\n\n{summary}\n\n"
            f"## Bounded synthesis\n\n{section(reconciled, 'Bounded synthesis').strip()}\n\n"
            f"## Limitations\n\n{section(reconciled, 'Limitations').strip()}\n\n"
            "## Verification and blockers\n\n"
            f"### Semantic verification\n\n{semantic}\n\n"
            f"### Deterministic validation\n\n{self.validation_text(run_dir)}\n\n"
            f"### Blockers\n\n{blockers}\n"
        )
        return dump_frontmatter(
            self.overview_frontmatter(opening, fields),
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
            "## Lens scoping\n\n"
            f"### Memory/context scope\n\n{not_reached}\n\n"
            f"### Epistemic scope\n\n{not_reached}\n\n"
            f"## Reconciliation\n\n{not_reached}\n\n"
            f"## Bounded synthesis\n\n{not_reached}\n\n"
            f"## Limitations\n\n{reason}\n\n"
            "## Verification and blockers\n\n"
            f"### Semantic verification\n\n{not_reached}\n\n"
            f"### Deterministic validation\n\n{self.validation_text(run_dir)}\n\n"
            f"### Blockers\n\n{reason}\n"
        )
        (run_dir / OUTPUT_DIR).mkdir(exist_ok=True)
        (run_dir / OVERVIEW).write_text(
            dump_frontmatter(
                self.overview_frontmatter(opening, fields),
                self.overview_body(boundary_body, rest),
            ),
            encoding="utf-8",
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
        extra, body = split((run_dir / REVIEW_BODY).read_text(encoding="utf-8"))
        frontmatter = {
            "type": REVIEW_TYPE,
            "description": extra["description"],
            "generated-by": "analyse-agentic-system",
            "analysis-run": self.run_id,
            "source-identity": fields["source"]["identity"],
            "reviewed-revision": fields["reviewed-boundary"],
            "analysis-artifact": (
                RETAINED_ROOT / self.run_id / "ARTIFACT.yaml"
            ).as_posix(),
            "analysis-artifact-sha256": digest(run_dir / MANIFEST),
        }
        (run_dir / CANDIDATE).write_text(
            dump_frontmatter(frontmatter, body), encoding="utf-8"
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
        if (
            state.get("run-status") == "running"
            and current == spec.expected_incumbent_sha256
        ):
            return Recognition.ABSENT
        return Recognition.UNKNOWN

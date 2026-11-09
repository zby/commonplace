"""The gate sweep: review notes against criteria, one headless worker call per pair.

`pairs()` expands note paths and criterion requests into the applicable
(note, criterion) pairs through `criteria.select`: catalog gate ids and
bundle names filtered by the gate's `requires_type` and `requires_trait`, the
virtual `type` and `collection` lenses resolved from the note's frontmatter
and location, and the `critique` assay. Omitted requests mean all gates:
every bundle plus `type` and `collection`; critique stays opt-in. Each pair's
result contract follows from its criterion: a report for the critique
instruction, a verdict otherwise. A criterion may be a library file outside
the repository, as the gates are in an installed project; its text is read
through the library.

`sweep()` skips pairs whose result file is fresh, unless forced, and asks a
worker for each other pair in one Workjig run: one `checked()` call named
`<note>::<criterion-id>`, with inputs `note` and `criterion` and one output
`review`, checked by the strict outcome parser, so a malformed review is a
rejected attempt whose problem goes into the next prompt. An accepted review
is written as the pair's result file, hashed over the exact texts the worker
was given. A worker problem or a pair out of attempts writes nothing and is
reported for that pair. A launch failure or usage limit stops the sweep: no
pair not yet started is asked, results already written stay, and a rerun
with the same run directory continues.

The prompt around the two inputs is outside the freshness hashes: keep it
mechanical (how to read the inputs and write the result). Judgment belongs
in criterion files, where the hash sees it.

The checkout guard compares `git status` (with untracked files), the content
of every path it lists, and HEAD before and after the run, ignoring the
review state directory. What it can claim: a path it names changed while the
run was open. What it cannot claim: that a worker changed it. Other sessions
edit and commit in this checkout concurrently, so their changes during the
run show up too; a failed guard means "inspect these paths", and nothing is
reverted. It also misses a change to an ignored file and a change undone
before the run ended.
"""

from __future__ import annotations

import hashlib
import subprocess
import threading
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

from commonplace.headless.harness import HARNESSES, Profile
from commonplace.headless.jobs import (
    PROBLEM_REF,
    LaunchFailed,
    OutOfAttempts,
    Run,
    gather,
    input_ref,
    output_ref,
)
from commonplace.lib.library import library_root
from commonplace.lib.project_paths import (
    VALIDATION_IGNORE_MARKER,
    is_collection_metadata,
)
from commonplace.lib.review_workflows import criteria, results
from commonplace.lib.review_workflows.outcomes import parse_report, parse_verdict

STATE = Path("kb/reports/state/review")
RUNS = STATE / "runs"
PROFILES_REL = "instructions/review-profiles.yaml"
ATTEMPTS = 3
"""Attempts per pair, counting rejected reviews and launches that returned no answer."""


def profiles() -> Path:
    """The review worker profiles: the library's instructions/review-profiles.yaml."""
    return library_root() / PROFILES_REL


@dataclass(frozen=True)
class Pair:
    note: str          # repository-relative POSIX path
    criterion: str     # artifact identity: repository path or `commonplace:<path>`
    kind: str          # one of criteria.KINDS
    criterion_id: str  # results.criterion_id of the criterion

    @property
    def contract(self) -> str:
        """`verdict` (PASS, WARN or FAIL) or `report` (REPORT)."""
        return criteria.Criterion(self.criterion, self.kind).contract

    @property
    def job(self) -> str:
        """The Workjig call name: unique per pair, the same in every run."""
        return f"{self.note}::{self.criterion_id}"


@dataclass
class PairReport:
    note: str
    criterion: str
    job: str
    state: str                        # fresh, reviewed, problem, out-of-attempts or not-run
    outcome: str | None = None
    problem: str | None = None


@dataclass
class SweepReport:
    run_dir: str                      # repository-relative POSIX path
    pairs: list[PairReport]
    stopped: str | None = None        # the launch failure or usage limit that stopped the sweep
    changed: list[str] = field(default_factory=list)   # checkout paths the guard saw change

    @property
    def counts(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for pair in self.pairs:
            counts[pair.state] = counts.get(pair.state, 0) + 1
        return counts

    @property
    def ok(self) -> bool:
        """Every pair has a current result and the guard saw no change."""
        return (self.stopped is None and not self.changed
                and all(pair.state in ("fresh", "reviewed") for pair in self.pairs))

    def to_dict(self) -> dict:
        return {"run-dir": self.run_dir, "ok": self.ok, "counts": self.counts, "stopped": self.stopped,
                "guard": {"clean": not self.changed, "changed": self.changed},
                "pairs": [asdict(pair) for pair in self.pairs]}


# --- Pair expansion ------------------------------------------------------------

def _reviewable(path: Path, root: Path) -> bool:
    """A directory's member worth reviewing: not an index, a contract, a type spec or frontmatter-less."""
    if path.name == "index.md" or path.name.endswith("-index.md") or is_collection_metadata(path):
        return False
    if "types" in path.relative_to(root).parent.parts:
        return False
    with path.open(encoding="utf-8") as handle:
        return handle.read(4) == "---\n"


def note_paths(root: Path, requests: list[str]) -> list[str]:
    """Repository-relative note paths: a file as given, a directory as its reviewable notes (not recursive)."""
    root = root.resolve()
    found: list[str] = []
    for raw in requests:
        path = (root / raw).resolve()
        if not path.is_relative_to(root):
            raise ValueError(f"note is outside the repository: {raw}")
        if path.is_file():
            members = [path]
        elif path.is_dir():
            if any((parent / VALIDATION_IGNORE_MARKER).exists()
                   for parent in (path, *path.parents) if parent.is_relative_to(root)):
                raise ValueError(f"directory is validation-ignored; name its notes explicitly: {raw}")
            members = [child for child in sorted(path.glob("*.md")) if child.is_file() and _reviewable(child, root)]
            if not members:
                raise ValueError(f"no reviewable notes in directory: {raw}")
        else:
            raise ValueError(f"note not found: {raw}")
        found += [rel for rel in (member.relative_to(root).as_posix() for member in members) if rel not in found]
    return found


def pairs(root: Path, notes: list[str], requests: list[str] | None = None) -> list[Pair]:
    """The applicable (note, criterion) pairs for repository-relative notes and criterion requests.

    `requests` holds gate ids, bundle names and the lenses `type`,
    `type/<name>`, `collection`, `collection/<path>` and `critique`; None
    means all gates.
    """
    found: list[Pair] = []
    for note, criterion in criteria.select(root, notes, requests):
        pair = Pair(note, criterion.identity, criterion.kind, results.criterion_id(root, criterion.identity))
        if "#" in pair.job:
            raise ValueError(f"{pair.job}: '#' is reserved in job names by the runtime")
        found.append(pair)
    return found


# --- The worker call -----------------------------------------------------------

PROMPT = """\
Review one note against one criterion. Nobody will answer questions. If you \
cannot judge the pair, write {problem} instead of guessing.

The note is `{note}` in this repository; its text is {note_input}. The \
criterion is `{criterion}`; its text is {criterion_input}. Judge these input \
texts; the files on disk may have changed since.
{wrapper}
Reading scope:
- The note's relative links resolve from `{note_dir}/`. For grounding or \
consistency checks, read only files the note links to, except for one exact \
local path that the criterion explicitly tells you to derive from such a link.
- Ignore review backups, workshop copies and historical artifacts unless the \
note links to them.
- Do not delegate or start another agent.

Output:
- Write the review to {review}. Write nothing else: create, edit or delete no \
file in the repository, and run no command that changes it or its git state.
{contract}
"""

TYPE_WRAPPER = (
    "This is a type-conformance gate. The gate is the note's type spec:",
    "authoring instructions and a template, not a Failure mode / Test procedure.",
    "The embedded type spec below is the authoritative gate text for this pair.",
    "Judge whether the note does what the type spec's authoring instructions ask.",
    "If the type spec carries a `## Review` section, treat it as the operative test.",
    "- PASS: the note does what the authoring instructions ask.",
    "- WARN: the note conforms overall, but specific instructions go unmet; name each unmet instruction as a finding.",
    "- FAIL: the note does not do what the authoring instructions ask.",
    "Structural checks (frontmatter fields, schema conformance) are the deterministic validator's job; do not re-check them here.",
)
"""Mechanical only: how to apply a type spec as a gate. What a good note of the type is belongs in the spec."""

COLLECTION_WRAPPER = (
    "This is a collection-conformance gate. The gate is the authoring contract",
    "(COLLECTION.md) of the collection the note lives in: conventions and routing",
    "rules, not a Failure mode / Test procedure.",
    "The embedded contract below is the authoritative gate text for this pair.",
    "Judge whether the note follows the collection's authoring conventions:",
    "placement, title and description conventions, quality goal, and outbound linking rules.",
    "If the COLLECTION.md carries a `## Review` section, treat it as the operative test.",
    "- PASS: the note follows the collection's conventions.",
    "- WARN: the note conforms overall, but specific conventions go unmet; name each unmet convention as a finding.",
    "- FAIL: the note does not follow the collection's conventions: wrong placement, or its conventions are systematically unmet.",
    "Structural checks (frontmatter fields, schema conformance) are the deterministic validator's job; do not re-check them here.",
    "The note's conformance to its type spec is the type-conformance pair's job; judge only what the collection contract asks beyond the type contract.",
)
"""Mechanical only: how to apply a collection contract as a gate; its criteria belong in the contract."""

VERDICT_OUTPUT = """\
- Structure the review as `### Summary` (a short paragraph), `### Findings` \
(`- <severity>: <finding>` items) and, when needed, `### Suggested Revision`.
- End with exactly one result line, the last non-empty line of the file: \
`## Result: PASS`, `## Result: WARN` or `## Result: FAIL`. Do not use aliases \
such as Verdict, Outcome, OK or UNKNOWN, and write no other result-like line."""

REPORT_OUTPUT = """\
- Write the complete report the criterion asks for.
- End with exactly one result line, the last non-empty line of the file: \
`## Result: REPORT`. Do not write PASS, WARN or FAIL."""


def prompt(pair: Pair, problems: list[list[str]] = ()) -> str:
    """The reviewer's task for one pair; `problems` are earlier attempts' rejections, oldest first."""
    wrapper = {criteria.TYPE: TYPE_WRAPPER, criteria.COLLECTION: COLLECTION_WRAPPER}.get(pair.kind, ())
    text = PROMPT.format(
        problem=PROBLEM_REF, note=pair.note, note_input=input_ref("note"), criterion=pair.criterion,
        criterion_input=input_ref("criterion"), wrapper="".join(f"\n{line}" for line in wrapper) + "\n" * bool(wrapper),
        note_dir=Path(pair.note).parent.as_posix(), review=output_ref("review"),
        contract=VERDICT_OUTPUT if pair.contract == "verdict" else REPORT_OUTPUT)
    if problems:
        text += "\nAn earlier review of this pair was rejected. Write it again, correcting:\n"
        text += "".join(f"- {problem}\n" for problem in problems[-1])
    return text


def check(pair: Pair, text: str) -> list[str]:
    """The strict result-line check: empty when the review is acceptable."""
    try:
        if pair.contract == "verdict":
            parse_verdict(text)
        else:
            parse_report(text)
    except ValueError as error:
        return [str(error)]
    return []


def outcome(pair: Pair, text: str) -> str:
    return parse_verdict(text) if pair.contract == "verdict" else "report"


# --- The checkout guard ------------------------------------------------------------

def _git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True,
                          encoding="utf-8").stdout


def checkout_state(root: Path) -> dict[str, str]:
    """HEAD, and each path `git status` lists outside the review state, with its status and content digest."""
    entries = _git(root, "status", "--porcelain", "-z", "--untracked-files=all").split("\0")
    state = {"HEAD": _git(root, "rev-parse", "HEAD").strip()}
    index = 0
    while index < len(entries):
        entry = entries[index]
        index += 1
        if not entry:
            continue
        code, path = entry[:2], entry[3:]
        if "R" in code or "C" in code:
            index += 1                                  # -z lists a rename's source after it
        if path.startswith(f"{STATE.as_posix()}/"):
            continue
        target = root / path
        digest = hashlib.sha256(target.read_bytes()).hexdigest() if target.is_file() else "-"
        state[path] = f"{code} {digest}"
    return state


def changed_paths(before: dict[str, str], after: dict[str, str]) -> list[str]:
    return sorted(path for path in before.keys() | after.keys() if before.get(path) != after.get(path))


# --- The sweep ---------------------------------------------------------------------

def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def sweep(root: Path, wanted: list[Pair], profile: Profile, run_dir: Path, *, max_workers: int | None = None,
          timeout: float | None = None, force: bool = False, harnesses=HARNESSES) -> SweepReport:
    """Review the pairs without a fresh result (all of them when `force`) in the run at `run_dir`."""
    run_id = run_dir.resolve().relative_to(root.resolve()).as_posix()
    reports = {pair: PairReport(pair.note, pair.criterion, pair.job, "not-run") for pair in wanted}
    pending = []
    for pair in wanted:
        if not force and results.freshness(root, pair.note, pair.criterion).state == "fresh":
            reports[pair].state = "fresh"
        else:
            pending.append(pair)
    if not pending:
        return SweepReport(run_id, list(reports.values()))

    stop = threading.Event()
    stopped: list[str] = []

    def review(run: Run, pair: Pair) -> None:
        if stop.is_set():
            return
        report = reports[pair]
        note_text = (root / pair.note).read_text(encoding="utf-8")
        criterion_text = results.criterion_file(root, pair.criterion).read_text(encoding="utf-8")
        try:
            answer = run.checked(pair.job, lambda problems: prompt(pair, problems),
                                 lambda answer: check(pair, answer.outputs["review"]), ["review"],
                                 attempts=ATTEMPTS, inputs={"note": note_text, "criterion": criterion_text})
        except OutOfAttempts as spent:
            report.state = "out-of-attempts"
            report.problem = str(spent)
            return
        except LaunchFailed as failure:              # and UsageLimited: the environment needs the operator
            stop.set()
            stopped.append(str(failure))
            return
        if answer.problem is not None:
            report.state, report.problem = "problem", answer.problem
            return
        text = answer.outputs["review"]
        result = results.make_result(
            pair.note, note_text, pair.criterion, criterion_text, outcome=outcome(pair, text),
            profile={"harness": profile.harness, "launch-model": profile.launch_model, "effort": profile.effort},
            model=answer.record["model"], run=run_id, launch=Path(answer.record["launches"][-1]).name,
            completed_at=_now(), body=text)
        results.write_result(root, result)
        report.state, report.outcome = "reviewed", result.outcome

    before = checkout_state(root)
    with Run(run_dir, root, profile, timeout=timeout, harnesses=harnesses, max_workers=max_workers) as run:
        gather(*(lambda pair=pair: review(run, pair) for pair in pending), max_workers=max_workers)
    changed = changed_paths(before, checkout_state(root))
    return SweepReport(run_id, list(reports.values()), stopped[0] if stopped else None, changed)

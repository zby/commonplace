"""Rewrite one note from its sources, as a workflow over headless workers.

The rewrite is the route for a note whose contribution is known but whose
claims or synthesis are unsettled, such as a note a review found a problem
with a claim in. It ports the edit path of the multistage writing skill
(`instructions/cp-skill-write-multistage/`): judgment lives in the role
instructions under `instructions/rewrite-a-note/`, and the prompts here say
only how to read inputs and write outputs. Code owns what each worker
receives, the checks of each output, the repair allowance, the binding of a
review to the exact candidate and the one write to the checkout.

**Commission.** The session agent writes the commission with the operator
before the run and supplies it with `--commission FILE`. It is Markdown with
YAML frontmatter: `note` names the note to rewrite and `sources` lists the
authorized sources, each a mapping with a repository `path` and its `role`.
The body always has the sections of `COMMISSION_SECTIONS`. The note's write
brief is the one lasting statement of what the note must do, keep and
exclude, so the sections of `BRIEF_SECTIONS`, which repeat the brief's, are
required only when the note has no brief. With a brief they are optional and
hold only what this rewrite adds; a brief item the operator amends is amended
in the brief before the run, and the commission says which item. Code checks
the sections and the frontmatter (`read_commission()`). Every invocation is
a new run (`edits.new_run_dir()`) and needs the commission. The run captures
the commission, with the note's write brief when the note declares one, the
sources and the note's type and collection contracts, in `INPUTS`
(`capture()`); the workers read the capture, and it stays as the record of
what the run read.

**Sources.** A source that git does not ignore and whose bytes are UTF-8 text
is captured: its text is an input. A source that git ignores, or that lies
under a `.snapshots/` directory, or whose bytes are not text, is referenced:
the worker receives its path and SHA-256 in the source list and reads the
file at that path. A referenced source is never copied into the run, so full
external sources stay out of operational state. The run holds no candidate
when a referenced source's bytes changed after the capture.

**Calls.** Each is a fresh worker with only its listed inputs:

One writer selects and writes from the commission, sources and old note. The
old note is not independent support. Incoming citation passages inform the
writer and reviewer; they do not bind claim selection. The independent
review can require one repair followed by a fresh review.

**The review operation.** Its criterion is the library instruction
`criteria.REWRITE_REL`, of kind `criteria.REWRITE`; its target is the
candidate text, judged in place of the note's file. Its operational inputs
are the commission, brief, sources, inbound passages, the candidate's
report as `candidate-report`, the note's start text as `start`, the
contracts, and `earlier-decisions` when the run has them.
`_review()` runs it alone through the sweep (`revise._sweep()`), publishing
nothing, in its own run under `REVIEWS`, named by the hash of the candidate
and those inputs, so another candidate or other inputs is a new review. The
sweep adds the operator's rejected findings of this note against this
criterion as `finding-decisions`, as for any review. The result is checked by
the review-result contract and `gates.rewrite_review_problems()`: outcome
`fail` exactly when a finding has level `fail`, and each `warn` or `fail`
finding's reason states its basis and its required change. Its
`target-sha256` binds it to the candidate; a result of any other text is
refused. The run keeps a copy as `artifact/review-<n>.md`.

Earlier operator decisions reach both workers when present.

**Publication.** After `pass` or `warn`, a candidate equal to the start text
ends the run with no change. Otherwise the run holds the candidate
(`edits.hold()`), as revise holds one that adds a validation warning, and
ends: the note is not written. The report's `held` names the candidate, its
diff, its new validation warnings and the command that publishes it; its
`accepted` names the accepted review and its `warn` findings, which the
`held` notice counts. `commonplace-revise publish RUN` publishes the exact
candidate on the operator's word, or with `--revised FILE` the operator's
revision of it, only over the start text and under the captured brief
(`edits.publish_held()`).

**After publication.** When the published text is the text the accepted
review judged, `store_accepted()` makes its result the note's current
result for the criterion (`results.write_result()`): it is fresh while the
note, the instruction and the output contract are unchanged, so
`commonplace-revise triage NOTE` presents its `warn` findings. A revised candidate
is not the judged text, so the result is not stored, and the `publish`
report's `not-current` says so.
"""

from __future__ import annotations

import contextlib
import json
import re
import subprocess
from dataclasses import asdict, dataclass, field
from pathlib import Path, PurePosixPath

from commonplace.headless.harness import HARNESSES, Profile
from commonplace.headless.jobs import (
    PROBLEM_REF,
    Answer,
    LaunchFailed,
    OutOfAttempts,
    Run,
    input_ref,
    output_ref,
)
from commonplace.lib import frontmatter
from commonplace.lib.library import artifact_file, library_root
from commonplace.lib.naming import write_brief_name_for
from commonplace.lib.note_parser import blank_fenced_code_blocks
from commonplace.lib.review_workflows import (
    criteria,
    decisions,
    edits,
    gates,
    inbound,
    observations,
    result_contract,
    results,
    revise,
)
from commonplace.lib.review_workflows.edits import (
    NO_WRITES,
    START,
    Conflict,
    Stop,
    capture_brief,
    guarded_changes,
)

WORKFLOW = "rewrite"
INSTRUCTIONS_DIR = "instructions/rewrite-a-note"
WRITER = "write-a-rewrite-candidate.md"
INPUTS = "rewrite-inputs.json"
"""The commission, brief, sources and contracts the run captured: what its workers read."""
COMMISSION_SECTIONS = ("Current direction",)
"""The commission's sections every commission has."""
BRIEF_SECTIONS = ("Intended contribution", "Must keep", "Must exclude", "Reserved decisions")
"""The commission's sections that repeat the write brief's: required only when the note has no brief."""
REPORT_SECTIONS = ("Affected citations",)
BLOCK = "fail"
"""The review outcome that blocks the candidate; `warn` and `pass` accept it."""
ATTEMPTS = 3
COMMAND = "commonplace-revise rewrite {artifact} --commission FILE"
EARLIER_DECISIONS = revise.EARLIER_DECISIONS
EARLIER_FILE = revise.EARLIER_FILE
"""The operator's earlier decisions the run used: a record of what it read."""
REVIEWS = "reviews"
"""The runs of the review operation under the rewrite run, one per candidate and inputs."""
START_INPUT, CANDIDATE_REPORT = "start", "candidate-report"
"""The review's operational inputs that hold the note's start text and the author's report."""
BLOCKED = ("The review failed the repaired candidate, and the one repair is used. Nothing was published; the "
           "run keeps every output under artifact/. Read review-2.md. When a finding asks for evidence the "
           "sources lack, ground or add a source, then start a new run with a changed commission: `{command}`. "
           "When a finding needs the operator's decision, settle it in the commission and start a new run the "
           "same way.")
HELD_NOTICE = ("The candidate is published only on the operator's word, with the command `{command}`, or with "
               "`--revised FILE` for the operator's revision of it. Tell the operator of each new validation "
               "warning before asking.")
FINDINGS_NOTICE = (" The accepted review {review} left {count} finding(s) of level warn, which do not block "
                   "publication. Tell the operator how many there are and where the review is before asking for "
                   "the decision. When this exact candidate is published, `commonplace-revise triage {artifact}` "
                   "presents them.")
NOT_CURRENT = ("The published text is the operator's revised candidate, not the candidate the accepted review "
               "judged, so the review is not stored as the note's current result.")


# --- The commission and the capture -------------------------------------------------------

def sections(text: str) -> list[str]:
    """The H2 headings of a Markdown body, outside fenced code."""
    return [match.group(1).strip() for match in re.finditer(r"^## +(.+?)[ \t]*$", blank_fenced_code_blocks(text),
                                                            re.MULTILINE)]


def _missing(text: str, wanted: tuple[str, ...]) -> list[str]:
    found = sections(text)
    return [f"the section `## {name}` is missing" for name in wanted if name not in found]


def read_commission(root: Path, note: str, text: str, *, brief: bool) -> list[dict]:
    """The commission's sources as `{"path", "role"}`; ValueError lists what the commission breaks.

    The frontmatter names `note` and a non-empty `sources` list; each source
    is a file in the repository other than the note, its write brief and run
    state; the body has every section of `COMMISSION_SECTIONS`, and, when the
    note has no write brief (`brief` false), every section of `BRIEF_SECTIONS`.
    """
    parsed = frontmatter.parse(text)
    if not frontmatter.opens_frontmatter(text) or not parsed.ok:
        raise ValueError("commission: the YAML frontmatter does not parse")
    data, problems = parsed.data, []
    if data.get("note") != note:
        problems.append(f"`note` must be {note}, the note this run rewrites")
    given = data.get("sources")
    if not isinstance(given, list) or not given:
        problems.append("`sources` must list at least one source, each with `path` and `role`")
        given = []
    excluded = {note, (Path(note).parent / write_brief_name_for(Path(note))).as_posix()}
    sources, seen = [], set()
    for index, source in enumerate(given, 1):
        if (not isinstance(source, dict) or set(source) != {"path", "role"}
                or not all(isinstance(source[key], str) and source[key].strip() for key in ("path", "role"))):
            problems.append(f"source {index} must be a mapping with exactly `path` and `role`, both text")
            continue
        try:
            path = observations.safe_path(root, source["path"])
        except ValueError as error:
            problems.append(f"source {index}: {error}")
            continue
        rel = path.resolve().relative_to(root.resolve()).as_posix()
        if not path.is_file():
            problems.append(f"source {index}: {source['path']} is not a file in the repository")
        elif rel in excluded:
            problems.append(f"source {index}: {rel} is the note or its write brief; the run supplies them itself")
        elif PurePosixPath(rel).is_relative_to(gates.RUNS.as_posix()):
            problems.append(f"source {index}: {rel} is run state, not a source")
        elif rel in seen:
            problems.append(f"source {index}: {rel} is listed twice")
        else:
            seen.add(rel)
            sources.append({"path": rel, "role": source["role"].strip()})
    problems += _missing(frontmatter.strip(text), COMMISSION_SECTIONS + (() if brief else BRIEF_SECTIONS))
    if problems:
        raise ValueError("commission: " + "; ".join(problems))
    return sources


def _referenced(root: Path, rel: str) -> bool:
    """Whether a source is referenced by path, not captured: git ignores it, or it lies under `.snapshots/`."""
    if ".snapshots" in PurePosixPath(rel).parts:
        return True
    found = subprocess.run(["git", "check-ignore", "-q", "--", rel], cwd=root, capture_output=True,
                           check=False)
    if found.returncode not in (0, 1):
        raise ValueError(f"cannot tell whether {rel} is ignored: {found.stderr.decode(errors='replace').strip()}")
    return found.returncode == 0


def _contracts(root: Path, note: str, start: str) -> dict[str, dict[str, str]]:
    """The note's type spec and collection contract, by input role, with their origin and text."""
    found = {}
    for role, identity in (("type-contract", criteria.note_type_spec(root, root / note, start)),
                           ("collection-contract", criteria.note_collection_contract(root, root / note))):
        if identity is not None:
            found[role] = {"origin": identity, "text": artifact_file(root, identity).read_text(encoding="utf-8")}
    return found


def capture(root: Path, note: str, start: str, commission: Path, brief: dict[str, str]) -> dict:
    """Read the commission, its sources and the contracts, as the run keeps them in `INPUTS`.

    A captured source keeps its text; a referenced one keeps only its path,
    role and SHA-256.
    """
    text = commission.read_text(encoding="utf-8")
    sources = []
    for index, source in enumerate(read_commission(root, note, text, brief="brief" in brief), 1):
        content = (root / source["path"]).read_bytes()
        entry = {**source, "sha256": observations.sha(content), "mode": "referenced", "input": None}
        if not _referenced(root, source["path"]):
            with contextlib.suppress(UnicodeDecodeError):     # a file that is not text is referenced
                entry |= {"mode": "captured", "input": f"source-{index}", "text": content.decode("utf-8")}
        sources.append(entry)
    origin = commission.resolve()
    origin = (origin.relative_to(root).as_posix() if origin.is_relative_to(root) else str(origin))
    return {"commission": {"origin": origin, "text": text}, "brief": brief.get("brief"), "sources": sources,
            "contracts": _contracts(root, note, start)}


def source_list(sources: list[dict]) -> str:
    """The `sources` input: every authorized source with its role and how the worker reads it."""
    lines = ["# Sources", "",
             ("The authorized sources of this rewrite, each with its role. Read a captured source in the input "
              "named; read a referenced source in the repository file at its path, which has the SHA-256 given. "
              "Use no other source."), ""]
    for index, source in enumerate(sources, 1):
        how = (f"captured as the input `{source['input']}`" if source["mode"] == "captured"
               else f"referenced: read the file `{source['path']}`; SHA-256 `{source['sha256']}`")
        lines.append(f"{index}. `{source['path']}`. Role: {source['role']}. {how}.")
    return "\n".join(lines) + "\n"


def _changed_sources(root: Path, sources: list[dict]) -> list[str]:
    """The referenced sources whose bytes are not the captured ones."""
    changed = []
    for source in sources:
        if source["mode"] != "referenced":
            continue
        path = root / source["path"]
        if not path.is_file() or observations.sha(path.read_bytes()) != source["sha256"]:
            changed.append(source["path"])
    return changed


# --- The report ---------------------------------------------------------------------------

@dataclass
class RewriteReport:
    run_dir: str
    artifact: str
    commission: str | None = None     # the captured commission in the run, and where it came from
    origin: str | None = None
    brief: str | None = None          # the captured write brief in the run, when the note declares one
    sources: list[dict] = field(default_factory=list)   # path, role, sha256, and mode: captured or referenced
    steps: list[dict] = field(default_factory=list)     # each answered call: job, key, model and its files
    reviews: list[dict] = field(default_factory=list)   # each review: its copy, run, candidate, hash and outcome
    accepted: dict | None = None      # the accepted review, its outcome and its `warn` findings
    repair_used: bool = False
    blocked: str | None = None        # the second review failed; nothing is held
    unchanged: bool = False           # the accepted candidate is the start text; nothing to publish
    proposed: str | None = None
    new_warnings: list[str] = field(default_factory=list)
    held: dict | None = None          # the candidate held for the operator, and the commands that publish it
    stopped: str | None = None
    conflict: str | None = None
    changed: list[str] = field(default_factory=list)

    @property
    def complete(self) -> bool:
        """Nothing is left: no held candidate, no stop and no conflict."""
        return self.held is None and self.stopped is None and self.conflict is None

    @property
    def ok(self) -> bool:
        """No stop and no conflict; a held candidate and a block are ok. The guard is reported apart."""
        return self.stopped is None and self.conflict is None

    def to_dict(self) -> dict:
        data = {key.replace("_", "-"): value for key, value in asdict(self).items() if key != "changed"}
        return {"ok": self.ok, "complete": self.complete, **data,
                "guard": {"clean": not self.changed, "changed": self.changed}}


# --- The prompts: mechanical only ----------------------------------------------------------

PROMPT = """\
Do one step of the rewrite of one note. Nobody will answer questions. If you \
cannot do it, write {problem} instead of guessing.

The note is `{artifact}` in this repository. The instruction for this step is \
{instruction}; follow it. {given}
The inputs, by role:
{inputs}
Output:
{outputs}- {no_writes}
"""

GIVEN = {
    "candidate": ("The note's text when the run started is `note`; it is not evidence for its own claims. "
                  "The candidate keeps the note's frontmatter `title`, `type` and `brief` declaration and its "
                  "H1, drops `user-verified` when the body changes and adds no validation failure."),
    "candidate-repair": ("The note's text when the run started is `note`; it is not evidence for its own claims. "
                         "A reviewer blocked the candidate `blocked-candidate` with the review `review`; write the "
                         "candidate again, making the changes its findings require. The candidate keeps the "
                         "note's frontmatter `title`, `type` and `brief` declaration and its H1, drops "
                         "`user-verified` when the body changes and adds no validation failure."),
}
ROLES = {
    "instruction": "the instruction for this step",
    "commission": "the commission: the current direction, the sources, and the intent and boundaries of this "
                  "rewrite beyond the write brief",
    "brief": "the note's write brief: binding retained intent",
    "type-contract": "the note's type spec",
    "collection-contract": "the contract of the note's collection",
    "sources": "the source list",
    "note": "the note's text when the run started",
    "review": "the typed review result that blocked the candidate",
    "blocked-candidate": "the candidate the review blocked",
    inbound.INPUT: "the passages that cite the note; not evidence or preservation requirements",
    EARLIER_DECISIONS: "the operator's decisions in earlier runs on this note",
}
OUTPUTS = ("- Write the complete candidate text, frontmatter included, to {candidate}.\n"
           "- Write the citation consequences to {report}, under `## Affected citations`.\n")


def _prompt(step: str, artifact: str, inputs: dict[str, str]) -> str:
    listed = "".join(f"- `{name}` ({ROLES.get(name, 'a captured source')}): {input_ref(name)}\n"
                     for name in inputs if name != "instruction")
    return PROMPT.format(
        problem=PROBLEM_REF, artifact=artifact, instruction=input_ref("instruction"),
        given=GIVEN[step], inputs=listed,
        outputs=OUTPUTS.format(candidate=output_ref("candidate"), report=output_ref("report")),
        no_writes=NO_WRITES)


# --- The workflow ----------------------------------------------------------------------------

def _rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


class _Steps:
    """The calls of one run: each asked, checked, and its outputs kept under `artifact/`."""

    def __init__(self, run: Run, root: Path, artifact: str, profile: Profile, report: RewriteReport,
                 timeout: float | None, harnesses):
        self.run, self.root, self.artifact, self.profile, self.report = run, root, artifact, profile, report
        self.timeout, self.harnesses = timeout, harnesses

    def ask(self, job: str, inputs: dict[str, str], outputs: list[str], check) -> Answer:
        prompt = _prompt(job, self.artifact, inputs)
        answer = self.run.checked(job, lambda problems: prompt + edits.rejection(problems),
                                  lambda answer: check(answer.outputs), outputs, attempts=ATTEMPTS, inputs=inputs,
                                  profile=self.profile)
        if answer.problem is not None:
            raise Stop(f"{job}: worker problem: {answer.problem}")
        self.report.steps.append({"job": job, "key": answer.key, "model": answer.record["model"], "files": {}})
        return answer

    def keep(self, name: str, text: str) -> str:
        path = _rel(self.root, self.run.accept(name, text))
        self.report.steps[-1]["files"][Path(name).stem] = path
        return path


def _candidate_check(root: Path, artifact: str, start: str, baseline: set[str], blocked: str | None):
    def check(outputs: dict[str, str]) -> list[str]:
        problems = [f"report: {problem}" for problem in _missing(outputs["report"], REPORT_SECTIONS)]
        problems += [f"candidate: {problem}"
                     for problem in edits.artifact_bounds(root, artifact, start, outputs["candidate"], baseline)]
        if blocked is not None and outputs["candidate"] == blocked:
            problems.append("the candidate is the blocked candidate; make the changes the review requires")
        return problems
    return check


def _review(steps: _Steps, job: str, number: int, candidate: str, written: str,
            supplied: dict[str, dict[str, str]]) -> results.Result:
    """Run the review operation alone on the exact `candidate`; keep its typed result and return it.

    `written` is the candidate's report; `supplied` holds the other
    operational inputs by role, each with its origin and text. Stop when the
    result judged another text than the candidate.
    """
    root, run = steps.root, steps.run
    inputs = {**supplied, CANDIDATE_REPORT: {"origin": _rel(root, run.artifact / f"candidate-{number}-report.md"),
                                             "text": written}}
    identity = criteria.rewrite_review_identity(root)
    pair = gates.Pair(steps.artifact, identity, criteria.REWRITE, results.criterion_id(root, identity))
    name = observations.sha(json.dumps([candidate, inputs], sort_keys=True).encode("utf-8"))[:12]
    swept = revise._sweep(root, run.root / REVIEWS / name, [pair], steps.profile, steps.timeout, steps.harnesses,
                          inputs, WORKFLOW, targets={steps.artifact: candidate})
    [done] = swept.pairs
    result, sha = done.result, observations.sha(candidate.encode("utf-8"))
    if result.target_sha256 != sha:
        raise Stop(f"{job}: the review in {swept.run_dir} judged the text {result.target_sha256}, not the "
                   f"candidate {sha}; it is refused")
    path = _rel(root, run.accept(f"review-{number}.md", results.result_text(result)))
    steps.report.steps.append({"job": job, "run": swept.run_dir, "model": result.model,
                               "files": {f"review-{number}": path}})
    steps.report.reviews.append({"review": path, "run": swept.run_dir,
                                 "candidate": _rel(root, run.artifact / f"candidate-{number}.md"),
                                 "candidate-sha256": sha, "outcome": result.outcome})
    return result


def store_accepted(root: Path, run_dir: Path, published: dict) -> dict:
    """After `publish RUN` on a rewrite run: store its accepted review as the note's current result, if it applies.

    `published` is `edits.publish_held()`'s report. `publish_held()` has
    refused a review file whose hash is not the one `HELD` recorded; the
    file is checked again here, after publication. The review is stored
    (`results.write_result()`) only when it is that file and the published
    text is the text it judged; a revised candidate is not. Returns the report's
    `current-result`, the stored result and its freshness, or `not-current`,
    why it was not stored.
    """
    held = json.loads((run_dir / edits.HELD).read_text(encoding="utf-8"))
    artifact = published["artifact"]
    text = (root / held["review"]).read_text(encoding="utf-8")
    if edits.sha256(text) != held["review-sha256"]:
        return {"current-result": None,
                "not-current": f"{held['review']} is not the review the run accepted; it was changed after the run"}
    result = results.parse_result(text)
    if result.target_sha256 != published["published"]["sha256"]:
        return {"current-result": None, "not-current": NOT_CURRENT}
    try:
        path = results.write_result(root, result)
    except (ValueError, result_contract.ControllerError) as error:
        return {"current-result": None,
                "not-current": f"the accepted review could not be stored as the note's current result: {error}"}
    return {"current-result": {"result": _rel(root, path),
                               "freshness": results.freshness(root, artifact, result.criterion).state},
            "not-current": None}


def rewrite(root: Path, artifact: str, run_dir: Path, profile: Profile, *, commission: Path,
            timeout: float | None = None, harnesses=HARNESSES) -> RewriteReport:
    """Rewrite the repository-relative `artifact` in the new run at `run_dir`, under the `commission` file.

    The note's current text is the start text. Invalid commissions raise ValueError.
    """
    root = root.resolve()
    report = RewriteReport(_rel(root, run_dir.resolve()), artifact)
    before = gates.checkout_state(root)
    start = (root / artifact).read_text(encoding="utf-8")
    try:
        brief = capture_brief(root, artifact, start)
        captured = capture(root, artifact, start, commission, brief)
        edits.begin(run_dir, artifact, start, brief)
        observations.atomic_json(run_dir / INPUTS, captured)
        with Run(run_dir, root, profile, timeout=timeout, harnesses=harnesses) as run:
            earlier = decisions.earlier(root, artifact, run_dir)
            observations.atomic_json(run_dir / EARLIER_FILE, {"decisions": earlier})
            _steps(_Steps(run, root, artifact, profile, report, timeout, harnesses), start, captured, earlier)
    except Conflict as conflict:
        report.conflict = str(conflict)
    except (Stop, OutOfAttempts, LaunchFailed) as stop:      # LaunchFailed includes UsageLimited
        report.stopped = str(stop)
    report.changed = guarded_changes(root, before, artifact, None)
    return report


def _steps(steps: _Steps, start: str, captured: dict, earlier: list[dict]) -> None:
    """Write from the captured inputs, review and hold the accepted candidate."""
    run, root, artifact, report = steps.run, steps.root, steps.artifact, steps.report
    sources = captured["sources"]
    report.origin = captured["commission"]["origin"]
    report.sources = [{key: source[key] for key in ("path", "role", "sha256", "mode")} for source in sources]
    report.commission = _rel(root, run.accept("commission.md", captured["commission"]["text"]))
    if captured["brief"] is not None:
        report.brief = _rel(root, run.accept("brief.md", captured["brief"]))
    listing = source_list(sources)
    run.accept("sources.md", listing)
    supplied = {"commission": {"origin": report.commission, "text": captured["commission"]["text"]},
                **({"brief": {"origin": report.brief, "text": captured["brief"]}} if report.brief else {}),
                **{role: {"origin": contract["origin"], "text": contract["text"]}
                   for role, contract in captured["contracts"].items()},
                START_INPUT: {"origin": _rel(root, run.accept(START, start)), "text": start}}

    supplied["sources"] = {"origin": _rel(root, run.artifact / "sources.md"), "text": listing}
    supplied.update({source["input"]: {"origin": source["path"], "text": source["text"]}
                     for source in sources if source["mode"] == "captured"})
    supplied[inbound.INPUT] = inbound.supplied(root, artifact)
    instruction = (library_root() / INSTRUCTIONS_DIR / WRITER).read_text(encoding="utf-8")
    if earlier:
        supplied[EARLIER_DECISIONS] = {"origin": _rel(root, run.root / EARLIER_FILE),
                                       "text": decisions.earlier_text(earlier)}
    common = {**_texts(supplied, START_INPUT), "note": start}
    baseline = edits.validation_fails(root, artifact, start)
    answer = steps.ask("candidate", {"instruction": instruction, **common}, ["candidate", "report"],
                       _candidate_check(root, artifact, start, baseline, None))
    candidate, written = answer.outputs["candidate"], answer.outputs["report"]
    steps.keep("candidate-1.md", candidate)
    steps.keep("candidate-1-report.md", written)
    result = _review(steps, "review", 1, candidate, written, supplied)
    if result.outcome == BLOCK:
        report.repair_used = True
        review = (run.artifact / "review-1.md").read_text(encoding="utf-8")
        inputs = {"instruction": instruction, **common, "review": review, "blocked-candidate": candidate}
        answer = steps.ask("candidate-repair", inputs, ["candidate", "report"],
                           _candidate_check(root, artifact, start, baseline, candidate))
        candidate, written = answer.outputs["candidate"], answer.outputs["report"]
        steps.keep("candidate-2.md", candidate)
        steps.keep("candidate-2-report.md", written)
        result = _review(steps, "review-repair", 2, candidate, written, supplied)
        if result.outcome == BLOCK:
            report.blocked = BLOCKED.format(command=COMMAND.format(artifact=artifact))
            return
    warned = [finding for finding in result.findings if finding.get("level") == "warn"]
    report.accepted = {"review": report.reviews[-1]["review"], "outcome": result.outcome, "warn-findings": warned}
    if candidate == start:
        report.unchanged = True
        return
    changed = _changed_sources(root, sources)
    if changed:
        raise Stop(f"referenced sources changed after the run captured them: {', '.join(changed)}; nothing is "
                   "held. A new run rewrites from their current text")
    report.held = edits.hold(run, root, artifact, start, candidate, [], review=report.accepted["review"])
    report.held["what"] = HELD_NOTICE.format(command=report.held["command"]) + (
        FINDINGS_NOTICE.format(review=report.accepted["review"], count=len(warned), artifact=artifact)
        if warned else "")
    report.proposed, report.new_warnings = report.held["candidate"], report.held["new-warnings"]


def _texts(supplied: dict[str, dict[str, str]], *left_out: str) -> dict[str, str]:
    """The text of each supplied input by role, without the roles `left_out`."""
    return {role: item["text"] for role, item in supplied.items() if role not in left_out}

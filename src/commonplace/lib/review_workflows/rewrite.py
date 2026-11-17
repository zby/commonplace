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
the sections and the frontmatter (`read_commission()`). The run captures the
commission once, with the note's write brief when the note declares one, the
sources and the note's type and collection contracts, in `INPUTS`
(`capture()`). A repeat uses the capture. A commission file whose
text differs from the capture is refused unless `restart` is set: a restart
captures again, removes the step files under `artifact/` and asks every call
again with the new inputs; earlier calls stay in the run's records.

**Sources.** A source that git does not ignore and whose bytes are UTF-8 text
is captured: its text is an input. A source that git ignores, or that lies
under a `.snapshots/` directory, or whose bytes are not text, is referenced:
the worker receives its path and SHA-256 in the source list and reads the
file at that path. A referenced source is never copied into the run, so full
external sources stay out of operational state. Each invocation refuses to go
on when a referenced source's bytes changed since capture.

**Calls.** Each is a fresh worker with only its listed inputs:

1. `reconstruct`: commission, brief, source list, captured sources, contracts.
   Not the note. Output `reconstruction`, with the sections of
   `RECONSTRUCTION_SECTIONS`.
2. `claim-account`: commission, brief, reconstruction, contracts. Not the
   note. Output `claim-account`, one `## ` section per material commitment.
3. `candidate`: all of the above but the sources, the claim account, the
   note's start text, and `kb-role` and `earlier-decisions` when the run has
   them (below). Outputs `candidate`, which must keep the candidate bounds of
   `edits.artifact_bounds()`, and `report`, with the sections of
   `REPORT_SECTIONS`.
4. `review`: a review operation (below) whose target is the candidate.
   Output: a typed review result (`types/review-result.md`) with a verdict.
   `fail` blocks; `warn` accepts with findings; `pass` accepts with none.
5. On `fail`, one repair: `candidate-repair` also receives the typed review
   as `review` and the blocked candidate, then `review-repair`, a fresh review
   of the repaired candidate. A second `fail` ends the run; nothing is
   published.

**The review operation.** Its criterion is the library instruction
`criteria.REWRITE_REL`, of kind `criteria.REWRITE`; its target is the
candidate text, judged in place of the note's file. Its operational inputs
are the commission, brief, reconstruction, claim account, the candidate's
report as `candidate-report`, the note's start text as `start`, the
contracts, and `kb-role` and `earlier-decisions` when the run has them.
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

The reconstruct and claim-account workers are not given the note, and their
prompt tells them not to open it; they can still read the checkout. The
isolation is by supplied inputs and instruction, not by sandbox. They also
receive neither `kb-role` nor `earlier-decisions`: both describe the note's
current text, and the claim selection must come from the sources alone.

**What revise workers also receive.** Before the candidate call, the run
obtains the note's role report once and keeps it in `ROLE_FILE`: a fresh one
the full revise procedure kept for the same text (`revise.stored_role()`),
which costs no launch, or else one call of the role report alone, on the
review profile, in `ROLE_DIR` under the run (`revise.role_report()`). Its
`## Role` section is the input `kb-role` of the candidate, repair and review
calls. When the run starts, code collects the operator's earlier decisions
on the note from the other revise and rewrite runs (`decisions.earlier()`)
and keeps them in `EARLIER_FILE`; when there is at least one, the same calls
receive them as `earlier-decisions`. A repeat reads both files; a restart
obtains both again.

**Publication.** After `pass` or `warn`, a candidate equal to the start text
ends the run with no change. Otherwise the run always stops at the
publication stop of `edits.publish()`, which revise uses only for a
candidate that adds a validation warning: the operator approves the exact
candidate, may accept it with a revision (`supply_revised()`), is told of new
validation warnings, and the note is written only after approval and only
over the start text. The report's `accepted` names the accepted review and
its `warn` findings, and the waiting text says how many there are and where
the review is. The proposal key binds the start text, the candidate, the
capture, every call's key and each review's raw output.

**After publication.** When the published text is the text the accepted
review judged, its result becomes the note's current result for the
criterion (`results.write_result()`): it is fresh while the note, the
instruction and the output contract are unchanged, so
`run revise NOTE --triage` presents its `warn` findings. A revised candidate
is not the judged text, so the result is not stored, and the report's
`not-current` says so.
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
INSTRUCTIONS = {
    "reconstruct": "reconstruct-the-sources-of-a-rewrite.md",
    "claim-account": "account-for-the-claims-of-a-rewrite.md",
    "candidate": "write-a-rewrite-candidate.md",
}
"""The role instruction of each worker step, under `INSTRUCTIONS_DIR`; the review's is `criteria.REWRITE_REL`."""
INPUTS = "rewrite-inputs.json"
"""The commission, brief, sources and contracts the run captured once; a repeat reads them here."""
COMMISSION_SECTIONS = ("Current direction",)
"""The commission's sections every commission has."""
BRIEF_SECTIONS = ("Intended contribution", "Must keep", "Must exclude", "Reserved decisions")
"""The commission's sections that repeat the write brief's: required only when the note has no brief."""
RECONSTRUCTION_SECTIONS = ("Support", "Inference", "Conflicts", "Scope", "Gaps")
REPORT_SECTIONS = ("Kept", "Replaced", "Omitted")
BLOCK = "fail"
"""The review outcome that blocks the candidate; `warn` and `pass` accept it."""
ATTEMPTS = 3
REPEAT = "commonplace-review run rewrite {artifact}"
CHANGE = "change the commission and repeat with --commission FILE --restart"
"""How the publication stop's waiting text tells the operator to change the rewrite's candidate otherwise."""
KB_ROLE, EARLIER_DECISIONS = revise.KB_ROLE, revise.EARLIER_DECISIONS
ROLE_FILE = "role.json"
"""The role report the run used and its `## Role` section, obtained once: a repeat reads them here."""
ROLE_DIR = "role"
"""The run of the role report alone, under the rewrite run, when no fresh stored one exists."""
EARLIER_FILE = revise.EARLIER_FILE
"""The operator's earlier decisions the run used, captured once: a repeat reads them here."""
REVIEWS = "reviews"
"""The runs of the review operation under the rewrite run, one per candidate and inputs."""
START_INPUT, CANDIDATE_REPORT = "start", "candidate-report"
"""The review's operational inputs that hold the note's start text and the author's report."""
STEP_FILES = ("reconstruction.md", "claim-account.md", "candidate-1.md", "candidate-1-report.md", "review-1.md",
              "candidate-2.md", "candidate-2-report.md", "review-2.md", *edits.PUBLICATION_FILES)
"""The files under `artifact/` a restart removes: every step's output and the publication files."""
BLOCKED = ("The review failed the repaired candidate, and the one repair is used. Nothing was published; the "
           "run keeps every output under artifact/. Read review-2.md. When a finding asks for evidence the "
           "sources lack, ground or add a source, then start again with a changed commission: `{command} "
           "--commission FILE --restart`. When a finding needs the operator's decision, settle it in the "
           "commission and start again the same way.")
FINDINGS_NOTICE = ("The accepted review {review} left {count} finding(s) of level warn, which do not block "
                   "publication. Tell the operator how many there are and where the review is before asking for "
                   "the decision. When this exact candidate is published, `commonplace-review run revise {artifact} "
                   "--triage` presents them. ")
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
    """Read the commission, its sources and the contracts once, as the run keeps them in `INPUTS`.

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
    role: dict | None = None          # the role report the candidate and review calls used, and whether it was reused
    sources: list[dict] = field(default_factory=list)   # path, role, sha256, and mode: captured or referenced
    restarted: bool = False
    steps: list[dict] = field(default_factory=list)     # each answered call: job, key, model and its files
    reviews: list[dict] = field(default_factory=list)   # each review: its copy, run, candidate, hash and outcome
    accepted: dict | None = None      # the accepted review, its outcome and its `warn` findings
    repair_used: bool = False
    blocked: str | None = None        # the second review failed; nothing is published
    unchanged: bool = False           # the accepted candidate is the start text; nothing to publish
    proposed: str | None = None
    revised_candidate: dict | None = None
    new_warnings: list[str] = field(default_factory=list)
    applied: bool = False
    not_applied: str | None = None
    current_result: dict | None = None   # after publication: the stored current result and its freshness
    not_current: str | None = None    # after publication: why the accepted review is not the current result
    waiting_for: dict | None = None
    stopped: str | None = None
    conflict: str | None = None
    changed: list[str] = field(default_factory=list)

    @property
    def complete(self) -> bool:
        return self.waiting_for is None and self.stopped is None and self.conflict is None

    @property
    def ok(self) -> bool:
        """No stop, no conflict and no unexpected change; waiting for the operator and a block are ok."""
        return self.stopped is None and self.conflict is None and not self.changed

    def to_dict(self) -> dict:
        data = {key.replace("_", "-"): value for key, value in asdict(self).items() if key != "changed"}
        return {"ok": self.ok, "complete": self.complete, **data,
                "guard": {"clean": not self.changed, "changed": self.changed}}


# --- The prompts: mechanical only ----------------------------------------------------------

PROMPT = """\
Do one step of the rewrite of one note. Nobody will answer questions. If you \
cannot do it, write {problem} instead of guessing.

The note is `{artifact}` in this repository. The instruction for this step is \
{instruction}; follow it. {withheld}{given}
The inputs, by role:
{inputs}
Output:
{outputs}- {no_writes}
"""

WITHHELD = ("You do not receive the note's text, and you must not read it: do not open `{artifact}`, its write "
            "brief file, any earlier text of it in git history or under kb/reports/, or any file that quotes it. "
            "Read no repository file except the referenced sources the source list names. ")
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
    "reconstruction": "the reconstruction of the sources",
    "claim-account": "the claim account",
    "note": "the note's text when the run started",
    "review": "the typed review result that blocked the candidate",
    "blocked-candidate": "the candidate the review blocked",
    KB_ROLE: "the note's role in the KB: the `## Role` section of its role report",
    EARLIER_DECISIONS: "the operator's decisions in earlier runs on this note",
}
OUTPUTS = {
    "reconstruct": ("- Write the reconstruction to {reconstruction}: Markdown with the sections `## Support`, "
                       "`## Inference`, `## Conflicts`, `## Scope` and `## Gaps`. Write `None.` in a section "
                       "with nothing in it.\n"),
    "claim-account": ("- Write the claim account to {claim_account}: Markdown with one `## ` section per material "
                      "commitment of the reconstruction, saying how the note treats it.\n"),
    "candidate": ("- Write the complete candidate text of the note, frontmatter included, to {candidate}.\n"
                  "- Write the reconciliation report to {report}: Markdown with the sections `## Kept`, "
                  "`## Replaced` and `## Omitted`, which together account for every material commitment of "
                  "the note's text with the reason. Write `None.` in a section with nothing in it.\n"),
}


def _prompt(step: str, artifact: str, inputs: dict[str, str]) -> str:
    kind = "candidate" if step.startswith("candidate") else step
    listed = "".join(f"- `{name}` ({ROLES.get(name, 'a captured source')}): {input_ref(name)}\n"
                     for name in inputs if name != "instruction")
    given = GIVEN.get(step, GIVEN.get(kind, ""))
    return PROMPT.format(
        problem=PROBLEM_REF, artifact=artifact, instruction=input_ref("instruction"),
        withheld=WITHHELD.format(artifact=artifact) if kind in ("reconstruct", "claim-account") else "",
        given=given, inputs=listed,
        outputs=OUTPUTS[kind].format(reconstruction=output_ref("reconstruction"),
                                     claim_account=output_ref("claim-account"), candidate=output_ref("candidate"),
                                     report=output_ref("report")),
        no_writes=NO_WRITES)


# --- The workflow ----------------------------------------------------------------------------

def _rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


class _Steps:
    """The calls of one invocation: each asked or replayed, checked, and its outputs kept under `artifact/`."""

    def __init__(self, run: Run, root: Path, artifact: str, profile: Profile, report: RewriteReport,
                 timeout: float | None, harnesses):
        self.run, self.root, self.artifact, self.profile, self.report = run, root, artifact, profile, report
        self.timeout, self.harnesses = timeout, harnesses
        self.keys: dict[str, str] = {}
        """Each call's key; for a review, the SHA-256 of its raw output, which identifies its answer."""

    def ask(self, job: str, inputs: dict[str, str], outputs: list[str], check) -> Answer:
        prompt = _prompt(job, self.artifact, inputs)
        answer = self.run.checked(job, lambda problems: prompt + edits.rejection(problems),
                                  lambda answer: check(answer.outputs), outputs, attempts=ATTEMPTS, inputs=inputs,
                                  profile=self.profile)
        if answer.problem is not None:
            raise Stop(f"{job}: worker problem: {answer.problem}")
        self.keys[job] = answer.key
        self.report.steps.append({"job": job, "key": answer.key, "model": answer.record["model"], "files": {}})
        return answer

    def keep(self, name: str, text: str) -> str:
        path = _rel(self.root, self.run.accept(name, text))
        self.report.steps[-1]["files"][Path(name).stem] = path
        return path


def _instruction(step: str) -> str:
    return (library_root() / INSTRUCTIONS_DIR / INSTRUCTIONS[step]).read_text(encoding="utf-8")


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
    """Run the review operation alone on the exact `candidate`, or replay it; keep its typed result and return it.

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
    steps.keys[job] = result.raw_output_sha256
    steps.report.steps.append({"job": job, "run": swept.run_dir, "model": result.model,
                               "files": {f"review-{number}": path}})
    steps.report.reviews.append({"review": path, "run": swept.run_dir,
                                 "candidate": _rel(root, run.artifact / f"candidate-{number}.md"),
                                 "candidate-sha256": sha, "outcome": result.outcome})
    return result


def _store(root: Path, artifact: str, published: str, result: results.Result, report: RewriteReport) -> None:
    """Store the accepted review as the note's current result when `published` is the text it judged."""
    if result.target_sha256 != observations.sha(published.encode("utf-8")):
        report.not_current = NOT_CURRENT
        return
    try:
        path = results.write_result(root, result)
    except (ValueError, result_contract.ControllerError) as error:
        report.not_current = f"the accepted review could not be stored as the note's current result: {error}"
        return
    report.current_result = {"result": _rel(root, path),
                             "freshness": results.freshness(root, artifact, result.criterion).state}


def _inputs(run_dir: Path, root: Path, artifact: str, start: str, brief: dict[str, str], commission: Path | None,
            restart: bool, report: RewriteReport) -> dict:
    """The captured inputs: read from `INPUTS` on a repeat, captured from `commission` on a new run or a restart.

    ValueError (a command error) for a new run without a commission, a
    restart without one, or a commission that differs from the capture
    without a restart.
    """
    path = run_dir / INPUTS
    if path.is_file() and not restart:
        captured = json.loads(path.read_text(encoding="utf-8"))
        if commission is not None and commission.read_text(encoding="utf-8") != captured["commission"]["text"]:
            raise ValueError("the commission differs from the one this run captured; to rewrite under the new "
                             "commission, repeat with --commission FILE --restart, which asks every call again")
        if captured["brief"] != brief.get("brief"):
            raise ValueError(f"the write brief of {artifact} changed since the run captured it; repeat with "
                             "--commission FILE --restart to rewrite under the current brief")
        return captured
    if commission is None:
        raise ValueError("a new rewrite run needs --commission FILE" if not restart
                         else "--restart needs --commission FILE")
    captured = capture(root, artifact, start, commission, brief)
    if path.is_file():                               # a restart: the earlier steps' files go
        report.restarted = True
        for name in STEP_FILES:
            (run_dir / "artifact" / name).unlink(missing_ok=True)
        for name in (edits.REVISED_RECORD, ROLE_FILE, EARLIER_FILE, f"{ROLE_DIR}/review-request.json"):
            (run_dir / name).unlink(missing_ok=True)
    observations.atomic_json(path, captured)
    return captured


def rewrite(root: Path, artifact: str, run_dir: Path, profile: Profile, *, commission: Path | None = None,
            restart: bool = False, review: Profile | None = None, timeout: float | None = None,
            harnesses=HARNESSES) -> RewriteReport:
    """Rewrite the repository-relative `artifact` in the run at `run_dir`, new or continued.

    The note's current text is the start text. `commission` is the
    commission file: required for a new run and for `restart`, optional on a
    repeat, where it must equal the capture. `review` is the profile of the
    role report when it must run; without it, `profile`.
    """
    root = root.resolve()
    report = RewriteReport(_rel(root, run_dir.resolve()), artifact)
    before = gates.checkout_state(root)
    start = (root / artifact).read_text(encoding="utf-8")
    final = None
    try:
        brief = capture_brief(root, artifact, start)
        with Run(run_dir, root, profile, timeout=timeout, harnesses=harnesses) as run:
            captured = _inputs(run_dir, root, artifact, start, brief, commission, restart, report)
            earlier = _earlier(run_dir, root, artifact)
            final = _steps(_Steps(run, root, artifact, profile, report, timeout, harnesses), start, brief,
                           captured, earlier,
                           lambda: _role(run_dir, root, artifact, start, review or profile, timeout, harnesses,
                                         report))
    except Conflict as conflict:
        report.conflict = str(conflict)
    except (Stop, OutOfAttempts, LaunchFailed) as stop:      # LaunchFailed includes UsageLimited
        report.stopped = str(stop)
    report.changed = guarded_changes(root, before, artifact, final if report.applied else None)
    return report


def _earlier(run_dir: Path, root: Path, artifact: str) -> list[dict]:
    """The operator's earlier decisions on the note: read from `EARLIER_FILE`, or collected once and kept there."""
    path = run_dir / EARLIER_FILE
    if path.is_file():                                # a repeat: other runs may have decided more since
        return json.loads(path.read_text(encoding="utf-8"))["decisions"]
    found = decisions.earlier(root, artifact, run_dir)
    observations.atomic_json(path, {"decisions": found})
    return found


def _role(run_dir: Path, root: Path, artifact: str, start: str, profile: Profile, timeout: float | None, harnesses,
          report: RewriteReport) -> dict[str, str] | None:
    """The `kb-role` input, origin and text, from the note's role report; None when it has no `## Role` section.

    The report is read from `ROLE_FILE`, or obtained once and kept there: a
    fresh stored one (`revise.stored_role()`), without a launch, or else
    the role report run alone in `ROLE_DIR` (`revise.role_report()`).
    """
    path = run_dir / ROLE_FILE
    if path.is_file():
        found = json.loads(path.read_text(encoding="utf-8"))
    else:
        stored = revise.stored_role(root, artifact, start)
        given = stored or revise.role_report(root, artifact, start, run_dir / ROLE_DIR, profile, timeout, harnesses,
                                             WORKFLOW)
        found = {"report": None if given is None else given.path, "reused": stored is not None,
                 "section": None if given is None else revise.role_section(given.text)}
        observations.atomic_json(path, found)
    report.role = {"report": found["report"], "reused": found["reused"]}
    return None if found["section"] is None else {"origin": found["report"], "text": found["section"]}


def _steps(steps: _Steps, start: str, brief: dict[str, str], captured: dict, earlier: list[dict],
           role) -> str | None:
    """Run or replay the calls to an accepted candidate, then stop at publication; return the text to publish.

    `earlier` holds the operator's earlier decisions on the note; `role()`
    gives the `kb-role` input. The candidate, repair and review calls
    receive both, each when it has content; the first two calls receive
    neither. After publication of the judged candidate, the accepted review
    becomes the note's current result (`_store()`).
    """
    run, root, artifact, report = steps.run, steps.root, steps.artifact, steps.report
    sources = captured["sources"]
    report.origin = captured["commission"]["origin"]
    report.sources = [{key: source[key] for key in ("path", "role", "sha256", "mode")} for source in sources]
    changed = _changed_sources(root, sources)
    if changed:
        raise Stop(f"referenced sources changed since the run captured them: {', '.join(changed)}; repeat with "
                   "--commission FILE --restart to rewrite from their current text")
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

    inputs = {"instruction": _instruction("reconstruct"), **_texts(supplied, START_INPUT), "sources": listing,
              **{source["input"]: source["text"] for source in sources if source["mode"] == "captured"}}
    answer = steps.ask("reconstruct", inputs, ["reconstruction"],
                       lambda outputs: _missing(outputs["reconstruction"], RECONSTRUCTION_SECTIONS))
    reconstruction = answer.outputs["reconstruction"]
    supplied["reconstruction"] = {"origin": steps.keep("reconstruction.md", reconstruction), "text": reconstruction}

    inputs = {"instruction": _instruction("claim-account"), **_texts(supplied, START_INPUT)}
    answer = steps.ask("claim-account", inputs, ["claim-account"],
                       lambda outputs: [] if sections(outputs["claim-account"])
                       else ["the claim account has no `## ` section; write one per material commitment"])
    account = answer.outputs["claim-account"]
    supplied["claim-account"] = {"origin": steps.keep("claim-account.md", account), "text": account}

    kb_role = role()
    if kb_role:
        supplied[KB_ROLE] = kb_role
    if earlier:
        supplied[EARLIER_DECISIONS] = {"origin": _rel(root, run.root / EARLIER_FILE),
                                       "text": decisions.earlier_text(earlier)}
    common = {**_texts(supplied, START_INPUT), "note": start}
    baseline = edits.validation_fails(root, artifact, start)
    answer = steps.ask("candidate", {"instruction": _instruction("candidate"), **common}, ["candidate", "report"],
                       _candidate_check(root, artifact, start, baseline, None))
    candidate, written = answer.outputs["candidate"], answer.outputs["report"]
    steps.keep("candidate-1.md", candidate)
    steps.keep("candidate-1-report.md", written)
    result = _review(steps, "review", 1, candidate, written, supplied)
    if result.outcome == BLOCK:
        report.repair_used = True
        review = (run.artifact / "review-1.md").read_text(encoding="utf-8")
        inputs = {"instruction": _instruction("candidate"), **common, "review": review, "blocked-candidate": candidate}
        answer = steps.ask("candidate-repair", inputs, ["candidate", "report"],
                           _candidate_check(root, artifact, start, baseline, candidate))
        candidate, written = answer.outputs["candidate"], answer.outputs["report"]
        steps.keep("candidate-2.md", candidate)
        steps.keep("candidate-2-report.md", written)
        result = _review(steps, "review-repair", 2, candidate, written, supplied)
        if result.outcome == BLOCK:
            report.blocked = BLOCKED.format(command=REPEAT.format(artifact=artifact))
            return None
    warned = [finding for finding in result.findings if finding.get("level") == "warn"]
    report.accepted = {"review": report.reviews[-1]["review"], "outcome": result.outcome, "warn-findings": warned}
    if candidate == start:
        report.unchanged = True
        return None
    context = {"workflow": WORKFLOW, "inputs": observations.sha(json.dumps(captured, sort_keys=True).encode()),
               "calls": steps.keys, "profile": asdict(steps.profile)}
    notice = (FINDINGS_NOTICE.format(review=report.accepted["review"], count=len(warned), artifact=artifact)
              if warned else "")
    published, report.not_applied = edits.publish(run, root, artifact, start, candidate, context, brief,
                                                  REPEAT.format(artifact=artifact), report, change=CHANGE,
                                                  notice=notice)
    report.applied = report.not_applied is None
    if report.applied:
        _store(root, artifact, published, result, report)
    return published


def _texts(supplied: dict[str, dict[str, str]], *left_out: str) -> dict[str, str]:
    """The text of each supplied input by role, without the roles `left_out`."""
    return {role: item["text"] for role, item in supplied.items() if role not in left_out}


def supply_revised(root: Path, artifact: str, run_dir: Path, profile: Profile, revised: str, source: Path, *,
                   harnesses=HARNESSES) -> RewriteReport:
    """Capture the operator's revised candidate at the publication stop and wait for its approval; launch nothing.

    The checks and the capture are `edits.supply_revised()`'s, as for revise.
    """
    root, run_dir = root.resolve(), run_dir.resolve()
    edits.revised_source(run_dir, source, artifact)
    with Run(run_dir, root, profile, harnesses=harnesses) as run:
        supplied = edits.supply_revised(run, root, artifact, revised, REPEAT.format(artifact=artifact),
                                        change=CHANGE)
    return RewriteReport(_rel(root, run_dir), artifact, proposed=supplied["proposed"],
                         revised_candidate=supplied["revised-candidate"], new_warnings=supplied["new-warnings"],
                         not_applied=supplied["not-applied"], waiting_for=supplied["waiting-for"])

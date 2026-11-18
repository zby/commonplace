"""Edit operations: one typed operation run on one note text, with a typed, retained result.

An edit operation (`types/edit-operation.md`) is an instruction that takes one
text of a note and returns a changed text, the unchanged text or a list of
proposed changes. `ask()` runs one operation in one Workjig call and returns
its completed edit result (`types/edit-result.md`). The worker writes two
outputs: the result fragment and, for `changed`, the candidate text. Code
completes the fragment with provenance and checks it (`_complete()`): the
outcome the operation's `decision` allows, the bounds of
`edits.artifact_bounds()` and `edits.preserved()`, proposal quotes found once
in the input, and the result schema. A rejected answer goes back to the
worker with its problems. A controller failure stops. A worker problem
becomes a result with outcome `problem`.

Each execution is an observation under the run's `artifact/edits/`: the exact
input text, operation, prompt, supplied inputs and contract, the raw output,
the completed result and the candidate (`observations.begin()`). A fixture
reruns one such observation (`fixtures.trial()`). `ask()` writes nothing to
the checkout. `commonplace-review run edit` runs one operation alone through
`run()`; the revise workflow runs every pass through `ask()`.

A `per-item` operation runs twice. The first run returns `proposed`; that
result is the question of a stop (`types/answers.md`). After the operator
answers it, the second run gets the answers file as its `answers` input and
returns `changed`. Code accepts the answers only when the validator accepts
them and their question is an edit result of the same operation on the same
input text (`decided()`). The worker applies the `approved` items; code
checks that the passage of every other item is still in the candidate.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from commonplace.headless.harness import HARNESSES, Profile
from commonplace.headless.jobs import (
    PROBLEM_REF,
    Answer,
    LaunchFailed,
    NoProgress,
    OutOfAttempts,
    Run,
    input_ref,
    output_ref,
)
from commonplace.lib import frontmatter
from commonplace.lib.library import (
    LIBRARY_IDENTITY_PREFIX,
    artifact_file,
    artifact_identity,
    library_root,
)
from commonplace.lib.quote_matching import match_quote, normalize_text
from commonplace.lib.review_workflows import edits, gates, observations, result_contract
from commonplace.lib.tasks import load_profile
from commonplace.lib.validation import ValidationRun

TYPE = "types/edit-operation.md"
RESULT_TYPE = "types/edit-result.md"
FORMAT = 1
KIND = "edit"
"""The observation kind of an edit execution, beside the review criterion kinds."""
FAMILY = "edits"
"""The directory under a run's `artifact/` that holds edit observations."""
EFFORTS = ("simple", "judgment")
DECISIONS = ("none", "per-item")
OUTCOMES = ("changed", "unchanged", "proposed", "problem")
WORKER_FIELDS = frozenset({"type", "outcome", "changes", "proposals", "removed-links"})
ANSWERS = "answers"
"""The input role of an answered list, which makes a `per-item` operation apply the approved entries."""
EXECUTION_REL = "instructions/simplification-passes/execute-a-revision-pass.md"
"""The shared edit contract every worker receives as its `execution` input."""
RESERVED = frozenset({"text", "operation", "execution"})
ATTEMPTS = 3
ALLOWED = {"edit": ("changed", "unchanged"), "propose": ("proposed", "unchanged"), "apply": ("changed",)}
"""The outcomes a worker may return: by a `none` operation, a `per-item` first run, and a run with answers."""


class Rejected(ValueError):
    """A worker answer that breaks the result contract; its problems go back to the worker."""

    def __init__(self, problems: list[str]):
        super().__init__("; ".join(problems))
        self.problems = problems


@dataclass(frozen=True)
class Operation:
    identity: str                      # repository path, or `commonplace:<path>` for a library file
    text: str
    effort: str
    decision: str
    depth: int | None = None
    responds_to: tuple[str, ...] = ()

    @property
    def name(self) -> str:
        return Path(self.identity.removeprefix(LIBRARY_IDENTITY_PREFIX)).stem


def parse(identity: str, text: str) -> Operation:
    """The operation `text` declares; ValueError when it is not an edit operation."""
    parsed = frontmatter.parse(text)
    data = parsed.data if parsed.ok else {}
    if data.get("type") != TYPE:
        raise ValueError(f"{identity}: not an edit operation; it must declare type: {TYPE}")
    if data.get("effort") not in EFFORTS or data.get("decision") not in DECISIONS:
        raise ValueError(f"{identity}: `effort` must be one of {', '.join(EFFORTS)} "
                         f"and `decision` one of {', '.join(DECISIONS)}")
    depth = data.get("depth")
    if depth is not None and (not isinstance(depth, int) or isinstance(depth, bool)):
        raise ValueError(f"{identity}: `depth` must be an integer")
    return Operation(identity, text, data["effort"], data["decision"], depth, tuple(data.get("responds-to") or ()))


def identity(root: Path, raw: str) -> str:
    """The identity of the operation `raw` names: a repository path, a library path or `commonplace:<path>`."""
    if raw.startswith(LIBRARY_IDENTITY_PREFIX):
        if artifact_file(root, raw).is_file():
            return raw
    else:
        for path in (root / raw, library_root() / raw):
            if path.is_file():
                return artifact_identity(root, path)
    raise ValueError(f"edit operation not found: {raw}")


def load(root: Path, raw: str) -> Operation:
    found = identity(root, raw)
    return parse(found, artifact_file(root, found).read_text(encoding="utf-8"))


def effort_profiles(root: Path, overrides: dict[str, str | None]) -> dict[str, Profile]:
    """The profile per effort: the profile file's `effort` mapping, with the operator's names in its place."""
    config = yaml.safe_load(gates.profiles().read_text(encoding="utf-8"))
    mapping = config.get("effort") or {}
    chosen = {effort: overrides.get(effort) or mapping.get(effort) for effort in EFFORTS}
    missing = [effort for effort, name in chosen.items() if not name]
    if missing:
        raise ValueError(f"no profile for effort {', '.join(missing)} in {gates.PROFILES_REL}")
    return {effort: load_profile(root, name, gates.profiles()) for effort, name in chosen.items()}


# --- The answers ---------------------------------------------------------------------------

def decided(root: Path, operation: Operation, note: str, text: str, answers: dict) -> tuple[list[dict], list[dict]]:
    """The approved and the other items of an `answers` input, each as its proposal; ValueError when unusable.

    `answers` is the role's `{"origin", "text"}`. The validator must accept
    the text at its origin, and the question must be an edit result of
    `operation` on `note` made from exactly `text`.
    """
    data, problems = edits.answered(root, root / answers["origin"], answers["text"])
    if not problems:
        question = frontmatter.parse((root / data["question"]).read_text(encoding="utf-8")).data
        if question.get("type") != RESULT_TYPE:
            problems.append(f"the question {data['question']} is not an edit result")
        elif question.get("operation") != operation.identity or question.get("note") != note:
            problems.append(f"the question {data['question']} is a result of {question.get('operation')} "
                            f"on {question.get('note')}, not of {operation.identity} on {note}")
        elif question.get("input-sha256") != observations.sha(text.encode("utf-8")):
            problems.append(f"the question {data['question']} was made from another text than this input")
    if problems:
        raise ValueError(f"{ANSWERS}: " + "; ".join(problems))
    approved = [item["proposal"] for item in data["items"] if item["state"] == "approved"]
    if not approved:
        raise ValueError(f"{ANSWERS}: no item is approved; there is nothing to apply")
    return approved, [item["proposal"] for item in data["items"] if item["state"] != "approved"]


# --- The worker call ------------------------------------------------------------------------

PROMPT = """\
Run one edit operation on one note. Nobody will answer questions. If you \
cannot run it within its bounds, write {problem} instead of guessing.

The note is `{note}` in this repository; the text to edit is {text_input}. \
The note's file in the checkout may hold another text: work on this input, \
not the file. The operation is `{operation}`; its text is {operation_input}. \
The shared edit contract is {execution_input}; follow it.
{roles}{task}
Output:
- Write the edit result to {result}: YAML frontmatter, then a `# Report` \
heading and the report the operation's Report section describes. The \
frontmatter holds `type: {result_type}`, `outcome` and the fields that \
outcome needs:
{outcomes}- Supply only these fields; code adds every hash, path and identity. {no_writes}
"""

TASKS = {
    "edit": "",
    "propose": "\nThis operation asks before it edits: list the changes you propose and apply none.\n",
    "apply": ("\nThe operator answered this operation's proposals in an answers file: {answers_input}. "
              "Each item's `proposal` holds a `quote`, a `change` and a `reason`. Apply each item whose "
              "`state` is `approved`, as the operation directs. Apply no other item and make no other "
              "change.\n"),
}

OUTCOME_RULES = {
    "changed": ("  - `outcome: changed` when you applied changes: one line per change under `changes`, "
                "the target of every link you removed under `removed-links`, and the complete changed "
                "text, frontmatter included, written to {candidate}.\n"),
    "unchanged": "  - `outcome: unchanged` when nothing needs changing: say why in the report. Write no candidate.\n",
    "proposed": ("  - `outcome: proposed` to propose changes and apply none: under `proposals`, give each a "
                 "`quote` (a passage copied from the input text that occurs there exactly once), the "
                 "`change` and the `reason`. Write no candidate.\n"),
}


def _mode(operation: Operation, roles: dict) -> str:
    if ANSWERS in roles:
        return "apply"
    return "propose" if operation.decision == "per-item" else "edit"


def prompt(operation: Operation, note: str, roles: dict) -> str:
    mode = _mode(operation, roles)
    listed = "".join(f"- `{role}` (from `{item['origin']}`): {input_ref(role)}\n"
                     for role, item in roles.items() if role != ANSWERS)
    return PROMPT.format(
        problem=PROBLEM_REF, note=note, text_input=input_ref("text"), operation=operation.identity,
        operation_input=input_ref("operation"), execution_input=input_ref("execution"),
        roles=f"\nThe caller supplies these inputs, by role:\n{listed}" if listed else "",
        task=TASKS[mode].format(answers_input=input_ref(ANSWERS)), result=output_ref("result"),
        result_type=RESULT_TYPE,
        outcomes="".join(OUTCOME_RULES[outcome].format(candidate=output_ref("candidate", optional=True))
                         for outcome in ALLOWED[mode]),
        no_writes=edits.NO_WRITES)


@dataclass(frozen=True)
class Target:
    """What an observation records of one edit execution, in the fields a review pair has."""
    note: str
    criterion: str                     # the operation's identity
    job: str
    kind: str = KIND
    contract: str = KIND

    @property
    def criterion_id(self) -> str:
        return self.criterion


@dataclass
class Edit:
    outcome: str
    data: dict                         # the completed frontmatter
    body: str
    text: str                          # the completed result file's text
    candidate: str | None              # the candidate text; the input for `unchanged`, None otherwise
    path: Path                         # the retained result file
    observation: Path
    answer: Answer


def _rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _validate(root: Path, path: Path, text: str, snapshot) -> None:
    report = ValidationRun(repo_root=root, paths=(path,), content_overrides={path.resolve(): text},
                           criteria=snapshot).validate(path)
    if report.fails:
        raise Rejected([f"result: {fail}" for fail in report.fails])


def validate_saved(root: Path, path: Path, text: str, contracts: dict[str, bytes]) -> None:
    """Check a retained edit result against its captured contract and its retained evidence."""
    parsed = frontmatter.parse(text)
    if not parsed.ok or parsed.data.get("type") != RESULT_TYPE or parsed.data.get("format") != FORMAT:
        raise ValueError(f"unsupported edit result: {path}")
    for key, digest in (("candidate", "candidate-sha256"), ("raw-output", "raw-output-sha256")):
        name = parsed.data.get(key)
        if name is None:
            continue
        evidence = observations.safe_path(root, name)
        if observations.sha(evidence.read_bytes()) != parsed.data.get(digest):
            raise result_contract.ControllerError(f"{key}: retained evidence hash mismatch")
    _validate(root, path, text, result_contract.preflight(root, contracts, RESULT_TYPE))


def ask(run: Run, root: Path, operation: Operation, note: str, text: str, roles: dict[str, dict] | None = None, *,
        job: str | None = None, profile: Profile | None = None, contracts: dict[str, bytes] | None = None,
        execution: str | None = None) -> Edit:
    """Run `operation` on the input `text` of `note` and return its accepted, retained edit result.

    `roles` maps an input role to `{"origin", "text"}`: an explicitly supplied
    file the worker receives under that name. Raises ValueError for unusable
    inputs before any launch, `result_contract.ControllerError` for broken
    controller evidence, and Workjig's `OutOfAttempts` and `LaunchFailed`.
    """
    roles = dict(roles or {})
    clash = sorted(role for role in roles if role in RESERVED or role.startswith("output-contract"))
    if clash:
        raise ValueError(f"input roles {', '.join(clash)} are reserved by the edit route")
    mode = _mode(operation, roles)
    withheld: list[dict] = []
    if mode == "apply":
        if operation.decision != "per-item":
            raise ValueError(f"{operation.identity}: only a per-item operation takes an `{ANSWERS}` input")
        _, withheld = decided(root, operation, note, text, roles[ANSWERS])
    job = job or f"{note}::{operation.name}"
    if "#" in job:
        raise ValueError(f"{job}: '#' is reserved in job names by the runtime")
    contracts = contracts if contracts is not None else result_contract.capture_contract(root, RESULT_TYPE)
    snapshot = result_contract.preflight(root, contracts, RESULT_TYPE)
    observations.prepare(run)
    execution = execution if execution is not None else (library_root() / EXECUTION_REL).read_text(encoding="utf-8")
    baseline = edits.validation_fails(root, note, text)
    inputs = {"text": text, "operation": operation.text, "execution": execution,
              **{f"output-contract-{index}": value.decode("utf-8")
                 for index, (_, value) in enumerate(sorted(contracts.items()))},
              **{role: item["text"] for role, item in roles.items()}}
    task = prompt(operation, note, roles)
    directory, record = observations.begin(run, root, Target(note, operation.identity, job), text, operation.text,
                                           contracts, task, job, inputs, roles, family=FAMILY,
                                           profile=profile)
    run_id = _rel(root.resolve(), run.root.resolve())
    used = profile or run.profile
    provenance = {"harness": used.harness, "launch-model": used.launch_model, "effort": used.effort}

    def metadata(answer: Answer, outcome: str, launch: Path, raw: Path | None, candidate: str | None) -> dict:
        saved = directory / "results" / launch.name
        completed_at = observations.timestamp()
        if (saved / "result.md").exists():
            completed_at = frontmatter.parse((saved / "result.md").read_text(encoding="utf-8")).data["completed-at"]
        return {
            "description": f"Retained {outcome} result of {operation.identity} on {note}", "format": FORMAT,
            "operation": operation.identity, "operation-sha256": observations.sha(operation.text.encode()),
            "note": note, "input-sha256": observations.sha(text.encode()),
            "candidate": _rel(root, saved / "candidate.md") if candidate is not None else None,
            "candidate-sha256": observations.sha(candidate.encode()) if candidate is not None else None,
            "observation": _rel(root, directory / "observation.json"),
            "contract-sha256": result_contract.fingerprint(contracts), "profile": provenance,
            "model": answer.record["model"], "run": run_id, "launch": launch.name, "completed-at": completed_at,
            "raw-output": _rel(root, raw) if raw is not None else None,
            "raw-output-sha256": observations.sha(raw.read_bytes()) if raw is not None else None,
        }

    def complete(answer: Answer) -> Edit:
        launch = Path(answer.record["launches"][-1])
        if (launch / "inputs/text.md").read_bytes() != text.encode("utf-8"):
            raise result_contract.ControllerError("launch input text differs from the retained capture")
        raw = launch / "outputs" / "result.md"
        fragment = raw.read_bytes().decode("utf-8")
        parsed = frontmatter.parse(fragment)
        if not parsed.ok:
            raise Rejected([f"result: {error}" for error in parsed.errors])
        data, problems = parsed.data, []
        if data.get("type") != RESULT_TYPE:
            problems.append(f"result: declare type: {RESULT_TYPE}")
        reserved = sorted(data.keys() - WORKER_FIELDS)
        if reserved:
            problems.append(f"result: remove controller-owned or unknown fields: {', '.join(reserved)}")
        outcome = data.get("outcome")
        if outcome not in ALLOWED[mode]:
            problems.append(f"result: `outcome` must be {' or '.join(ALLOWED[mode])} here; "
                            "when you cannot proceed, write the problem file instead")
        candidate = answer.outputs.get("candidate")
        if outcome == "changed":
            if candidate is None:
                problems.append("write the complete changed text to the candidate output")
            elif candidate == text:
                problems.append("the candidate equals the input text; use `outcome: unchanged`")
            else:
                removed = data.get("removed-links") if isinstance(data.get("removed-links"), list) else []
                problems += edits.artifact_bounds(root, note, text, candidate, baseline)
                problems += edits.preserved(text, candidate, removed)
                plain = normalize_text(candidate, "prose")
                problems += [f"the item `{item['quote'][:60]}` is not approved but was applied; "
                             "leave its passage as it was"
                             for item in withheld if normalize_text(item["quote"], "prose") not in plain]
        elif candidate is not None and candidate != text:
            problems.append(f"`outcome: {outcome}` writes no changed text; remove the candidate output")
        if outcome == "proposed" and isinstance(data.get("proposals"), list):
            for index, proposal in enumerate(data["proposals"], 1):
                quote = proposal.get("quote") if isinstance(proposal, dict) else None
                if not isinstance(quote, str) or not quote:
                    continue                                   # the schema reports it
                found = match_quote(quote, text, kind="prose")
                if not found.matched:
                    problems.append(f"proposal {index}: the quote `{quote[:60]}` occurs {found.count} times "
                                    "in the input text; quote a passage that occurs exactly once")
        if problems:
            raise Rejected(problems)
        kept = candidate if outcome == "changed" else text if outcome == "unchanged" else None
        body = frontmatter.strip(fragment)
        full = {**data, **metadata(answer, outcome, launch, raw, kept)}
        path = directory / "results" / launch.name / "result.md"
        rendered = result_contract.render(full, body)
        _validate(root, path, rendered, snapshot)
        return Edit(outcome, full, body, rendered, kept, path, directory, answer)

    def problem(answer: Answer) -> Edit:
        launch = Path(answer.record["launches"][-1])
        body = f"# Problem\n\n{answer.problem.strip()}\n"
        full = {"type": RESULT_TYPE, "outcome": "problem", **metadata(answer, "problem", launch, None, None)}
        path = directory / "results" / launch.name / "result.md"
        rendered = result_contract.render(full, body)
        try:
            _validate(root, path, rendered, snapshot)
        except Rejected as error:
            raise result_contract.ControllerError(f"problem result does not validate: {error}") from error
        return Edit("problem", full, body, rendered, None, path, directory, answer)

    accepted: dict[str, Edit] = {}

    def check(answer: Answer) -> list[str]:
        try:
            accepted[answer.key] = complete(answer)
        except Rejected as rejected:
            return rejected.problems
        except OSError as error:
            raise result_contract.ControllerError(f"missing launch evidence: {error}") from error
        return []

    state = "interrupted"
    try:
        answer = run.checked(job, lambda problems: task + edits.rejection(problems), check, ["result"],
                             optional=["candidate"], attempts=ATTEMPTS, inputs=inputs, profile=profile)
        edit = problem(answer) if answer.problem is not None else accepted[answer.key]
        _retain(directory, record, edit)
        state = "completed"
        return edit
    except result_contract.ControllerError as error:
        state = "controller-error"
        run.log(event="controller-error", job=job, problem=str(error))
        raise
    except NoProgress:
        state = "no-progress"
        raise
    except OutOfAttempts:
        state = "out-of-attempts"
        raise
    except LaunchFailed:
        state = "stopped"
        raise
    finally:
        observations.refresh(run, directory, record, state=state)


def _retain(directory: Path, record: dict, edit: Edit) -> None:
    """Write the result and its candidate into the observation; a replay must write the same bytes."""
    files = {edit.path: edit.text}
    if edit.candidate is not None:
        files[edit.path.with_name("candidate.md")] = edit.candidate
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists() and path.read_bytes() != content.encode("utf-8"):
            raise result_contract.ControllerError(f"retained result changed on replay: {path}")
        path.write_bytes(content.encode("utf-8"))
        relative = path.relative_to(directory).as_posix()
        if relative not in record["completed-results"]:
            record["completed-results"].append(relative)
            record["completed-result-sha256"][relative] = observations.sha(content.encode("utf-8"))
    record["latest-result"] = edit.path.relative_to(directory).as_posix()


def run(root: Path, operation: Operation, note: str, text: str, roles: dict[str, dict], profile: Profile,
        run_dir: Path, *, timeout: float | None = None, harnesses=HARNESSES) -> dict:
    """Run one operation alone in its own run, between two checkout snapshots; return the command's report."""
    root = root.resolve()
    before = gates.checkout_state(root)
    report = {"run-dir": _rel(root, run_dir.resolve()), "operation": operation.identity, "note": note,
              "state": "not-run", "outcome": None, "result": None, "candidate": None, "problem": None,
              "stopped": None}
    try:
        with Run(run_dir, root, profile, timeout=timeout, harnesses=harnesses) as active:
            edit = ask(active, root, operation, note, text, roles)
        report.update({"state": "edited", "outcome": edit.outcome, "result": _rel(root, edit.path),
                       "observation": _rel(root, edit.observation)})
        if edit.candidate is not None:
            report["candidate"] = edit.data["candidate"]
        if edit.outcome == "problem":
            report["problem"] = edit.body.removeprefix("# Problem\n\n").strip()
    except NoProgress as spent:
        report.update({"state": "no-progress", "problem": str(spent)})
    except OutOfAttempts as spent:
        report.update({"state": "out-of-attempts", "problem": str(spent)})
    except result_contract.ControllerError as error:
        report.update({"state": "controller-error", "stopped": str(error)})
    except LaunchFailed as failure:
        report.update({"state": "stopped", "stopped": str(failure)})
    changed = gates.changed_paths(before, gates.checkout_state(root))
    report["guard"] = {"clean": not changed, "changed": changed}
    report["ok"] = report["state"] == "edited" and report["outcome"] != "problem"
    return report

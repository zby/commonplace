"""The gate sweep: review notes against criteria in headless worker calls.

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

`ask()` asks the worker calls for a set of pairs over given note texts and
returns each pair's report, with the accepted review as a result
(`results.Result`) that is not yet written. It reads and writes no result
file. It forms the calls in one of two groupings:

- `pair`: one `checked()` call per pair, named `<note>::<criterion-id>`, with
  inputs `note` and `criterion` and one output `review`;
- `bundle`: one call per note and bundle of catalog gates, named
  `<note>::<bundle>/*`, with input `note`, one input `gate-<name>` and one
  output `review-<name>` per asked gate of that bundle. A launch's fixed
  context dominates its cost, so this shares it across the bundle. A bundle
  with one asked gate, and every type, collection and critique pair, is a
  pair call.

Each review is checked by the strict outcome parser, so a malformed review is
a rejected attempt whose problem goes into the next prompt (in a bundle call,
the whole call is asked again). An accepted review becomes its pair's
result, hashed over the exact texts the worker was given. A worker problem
or a call out of attempts gives no result and is reported for each of its
pairs. A launch failure or usage limit stops the asking: no call not yet
started is asked, and a rerun with the same run directory continues by
replay.

`sweep()` is the `run gates` command. It reads the notes from disk, skips
pairs whose result file is fresh unless forced, runs `ask()` in its own run
between two checkout snapshots, and writes each result file as its answer
arrives, so results already written stay after a stop. The full pass uses
`ask()` alone and writes its result files once, at its end.

The prompt around the inputs is outside the freshness hashes: keep it
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
import json
import subprocess
import threading
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
from commonplace.lib.review_workflows import (
    criteria,
    observations,
    result_contract,
    results,
)

STATE = Path("kb/reports/state/review")
RUNS = STATE / "runs" / "v2"
PROFILES_REL = "instructions/review-profiles.yaml"
ATTEMPTS = 3
"""Attempts per call, counting rejected reviews and launches that returned no answer."""
GROUPINGS = ("pair", "bundle")


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

    @property
    def bundle(self) -> str | None:
        """The catalog bundle of a gate pair; None for the type, collection and critique lenses."""
        return self.criterion_id.split("/", 1)[0] if self.kind == "gate" else None


@dataclass(frozen=True)
class Call:
    """One worker call: a single pair, or the stale gates of one bundle on one note."""
    job: str
    pairs: tuple[Pair, ...]

    def names(self) -> list[tuple[Pair, str, str]]:
        """Each pair with its criterion input and review output name."""
        if len(self.pairs) == 1:
            return [(self.pairs[0], "criterion", "review")]
        return [(pair, f"gate-{name}", f"review-{name}")
                for pair, name in ((pair, pair.criterion_id.split("/", 1)[1]) for pair in self.pairs)]


def calls(pending: list[Pair], grouping: str = "pair") -> list[Call]:
    """The worker calls for the pending pairs: one per pair, or one per note and bundle of gates."""
    if grouping not in GROUPINGS:
        raise ValueError(f"grouping must be one of {', '.join(GROUPINGS)}: {grouping}")
    groups: dict[tuple[str, str], list[Pair]] = {}
    for pair in pending:
        key = (pair.note, pair.bundle) if grouping == "bundle" and pair.bundle else (pair.job, "")
        groups.setdefault(key, []).append(pair)
    return [Call(members[0].job if len(members) == 1 else f"{note}::{bundle}/*", tuple(members))
            for (note, bundle), members in groups.items()]


@dataclass
class PairReport:
    note: str
    criterion: str
    job: str
    state: str                        # fresh, reviewed, problem, out-of-attempts or not-run
    outcome: str | None = None
    problem: str | None = None
    result: results.Result | None = field(default=None, repr=False)   # the accepted review, not yet written


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
                "pairs": [{key: value for key, value in asdict(pair).items() if key != "result"}
                          for pair in self.pairs]}


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


def pairs(root: Path, notes: list[str], requests: list[str] | None = None,
          texts: dict[str, str] | None = None) -> list[Pair]:
    """The applicable (note, criterion) pairs for repository-relative notes and criterion requests.

    `requests` holds gate ids, bundle names and the lenses `type`,
    `type/<name>`, `collection`, `collection/<path>` and `critique`; None
    means all gates. `texts` gives a note's text in place of the file's.
    """
    found: list[Pair] = []
    for note, criterion in criteria.select(root, notes, requests, texts):
        pair = Pair(note, criterion.identity, criterion.kind, results.criterion_id(root, criterion.identity))
        if "#" in pair.job:
            raise ValueError(f"{pair.job}: '#' is reserved in job names by the runtime")
        found.append(pair)
    return found


# --- The worker call -----------------------------------------------------------

READING = """\
Reading scope:
- The note's relative links resolve from `{note_dir}/`. For grounding or \
consistency checks, read only files the note links to, except for one exact \
local path that the criterion explicitly tells you to derive from such a link.
- Ignore review backups, workshop copies and historical artifacts unless the \
note links to them.
- Never browse shared operational state or other runs, even through a link. Operational inputs must be supplied copies.\n- Do not delegate or start another agent.
"""

PROMPT = """\
Review one note against one criterion. Nobody will answer questions. If you \
cannot judge the pair, write {problem} instead of guessing.

The note is `{note}` in this repository; its text is {note_input}. The \
criterion is `{criterion}`; its text is {criterion_input}. Judge these input \
texts; the files on disk may have changed since.
{wrapper}
{reading}
Output:
- Write the review to {review}. Write nothing else: create, edit or delete no \
file in the repository, and run no command that changes it or its git state.
{contract}
"""

BUNDLE_PROMPT = """\
Review one note against each gate of one bundle. Nobody will answer questions. \
If you cannot judge the note, write {problem} instead of guessing.

The note is `{note}` in this repository; its text is {note_input}. Judge this \
input text; the file on disk may have changed since. Each gate's text is an \
input, and each gate's review is its own output:
{gates}
Judge each gate independently, as if it were the only one: apply only its own \
failure mode and test, and let no finding or result under one gate decide another.

{reading}
Output:
- Write each gate's review to its output. Write nothing else: create, edit or \
delete no file in the repository, and run no command that changes it or its git state.
- Each review stands alone, with its own typed findings and outcome:
{contract}
"""

TITLE_AND_DESCRIPTION = (
    "Catalog gates judge four properties for every note: whether a claim title is a proposition, whether it is"
    " contestable, whether it composes as a linkable phrase, and whether the description discriminates the note."
    " Leave those to their gates; judge a title or description here only against a convention this document adds."
)
"""The boundary against the frontmatter gates, shared by both conformance wrappers (ADR 131)."""

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
    TITLE_AND_DESCRIPTION,
)
"""Mechanical only: how to apply a type spec as a gate. What a good note of the type is belongs in the spec."""

COLLECTION_WRAPPER = (
    "This is a collection-conformance gate. The gate is the authoring contract",
    "(COLLECTION.md) of the collection the note lives in: conventions and routing",
    "rules, not a Failure mode / Test procedure.",
    "The embedded contract below is the authoritative gate text for this pair.",
    "Judge whether the note follows the collection's authoring conventions:",
    "placement, quality goal, outbound linking rules, and the title and description conventions",
    "that are specific to this collection.",
    "If the COLLECTION.md carries a `## Review` section, treat it as the operative test.",
    "- PASS: the note follows the collection's conventions.",
    "- WARN: the note conforms overall, but specific conventions go unmet; name each unmet convention as a finding.",
    "- FAIL: the note does not follow the collection's conventions: wrong placement, or its conventions are systematically unmet.",
    "Structural checks (frontmatter fields, schema conformance) are the deterministic validator's job; do not re-check them here.",
    "The note's conformance to its type spec is the type-conformance pair's job; judge only what the collection contract asks beyond the type contract.",
    TITLE_AND_DESCRIPTION,
)
"""Mechanical only: how to apply a collection contract as a gate; its criteria belong in the contract."""

VERDICT_OUTPUT = """\
- Write YAML frontmatter with type: types/review-result.md, findings, then outcome: pass | warn | fail.
- Each finding has scope: passage | document, quotes (verbatim target spans that occur once, empty for document scope;
  line wraps and quote-mark style are ignored when matching),
  reason, and level: info | warn | fail. WARN/FAIL require findings; PASS may have INFO findings.
- Follow with a # Review title and explanatory body. No terminal Result footer.
- The supplied review-result type and schema define the output contract. Supply only worker-owned fields;
  the controller supplies all provenance. Express findings once in frontmatter, not a second prose list."""

REPORT_OUTPUT = """\
- Write YAML frontmatter with type: types/review-result.md, findings, outcome: report, and attack-outcome.
- Findings have scope, quotes and reason, but no severity level. An empty list is allowed.
- Write the complete critique body, including its central commitment, mode and required sections.
- Use the supplied review-result contract. Supply only worker-owned fields. No terminal Result footer."""


def prompt(call: Call | Pair, problems: list[list[str]] = ()) -> str:
    """The reviewer's task for one call; `problems` are earlier attempts' rejections, oldest first."""
    call = call if isinstance(call, Call) else Call(call.job, (call,))
    first = call.pairs[0]
    reading = READING.format(note_dir=Path(first.note).parent.as_posix())
    if len(call.pairs) == 1:
        wrapper = {criteria.TYPE: TYPE_WRAPPER, criteria.COLLECTION: COLLECTION_WRAPPER}.get(first.kind, ())
        text = PROMPT.format(
            problem=PROBLEM_REF, note=first.note, note_input=input_ref("note"), criterion=first.criterion,
            criterion_input=input_ref("criterion"),
            wrapper="".join(f"\n{line}" for line in wrapper) + "\n" * bool(wrapper), reading=reading,
            review=output_ref("review"), contract=VERDICT_OUTPUT if first.contract == "verdict" else REPORT_OUTPUT)
    else:
        gates = "".join(f"- `{pair.criterion}`: its text is {input_ref(given)}; write its review to "
                        f"{output_ref(output)}.\n" for pair, given, output in call.names())
        text = BUNDLE_PROMPT.format(problem=PROBLEM_REF, note=first.note, note_input=input_ref("note"),
                                    gates=gates, reading=reading, contract=VERDICT_OUTPUT)
    if problems:
        text += ("\nAn earlier review of this pair was rejected. Write it again, correcting:\n" if len(call.pairs) == 1
                 else "\nAn earlier answer to this bundle was rejected. Write every review again, correcting:\n")
        text += "".join(f"- {problem}\n" for problem in problems[-1])
    return text



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

def ask(run: Run, root: Path, wanted: list[Pair], texts: dict[str, str], *, grouping: str = "pair",
        max_workers: int | None = None, publish=None, captured_criteria: dict[str, str] | None = None,
        contracts: dict[str, bytes] | None = None,
        operational_inputs: dict[str, dict[str, str]] | None = None) -> tuple[list[PairReport], str | None]:
    """Assess captured inputs, retain typed observations, and optionally publish current views."""
    run_id = run.root.resolve().relative_to(root.resolve()).as_posix()
    profile = {"harness": run.profile.harness, "launch-model": run.profile.launch_model, "effort": run.profile.effort}
    criterion_texts = captured_criteria if captured_criteria is not None else {
        pair.criterion: results.criterion_file(root, pair.criterion).read_bytes().decode("utf-8") for pair in wanted}
    contracts = contracts if contracts is not None else result_contract.capture_contract()
    operational_inputs = operational_inputs or {}
    reports = {pair: PairReport(pair.note, pair.criterion, pair.job, "not-run") for pair in wanted}
    stop = threading.Event()
    stopped: list[str] = []

    def one(call: Call) -> None:
        if stop.is_set():
            return
        names = call.names()
        note_text = texts[call.pairs[0].note]
        inputs = {"note": note_text, **{given: criterion_texts[pair.criterion] for pair, given, _ in names},
                  **{f"output-contract-{index}": value.decode("utf-8")
                     for index, (_, value) in enumerate(sorted(contracts.items()))},
                  **{f"supplied-{name}": item["text"] for name, item in operational_inputs.items()}}

        def invocation(problems=()):
            text = prompt(call, problems)
            if operational_inputs:
                text += "\nExplicit self-contained operational inputs (do not browse their origins):\n" + "\n".join(
                    f"- {name}: `{item['origin']}` supplied as {input_ref('supplied-' + name)}"
                    for name, item in operational_inputs.items())
            return text

        records = {}
        for pair, given, _ in names:
            directory, record = observations.begin(run, root, pair, note_text, inputs[given], contracts,
                                                   invocation(), call.job, inputs, operational_inputs)
            records[pair] = directory, record
        candidates = {}

        def candidate(answer, pair, given, output):
            launch = Path(answer.record["launches"][-1])
            raw_path = launch / "outputs" / f"{output}.md"
            raw = raw_path.read_bytes()
            if (launch / "inputs/note.md").read_bytes() != note_text.encode("utf-8"):
                raise ValueError("launch target bytes differ from retained capture")
            if (launch / "inputs" / f"{given}.md").read_bytes() != inputs[given].encode("utf-8"):
                raise ValueError("launch criterion bytes differ from retained capture")
            directory, _ = records[pair]
            saved = directory / "results" / launch.name / f"{output}.md"
            completed_at = observations.timestamp()
            if saved.exists():
                completed_at = results.frontmatter.parse(saved.read_bytes().decode("utf-8")).data["completed-at"]
            metadata = {
                "description": f"Retained {pair.contract} review of {pair.note} against {pair.criterion}",
                "contract": pair.contract, "note": pair.note, "criterion": pair.criterion,
                "note-sha256": results.note_sha256(note_text, inputs[given]),
                "criterion-sha256": results.criterion_sha256(inputs[given]),
                "target-sha256": observations.sha(note_text.encode()),
                "target-capture": (directory / "inputs/target" / pair.note).relative_to(root).as_posix(),
                "observation": (directory / "observation.json").relative_to(root).as_posix(),
                "contract-sha256": result_contract.fingerprint(contracts), "profile": profile,
                "model": answer.record["model"], "run": run_id, "launch": launch.name,
                "completed-at": completed_at, "raw-output": raw_path.relative_to(root).as_posix(),
                "raw-output-sha256": observations.sha(raw),
            }
            checked = result_contract.complete(root, results.result_path(root, pair.note, pair.criterion_id),
                                               raw.decode("utf-8"), metadata=metadata,
                                               target=note_text, contracts=contracts)
            return checked, saved

        def found(answer) -> list[str]:
            problems = []
            for pair, given, output in names:
                try:
                    candidates[pair] = candidate(answer, pair, given, output)
                except ValueError as error:
                    problems.append(f"{output}: {error}")
            return problems
        state = "interrupted"
        try:
            answer = run.checked(call.job, invocation, found,
                                 [output for _, _, output in names], attempts=ATTEMPTS, inputs=inputs)
            if answer.problem is not None:
                state = "problem"
                for pair in call.pairs:
                    reports[pair].state, reports[pair].problem = state, answer.problem
                return
            for pair, _, output in names:
                checked, saved = candidates[pair]
                saved.parent.mkdir(parents=True, exist_ok=True)
                if saved.exists() and saved.read_bytes() != checked.text.encode("utf-8"):
                    raise ValueError(f"retained result changed on replay: {saved}")
                saved.write_bytes(checked.text.encode("utf-8"))
                result = results.from_candidate(checked)
                directory, record = records[pair]
                relative = saved.relative_to(directory).as_posix()
                if relative not in record["completed-results"]:
                    record["completed-results"].append(relative)
                    record["completed-result-sha256"][relative] = observations.sha(saved.read_bytes())
                record["latest-result"] = relative
                record["validation-warnings"] = list(checked.warnings)
                observations.refresh(run, directory, record, state="completed")
                if publish is not None:
                    publish(result)
                report = reports[pair]
                report.state, report.outcome, report.result = "reviewed", result.outcome, result
            state = "completed"
        except OutOfAttempts as spent:
            state = "out-of-attempts"
            for pair in call.pairs:
                reports[pair].state, reports[pair].problem = state, str(spent)
        except LaunchFailed as failure:
            state = "stopped"
            stop.set()
            stopped.append(str(failure))
        finally:
            for directory, record in records.values():
                observations.refresh(run, directory, record, state=state)

    gather(*(lambda call=call: one(call) for call in calls(wanted, grouping)), max_workers=max_workers)
    return list(reports.values()), stopped[0] if stopped else None


def sweep(root: Path, wanted: list[Pair], profile: Profile, run_dir: Path, *, max_workers: int | None = None,
          timeout: float | None = None, force: bool = False, grouping: str = "pair",
          harnesses=HARNESSES, publish_results: bool = True,
          operational_inputs: dict[str, dict[str, str]] | None = None) -> SweepReport:
    """Review frozen request inputs. Resuming never silently substitutes live bytes."""
    run_id = run_dir.resolve().relative_to(root.resolve()).as_posix()
    before = checkout_state(root)
    with Run(run_dir, root, profile, timeout=timeout, harnesses=harnesses, max_workers=max_workers) as run:
        snapshot_path = run_dir / "review-request.json"
        selection = [asdict(pair) for pair in wanted]
        if snapshot_path.exists():
            snapshot = json.loads(snapshot_path.read_text())
            if (snapshot["pairs"] != selection or snapshot["grouping"] != grouping
                    or snapshot["publish-results"] != publish_results):
                raise ValueError("resume selection differs from the captured request; start a new run")
            if timeout is not None and timeout != snapshot["timeout"]:
                raise ValueError("resume timeout differs from the captured request")
            run.timeout = snapshot["timeout"]
            texts, criterion_texts = snapshot["targets"], snapshot["criteria"]
            operational_inputs = snapshot["operational-inputs"]
            contracts = {name: value.encode("utf-8") for name, value in snapshot["contracts"].items()}
            if result_contract.fingerprint(result_contract.capture_contract()) != result_contract.fingerprint(contracts):
                raise ValueError("output contract changed; start a new run instead of resuming")
        else:
            texts = {pair.note: (root / pair.note).read_bytes().decode("utf-8") for pair in wanted}
            criterion_texts = {pair.criterion: results.criterion_file(root, pair.criterion).read_bytes().decode("utf-8")
                               for pair in wanted}
            contracts = result_contract.capture_contract()
            snapshot = {"version": observations.VERSION, "pairs": selection, "grouping": grouping,
                        "timeout": run.timeout, "max-workers": max_workers,
                        "operational-inputs": operational_inputs or {},
                        "publish-results": publish_results, "targets": texts, "criteria": criterion_texts,
                        "contracts": {name: value.decode("utf-8") for name, value in contracts.items()},
                        "kb-commit": observations.git_head(root)}
            observations.atomic_json(snapshot_path, snapshot)
        fresh = set()
        if not force:
            for pair in wanted:
                path = results.result_path(root, pair.note, pair.criterion_id)
                if path.exists():
                    stored = results.read_result(path)
                    if (stored.note_sha256 == results.note_sha256(texts[pair.note], criterion_texts[pair.criterion])
                            and stored.criterion_sha256 == results.criterion_sha256(criterion_texts[pair.criterion])
                            and stored.contract_sha256 == result_contract.fingerprint(contracts)):
                        fresh.add(pair)
        asked, stopped = ask(run, root, [pair for pair in wanted if pair not in fresh], texts, grouping=grouping,
                             max_workers=max_workers,
                             publish=(lambda result: results.write_result(root, result)) if publish_results else None,
                             captured_criteria=criterion_texts, contracts=contracts, operational_inputs=operational_inputs)
    found = {(report.note, report.criterion): report for report in asked}
    reports = [found.get((pair.note, pair.criterion)) or PairReport(pair.note, pair.criterion, pair.job, "fresh")
               for pair in wanted]
    return SweepReport(run_id, reports, stopped, changed_paths(before, checkout_state(root)))

"""Revise one markdown artifact through the simplification passes, as a workflow over headless workers.

The judgment lives in the library's instruction files: `revise-an-article-or-note.md`
is the assessment's `criterion` input, and each pass file under
`instructions/simplification-passes/` is an edit operation that
`edit_operations.ask()` runs. Editors receive `execute-a-revision-pass.md`
as `execution`, not the planning instruction. Fixed-plan execution does not construct an assessment request.
Prompts here say only how to read inputs and write outputs.
Code owns the plan's check, the order, the bounds it can check and the one
write to the checkout.

Every invocation is a new run, in `edits.new_run_dir()`, named by its UTC
start time under the note's path; the run records the hash of its start
text (`edits.begin()`). No run is repeated or resumed. A run ends in one of
three ways: it completed, it needs continuation, or it failed. It publishes
before it asks a per-item pass for proposals and at the end of its plan, so
at most twice, and writes nothing to the note after it ends. What it could not finish is
its **continuation record** (`CONTINUATION`, `continuation()`), also given in
the report: the text it was made for and each unfinished item in dependency
order, with the actor expected to resolve it, the items to settle first,
the command or instruction step that proceeds and the evidence. An entry
not run is continued from a one-entry plan file the run writes under
`artifact/continue/` (`CONTINUE_DIR`), so its scope is kept; a fix entry
names the run's copy of its review result (`_kept_finding()`). A later
command acts on a stop's output by naming the file or the run:

1. **Assessment.** One `decide()` ask, on the judgment profile, with two
   outputs: `assessment` for the operator and `plan` for code. Code hands the
   assessor the closed list of passes with their `effort` and `depth`
   (`catalog()`), and `plan_problems()` rejects unknown passes, missing
   fields and an order against the depth the pass files declare. The run
   keeps `artifact/assessment.md` and `artifact/plan.yaml`, then proceeds.
   A plan whose `stop` is set ends the run there, with the pending answers
   file `artifact/stop-answers.md` over the plan; the operator's decision is
   kept with `commonplace-revise answers record FILE`, and a replacement plan
   runs with `--plan`. A named plan bypasses assessment but still requires
   validation.
   The assessor also receives the artifact's fresh stored review results
   with outcome warn or fail (`current_findings()`); it launches no review.
   A finding the operator rejected at a triage of that same result is
   removed from it (`without_rejected()`), and the operator's rejected and
   deferred findings of the note come as `earlier-decisions`. So do the
   operator's decisions on the stops of other revise runs on the note
   (`decisions.earlier_stops()`), kept in `STOPS_FILE`; only the assessor
   receives them. The run keeps the results it assessed in
   `ASSESSMENT_INPUTS`, as a record of what it read.
   A pass that declares `responds-to`, the fix of `FIX_REL`, takes one such
   result as its `finding` input: its plan entry names the result file and
   takes the depth of the result's criterion. `one_entry_plan()` writes the
   plan of `--pass NAME` and `--finding RESULT`. With a `review` profile
   (`--full`), the assessment is preceded by the review step: every review
   operation with a depth (`review_pairs()`), the type and collection
   reviews among them, runs through
   `gates.sweep()` in `reviews/` under the run directory, publishing results
   and reusing fresh ones. Then each review operation that judges
   operational inputs (`criteria.SUPPLIED`) runs alone in its own run and
   publishes nothing: the compression synthesis in `synthesis/` on the
   checks' results, and the role report in `role/` on the artifact's inbound
   contexts (`inbound.collect()`). The assessor also receives the depth 1
   reports, the synthesis report and the role report, and its plan's `stop`
   is how a depth 1 proposal ends the run. A review without a result stops the run.
   **Triage** (`triage`) asks the operator instead of an assessor. It takes
   the results `current_findings()` gives, keeps those with a warn or fail
   finding (`triage_findings()`), records them in `triage-inputs.json` and
   copies each into `artifact/findings/` as the question of a pending answers
   file `artifact/finding-answers-<key>.md`. Then it ends. The decided files,
   named to `commonplace-revise apply FILE ...` (`answers_plan()`), make a
   new run whose plan holds one fix entry per result with an `approved`
   finding, in depth order, naming the copy as its `finding`; the fix also
   receives the answers as `finding-answers` and fixes only those findings.
2. **Passes.** Validated plans run automatically. An invalid named plan
   raises ValueError, a command error, not a worker retry. The artifact's text is kept as
   `artifact/start.md`. Each listed pass is one run of the edit route
   (`edit_operations.ask()`) on the profile its `effort` selects, with the
   current text and the roles `purpose`, `must-keep`, `scope` and `brief`. The
   route checks the edit result and the candidate and retains both in its
   observation under `artifact/edits/`; the next pass works on the
   candidate. Each pass's report and the text it left are kept under
   `artifact/reports/` and `artifact/texts/`, so the operator can read each
   pass's diff. A pass whose result is `unchanged` is `no-change`. A pass
   whose worker reports a problem, runs out of correction attempts or cannot
   launch is `problem`: the run publishes what the entries before it applied
   and ends, and that entry and the later ones are left in the continuation
   record.
3. **Per-item decisions.** The run ends at its first pass whose `decision`
   is `per-item` that proposes anything: it publishes what the earlier
   entries applied (step 5), then asks the worker for the proposals on the
   published text; when that publication fails or is held, nothing is
   asked. It writes their pending answers file (`types/answers.md`,
   `answers.pending()`) as `artifact/<pass>-answers.md`, and ends. Later
   entries wait in the continuation record, so they run on text that already
   has the approved items. The decided file, named to `commonplace-revise
   apply FILE`, makes a new run of that one pass with the answers as its
   `answers` input; naming it is the approval, and the run keeps a copy
   (`decisions.keep_answers()`). It is refused unless the validator accepts
   the answers, the note holds exactly the text the proposals were made
   for, and the note's write brief is the one the asking run recorded in
   `start.json`. Only `approved` items are applied. A file that approves no item is
   kept with `commonplace-revise answers record FILE` instead.
   When the run starts, code collects the operator's decided items from the
   other revise and rewrite runs on the same note (`decisions.earlier()`)
   and keeps them in `earlier-decisions.json`. Each per-item pass and each
   fix of a finding receives them as the input `earlier-decisions`. A
   proposal with the same `quote` and `change` as an earlier decided item
   starts decided as before, with `carried-from` naming the earlier answers
   file.
4. **Interactive passes.** `narrow-overclaims` takes its evidence from the
   conversation, which no headless worker has; it runs only when the plan's
   `must-keep` list carries that evidence explicitly (is non-empty), and is
   skipped otherwise. `split-out-a-treatment` writes a second file and the
   collection index from the discussion's text, so it is always skipped. A
   skipped pass is left in the continuation record for the session agent.
5. **Publication.** Before a per-item pass is asked for proposals, and when
   the run ends, a candidate other than the note's text is written to the
   note without a stop (`_publish()`), so a run may publish twice: changes
   applied without a decision, and items the operator already decided, need
   no second approval of the whole text. The publication is recorded in
   `edits.PUBLISHED`, with its text and its diff under
   `artifact/publications/`, the plan entries it covers and the time; the
   report lists it under `publications`. Nothing is committed. The note is
   written only while it holds the run's start text or its last publication,
   and only while the brief is unchanged. A candidate that adds a validation warning the note's text
   does not have (`edits.new_warnings()`) is not published: the run holds it
   (`edits.hold()`) as `artifact/final.md` with its diff, and ends there,
   before asking a per-item pass for proposals on a text that may never be
   published. `commonplace-revise publish RUN` publishes that exact
   candidate later, or with `--revised FILE` the operator's revision of it
   (`edits.publish_held()`).
6. **Record.** When the operator answered a run's findings in a session,
   for example by splitting the note, `record()` writes the triage's
   pending answers file over each review result the run's assessor or
   triage received, for `commonplace-revise answers record FILE`. It
   launches nothing and plans, fixes and publishes nothing, so it also
   serves an overtaken run. The recorded files are decisions on findings
   like a triage's.
"""

from __future__ import annotations

import json
import re
import shlex
from dataclasses import asdict, dataclass, field, replace
from pathlib import Path

import yaml

from commonplace.headless.decisions import decide, parse, violations
from commonplace.headless.harness import HARNESSES, Profile
from commonplace.headless.jobs import (
    PROBLEM_REF,
    Answer,
    LaunchFailed,
    OutOfAttempts,
    Run,
    input_ref,
    output_ref,
    run_lock,
)
from commonplace.lib import answers, frontmatter
from commonplace.lib.library import (
    LIBRARY_IDENTITY_PREFIX,
    artifact_identity,
    library_root,
)
from commonplace.lib.naming import write_brief_name_for
from commonplace.lib.review_workflows import (
    criteria,
    decisions,
    edit_operations,
    edits,
    gates,
    inbound,
    observations,
    result_contract,
    results,
)
from commonplace.lib.review_workflows.edit_operations import EFFORTS
from commonplace.lib.review_workflows.edits import (
    NO_WRITES,
    START,
    Conflict,
    Stop,
    capture_brief,
    guarded_changes,
)

PASSES_DIR = "instructions/simplification-passes"
FIX_REL = "instructions/fix-warnings/fix-strategy-taxonomy.md"
"""The edit operation that fixes one review finding; a plan entry for it names the finding."""
FIX = Path(FIX_REL).stem
FINDING = "finding"
"""The plan field, and the input role, that names a review result file."""
FINDING_OUTCOMES = ("warn", "fail")
"""The outcomes of the stored results the assessor receives; INFO-level findings sit in `pass` results."""
ASSESSMENT_INPUTS = "assessment-inputs.json"
"""The review results the assessor received: a record of what the run read."""
TRIAGE_INPUTS = "triage-inputs.json"
"""The review results a triage asked about: a record of what the run read."""
TRIAGE_DIR = "findings"
CONTINUE_DIR = "continue"
"""Under a run's `artifact/`: one plan file per continuation item for an entry not run, named by the item's id."""
"""Where a triage keeps, under the run's `artifact/`, a copy of each review result it asks about: the question."""
FINDING_ANSWERS = "finding-answers"
"""The input role that hands the fix the operator's approved answers on its finding's review result."""
TRIAGE_PURPOSE = "Fix the findings the operator approved at triage; the operator named no other purpose."
"""The purpose of a plan made from a triage's answers when the operator gives none."""
NOTHING_TO_TRIAGE = ("No fresh review result of the artifact has outcome warn or fail with a finding of level warn "
                     "or fail. There is nothing to triage; nothing is changed.")
REVIEWS = "reviews"
SUPPLIED_DIRS = {criteria.SYNTHESIS: "synthesis", criteria.ROLE: "role"}
"""The run directories of the full procedure's review step, under the revise run."""
REVIEW_WORKERS = 4
FOCUSED_PURPOSE ="Apply this one operation as its instruction directs; the operator named no other purpose."
"""The purpose of a one-entry plan made with `--pass` or `--finding` when the operator gives none."""
INSTRUCTION_REL = f"{PASSES_DIR}/revise-an-article-or-note.md"
EXECUTION_REL = edit_operations.EXECUTION_REL
ATTEMPTS = 3
CONVERSATION = "narrow-overclaims"
"""The pass whose evidence is the conversation: it runs only with a non-empty must-keep list."""
INTERACTIVE = {"split-out-a-treatment": "it writes a second file and the collection index from the "
                                        "discussion's text, which a headless worker has not seen"}
"""Passes the workflow never runs, with the reason."""
MUST_KEEP = "must-keep"
"""The plan field, and the input role, listing what this run keeps beyond the write brief's Must keep."""
PLAN_SCHEMA = {"purpose": str, MUST_KEEP: list, "passes": list, "stop": (str, type(None))}
ASSESSMENT, PLAN = "assessment.md", "plan.yaml"
COMMAND = "commonplace-revise"
STOP_ANSWERS = decisions.STOP_ANSWERS
"""The answers file for a plan that stops: one item, the plan."""
STOPS_FILE = "earlier-stops.json"
"""The operator's decided stops of other runs on the note that the assessor received: a record of what it read."""
CONTINUATION = decisions.CONTINUATION
REPORT = "report.json"
"""The run's report, as printed, kept in the run directory as evidence for the continuation record."""


@dataclass(frozen=True)
class Pass:
    name: str
    effort: str
    depth: int | None                 # the depth order of revise-an-article-or-note; None runs anywhere
    rel: str                          # library-relative path
    text: str
    description: str
    decision: str | None = None       # the edit operation's `decision`; None for a pass that is not one
    responds_to: tuple[str, ...] = () # criteria whose findings it fixes; a pass declaring them takes a `finding`


def passes() -> dict[str, Pass]:
    """The operations a plan may name: each simplification pass whose frontmatter declares `effort`, and the fix."""
    found = {}
    for path in [*sorted((library_root() / PASSES_DIR).glob("*.md")), library_root() / FIX_REL]:
        text = path.read_text(encoding="utf-8")
        data = frontmatter.parse(text).data
        if "effort" not in data:
            continue
        if data["effort"] not in EFFORTS or not isinstance(data.get("depth", 0), int):
            raise ValueError(f"{path.name}: `effort` must be one of {', '.join(EFFORTS)} and `depth` an integer")
        found[path.stem] = Pass(path.stem, data["effort"], data.get("depth"),
                                path.relative_to(library_root()).as_posix(), text, data.get("description", ""),
                                data.get("decision"), tuple(data.get("responds-to") or ()))
    return found


@dataclass(frozen=True)
class Finding:
    """A review result named as a plan entry's `finding`."""
    path: str                         # repository path of the review result file
    criterion: str                    # the criterion's identity
    criterion_id: str
    depth: int | None                 # the criterion file's `depth`; None when it declares none
    outcome: str | None
    text: str


CONTRACT_DEPTH = 2
"""The depth of the type and collection reviews.

A type spec and a collection contract are not review files and declare no
`depth`, so the full procedure names it here. Both say what the artifact
must be, which is the concern of depth 2. A best-effort value, as the
declared depths are.
"""
TYPE_SPEC = "types/type-spec.md"


def criterion_depth(root: Path, criterion: str) -> int | None:
    """The criterion's depth: the `depth` its file declares, or `CONTRACT_DEPTH` for a type spec or contract.

    A collection contract is a file named `COLLECTION.md`; a type spec
    declares the type `TYPE_SPEC`. None for any other file without `depth`.
    """
    path = results.criterion_file(root, criterion)
    data = frontmatter.parse(path.read_text(encoding="utf-8")).data
    depth = data.get("depth")
    if isinstance(depth, int) and not isinstance(depth, bool):
        return depth
    return CONTRACT_DEPTH if path.name == "COLLECTION.md" or data.get("type") == TYPE_SPEC else None


def read_finding(root: Path, artifact: str, raw: str) -> Finding:
    """The review result at the repository path `raw`; ValueError unless it is a review result of `artifact`."""
    path = observations.safe_path(root, raw)
    if not path.is_file():
        raise ValueError(f"finding not found: {raw}")
    text = path.read_text(encoding="utf-8")
    parsed = frontmatter.parse(text)
    data = parsed.data if parsed.ok else {}
    if data.get("type") != result_contract.TYPE or not isinstance(data.get("criterion"), str):
        raise ValueError(f"finding {raw} is not a review result")
    if data.get("note") != artifact:
        raise ValueError(f"finding {raw} is a review result of {data.get('note')}, not of {artifact}")
    criterion = data["criterion"]
    try:
        depth = criterion_depth(root, criterion)
    except (OSError, ValueError) as error:
        raise ValueError(f"finding {raw}: its criterion {criterion} cannot be read: {error}") from error
    return Finding(path.relative_to(root).as_posix(), criterion, results.criterion_id(root, criterion), depth,
                   data.get("outcome"), text)


def current_findings(root: Path, artifact: str) -> list[Finding]:
    """The artifact's fresh stored review results whose outcome is warn or fail."""
    return [read_finding(root, artifact, row.path.relative_to(root).as_posix())
            for row in results.note_rows(root, artifact)
            if row.freshness.state == "fresh" and row.outcome in FINDING_OUTCOMES]


def without_rejected(findings: list[Finding], earlier: list[dict]) -> list[Finding]:
    """The findings with each finding the operator rejected in answers to that same result removed.

    A rejection counts only when its answers' `question-sha256` is the hash
    of the result's text: the operator answered this result, not an earlier
    one. A result left with no warn or fail finding is dropped. A rejection
    of an earlier result removes nothing; the assessor receives it among
    the earlier decisions instead.
    """
    kept = []
    for finding in findings:
        rejected = decisions.rejected_in(earlier, finding.criterion, answers.sha(finding.text.encode("utf-8")))
        if not rejected:
            kept.append(finding)
            continue
        parsed = frontmatter.parse(finding.text)
        data = dict(parsed.data)
        data["findings"] = [given for given in data.get("findings") or []
                            if {key: given[key] for key in answers.FINDING_FIELDS if key in given} not in rejected]
        if any(given.get("level") in answers.FINDING_LEVELS for given in data["findings"]):
            kept.append(replace(finding, text=result_contract.render(data, frontmatter.strip(finding.text))))
    return kept


def catalog(known: dict[str, Pass]) -> str:
    """The passes the assessor may choose from, one line each, for its `passes` input."""
    def note(current: Pass) -> str:
        if current.name in INTERACTIVE:
            return " This workflow does not run it: it is left for the interactive path."
        if current.name == CONVERSATION:
            return f" This workflow runs it only when `{MUST_KEEP}` is not empty."
        if current.responds_to:
            return (f" Each entry names one review result file as `{FINDING}` and takes the depth of that "
                    "result's criterion; list one entry per finding.")
        return " The operator decides its proposals before any is applied." if current.decision == "per-item" else ""

    def depth(current: Pass) -> str:
        if current.responds_to:
            return "the depth of its finding's criterion"
        return "any" if current.depth is None else str(current.depth)
    lines = [f"- `{p.name}` (effort: {p.effort}; depth: {depth(p)}): "
             f"{p.description.rstrip('.')}.{note(p)}" for p in known.values()]
    return ("Passes, by name. Run passes with a depth in increasing depth; a pass with depth `any` "
            "may run at any point.\n\n" + "\n".join(lines) + "\n")


# --- The plan -------------------------------------------------------------------------

def label(name: str, finding: Finding | None) -> str:
    """An entry's name in jobs and run files: its pass, and for a finding also the finding's criterion id."""
    return name if finding is None else f"{name}/{finding.criterion_id}"


def _order_problems(entries: list[tuple[str, int | None]]) -> list[str]:
    problems, last = [], None
    for name, depth in entries:
        if depth is None:
            continue
        if last is not None and depth < last[1]:
            problems.append(f"`{name}` (depth {depth}) must run before `{last[0]}` "
                            f"(depth {last[1]}): list passes in increasing depth")
        last = (name, depth) if last is None or depth >= last[1] else last
    return problems


def unknown_fields(data: dict) -> list[str]:
    """The plan's top-level fields outside `PLAN_SCHEMA`, as one problem; empty when there is none."""
    unknown = sorted(str(name) for name in set(data) - set(PLAN_SCHEMA))
    return [f"the plan has unknown fields: {', '.join(unknown)}"] if unknown else []


def plan_checks(data: dict, known: dict[str, Pass], root: Path, artifact: str) -> list[str]:
    """What a plan breaks beyond its schema: unknown fields, purpose, must-keep items, entries, findings, order.

    An entry for a pass that declares `responds-to` names one review result
    of `artifact` as `finding` and takes the depth of that result's
    criterion; no other entry names a finding.
    """
    problems = unknown_fields(data) + ([] if data["purpose"].strip() else ["`purpose` is empty"])
    if not all(isinstance(claim, str) and claim.strip() for claim in data[MUST_KEEP]):
        problems.append(f"each `{MUST_KEEP}` item is a claim's text")
    entries, seen = [], set()
    for index, entry in enumerate(data["passes"], 1):
        if not isinstance(entry, dict) or not isinstance(entry.get("pass"), str):
            problems.append(f"passes item {index} must be a mapping with `pass`, optional `scope` "
                            f"and, for a pass that fixes a finding, `{FINDING}`")
            continue
        extra = sorted(set(entry) - {"pass", "scope", FINDING})
        if extra:
            problems.append(f"passes item {index} has unknown fields: {', '.join(extra)}")
        if not isinstance(entry.get("scope"), (str, type(None))):
            problems.append(f"passes item {index}: `scope` must be text or null")
        if entry["pass"] not in known:
            problems.append(f"unknown pass `{entry['pass']}`; choose from {', '.join(known)}")
            continue
        current, finding = known[entry["pass"]], None
        if current.responds_to:
            if not isinstance(entry.get(FINDING), str):
                problems.append(f"passes item {index}: `{current.name}` fixes one review finding; "
                                f"name its result file as `{FINDING}`")
                continue
            try:
                finding = read_finding(root, artifact, entry[FINDING])
            except ValueError as error:
                problems.append(f"passes item {index}: {error}")
                continue
        elif entry.get(FINDING) is not None:
            problems.append(f"passes item {index}: `{current.name}` takes no `{FINDING}`")
            continue
        name = label(current.name, finding)
        if name in seen:
            problems.append(f"`{name}` is listed twice")
            continue
        seen.add(name)
        entries.append((name, current.depth if finding is None else finding.depth))
    return problems + _order_problems(entries)


def read_plan(text: str, root: Path, artifact: str, known: dict[str, Pass] | None = None) -> dict:
    """The plan in `text`, checked and normalized (`scope` present on each pass); ValueError lists its problems."""
    known = passes() if known is None else known
    data = parse(text)
    problems = (["the plan must be a YAML mapping"] if not isinstance(data, dict)
                else violations(data, PLAN_SCHEMA) + unknown_fields(data) or plan_checks(data, known, root, artifact))
    if problems:
        raise ValueError("invalid plan: " + "; ".join(problems))
    return {"purpose": data["purpose"], MUST_KEEP: list(data[MUST_KEEP]), "stop": data["stop"],
            "passes": [{"pass": entry["pass"], "scope": entry.get("scope"),
                        **({FINDING: entry[FINDING]} if entry.get(FINDING) is not None else {})}
                       for entry in data["passes"]]}


def one_entry_plan(name: str, finding: str | None, purpose: str | None, must_keep: list[str],
                   scope: str | None = None) -> str:
    """The plan of a focused run: one entry for the pass `name`, with its scope and, when it takes one, finding."""
    entry = {"pass": name, **({"scope": scope} if scope else {}), **({FINDING: finding} if finding is not None else {})}
    return yaml.safe_dump({"purpose": purpose or FOCUSED_PURPOSE, MUST_KEEP: list(must_keep), "stop": None,
                           "passes": [entry]}, sort_keys=False, allow_unicode=True)


# --- Reports --------------------------------------------------------------------------------

@dataclass
class PassState:
    name: str                         # the entry's label: its pass, and the finding's criterion id for a fix
    scope: str | None
    effort: str
    finding: str | None = None        # repository path of the review result the entry fixes
    state: str = "pending"            # applied, no-change, skipped, problem, waiting or pending (not run)
    reason: str | None = None
    profile: dict | None = None       # the answering call's profile and recorded model
    model: str | None = None
    report: str | None = None         # repository path of the pass's report
    text: str | None = None           # repository path of the text the pass left, to diff against the one before
    answers: str | None = None        # the entry's answers file: pending while `waiting`, else the decided one it applies


@dataclass
class ReviseReport:
    run_dir: str
    artifact: str
    mode: str = "fixed-plan"
    plan: dict | None = None
    answers: list[str] = field(default_factory=list)    # the answers files this run consumed, as named
    reviews: list[dict] = field(default_factory=list)    # the review step's sweep reports, in the full procedure
    findings: list[str] = field(default_factory=list)   # review results the assessor or the triage received
    triage: dict | None = None        # a triage's answers file per review result
    passes: list[PassState] = field(default_factory=list)
    proposed: str | None = None       # repository path of the final revised text in the run directory
    new_warnings: list[str] = field(default_factory=list)   # validation warnings the text to publish adds
    published: bool = False           # this run wrote its candidate to the artifact
    publications: list[dict] = field(default_factory=list)   # the run's publication (`edits.PUBLISHED`)
    not_published: str | None = None  # why the proposed text was not written
    held: dict | None = None          # the candidate held for the operator, and the commands that publish it
    plan_stop: str | None = None      # the plan's `stop` text: the assessment is the result
    continuation: dict | None = None  # the unfinished work, as in the run's `CONTINUATION` file
    stopped: str | None = None
    conflict: str | None = None
    changed: list[str] = field(default_factory=list)

    @property
    def outcome(self) -> str:
        """How the run ended: `failed`, `needs-continuation` or `completed`.

        `failed`: a worker, a review or the write to the note failed
        (`stopped` or `conflict`). `needs-continuation`: the run did what
        it could and left a continuation record; it may have published.
        `completed`: nothing is left. The checkout guard does not enter
        into it.
        """
        if self.stopped is not None or self.conflict is not None:
            return "failed"
        return "needs-continuation" if self.continuation is not None else "completed"

    @property
    def ok(self) -> bool:
        """No failure and no conflict; leaving work to continue is ok. The guard is reported apart."""
        return self.stopped is None and self.conflict is None

    def to_dict(self) -> dict:
        data = {key.replace("_", "-"): value for key, value in asdict(self).items() if key != "changed"}
        return {"ok": self.ok, "outcome": self.outcome, **data,
                "guard": {"clean": not self.changed, "changed": self.changed}}


# --- The assessment prompt: mechanical only ------------------------------------------------

ASSESS_PROMPT = """\
Assess one artifact for revision. Nobody will answer questions. If you cannot, \
write {problem} instead of guessing.

The artifact is `{artifact}` in this repository; its text is {artifact_input}. \
Judge this input text; the file on disk may differ. The instruction is \
{criterion_input}: do its step 1, the assessment, and nothing after it. The \
plan is validated and ordinary passes run automatically. \
{purpose}{must_keep}{brief}The passes you may recommend are listed in {passes_input}; \
choose only from them, by name.
{findings}
Output:
- Write the assessment to {assessment}, as the instruction's step 1 describes.
- Write the plan to {plan}: a YAML mapping holding exactly the decision fields \
below. `purpose` is the purpose the assessment works under; `must-keep` lists \
what this run keeps beyond the write brief's Must keep, as the instruction's \
step 1 says, each item as a claim's text; `passes` \
lists the recommended passes in run order, each a mapping with `pass` (its \
name) and, when the pass should touch only part of the artifact, `scope` \
naming that part{finding_field}; `stop` is null, or the reason when the \
instruction says to stop. {no_writes}
"""

FINDINGS_INTRO = ("\nThe artifact's stored review results with outcome warn or fail are inputs. Each line gives "
                  "the result file's repository path, its criterion and the depth the criterion declares:\n")
REPORTS_INTRO = ("\nThe depth 1 review reports on this text, the compression synthesis when it ran, and the "
                 "role report are inputs. Each line gives the result file's repository path, or for the "
                 "synthesis and the role report its run "
                 "directory, and its criterion:\n")
DECISIONS_INTRO = ("\nThe operator's decisions on findings of this note, the rejected and the deferred ones, are "
                   "{decisions}.\n")
STOPS_INTRO = ("\nThe operator's decisions on the stops of earlier assessments of this note are in the section "
               "`Earlier stops` of {decisions}.\n")
FINDING_FIELD = (", and, for a pass that fixes a finding, `finding` naming that review result file's "
                 "repository path, as listed above")

# --- The workflow ------------------------------------------------------------------------------

def _rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _assessment_request(artifact: str, text: str, purpose: str | None, must_keep: list[str],
                        known: dict[str, Pass], brief: dict[str, str], findings: list[Finding] = (),
                        reports: list[Finding] = (), told: list[dict] = (),
                        stops: list[dict] = ()) -> tuple[str, dict[str, str]]:
    """The assessor's prompt and inputs.

    `findings` are the stored warn and fail results the assessor may turn
    into plan entries; `reports` are review reports it reads. Without
    findings, the passes that fix a finding are not offered. `told` holds
    the operator's rejected and deferred findings of the note
    (`decisions.planning_decisions()`); `stops` holds the operator's
    decided stops of other runs on the note (`decisions.earlier_stops()`),
    as a section after them. When there is either, the assessor receives
    them as `earlier-decisions`, and the request is otherwise unchanged.
    """
    offered = known if findings else {name: current for name, current in known.items() if not current.responds_to}
    inputs = {"artifact": text, "criterion": (library_root() / INSTRUCTION_REL).read_text(encoding="utf-8"),
              "passes": catalog(offered), **brief}
    if purpose:
        inputs["purpose"] = purpose
    if must_keep:
        inputs[MUST_KEEP] = "".join(f"- {claim}\n" for claim in must_keep)
    listed = ""
    for prefix, intro, given in (("finding", FINDINGS_INTRO, findings), ("report", REPORTS_INTRO, reports)):
        if not given:
            continue
        listed += intro
        for index, finding in enumerate(given, 1):
            inputs[f"{prefix}-{index}"] = finding.text
            depth = "" if prefix == "report" else f", depth {'none' if finding.depth is None else finding.depth}"
            listed += (f"- `{finding.path}` (criterion `{finding.criterion_id}`{depth}, outcome "
                       f"{finding.outcome}): {input_ref(f'{prefix}-{index}')}\n")
    if told or stops:
        inputs[EARLIER_DECISIONS] = "\n".join(
            [*([decisions.earlier_text(list(told))] if told else []),
             *([decisions.stops_text(list(stops))] if stops else [])])
    if told:
        listed += DECISIONS_INTRO.format(decisions=input_ref(EARLIER_DECISIONS))
    if stops:
        listed += STOPS_INTRO.format(decisions=input_ref(EARLIER_DECISIONS))
    prompt = ASSESS_PROMPT.format(
        problem=PROBLEM_REF, artifact=artifact, artifact_input=input_ref("artifact"),
        criterion_input=input_ref("criterion"), passes_input=input_ref("passes"),
        purpose=(f"The operator's purpose is {input_ref('purpose')}. " if purpose
                 else "The operator named no purpose: propose one as the instruction directs. "),
        must_keep=(f"The operator's must-keep list for this run is {input_ref(MUST_KEEP)}. " if must_keep
                   else ""),
        brief=f"The write brief is {input_ref('brief')}. " if brief else "",
        findings=listed, finding_field=FINDING_FIELD if findings else "",
        assessment=output_ref("assessment"), plan=output_ref("plan"), no_writes=NO_WRITES)
    return prompt, inputs


def _assess(run: Run, root: Path, artifact: str, prompt: str, inputs: dict[str, str], known: dict[str, Pass],
            profile: Profile) -> Answer:
    """Ask for the assessment and plan; keep the assessment and return its answer."""
    data, answer = decide(run, "assessment", prompt, PLAN_SCHEMA, output="plan", also=["assessment"],
                          check=lambda data, _text: plan_checks(data, known, root, artifact), attempts=ATTEMPTS,
                          inputs=inputs, profile=profile)
    if data is None:
        raise Stop(f"assessment: worker problem: {answer.problem}")
    run.accept(ASSESSMENT, answer.outputs["assessment"])
    return answer


def _asks(finding: Finding) -> bool:
    """Whether a review result is a question: it has a finding of level warn or fail."""
    try:
        answers.question_items(finding.path, finding.text.encode("utf-8"))
    except ValueError:
        return False
    return True


def triage_findings(root: Path, artifact: str) -> list[Finding]:
    """The review results a triage asks about: `current_findings()` that are questions, in depth order.

    A criterion without a depth runs anywhere; its result comes last.
    """
    return sorted((finding for finding in current_findings(root, artifact) if _asks(finding)),
                  key=lambda finding: (finding.depth is None, finding.depth or 0, finding.criterion_id))


def _triage(run: Run, root: Path, findings: list[Finding], earlier: list[dict], report: ReviseReport) -> None:
    """Write a pending answers file over each review result, and end; the run plans nothing.

    Each review result is copied into the run as the question of its answers
    file, so the question stays the same when the store changes. An item
    identical to one of the `earlier` decisions starts decided as before
    (`answers.pending()`).
    """
    for finding in findings:
        content = finding.text.encode("utf-8")
        question = _rel(root, run.accept(f"{TRIAGE_DIR}/{finding.criterion_id}.md", finding.text))
        file = run.accept(f"{decisions.FINDING}-answers-{answers.sha(content)[:12]}.md",
                          answers.pending(question, content, earlier))
        report.triage["results"].append({"result": finding.path, "criterion": finding.criterion_id,
                                         "question": question, "answers": _rel(root, file)})


def triage_plan(entries: list[dict], purpose: str | None, must_keep: list[str]) -> str:
    """The plan made from a triage's answers: one fix entry per review result with an approved finding."""
    return yaml.safe_dump({"purpose": purpose or TRIAGE_PURPOSE, MUST_KEEP: list(must_keep), "stop": None,
                           "passes": entries}, sort_keys=False, allow_unicode=True)


NO_RESULTS = ("{run} holds no review results: it is not a revise run that made an assessment ({assessed}) or a "
              "triage ({triaged})")


def record(root: Path, run_dir: Path) -> dict:
    """Write a pending answers file over each review result the revise run at `run_dir` holds; launch nothing.

    The results are those the run's assessor or triage received, recorded in
    `ASSESSMENT_INPUTS` or `TRIAGE_INPUTS`; only a result that is a question
    (`_asks()`) gets a file. Each file is built as a triage builds it: a copy
    of the result in `artifact/findings/` as its question, and
    `finding-answers-<key>.md`, with the run's earlier decisions carried
    over. A file that exists, written by a triage or an earlier record, is
    left as it is. Nothing is planned, fixed or published, and the note is
    not read, so this works for an overtaken run. The operator's decided
    file is kept with `commonplace-revise answers record FILE`, and
    `decisions.earlier()` then reads it as it reads a triage's. ValueError
    when the run holds no results.
    """
    root, run_dir = root.resolve(), run_dir.resolve()
    base = (root / gates.RUNS / "revise").resolve()
    if not run_dir.is_relative_to(base) or run_dir.parent == base:
        raise ValueError(f"not a revise run: {run_dir}")
    run_rel, artifact = _rel(root, run_dir), run_dir.parent.relative_to(base).as_posix() + ".md"
    captured = [run_dir / name for name in (ASSESSMENT_INPUTS, TRIAGE_INPUTS) if (run_dir / name).is_file()]
    if not captured:
        raise ValueError(NO_RESULTS.format(run=run_rel, assessed=ASSESSMENT_INPUTS, triaged=TRIAGE_INPUTS))
    found: dict[str, Finding] = {}
    for path in captured:
        for given in json.loads(path.read_text(encoding="utf-8"))["findings"]:
            finding = Finding(**given)
            if _asks(finding):
                found.setdefault(answers.sha(finding.text.encode("utf-8")), finding)
    told = run_dir / EARLIER_FILE
    earlier = json.loads(told.read_text(encoding="utf-8"))["decisions"] if told.is_file() else []
    listed = []
    with run_lock(run_dir):
        for key, finding in sorted(found.items(), key=lambda pair: (
                pair[1].depth is None, pair[1].depth or 0, pair[1].criterion_id, pair[0])):
            file = run_dir / "artifact" / f"{decisions.FINDING}-answers-{key[:12]}.md"
            written = not file.is_file()
            if written:
                name = f"{TRIAGE_DIR}/{finding.criterion_id}.md"
                copy = run_dir / "artifact" / name
                if copy.is_file() and copy.read_text(encoding="utf-8") != finding.text:
                    name = f"{TRIAGE_DIR}/{finding.criterion_id}-{key[:12]}.md"   # keep another file's question
                question = run_dir / "artifact" / name
                edits.write_text(question, finding.text)
                edits.write_text(file, answers.pending(_rel(root, question), finding.text.encode("utf-8"), earlier))
            listed.append({"result": finding.path, "criterion": finding.criterion_id,
                           "state": "written" if written else "exists", "file": _rel(root, file),
                           "command": decisions.RECORD.format(file=_rel(root, file))})
    return {"run-dir": run_rel, "artifact": artifact,
            "overtaken": decisions.overtaken(root, "revise", artifact, run_dir), "results": listed}


KB_ROLE = "kb-role"
"""The input role that hands an edit operation the `## Role` section of the note's role report."""
EARLIER_DECISIONS = "earlier-decisions"
"""The input role that hands a `per-item` pass and the fix the operator's earlier decisions on the note."""
EARLIER_FILE = "earlier-decisions.json"
"""The earlier decisions the run used: a record of what it read from the other runs."""


def role_section(report: str) -> str | None:
    """The `## Role` section of a role report's text, without its heading; None when it has none."""
    found = re.search(r"^## Role[ \t]*\n(.*?)(?=^## |\Z)", report, re.MULTILINE | re.DOTALL)
    return found.group(1).strip() or None if found else None


def _kept_finding(run: Run, root: Path, finding: Finding) -> Finding:
    """The finding as a file no later sweep replaces: a stored result is copied into the run's `findings/`.

    A result already under a run's records, such as a triage's copy, is
    kept where it is. The fix, the continuation record and its plan files
    name the copy, so a continued fix reads the result this run read.
    """
    if Path(finding.path).is_relative_to(gates.RUNS):
        return finding
    return replace(finding, path=_rel(root, run.accept(f"{TRIAGE_DIR}/{finding.criterion_id}.md", finding.text)))


def _failed(states: list[PassState], index: int, reason: str) -> None:
    """Mark the entry at `index` as `problem` with `reason`; the later entries stay `pending`."""
    states[index].state, states[index].reason = "problem", reason


def _passes(run: Run, root: Path, artifact: str, start: str, plan: dict, known: dict[str, Pass],
            profiles: dict[str, Profile], report: ReviseReport, brief: dict[str, dict], instruction: str,
            contracts: dict[str, bytes], kb_role: dict[str, str] | None = None, earlier: list[dict] = (),
            finding_answers: dict[str, dict] | None = None,
            given: dict[str, dict] | None = None, publish=None) -> tuple[str, str]:
    """Run the plan's passes from `start` through the edit route until the first stop; return the text and the end.

    The end is `done` when every entry ran or was skipped; `proposals` when a
    `per-item` pass proposed changes and the run ends at its pending answers
    file; `held` when the text so far adds a validation warning and the run
    ends before asking the next `per-item` pass for proposals; `failed` when
    an entry ended with a problem, or its answers were refused. Entries
    after the stop stay `pending`.

    Before a `per-item` pass is asked for proposals, the text the earlier
    passes applied is published (`publish(text)`), so the proposals are made
    for the note's text; a publication that fails raises, and nothing is
    asked.

    `kb_role` is the note's role in the KB, from the full procedure's role
    report; each pass receives it. `earlier` holds the operator's earlier
    decisions on this note; each `per-item` pass and each fix of a finding
    receives them, when there is at least one, as `earlier-decisions`.
    `finding_answers` maps a triage's finding to the operator's answers on
    it; the fix of that finding receives them as `finding-answers`. `given`
    maps a `per-item` entry's label to the operator's answers on its
    proposals, which the pass applies without proposing again.
    """
    finding_answers, given = finding_answers or {}, given or {}
    text = base = start                     # `base`: the note's text, the run's last publication or `start`
    findings = {entry[FINDING]: _kept_finding(run, root, read_finding(root, artifact, entry[FINDING]))
                for entry in plan["passes"] if entry.get(FINDING)}
    entries = [(known[entry["pass"]], findings.get(entry.get(FINDING))) for entry in plan["passes"]]
    report.passes = [PassState(label(current.name, finding), entry["scope"], current.effort,
                               finding.path if finding else None)
                     for entry, (current, finding) in zip(plan["passes"], entries, strict=True)]
    for state, (_, finding) in zip(report.passes, entries, strict=True):    # what each entry applies
        decided = given.get(state.name) or (finding_answers.get(finding.path) if finding else None)
        state.answers = decided["origin"] if decided else None
    must_keep = "".join(f"- {claim}\n" for claim in plan[MUST_KEEP])
    route = {"contracts": contracts, "execution": instruction}
    told = ({EARLIER_DECISIONS: {"origin": _rel(root, run.root / EARLIER_FILE),
                                 "text": decisions.earlier_text(list(earlier))}} if earlier else {})
    for index, (state, (current, finding)) in enumerate(zip(report.passes, entries, strict=True)):
        if current.name in INTERACTIVE or (current.name == CONVERSATION and not must_keep):
            state.state = "skipped"
            state.reason = ("left for the interactive path: "
                            + INTERACTIVE.get(current.name, "its evidence is the conversation, and the plan's "
                                              f"`{MUST_KEEP}` list is empty"))
            continue
        operation = edit_operations.parse(artifact_identity(root, library_root() / current.rel), current.text)
        roles = {"purpose": {"origin": "plan:purpose", "text": plan["purpose"]}, **brief,
                 **({MUST_KEEP: {"origin": f"plan:{MUST_KEEP}", "text": must_keep}} if must_keep else {}),
                 **({"scope": {"origin": "plan:scope", "text": state.scope}} if state.scope else {}),
                 **({KB_ROLE: kb_role} if kb_role else {}),
                 **({FINDING: {"origin": finding.path, "text": finding.text}} if finding else {}),
                 **({FINDING_ANSWERS: finding_answers[finding.path]}
                    if finding and finding.path in finding_answers else {}),
                 **(told if operation.decision == "per-item" or current.responds_to else {})}
        profile = profiles[current.effort]
        proposing = operation.decision == "per-item" and state.name not in given
        if proposing and text != base:
            if edits.new_warnings(root, artifact, start, text):
                return text, "held"
            publish(text)
            base = text
        try:
            if proposing:
                edit = edit_operations.ask(run, root, operation, artifact, text, roles, job=f"{state.name}/propose",
                                           profile=profile, **route)
            else:
                if state.name in given:
                    roles[edit_operations.ANSWERS] = given[state.name]
                edit = edit_operations.ask(run, root, operation, artifact, text, roles,
                                           job=f"{state.name}/apply" if state.name in given else state.name,
                                           profile=profile, **route)
        except (OutOfAttempts, LaunchFailed) as failure:         # LaunchFailed includes UsageLimited
            _failed(report.passes, index, str(failure))
            return text, "failed"
        except ValueError as refused:      # the route refused the operator's answers, such as for a changed note
            _failed(report.passes, index, str(refused))
            return text, "failed"
        state.profile, state.model = edit.data["profile"], edit.data["model"]
        if edit.outcome == "problem":
            _failed(report.passes, index, f"worker problem: {edit.answer.problem}")
            return text, "failed"
        state.report = _rel(root, run.accept(f"reports/{state.name}.md", edit.body))
        if edit.outcome == "unchanged":
            state.state = "no-change"
            if proposing:
                state.reason = "the pass found no candidate"
            continue
        if proposing:
            state.state = "waiting"
            state.answers = _rel(root, run.accept(f"{state.name}-answers.md", answers.pending(
                _rel(root, edit.path), edit.text.encode("utf-8"), list(earlier))))
            return text, "proposals"
        state.text = report.proposed = _rel(root, run.accept(f"texts/{state.name}.md", edit.candidate))
        state.state, text = "applied", edit.candidate
    return text, "done"


# --- The review step of the full procedure ----------------------------------------------------

def review_pairs(root: Path, artifact: str, text: str) -> tuple[list[gates.Pair], list[gates.Pair]]:
    """The review operations with a depth that apply to `text`, and apart those of `criteria.SUPPLIED`.

    An operation has a depth when its criterion file declares one, or when
    it is the type or the collection review (`criterion_depth()`).

    The second list holds the compression synthesis, only when a compression
    check applies, since it takes the checks' results as inputs, and the role
    report.
    """
    bundles = sorted(entry.name for entry in criteria.gates_dir().iterdir() if entry.is_dir())
    requests = [*bundles, criteria.TYPE, criteria.COLLECTION, *criteria.compression_checks(),
                *(selector for selector in criteria.REPORTS if selector not in criteria.SUPPLIED)]
    texts = {artifact: text}
    found = [pair for pair in gates.pairs(root, [artifact], requests, texts)
             if criterion_depth(root, pair.criterion) is not None]
    wanted = [selector for selector in criteria.SUPPLIED
              if selector != criteria.SYNTHESIS or any(pair.kind == criteria.COMPRESSION for pair in found)]
    supplied = [pair for pair in gates.pairs(root, [artifact], wanted, texts)
                if criterion_depth(root, pair.criterion) is not None]
    return found, supplied


def _supplied_inputs(root: Path, pair: gates.Pair, reviewed: list[gates.Pair]) -> dict[str, dict[str, str]]:
    """The operational inputs of a `criteria.SUPPLIED` pair: the compression checks' results, or the inbound contexts."""
    if pair.kind == criteria.ROLE:
        return {inbound.INPUT: inbound.supplied(root, pair.note)}
    found = {}
    for check in reviewed:
        if check.kind == criteria.COMPRESSION:
            path = results.result_path(root, check.note, check.criterion_id)
            found[Path(check.criterion_id).name] = {           # the check's name, such as detail-overhang
                "origin": _rel(root, path), "text": path.read_text(encoding="utf-8")}
    return found


def _sweep(root: Path, run_dir: Path, wanted: list[gates.Pair], profile: Profile, timeout: float | None,
           harnesses, inputs: dict[str, dict[str, str]] | None = None, workflow: str = "revise",
           targets: dict[str, str] | None = None) -> gates.SweepReport:
    """Run `wanted` through the sweep in its own new run; Stop unless every pair has a result.

    Without `inputs`, results are published to the shared store and fresh
    ones are reused. With them (a criterion of `criteria.SUPPLIED`, or the
    rewrite's review), nothing is published and the pair is always asked, as
    `commonplace-review --input` does. `targets` gives a note's text in place of its
    file (`gates.sweep()`).
    """
    observations.atomic_json(run_dir / "sweep.json", {"format": observations.VERSION, "workflow": workflow,
                                                     "profile": asdict(profile)})
    swept = gates.sweep(root, wanted, profile, run_dir, max_workers=REVIEW_WORKERS, timeout=timeout,
                        force=inputs is not None, grouping="bundle", harnesses=harnesses,
                        publish_results=inputs is None, operational_inputs=inputs, targets=targets)
    if swept.stopped:
        raise Stop(f"reviews in {swept.run_dir}: {swept.stopped}")
    unfinished = [pair.job for pair in swept.pairs if pair.state not in ("fresh", "reviewed")]
    if unfinished:
        raise Stop(f"reviews in {swept.run_dir} ended without a result: {', '.join(unfinished)}. Read the problem "
                   f"with `commonplace-review show {swept.run_dir}`; a new run asks again")
    return swept


def _review(root: Path, artifact: str, text: str, run_dir: Path, profile: Profile, timeout: float | None,
            harnesses, report: ReviseReport) -> list[Finding]:
    """Run every review operation with a depth (`review_pairs()`) on `text`, writing results as the sweep does.

    Then runs each criterion of `criteria.SUPPLIED` alone, in its own run,
    on its operational inputs, and returns those reports, which are not in
    the store, for the assessor.
    """
    wanted, supplied = review_pairs(root, artifact, text)
    report.reviews.append(_sweep(root, run_dir / REVIEWS, wanted, profile, timeout, harnesses).to_dict())
    found = []
    for pair in supplied:
        swept = _sweep(root, run_dir / SUPPLIED_DIRS[pair.kind], [pair], profile, timeout, harnesses,
                       _supplied_inputs(root, pair, wanted))
        report.reviews.append(swept.to_dict())
        found += [Finding(swept.run_dir, done.result.criterion, results.criterion_id(root, done.result.criterion),
                          criterion_depth(root, done.result.criterion), done.result.outcome,
                          results.result_text(done.result))
                  for done in swept.pairs if done.result is not None]
    return found


def role_pair(root: Path, artifact: str, text: str) -> gates.Pair | None:
    """The pair of `artifact` and the role report (`criteria.ROLE`) for `text`; None when it does not apply."""
    found = gates.pairs(root, [artifact], [criteria.ROLE], {artifact: text})
    return found[0] if found else None


def stored_role(root: Path, artifact: str, text: str) -> Finding | None:
    """The role report of a full procedure's run on this same `text`, when it is fresh; otherwise None.

    A role report publishes no result, so the shared store never holds one.
    The full procedure keeps its role report in `role/` under its revise
    run. The revise runs of the artifact are read newest first, and the
    first fresh report is returned. A report is fresh when its captured
    request holds the same pair, the same artifact text, the same criterion
    text, the same inbound contexts as `inbound.collect()` gives now and the
    same output contract, and the review completed.
    """
    base = root / gates.RUNS / "revise" / artifact.removesuffix(".md")
    requests = sorted(base.glob(f"*/{SUPPLIED_DIRS[criteria.ROLE]}/review-request.json"), reverse=True)
    pair = role_pair(root, artifact, text) if requests else None
    if pair is None:
        return None
    criterion = results.criterion_file(root, pair.criterion).read_text(encoding="utf-8")
    contexts, contract = inbound.collect(root, artifact), result_contract.capture_contract(root)
    for request in requests:
        data = json.loads(request.read_text(encoding="utf-8"))
        contracts = {name: value.encode("utf-8") for name, value in data["contracts"].items()}
        if (data["pairs"] != [asdict(pair)] or data["targets"].get(artifact) != text
                or data["criteria"].get(pair.criterion) != criterion
                or data["operational-inputs"].get(inbound.INPUT, {}).get("text") != contexts
                or result_contract.fingerprint(contracts) != result_contract.fingerprint(contract)):
            continue
        for record in sorted((request.parent / "artifact" / "reviews").glob("*/observation.json")):
            observation = json.loads(record.read_text(encoding="utf-8"))
            if observation.get("state") == "completed" and observation.get("latest-result"):
                path = record.parent / observation["latest-result"]
                report = path.read_text(encoding="utf-8")
                return Finding(_rel(root, path), pair.criterion, pair.criterion_id,
                               criterion_depth(root, pair.criterion), frontmatter.parse(report).data.get("outcome"),
                               report)
    return None


def role_report(root: Path, artifact: str, text: str, run_dir: Path, profile: Profile, timeout: float | None,
                harnesses, workflow: str) -> Finding | None:
    """Run the role report alone on `text` in the new run at `run_dir`; Stop unless it has a result.

    The run collects the inbound contexts (`inbound.collect()`). Nothing is
    published. None when the role report does not apply to the artifact.
    """
    pair = role_pair(root, artifact, text)
    if pair is None:
        return None
    swept = _sweep(root, run_dir, [pair], profile, timeout, harnesses, {inbound.INPUT: inbound.supplied(root, artifact)},
                   workflow)
    [done] = swept.pairs
    return Finding(swept.run_dir, done.result.criterion, results.criterion_id(root, done.result.criterion),
                   criterion_depth(root, done.result.criterion), done.result.outcome,
                   results.result_text(done.result))


def depth_one_reports(root: Path, artifact: str) -> list[Finding]:
    """The artifact's fresh stored review reports whose criterion declares depth 1."""
    found = [read_finding(root, artifact, row.path.relative_to(root).as_posix())
             for row in results.note_rows(root, artifact)
             if row.freshness.state == "fresh" and row.outcome == "report"]
    return [finding for finding in found if finding.depth == 1]


def _brief_sha(root: Path, artifact: str, note: str) -> str | None:
    """The SHA-256 of the note's write brief as `edits.begin()` records it; None without one. ValueError when broken."""
    try:
        brief = capture_brief(root, artifact, note)
    except Stop as error:
        raise ValueError(str(error)) from error
    return observations.sha(brief["brief"].encode("utf-8")) if "brief" in brief else None


def _asked_scope(asking: Path, name: str) -> str | None:
    """The scope of the entry for the per-item pass `name` in the plan of the run that asked its proposals."""
    plan = yaml.safe_load((asking / "artifact" / PLAN).read_text(encoding="utf-8"))
    return next((entry.get("scope") for entry in plan["passes"] if entry["pass"] == name), None)


def answers_plan(root: Path, artifact: str, given: list[dict], purpose: str | None,
                 must_keep: list[str]) -> tuple[str, dict[str, dict], dict[str, dict]]:
    """The plan, and the answers each entry receives, of a run that consumes the operator's answers files.

    `given` holds each named file's `origin` (repository path) and `text`.
    Naming a file is the operator's approval of its text; each must pass the
    validator against its question (`edits.answered()`). Either:

    - one file whose question is a `per-item` operation's proposals (an edit
      result) on `artifact`: the plan is that pass alone, and the pass
      applies the approved items. Refused unless the note holds exactly the
      text the proposals were made for, under the write brief the asking
      run recorded (`start.json`), and some item is approved. The entry
      keeps the scope the asking run's plan gave the pass; or
    - files whose questions are review results of `artifact`, such as a
      triage's: the plan holds one fix entry per result with an `approved`
      finding, in depth order, and each fix receives its answers as
      `finding-answers`, with no scope: a triage's results come from
      review results, not plan entries, and a scoped fix entry of a plan
      is continued with `--plan`, never with answers. Refused unless the
      parts of the note each result's
      criterion watches are those it judged (its `note-sha256`, as freshness
      compares them) and some finding is approved.

    Returns the plan's text, the answers by `per-item` entry label and the
    answers by finding path. ValueError, a command error, otherwise; a file
    whose decisions nothing applies is kept with `answers record`.
    """
    note = (root / artifact).read_text(encoding="utf-8")
    known, edited, entries = passes(), [], []
    nothing = ("no item of {files} is approved; there is nothing to apply. Keep the operator's decisions with "
               "`commonplace-revise answers record FILE`")
    for item in given:
        data, problems = edits.answered(root, root / item["origin"], item["text"])
        if problems:
            raise ValueError(f"{item['origin']}: the answers are not valid: " + "; ".join(problems))
        question = frontmatter.parse((root / data["question"]).read_text(encoding="utf-8")).data
        approved = [entry["id"] for entry in data["items"] if entry["state"] == "approved"]
        if question.get("type") == edit_operations.RESULT_TYPE:
            name = Path(str(question.get("operation", "")).removeprefix(LIBRARY_IDENTITY_PREFIX)).stem
            if name not in known or known[name].decision != "per-item" or question.get("note") != artifact:
                raise ValueError(f"{item['origin']}: its question is a result of {question.get('operation')} on "
                                 f"{question.get('note')}, not of a per-item pass on {artifact}")
            if question.get("input-sha256") != observations.sha(note.encode("utf-8")):
                raise ValueError(f"{artifact} no longer holds the text the proposals of {item['origin']} were "
                                 "made for; the proposals are stale. A new run of the pass proposes again")
            _, asking = decisions.run_of(root, root / data["question"])
            if (edits.started(asking) or {}).get("brief-sha256", "") != _brief_sha(root, artifact, note):
                raise ValueError(f"the write brief of {artifact} is not the one the proposals of {item['origin']} "
                                 "were made under; the proposals are stale. A new run of the pass proposes again")
            if not approved:
                raise ValueError(nothing.format(files=item["origin"]))
            edited.append((name, item, _asked_scope(asking, name)))
        elif question.get("type") == result_contract.TYPE:
            finding = read_finding(root, artifact, data["question"])
            criterion = results.criterion_file(root, finding.criterion).read_text(encoding="utf-8")
            if question.get("note-sha256") != results.note_sha256(note, criterion):
                raise ValueError(f"{artifact} no longer holds the text the review result {data['question']} "
                                 "judged, in the parts its criterion watches; its findings are stale")
            if approved:
                entries.append((finding, item))
        else:
            raise ValueError(f"{item['origin']}: its question {data['question']} is neither an edit result nor a "
                             "review result; keep the decision with `commonplace-revise answers record FILE`")
    if edited and (entries or len(edited) > 1 or len(given) > 1):
        raise ValueError("apply takes one answers file over a per-item pass's proposals, or answers files "
                         "over review results, not both")
    if edited:
        [(name, item, scope)] = edited
        return (one_entry_plan(name, None, purpose, must_keep, scope),
                {name: {"origin": item["origin"], "text": item["text"]}}, {})
    if not entries:
        raise ValueError(nothing.format(files=", ".join(item["origin"] for item in given)))
    entries.sort(key=lambda pair: (pair[0].depth is None, pair[0].depth or 0, pair[0].criterion_id))
    return (triage_plan([{"pass": FIX, FINDING: finding.path} for finding, _ in entries], purpose, must_keep),
            {}, {finding.path: {"origin": item["origin"], "text": item["text"]} for finding, item in entries})


def revise(root: Path, artifact: str, profiles: dict[str, Profile], run_dir: Path, *, purpose: str | None = None,
           must_keep: list[str] = (), named_plan: str | None = None, review: Profile | None = None,
           triage: bool = False, consumed: list[dict] = (), given: dict[str, dict] | None = None,
           finding_answers: dict[str, dict] | None = None, timeout: float | None = None,
           harnesses=HARNESSES) -> ReviseReport:
    """Revise the repository-relative `artifact` in the new run at `run_dir`.

    The artifact's current text is the start text. Validated plans run
    automatically; `named_plan` bypasses assessment. A candidate that adds a
    validation warning is held, and other publication is automatic.
    `profiles` maps each effort to its profile; the assessment is a judgment
    ask. `review` is the profile of the full procedure's review step;
    without it no review is launched. `triage` writes the pending answers
    files over the artifact's fresh warn and fail review results and ends
    (`_triage()`); it launches no review and no assessor. `consumed` holds
    the answers files the operator named (`origin`, `text`), kept in the run
    before anything is launched; `given` and `finding_answers` are what
    `answers_plan()` made of them. The run ends at its first stop and writes
    its continuation record (`continuation()`) and its report (`REPORT`).
    """
    root = root.resolve()
    if sum((named_plan is not None, review is not None, triage)) > 1:
        raise ValueError("choose one of a named plan, the review step or the triage")
    report = ReviseReport(_rel(root, run_dir.resolve()), artifact,
                          mode="answers" if consumed else "fixed-plan" if named_plan is not None
                          else "full" if review else "triage" if triage else "quick")
    known = passes()
    before = gates.checkout_state(root)
    start = (root / artifact).read_text(encoding="utf-8")
    try:
        brief = capture_brief(root, artifact, start)
        edits.begin(run_dir, artifact, start, brief)
        for item in consumed:
            decisions.keep_answers(run_dir, item["origin"], item["text"])
        report.answers = [item["origin"] for item in consumed]
        with Run(run_dir, root, profiles["judgment"], timeout=timeout, harnesses=harnesses) as run:
            run.accept(START, start)
            instruction = (library_root() / EXECUTION_REL).read_text(encoding="utf-8")
            contracts = result_contract.capture_contract(root, edit_operations.RESULT_TYPE)
            kb_role, proposed = None, None
            earlier = decisions.earlier(root, artifact, run_dir)
            observations.atomic_json(run_dir / EARLIER_FILE, {"decisions": earlier})
            if triage:
                findings = triage_findings(root, artifact)
                observations.atomic_json(run_dir / TRIAGE_INPUTS, {"findings": [asdict(given) for given in findings]})
                report.findings = [finding.path for finding in findings]
                report.triage = {"results": []}
                if not findings:
                    report.triage["what"] = NOTHING_TO_TRIAGE
                _triage(run, root, findings, earlier, report)
            elif named_plan is None:
                reports = []
                if review is not None:
                    supplied = _review(root, artifact, start, run_dir, review, timeout, harnesses, report)
                    reports = [*depth_one_reports(root, artifact), *supplied]
                findings = without_rejected(current_findings(root, artifact), earlier)
                observations.atomic_json(run_dir / ASSESSMENT_INPUTS, {
                    "findings": [asdict(given) for given in findings],
                    "reports": [asdict(given) for given in reports], "reviews": report.reviews})
                stops = decisions.earlier_stops(root, artifact, run_dir)
                observations.atomic_json(run_dir / STOPS_FILE, {"stops": stops})
                for given_report in reports:
                    section = (role_section(given_report.text)
                               if given_report.criterion.endswith(criteria.REPORTS[criteria.ROLE]) else None)
                    if section:
                        kb_role = {"origin": given_report.path, "text": section}
                report.findings = [finding.path for finding in (*findings, *reports)]
                prompt, inputs = _assessment_request(artifact, start, purpose, list(must_keep), known, brief,
                                                     findings, reports, decisions.planning_decisions(earlier),
                                                     stops)
                proposed = _assess(run, root, artifact, prompt, inputs, known, profiles["judgment"]).outputs["plan"]
            else:
                proposed = named_plan
            if proposed is not None:
                _run_plan(run, root, artifact, proposed, known, profiles, report, brief, start,
                          instruction, contracts, kb_role, earlier, finding_answers or {}, given or {})
    except Conflict as conflict:
        report.conflict = str(conflict)
    except (Stop, OutOfAttempts, LaunchFailed) as stop:      # LaunchFailed includes UsageLimited
        report.stopped = str(stop)
    published = report.publications[-1]["text"] if report.publications else None    # the note's last write
    report.changed = guarded_changes(root, before, artifact,
                                     (root / published).read_text(encoding="utf-8") if published else None)
    report.continuation = continuation(root, artifact, run_dir, report, known, start,
                                       purpose=purpose, must_keep=list(must_keep))
    observations.atomic_json(run_dir / REPORT, report.to_dict())
    return report


def _publish(root: Path, artifact: str, run_dir: Path, start: str, final: str, brief: dict[str, str],
             report: ReviseReport) -> None:
    """Write `final` over the note's text as the run's automatic publication, and record it.

    The publication covers the entries applied since the run's last
    publication, and is written over that publication's text, or over
    `start`. The brief is checked first (`edits.unchanged_brief()`); the
    note must still hold the text written over (`edits.record_publication()`).
    """
    before = (root / report.publications[-1]["text"]).read_text(encoding="utf-8") if report.publications else start
    edits.unchanged_brief(root, artifact, start, brief)
    covered = {name for publication in report.publications for name in publication["entries"]}
    entries = [state.name for state in report.passes if state.state == "applied" and state.name not in covered]
    entry = edits.record_publication(run_dir, root, artifact, before, final, entries, observations.timestamp())
    report.publications.append(entry)
    report.published = True


def _run_plan(run: Run, root: Path, artifact: str, proposed: str, known: dict[str, Pass],
              profiles: dict[str, Profile], report: ReviseReport, brief: dict[str, str], start: str,
              instruction: str, contracts: dict[str, bytes], kb_role: dict[str, str] | None,
              earlier: list[dict], finding_answers: dict[str, dict], given: dict[str, dict]) -> None:
    """Check and keep the plan, then end on its stop or run its passes to the first stop and publish.

    A candidate other than the note's text is published
    automatically (`_publish()`) unless it adds a validation warning; then
    the run holds it (`edits.hold()`). That happens whether the passes ran
    to the end or ended with a problem: an entry that failed does not hold
    back the entries before it. Before a `per-item` pass's proposals, the
    passes publish what they applied themselves (`_passes()`).
    """
    plan = report.plan = read_plan(proposed, root, artifact, known)
    run.accept(PLAN, proposed)
    if plan["stop"]:
        report.plan_stop = plan["stop"]
        question = run.artifact / PLAN
        run.accept(STOP_ANSWERS, answers.pending(_rel(root, question), question.read_bytes()))
        return
    origin = (Path(artifact).parent / write_brief_name_for(Path(artifact))).as_posix()
    final, end = _passes(run, root, artifact, start, plan, known, profiles, report,
                         {name: {"origin": origin, "text": value} for name, value in brief.items()},
                         instruction, contracts, kb_role, earlier, finding_answers, given,
                         lambda text: _publish(root, artifact, run.root, start, text, brief, report))
    published = (root / report.publications[-1]["text"]).read_text(encoding="utf-8") if report.publications else start
    if final != published:
        warnings = edits.new_warnings(root, artifact, start, final)
        if warnings:
            covered = {name for publication in report.publications for name in publication["entries"]}
            entries = [state.name for state in report.passes if state.state == "applied" and state.name not in covered]
            report.held = edits.hold(run, root, artifact, published, final, entries)
            report.new_warnings, report.proposed = warnings, report.held["candidate"]
            report.not_published = (f"The proposed text is {report.proposed}; it is not published: it adds "
                                    "validation warnings the note does not have. It is published only when the "
                                    f"operator names this run: `{report.held['command']}`.")
        else:
            _publish(root, artifact, run.root, start, final, brief, report)
    if end == "failed":
        [failed] = [state for state in report.passes if state.state == "problem"]
        report.stopped = f"{failed.name}: {failed.reason}"


# --- The continuation record -------------------------------------------------------------------
#
# Each item names what is left (`kind`, `what`), the actor expected to be able
# to resolve it (`actor`: `operator`, `session-agent`, or `worker` with its
# `effort`), the items to settle first (`after`), how to proceed (`how`: the
# step of the continuation instruction, and a command where one exists) and
# the files it rests on (`evidence`). An item that waits for an answers file
# names it in `answers`. The actor is an estimate, not a permission.

CLAIM_QUESTIONS = re.compile(r"^#+\s*Claim questions for the operator\s*$(.*?)(?=^#|\Z)",
                             re.MULTILINE | re.DOTALL | re.IGNORECASE)


def _apply(files: list[str], purpose: str | None, must_keep: list[str]) -> str:
    """The command that applies the decided answers `files`, with the plan's purpose and must-keep list."""
    return shlex.join([COMMAND, "apply", *files, *(["--purpose", purpose] if purpose else []),
                       *[part for claim in must_keep for part in ("--must-keep", claim)]])


def _claim_questions(path: Path) -> bool:
    """Whether the assessment lists claim questions for the operator: the section has more than `None`."""
    if not path.is_file():
        return False
    found = CLAIM_QUESTIONS.search(path.read_text(encoding="utf-8"))
    return bool(found) and found.group(1).strip().rstrip(".").lower() not in ("", "none")


def continuation(root: Path, artifact: str, run_dir: Path, report: ReviseReport, known: dict[str, Pass],
                 start: str, *, purpose: str | None, must_keep: list[str]) -> dict | None:
    """Write the run's continuation record, `CONTINUATION`, and return it with its path; None when nothing is left.

    `made-for` names the note's text when the run ended: its publication, or
    its start text. Every item was computed on it, and it is never updated.
    """
    run_rel = _rel(root, run_dir.resolve())
    artifact_dir = f"{run_rel}/artifact"
    items: list[dict] = []

    def add(kind: str, what: str, actor: str, *, effort: str | None = None, after: list[str] = (),
            command: str | None = None, record: str | None = None, revised: str | None = None,
            answers_files: list[str] = (), evidence: list[str] = ()) -> str:
        item = {"id": str(len(items) + 1), "kind": kind, "what": what, "actor": actor,
                **({"effort": effort} if effort else {}), "after": list(after),
                "how": {**({"command": command} if command else {}),
                        **({"record": record} if record else {}), **({"revised": revised} if revised else {})},
                **({"answers": list(answers_files)} if answers_files else {}), "evidence": list(evidence)}
        items.append(item)
        return item["id"]

    plan = report.plan or {}
    purpose = plan.get("purpose", purpose) if report.mode != "triage" else purpose
    must_keep = plan.get(MUST_KEEP, must_keep) if report.mode != "triage" else must_keep
    failure = report.stopped or report.conflict
    failed = (add("failure", f"The run did not finish: {failure}", "session-agent", evidence=[f"{run_rel}/{REPORT}"])
              if failure else None)
    if report.triage and report.triage["results"]:
        files = [given["answers"] for given in report.triage["results"]]
        add("findings", "The operator decides the findings of each review result; the approved ones are fixed by "
            "one new run that names every decided file.", "operator",
            command=_apply(files, purpose, must_keep),
            record=decisions.RECORD.format(file="FILE"), answers_files=files,
            evidence=[path for given in report.triage["results"] for path in (given["question"], given["answers"])])
    if report.plan_stop:
        stop_file = f"{artifact_dir}/{STOP_ANSWERS}"
        add("plan-stop", f"The plan stops with a proposal, which names its own route: {report.plan_stop}", "operator",
            record=decisions.RECORD.format(file=stop_file), answers_files=[stop_file],
            evidence=[f"{artifact_dir}/{ASSESSMENT}", f"{artifact_dir}/{PLAN}"])
    held = None
    if report.held:
        held = add("held-candidate", "The candidate adds validation warnings the note does not have: "
                   + "; ".join(report.held["new-warnings"]) + ". It is published only on the operator's word.",
                   "operator", command=report.held["command"], revised=report.held["revised-command"],
                   evidence=[report.held["candidate"], report.held["diff"]])
    chain = held
    for state in report.passes:
        current = known.get(FIX if state.finding else state.name)
        if state.state == "waiting":
            chain = add("proposals", f"The operator decides the proposals of `{state.name}`; the approved items "
                        "are applied by a new run that names the file.", "operator",
                        command=_apply([state.answers], purpose, must_keep),
                        record=decisions.RECORD.format(file=state.answers), answers_files=[state.answers],
                        evidence=[state.answers, frontmatter.parse((root / state.answers).read_text(
                            encoding="utf-8")).data["question"]])
            continue
        if state.state not in ("skipped", "problem", "pending"):
            continue
        after = ([failed] if state.state == "problem" and failed else []) + ([chain] if chain else [])
        evidence = [path for path in (f"{artifact_dir}/{ASSESSMENT}", f"{artifact_dir}/{PLAN}")
                    if (root / path).is_file()]
        if (state.state == "skipped" or current.name in INTERACTIVE
                or (current.name == CONVERSATION and not must_keep)):
            item = add("interactive-entry", f"The plan entry `{state.name}` is left for the interactive path.",
                       "session-agent", after=[] if state.state == "skipped" else after, evidence=evidence)
        else:
            if state.answers:
                command, own = _apply([state.answers], purpose, must_keep), [state.answers]
            else:                   # the entry as the plan gave it, scope included, in a plan file of its own
                own = [f"{artifact_dir}/{CONTINUE_DIR}/{len(items) + 1}.yaml"]
                edits.write_text(root / own[0], one_entry_plan(current.name, state.finding, purpose, must_keep,
                                                               state.scope))
                command = shlex.join([COMMAND, artifact, "--plan", own[0]])
            if state.finding:
                item = add("fix-entry", f"The plan entry `{state.name}` was not run: it fixes a finding made on "
                           "an earlier text" + (", as the operator's answers decide" if state.answers else "") + ".",
                           "worker", effort=state.effort, after=after, command=command,
                           evidence=[*evidence, state.finding, *own])
            elif current.decision == "per-item":
                item = add("per-item-entry", f"The plan entry `{state.name}` was not run; " + (
                           "it applies the items the operator approved." if state.answers
                           else "its proposals then wait for the operator."), "worker", effort=state.effort,
                           after=after, command=command, evidence=[*evidence, *own])
            else:
                item = add("direct-entry", f"The plan entry `{state.name}` was not run.", "worker",
                           effort=state.effort, after=after, command=command, evidence=[*evidence, *own])
        if state.state != "skipped":
            chain = item
    if _claim_questions(run_dir / "artifact" / ASSESSMENT):
        add("claim-questions", "The assessment lists claim questions for the operator.", "operator",
            evidence=[f"{artifact_dir}/{ASSESSMENT}"])
    if not items:
        return None
    if report.published:
        stale = [row for row in results.note_rows(root, artifact)
                 if row.path is not None and row.freshness.state != "fresh"]
        if stale:
            add("stale-reviews", f"{len(stale)} stored review result(s) of the note are stale. Nothing schedules "
                "reviewing them again.", "worker",
                after=[item["id"] for item in items],
                command=shlex.join(["commonplace-review", "status", artifact, "--stale"]),
                evidence=[report.publications[-1]["diff"]])
    publication = report.publications[-1] if report.publications else None
    record = {"run-dir": run_rel,
              "made-for": {"note": artifact,
                           "sha256": publication["sha256"] if publication else observations.sha(start.encode()),
                           "text": publication["text"] if publication else f"{artifact_dir}/{START}"},
              "items": items}
    observations.atomic_json(run_dir / CONTINUATION, record)
    return {"file": f"{run_rel}/{CONTINUATION}", **record}

"""Revise one markdown artifact through the simplification passes, as a workflow over headless workers.

The judgment lives in the library's instruction files: `revise-an-article-or-note.md`
is the assessment's `criterion` input, and each pass file under
`instructions/simplification-passes/` is an edit operation that
`edit_operations.ask()` runs. Editors receive `execute-a-revision-pass.md`
as `execution`, not the planning instruction. Fixed-plan execution does not construct an assessment request.
Prompts here say only how to read inputs and write outputs.
Code owns the plan's check, the order, the bounds it can check and the one
write to the checkout.

The run directory is `edits.run_dir()`, derived from the artifact's path and
the hash of its text when the command runs. Assessment and settled edits
run automatically. Per-item decisions and final publication propose a file
through `headless.operator.answer()` and stop; the report's `waiting-for` names the
file, the explicit approval command and the command to repeat. Repeating
never approves: only the recorded approved text becomes the operator's answer:

1. **Assessment.** One `decide()` ask, on the judgment profile, with two
   outputs: `assessment` for the operator and `plan` for code. Code hands the
   assessor the closed list of passes with their `effort` and `depth`
   (`catalog()`), and `plan_problems()` rejects unknown passes, missing
   fields and an order against the depth the pass files declare. The run
   keeps `artifact/assessment.md` and `artifact/plan.yaml`, then proceeds.
   A plan whose `stop` is set ends the run there. To replace a stopped or
   generated plan, supply `--plan`; editing the captured plan is not an
   override. A named plan bypasses assessment but still requires validation.
   The assessor also receives the artifact's fresh stored review results
   with outcome warn or fail (`current_findings()`); it launches no review.
   A pass that declares `responds-to`, the fix of `FIX_REL`, takes one such
   result as its `finding` input: its plan entry names the result file and
   takes the depth of the result's criterion. `one_entry_plan()` writes the
   plan of `--pass NAME` and `--finding RESULT`. With a `review` profile
   (`--full`), the assessment is preceded by the review step: every review
   operation that declares `depth` (`review_pairs()`) runs through
   `gates.sweep()` in `reviews/` under the run directory, publishing results
   and reusing fresh ones. Then each review operation that judges
   operational inputs (`criteria.SUPPLIED`) runs alone in its own run and
   publishes nothing: the compression synthesis in `synthesis/` on the
   checks' results, and the role report in `role/` on the artifact's inbound
   contexts (`inbound.collect()`). The assessor also receives the depth 1
   reports, the synthesis report and the role report, and its plan's `stop`
   is how a depth 1 proposal ends the run. A review without a result stops the run.
2. **Passes.** Validated plans run automatically. An invalid named plan
   raises ValueError, a command error, not a worker retry. The artifact's text is kept as
   `artifact/start.md`. Each listed pass is one run of the edit route
   (`edit_operations.ask()`) on the profile its `effort` selects, with the
   current text and the roles `purpose`, `defend`, `scope` and `brief`. The
   route checks the edit result and the candidate and retains both in its
   observation under `artifact/edits/`; the next pass works on the
   candidate. Each
   pass's report and the text it left are kept under `artifact/reports/` and
   `artifact/texts/`, so the operator can read each pass's diff. A pass
   whose result is `unchanged` is `no-change`. A worker-reported problem
   stops the run; a pass out of correction attempts is `problem`, and the run
   can collect the remaining pass outputs but applies none of them.
3. **Per-item decisions.** A pass whose `decision` is `per-item` has the
   operator decide its proposals before any is applied: a proposing run whose
   edit result is the question, a stop with the pending answers file
   (`types/answers.md`, `answers.pending()`) in
   `artifact/<pass>-answers-<answer key prefix>.md`, and on the repeat the
   same operation run again with the explicitly approved answers file as its
   `answers` input. Answers the validator refuses block the pass until the
   operator approves a corrected file; answers that approve no item end the
   pass as `no-change`. Only `approved` items are applied. The reasons bind
   publication through the selection context. Proposals made again for other
   text have another key, so they get a new file and stop again.
4. **Interactive passes.** `narrow-overclaims` takes its evidence from the
   conversation, which no headless worker has; it runs only when the plan's
   `defend` list carries that evidence explicitly (is non-empty), and is
   skipped otherwise. `split-out-a-treatment` writes a second file and the
   collection index from the discussion's text, so it is always skipped. A
   skipped pass is reported as left for the interactive path.
5. **Publication.** When every pass is `applied`, `no-change` or `skipped`,
   changed final text is materialized as `artifact/final.md`, with a diff
   and a pending answers file `artifact/publication-answers.md` whose one
   item names the candidate's hash (`edits.publication()`). Only approved
   answers that approve that item permit `edits.apply()` to write the
   checkout. Approval binds the start, candidate and execution context;
   brief and live-text conflicts block the write. No-change runs complete without approval. Problems and genuine
   operator stops never write the artifact merely because the command repeats.

Because the plan and the operator's answers are inputs, an unedited repeat
replays every answered call. A replacement supplied with `--plan` re-asks
only passes whose inputs changed. Answers edited after approval are
reported as unapproved and never silently used.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

import yaml

from commonplace.headless import operator
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
)
from commonplace.lib import answers, frontmatter
from commonplace.lib.library import artifact_identity, library_root
from commonplace.lib.naming import write_brief_name_for
from commonplace.lib.review_workflows import (
    criteria,
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
    Conflict,
    Stop,
    apply,
    capture_brief,
    guarded_changes,
    publication,
    unchanged_brief,
)

PASSES_DIR = "instructions/simplification-passes"
FIX_REL = "instructions/fix-warnings/fix-strategy-taxonomy.md"
"""The edit operation that fixes one review finding; a plan entry for it names the finding."""
FIX = Path(FIX_REL).stem
FINDING = "finding"
"""The plan field, and the input role, that names a review result file."""
FINDING_OUTCOMES = ("warn", "fail")
"""The outcomes of the stored results the assessor receives; INFO-level findings sit in `pass` results."""
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
"""The pass whose evidence is the conversation: it runs only with a non-empty defend list."""
INTERACTIVE = {"split-out-a-treatment": "it writes a second file and the collection index from the "
                                        "discussion's text, which a headless worker has not seen"}
"""Passes the workflow never runs, with the reason."""
PLAN_SCHEMA = {"purpose": str, "defend": list, "passes": list, "stop": (str, type(None))}
ASSESSMENT, PLAN, START = "assessment.md", "plan.yaml", "start.md"
REPEAT = "commonplace-review run revise {artifact}"
UNAPPROVED = ("This file was edited after its approval. The run used the approved text, not the edit. "
              "Approve the file and repeat to use it.")
STOP_ANSWERS = "stop-answers.md"
"""The answers file for a plan that stops: one item, the plan. The run does not wait for it."""
STOP_HOW = ("The plan stops with a proposal. Record the operator's decision on the one item of this answers file: "
            "`approved` to act on the proposal as made, or `rejected` or `deferred` with the operator's reason, "
            "with `decided-by: operator` and `decided-at`. When the work that followed is done, add `resolution` "
            "and `refs` (commit hashes, paths) to the item. Approve the file each time it changes; the run does "
            "not wait for it.")
DECIDE_HOW = ("Record the operator's decision on each item of the {name} answers file: set `state` to `approved`, "
              "`rejected` with a `reason`, or `deferred` with a `reason` and a `revisit` condition, and add "
              "`decided-by: operator` and `decided-at` to each decided item; change no `id` or `proposal`. "
              "Only approved items are applied. In a session, follow instructions/decide-items.md. Then approve "
              "the file and repeat.")


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


def criterion_depth(root: Path, criterion: str) -> int | None:
    """The `depth` the criterion file declares; None when it declares none."""
    data = frontmatter.parse(results.criterion_file(root, criterion).read_text(encoding="utf-8")).data
    depth = data.get("depth")
    return depth if isinstance(depth, int) and not isinstance(depth, bool) else None


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


def catalog(known: dict[str, Pass]) -> str:
    """The passes the assessor may choose from, one line each, for its `passes` input."""
    def note(current: Pass) -> str:
        if current.name in INTERACTIVE:
            return " This workflow does not run it: it is left for the interactive path."
        if current.name == CONVERSATION:
            return " This workflow runs it only when `defend` is not empty."
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


def plan_checks(data: dict, known: dict[str, Pass], root: Path, artifact: str) -> list[str]:
    """What a plan breaks beyond its schema: purpose, defend items, pass entries, findings and depth order.

    An entry for a pass that declares `responds-to` names one review result
    of `artifact` as `finding` and takes the depth of that result's
    criterion; no other entry names a finding.
    """
    problems = [] if data["purpose"].strip() else ["`purpose` is empty"]
    if not all(isinstance(claim, str) and claim.strip() for claim in data["defend"]):
        problems.append("each `defend` item is a claim's text")
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
                else violations(data, PLAN_SCHEMA) or plan_checks(data, known, root, artifact))
    if problems:
        raise ValueError("invalid plan: " + "; ".join(problems))
    return {"purpose": data["purpose"], "defend": list(data["defend"]), "stop": data["stop"],
            "passes": [{"pass": entry["pass"], "scope": entry.get("scope"),
                        **({FINDING: entry[FINDING]} if entry.get(FINDING) is not None else {})}
                       for entry in data["passes"]]}


def one_entry_plan(name: str, finding: str | None, purpose: str | None, defend: list[str]) -> str:
    """The plan of a focused run: one entry for the pass `name`, naming its finding when it takes one."""
    entry = {"pass": name, **({FINDING: finding} if finding is not None else {})}
    return yaml.safe_dump({"purpose": purpose or FOCUSED_PURPOSE, "defend": list(defend), "stop": None,
                           "passes": [entry]}, sort_keys=False, allow_unicode=True)


# --- Reports --------------------------------------------------------------------------------

@dataclass
class PassState:
    name: str                         # the entry's label: its pass, and the finding's criterion id for a fix
    scope: str | None
    effort: str
    finding: str | None = None        # repository path of the review result the entry fixes
    state: str = "pending"            # applied, no-change, skipped, problem, waiting or pending
    reason: str | None = None
    profile: dict | None = None       # the answering call's profile and recorded model
    model: str | None = None
    report: str | None = None         # repository path of the pass's report
    text: str | None = None           # repository path of the text the pass left, to diff against the one before


@dataclass
class ReviseReport:
    run_dir: str
    artifact: str
    mode: str = "fixed-plan"
    plan: dict | None = None
    reviews: list[dict] = field(default_factory=list)    # the review step's sweep reports, in the full procedure
    findings: list[str] = field(default_factory=list)   # review results the assessor received
    passes: list[PassState] = field(default_factory=list)
    proposed: str | None = None       # repository path of the final revised text in the run directory
    applied: bool = False             # the final text was written to the artifact
    not_applied: str | None = None    # why the proposed text was not written
    waiting_for: dict | None = None   # the operator's file the run stopped for, and how to continue
    stop: str | None = None           # the plan's stop: the assessment is the result
    stop_answers: dict | None = None  # the answers file for the plan's stop, and how to approve it
    override: dict | None = None      # advice for explicitly replacing a stopped plan with --plan
    unapproved_edits: list[dict] = field(default_factory=list)   # drafts edited after approval; not in use
    stopped: str | None = None
    conflict: str | None = None
    changed: list[str] = field(default_factory=list)

    @property
    def complete(self) -> bool:
        return self.waiting_for is None and self.stopped is None and self.conflict is None

    @property
    def ok(self) -> bool:
        """No stop, no conflict and no unexpected change; waiting for the operator is ok."""
        return self.stopped is None and self.conflict is None and not self.changed

    def to_dict(self) -> dict:
        data = {key.replace("_", "-"): value for key, value in asdict(self).items() if key != "changed"}
        return {"ok": self.ok, "complete": self.complete, **data,
                "guard": {"clean": not self.changed, "changed": self.changed}}


# --- The assessment prompt: mechanical only ------------------------------------------------

ASSESS_PROMPT = """\
Assess one artifact for revision. Nobody will answer questions. If you cannot, \
write {problem} instead of guessing.

The artifact is `{artifact}` in this repository; its text is {artifact_input}. \
Judge this input text; the file on disk may differ. The instruction is \
{criterion_input}: do its step 1, the assessment, and nothing after it. The \
plan is validated and ordinary passes run automatically. \
{purpose}{defend}{brief}The passes you may recommend are listed in {passes_input}; \
choose only from them, by name.
{findings}
Output:
- Write the assessment to {assessment}, as the instruction's step 1 describes.
- Write the plan to {plan}: a YAML mapping holding exactly the decision fields \
below. `purpose` is the purpose the assessment works under; `defend` lists the \
claims the assessment marks as divergence, each as the claim's text; `passes` \
lists the recommended passes in run order, each a mapping with `pass` (its \
name) and, when the pass should touch only part of the artifact, `scope` \
naming that part{finding_field}; `stop` is null, or the reason when the \
instruction says to report a rewrite and stop. {no_writes}
"""

FINDINGS_INTRO = ("\nThe artifact's stored review results with outcome warn or fail are inputs. Each line gives "
                  "the result file's repository path, its criterion and the depth the criterion declares:\n")
REPORTS_INTRO = ("\nThe depth 1 review reports on this text, the compression synthesis when it ran, and the "
                 "role report are inputs. Each line gives the result file's repository path, or for the "
                 "synthesis and the role report its run "
                 "directory, and its criterion:\n")
FINDING_FIELD = (", and, for a pass that fixes a finding, `finding` naming that review result file's "
                 "repository path, as listed above")

# --- The workflow ------------------------------------------------------------------------------

def _rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _assessment_request(artifact: str, text: str, purpose: str | None, defend: list[str],
                        known: dict[str, Pass], brief: dict[str, str], findings: list[Finding] = (),
                        reports: list[Finding] = ()) -> tuple[str, dict[str, str]]:
    """The captured request, also bound into the final publication approval.

    `findings` are the stored warn and fail results the assessor may turn
    into plan entries; `reports` are review reports it reads. Without
    findings, the passes that fix a finding are not offered.
    """
    offered = known if findings else {name: current for name, current in known.items() if not current.responds_to}
    inputs = {"artifact": text, "criterion": (library_root() / INSTRUCTION_REL).read_text(encoding="utf-8"),
              "passes": catalog(offered), **brief}
    if purpose:
        inputs["purpose"] = purpose
    if defend:
        inputs["defend"] = "".join(f"- {claim}\n" for claim in defend)
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
    prompt = ASSESS_PROMPT.format(
        problem=PROBLEM_REF, artifact=artifact, artifact_input=input_ref("artifact"),
        criterion_input=input_ref("criterion"), passes_input=input_ref("passes"),
        purpose=(f"The operator's purpose is {input_ref('purpose')}. " if purpose
                 else "The operator named no purpose: propose one as the instruction directs. "),
        defend=f"The operator marks these claims as defended: {input_ref('defend')}. " if defend else "",
        brief=f"The write brief is {input_ref('brief')}. " if brief else "",
        findings=listed, finding_field=FINDING_FIELD if findings else "",
        assessment=output_ref("assessment"), plan=output_ref("plan"), no_writes=NO_WRITES)
    return prompt, inputs


def _assess(run: Run, root: Path, artifact: str, prompt: str, inputs: dict[str, str], known: dict[str, Pass],
            profile: Profile) -> Answer:
    """Ask or replay the assessment and plan; keep the assessment and return its answer identity."""
    data, answer = decide(run, "assessment", prompt, PLAN_SCHEMA, output="plan", also=["assessment"],
                          check=lambda data, _text: plan_checks(data, known, root, artifact), attempts=ATTEMPTS,
                          inputs=inputs, profile=profile)
    if data is None:
        raise Stop(f"assessment: worker problem: {answer.problem}")
    run.accept(ASSESSMENT, answer.outputs["assessment"])
    return answer


def _decide(run: Run, root: Path, artifact: str, text: str, operation: edit_operations.Operation,
            roles: dict[str, dict], profile: Profile, state: PassState, report: ReviseReport, context: dict,
            **route) -> edit_operations.Edit | None:
    """The applying run of a `per-item` pass; None when it stops for the operator or has nothing to apply.

    The first run returns the proposals: the question of the stop, whose
    pending answers file the operator decides. The second run is the same
    operation with the approved answers file as its `answers` input.
    """
    name = state.name
    proposed = edit_operations.ask(run, root, operation, artifact, text, roles, job=f"{name}/propose",
                                   profile=profile, **route)
    if proposed.outcome == "problem":
        return proposed
    selection = {"pass": name, "key": proposed.answer.key, "question": None, "answers": None}
    context["selections"].append(selection)
    if proposed.outcome == "unchanged":
        state.state, state.reason = "no-change", "the pass found no candidate"
        return None
    selection["question"] = proposed.text
    pending = answers.pending(_rel(root, proposed.path), proposed.text.encode("utf-8"))
    file = f"{name}-answers-{proposed.answer.key[:12]}.md"      # answers for another text wait again
    approved = operator.answer(run, file, pending, key=proposed.answer.key)
    selection["answers"] = approved
    if approved is None:
        state.state = "waiting"
        report.waiting_for = operator.waiting(run, root, file, DECIDE_HOW.format(name=name),
                                              REPEAT.format(artifact=artifact))
        return None
    if operator.edited(run, file):
        report.unapproved_edits.append(operator.waiting(run, root, file, UNAPPROVED, REPEAT.format(artifact=artifact)))
    data, problems = edits.answered(root, run.artifact / file, approved)
    if problems:
        state.state = "waiting"
        state.reason = "the approved answers are not valid: " + "; ".join(problems)
        report.waiting_for = operator.waiting(
            run, root, file, f"{state.reason}. {DECIDE_HOW.format(name=name)}", REPEAT.format(artifact=artifact))
        return None
    if not any(item["state"] == "approved" for item in data["items"]):
        state.state, state.reason = "no-change", "the operator approved no item"
        return None
    given = {"origin": _rel(root, run.artifact / file), "text": approved}
    return edit_operations.ask(run, root, operation, artifact, text, {**roles, edit_operations.ANSWERS: given},
                               job=f"{name}/apply", profile=profile, **route)


def _passes(run: Run, root: Path, artifact: str, start: str, plan: dict, known: dict[str, Pass],
            profiles: dict[str, Profile], report: ReviseReport, brief: dict[str, dict], instruction: str,
            context: dict, contracts: dict[str, bytes]) -> str:
    """Run the plan's passes from `start` through the edit route; return the text the last accepted pass left."""
    run.accept(START, start)
    text = start
    findings = {entry[FINDING]: read_finding(root, artifact, entry[FINDING])
                for entry in plan["passes"] if entry.get(FINDING)}
    entries = [(known[entry["pass"]], findings.get(entry.get(FINDING))) for entry in plan["passes"]]
    report.passes = [PassState(label(current.name, finding), entry["scope"], current.effort,
                               finding.path if finding else None)
                     for entry, (current, finding) in zip(plan["passes"], entries, strict=True)]
    defend = "".join(f"- {claim}\n" for claim in plan["defend"])
    route = {"contracts": contracts, "execution": instruction}
    for state, (current, finding) in zip(report.passes, entries, strict=True):
        if current.name in INTERACTIVE or (current.name == CONVERSATION and not defend):
            state.state = "skipped"
            state.reason = ("left for the interactive path: "
                            + INTERACTIVE.get(current.name, "its evidence is the conversation, and the plan's "
                                              "`defend` list is empty"))
            continue
        operation = edit_operations.parse(artifact_identity(root, library_root() / current.rel), current.text)
        roles = {"purpose": {"origin": "plan:purpose", "text": plan["purpose"]}, **brief,
                 **({"defend": {"origin": "plan:defend", "text": defend}} if defend else {}),
                 **({"scope": {"origin": "plan:scope", "text": state.scope}} if state.scope else {}),
                 **({FINDING: {"origin": finding.path, "text": finding.text}} if finding else {})}
        profile = profiles[current.effort]
        try:
            if operation.decision == "per-item":
                edit = _decide(run, root, artifact, text, operation, roles, profile, state, report, context, **route)
                if edit is None:
                    if state.state == "waiting":
                        return text
                    continue
            else:
                edit = edit_operations.ask(run, root, operation, artifact, text, roles, job=state.name,
                                           profile=profile, **route)
        except OutOfAttempts as spent:
            state.state, state.reason = "problem", str(spent)
            continue
        context["pass-answers"].append({"pass": state.name, "key": edit.answer.key, "result": edit.text,
                                        "candidate": edit.candidate})
        state.profile, state.model = edit.data["profile"], edit.data["model"]
        if edit.outcome == "problem":
            state.state, state.reason = "problem", f"worker problem: {edit.answer.problem}"
            raise Stop(f"{state.name}: {state.reason}")
        state.report = _rel(root, run.accept(f"reports/{state.name}.md", edit.body))
        if edit.outcome == "unchanged":
            state.state = "no-change"
            continue
        state.text = report.proposed = _rel(root, run.accept(f"texts/{state.name}.md", edit.candidate))
        state.state, text = "applied", edit.candidate
    return text


# --- The review step of the full procedure ----------------------------------------------------

def review_pairs(root: Path, artifact: str, text: str) -> tuple[list[gates.Pair], list[gates.Pair]]:
    """The review operations that declare `depth` and apply to `text`, and apart those of `criteria.SUPPLIED`.

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
           harnesses, inputs: dict[str, dict[str, str]] | None = None) -> gates.SweepReport:
    """Run `wanted` through the sweep in its own run, or continue that run; Stop unless every pair has a result.

    Without `inputs`, results are published to the shared store and fresh
    ones are reused. With them (a criterion of `criteria.SUPPLIED`), nothing
    is published and the pair is always asked, as `run gates --input` does.
    """
    request = run_dir / "review-request.json"
    if request.is_file():                         # a repeat: replay the captured request
        wanted = [gates.Pair(**pair) for pair in json.loads(request.read_text(encoding="utf-8"))["pairs"]]
        timeout = None
    else:
        observations.atomic_json(run_dir / "sweep.json", {"format": observations.VERSION, "workflow": "revise",
                                                         "profile": asdict(profile)})
    swept = gates.sweep(root, wanted, profile, run_dir, max_workers=REVIEW_WORKERS, timeout=timeout,
                        force=inputs is not None, grouping="bundle", harnesses=harnesses,
                        publish_results=inputs is None, operational_inputs=inputs)
    if swept.stopped:
        raise Stop(f"reviews in {swept.run_dir}: {swept.stopped}")
    unfinished = [pair.job for pair in swept.pairs if pair.state not in ("fresh", "reviewed")]
    if unfinished:
        raise Stop(f"reviews in {swept.run_dir} ended without a result: {', '.join(unfinished)}. Read the problem "
                   f"with `commonplace-review show {swept.run_dir}`, dismiss it with `commonplace-review retry "
                   f"{swept.run_dir} JOB`, then repeat")
    return swept


def _review(root: Path, artifact: str, text: str, run_dir: Path, profile: Profile, timeout: float | None,
            harnesses, report: ReviseReport) -> list[Finding]:
    """Run every review operation that declares `depth` on `text`, writing results as the sweep does.

    Then runs each criterion of `criteria.SUPPLIED` alone, in its own run,
    on its operational inputs, and returns those reports, which are not in
    the store, for the assessor.
    """
    wanted, supplied = review_pairs(root, artifact, text)
    report.reviews.append(_sweep(root, run_dir / REVIEWS, wanted, profile, timeout, harnesses).to_dict())
    found = []
    for pair in supplied:
        directory = run_dir / SUPPLIED_DIRS[pair.kind]
        resumed = (directory / "review-request.json").is_file()   # a repeat replays the captured inputs
        inputs = {} if resumed else _supplied_inputs(root, pair, wanted)
        swept = _sweep(root, directory, [pair], profile, timeout, harnesses, inputs)
        report.reviews.append(swept.to_dict())
        found += [Finding(swept.run_dir, done.result.criterion, results.criterion_id(root, done.result.criterion),
                          criterion_depth(root, done.result.criterion), done.result.outcome,
                          results.result_text(done.result))
                  for done in swept.pairs if done.result is not None]
    return found


def depth_one_reports(root: Path, artifact: str) -> list[Finding]:
    """The artifact's fresh stored review reports whose criterion declares depth 1."""
    found = [read_finding(root, artifact, row.path.relative_to(root).as_posix())
             for row in results.note_rows(root, artifact)
             if row.freshness.state == "fresh" and row.outcome == "report"]
    return [finding for finding in found if finding.depth == 1]


def revise(root: Path, artifact: str, profiles: dict[str, Profile], run_dir: Path, *, purpose: str | None = None,
           defend: list[str] = (), named_plan: str | None = None, review: Profile | None = None,
           timeout: float | None = None, harnesses=HARNESSES) -> ReviseReport:
    """Revise the repository-relative `artifact` in the run at `run_dir`, new or continued.

    The artifact's current text is the start text. Validated plans run
    automatically; `named_plan` bypasses assessment and explicitly replaces its
    plan. Editing the captured plan is not an override. Strike selections and
    final publication require explicit approval. `profiles` maps each effort
    to its profile; the assessment is a judgment ask. `review` is the profile
    of the full procedure's review step; without it no review is launched.
    """
    root = root.resolve()
    if named_plan is not None and review is not None:
        raise ValueError("a named plan runs without the review step")
    report = ReviseReport(_rel(root, run_dir.resolve()), artifact,
                          mode="fixed-plan" if named_plan is not None else "full" if review else "assess")
    known = passes()
    before = gates.checkout_state(root)
    start = (root / artifact).read_text(encoding="utf-8")
    final = None
    try:
        brief = capture_brief(root, artifact, start)
        with Run(run_dir, root, profiles["judgment"], timeout=timeout, harnesses=harnesses) as run:
            instruction = (library_root() / EXECUTION_REL).read_text(encoding="utf-8")
            contracts = result_contract.capture_contract(root, edit_operations.RESULT_TYPE)
            context = {"mode": report.mode, "execution": instruction, **brief,
                       "contract-sha256": result_contract.fingerprint(contracts),
                       "pass-answers": [], "selections": []}
            if named_plan is None:
                reports = []
                if review is not None:
                    supplied = _review(root, artifact, start, run_dir, review, timeout, harnesses, report)
                    reports = [*depth_one_reports(root, artifact), *supplied]
                findings = current_findings(root, artifact)
                report.findings = [finding.path for finding in (*findings, *reports)]
                prompt, inputs = _assessment_request(artifact, start, purpose, list(defend), known, brief, findings,
                                                     reports)
                context.update({"assessment": inputs, "assessment-prompt": prompt})
                assessed = _assess(run, root, artifact, prompt, inputs, known, profiles["judgment"])
                proposed = assessed.outputs["plan"]
                context["assessment-answer"] = {"key": assessed.key, "outputs": assessed.outputs}
            else:
                proposed = named_plan
            plan = report.plan = read_plan(proposed, root, artifact, known)
            context["plan"] = plan
            relevant = known if named_plan is None else {entry["pass"]: known[entry["pass"]] for entry in plan["passes"]}
            efforts = set(profiles) if named_plan is None else {current.effort for current in relevant.values()}
            context["passes"] = {name: asdict(current) for name, current in relevant.items()}
            context["profiles"] = {name: asdict(profiles[name]) for name in sorted(efforts)}
            run.accept(PLAN, proposed)
            if plan["stop"]:
                report.stop = plan["stop"]
                question = run.artifact / PLAN
                operator.answer(run, STOP_ANSWERS, answers.pending(_rel(root, question), question.read_bytes()),
                                key=answers.sha(question.read_bytes()))
                report.stop_answers = operator.waiting(run, root, STOP_ANSWERS, STOP_HOW,
                                                       REPEAT.format(artifact=artifact))
                report.override = {
                    "what": "The plan stops. To run passes instead, supply a validated replacement with --plan; "
                            "editing artifact/plan.yaml alone does not override the plan.",
                    "command": REPEAT.format(artifact=artifact) + " --plan <replacement-plan.yaml>",
                }
            else:
                origin = (Path(artifact).parent / write_brief_name_for(Path(artifact))).as_posix()
                final = _passes(run, root, artifact, start, plan, known, profiles, report,
                                {name: {"origin": origin, "text": value} for name, value in brief.items()},
                                instruction, context, contracts)
                problems = [state.name for state in report.passes if state.state == "problem"]
                if final != start and report.waiting_for is None and not problems:
                    unchanged_brief(root, artifact, start, brief)
                    report.proposed = _rel(root, run.artifact / "final.md")
                    report.waiting_for = publication(
                        run, root, artifact, start, final,
                        inputs=context,
                        command=REPEAT.format(artifact=artifact))
                    if report.waiting_for is None:
                        unchanged_brief(root, artifact, start, brief)
                        apply(root, artifact, start, final, root / report.proposed)
                        report.applied = True
                    else:
                        report.not_applied = (f"The proposed text is {report.proposed}; it is not applied: "
                                              "final publication needs explicit approval.")
                elif final != start:
                    why = ("the run waits for the operator" if report.waiting_for is not None
                           else f"{', '.join(problems)} ended with a problem")
                    report.not_applied = f"The proposed text is {report.proposed}; it is not applied: {why}."
    except Conflict as conflict:
        report.conflict = str(conflict)
    except (Stop, OutOfAttempts, LaunchFailed) as stop:      # LaunchFailed includes UsageLimited
        report.stopped = str(stop)
    report.changed = guarded_changes(root, before, artifact, final if report.applied else None)
    return report

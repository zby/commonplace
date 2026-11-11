"""Revise one markdown artifact through the simplification passes, as a workflow over headless workers.

The judgment lives in the library's instruction files, each handed to its
worker as the `criterion` input: `revise-an-article-or-note.md` for the
assessment, and each pass file under `instructions/simplification-passes/`
for its pass. Editors receive `execute-a-revision-pass.md`, not the planning
instruction. Fixed-plan execution does not construct an assessment request.
Prompts here say only how to read inputs and write outputs.
Code owns the plan's check, the order, the bounds it can check and the one
write to the checkout.

The run directory is `edits.run_dir()`, derived from the artifact's path and
the hash of its text when the command runs. Assessment and settled edits
run automatically. Strike selections and final publication propose a file
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
2. **Passes.** Validated plans run automatically. An invalid named plan
   raises ValueError, a command error, not a worker retry. The artifact's text is kept as
   `artifact/start.md`. Each listed pass is one `checked()` ask on the
   profile its `effort` selects, with the current text, the pass file, the
   purpose, the defend list and the scope as inputs, and the revised
   artifact and a pass report as outputs. Code checks the revised text
   (`artifact_bounds()`), and the next pass works on it. Each
   pass's report and the text it left are kept under `artifact/reports/` and
   `artifact/texts/`, so the operator can read each pass's diff. A pass
   whose text comes back unchanged is `no-change`. A worker-reported problem
   stops the run; a pass out of correction attempts is `problem`, and the run
   can collect the remaining pass outputs but applies none of them.
3. **Strikes.** A pass in `STRIKE` has the operator strike its list before
   any entry is applied: a list ask, a stop with
   `artifact/<pass>-list-<answer key prefix>.md`, and on the repeat an apply
   ask given the proposed list and the list the operator explicitly approved. A struck
   entry is deleted from the file. A list made again for other text has
   another key, so it gets a new file and stops again.
4. **Interactive passes.** `narrow-overclaims` takes its evidence from the
   conversation, which no headless worker has; it runs only when the plan's
   `defend` list carries that evidence explicitly (is non-empty), and is
   skipped otherwise. `split-out-a-treatment` writes a second file and the
   collection index from the discussion's text, so it is always skipped. A
   skipped pass is reported as left for the interactive path.
5. **Publication.** When every pass is `applied`, `no-change` or `skipped`,
   changed final text is materialized as `artifact/final.md`, with a diff
   and publication manifest. Only explicit approval of that exact manifest
   permits `edits.apply()` to write the checkout. Approval binds the start,
   candidate and execution context; brief and live-text conflicts block the
   write. No-change runs complete without approval. Problems and genuine
   operator stops never write the artifact merely because the command repeats.

Because the plan and the operator's list are inputs, an unedited repeat
replays every answered call. A replacement supplied with `--plan` re-asks
only passes whose inputs changed. Strike-list edits after approval are
reported as unapproved and never silently used.
"""

from __future__ import annotations

import re
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
from commonplace.lib import frontmatter
from commonplace.lib.library import library_root
from commonplace.lib.review_workflows import gates, results
from commonplace.lib.review_workflows.edits import (
    NO_WRITES,
    Conflict,
    Stop,
    apply,
    bounds,
    capture_brief,
    guarded_changes,
    publication,
    rejection,
    unchanged_brief,
    validation_fails,
)
from commonplace.lib.tasks import load_profile

PASSES_DIR = "instructions/simplification-passes"
INSTRUCTION_REL = f"{PASSES_DIR}/revise-an-article-or-note.md"
EXECUTION_REL = f"{PASSES_DIR}/execute-a-revision-pass.md"
EFFORTS = ("simple", "judgment")
ATTEMPTS = 3
STRIKE = ("plain-wording", "abstractions")
"""Passes whose file has the operator strike the proposed list before any entry is applied."""
CONVERSATION = "narrow-overclaims"
"""The pass whose evidence is the conversation: it runs only with a non-empty defend list."""
INTERACTIVE = {"split-out-a-treatment": "it writes a second file and the collection index from the "
                                        "discussion's text, which a headless worker has not seen"}
"""Passes the workflow never runs, with the reason."""
PLAN_SCHEMA = {"purpose": str, "defend": list, "passes": list, "stop": (str, type(None))}
ASSESSMENT, PLAN, START = "assessment.md", "plan.yaml", "start.md"
NO_CANDIDATES = "No candidates."
REPEAT = "commonplace-review run revise {artifact}"
UNAPPROVED = ("This file was edited after its approval. The run used the approved text, not the edit. "
              "Approve the file and repeat to use it.")


@dataclass(frozen=True)
class Pass:
    name: str
    effort: str
    depth: int | None                 # the depth order of revise-an-article-or-note; None runs anywhere
    rel: str                          # library-relative path
    text: str
    description: str


def passes() -> dict[str, Pass]:
    """The library's simplification passes: each file of the directory whose frontmatter declares `effort`."""
    found = {}
    for path in sorted((library_root() / PASSES_DIR).glob("*.md")):
        text = path.read_text(encoding="utf-8")
        data = frontmatter.parse(text).data
        if "effort" not in data:
            continue
        if data["effort"] not in EFFORTS or not isinstance(data.get("depth", 0), int):
            raise ValueError(f"{path.name}: `effort` must be one of {', '.join(EFFORTS)} and `depth` an integer")
        found[path.stem] = Pass(path.stem, data["effort"], data.get("depth"),
                                path.relative_to(library_root()).as_posix(), text, data.get("description", ""))
    return found


def catalog(known: dict[str, Pass]) -> str:
    """The passes the assessor may choose from, one line each, for its `passes` input."""
    def note(name: str) -> str:
        if name in INTERACTIVE:
            return " This workflow does not run it: it is left for the interactive path."
        if name == CONVERSATION:
            return " This workflow runs it only when `defend` is not empty."
        return " The operator strikes its list before any entry is applied." if name in STRIKE else ""
    lines = [f"- `{p.name}` (effort: {p.effort}; depth: {'any' if p.depth is None else p.depth}): "
             f"{p.description.rstrip('.')}.{note(p.name)}" for p in known.values()]
    return ("Passes, by name. Run passes with a depth in increasing depth; a pass with depth `any` "
            "may run at any point.\n\n" + "\n".join(lines) + "\n")


# --- The plan -------------------------------------------------------------------------

def _order_problems(entries: list[dict], known: dict[str, Pass]) -> list[str]:
    problems, last = [], None
    for entry in entries:
        current = known[entry["pass"]]
        if current.depth is None:
            continue
        if last is not None and current.depth < last.depth:
            problems.append(f"`{current.name}` (depth {current.depth}) must run before `{last.name}` "
                            f"(depth {last.depth}): list passes in increasing depth")
        last = current if last is None or current.depth >= last.depth else last
    return problems


def plan_checks(data: dict, known: dict[str, Pass]) -> list[str]:
    """What a plan breaks beyond its schema: purpose, defend items, pass entries and depth order."""
    problems = [] if data["purpose"].strip() else ["`purpose` is empty"]
    if not all(isinstance(claim, str) and claim.strip() for claim in data["defend"]):
        problems.append("each `defend` item is a claim's text")
    entries, seen = [], set()
    for index, entry in enumerate(data["passes"], 1):
        if not isinstance(entry, dict) or not isinstance(entry.get("pass"), str):
            problems.append(f"passes item {index} must be a mapping with `pass` and optional `scope`")
            continue
        extra = sorted(set(entry) - {"pass", "scope"})
        if extra:
            problems.append(f"passes item {index} has unknown fields: {', '.join(extra)}")
        if entry["pass"] not in known:
            problems.append(f"unknown pass `{entry['pass']}`; choose from {', '.join(known)}")
        elif entry["pass"] in seen:
            problems.append(f"`{entry['pass']}` is listed twice")
        else:
            seen.add(entry["pass"])
            entries.append(entry)
        if not isinstance(entry.get("scope"), (str, type(None))):
            problems.append(f"passes item {index}: `scope` must be text or null")
    return problems + _order_problems(entries, known)


def read_plan(text: str, known: dict[str, Pass] | None = None) -> dict:
    """The plan in `text`, checked and normalized (`scope` present on each pass); ValueError lists its problems."""
    known = passes() if known is None else known
    data = parse(text)
    problems = (["the plan must be a YAML mapping"] if not isinstance(data, dict)
                else violations(data, PLAN_SCHEMA) or plan_checks(data, known))
    if problems:
        raise ValueError("invalid plan: " + "; ".join(problems))
    return {"purpose": data["purpose"], "defend": list(data["defend"]), "stop": data["stop"],
            "passes": [{"pass": entry["pass"], "scope": entry.get("scope")} for entry in data["passes"]]}


def effort_profiles(root: Path, overrides: dict[str, str | None]) -> dict[str, Profile]:
    """The profile per effort: the profile file's `effort` mapping, with the operator's names in its place."""
    config = yaml.safe_load(gates.profiles().read_text(encoding="utf-8"))
    mapping = config.get("effort") or {}
    chosen = {effort: overrides.get(effort) or mapping.get(effort) for effort in EFFORTS}
    missing = [effort for effort, name in chosen.items() if not name]
    if missing:
        raise ValueError(f"no profile for effort {', '.join(missing)} in {gates.PROFILES_REL}")
    return {effort: load_profile(root, name, gates.profiles()) for effort, name in chosen.items()}


# --- Reports --------------------------------------------------------------------------------

@dataclass
class PassState:
    name: str
    scope: str | None
    effort: str
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
    passes: list[PassState] = field(default_factory=list)
    proposed: str | None = None       # repository path of the final revised text in the run directory
    applied: bool = False             # the final text was written to the artifact
    not_applied: str | None = None    # why the proposed text was not written
    waiting_for: dict | None = None   # the operator's file the run stopped for, and how to continue
    stop: str | None = None           # the plan's stop: the assessment is the result
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


# --- Prompts: mechanical only ------------------------------------------------------------

ASSESS_PROMPT = """\
Assess one artifact for revision. Nobody will answer questions. If you cannot, \
write {problem} instead of guessing.

The artifact is `{artifact}` in this repository; its text is {artifact_input}. \
Judge this input text; the file on disk may differ. The instruction is \
{criterion_input}: do its step 1, the assessment, and nothing after it. The \
plan is validated and ordinary passes run automatically. \
{purpose}{defend}{brief}The passes you may recommend are listed in {passes_input}; \
choose only from them, by name.

Output:
- Write the assessment to {assessment}, as the instruction's step 1 describes.
- Write the plan to {plan}: a YAML mapping holding exactly the decision fields \
below. `purpose` is the purpose the assessment works under; `defend` lists the \
claims the assessment marks as divergence, each as the claim's text; `passes` \
lists the recommended passes in run order, each a mapping with `pass` (its \
name) and, when the pass should touch only part of the artifact, `scope` \
naming that part; `stop` is null, or the reason when the instruction says to \
report a rewrite and stop. {no_writes}
"""

FRAME = """\
The artifact is `{artifact}` in this repository; the text under revision is \
{artifact_input}. The artifact's file in the checkout may hold an older text: \
work on this input, not the file. The pass is `{pass_rel}`; its text is \
{criterion_input}. The revision instruction is {workflow_input}. \
The purpose is {purpose_input}. {defend} {scope} {brief}
"""

PASS_PROMPT = """\
Run one simplification pass over one artifact. Nobody will answer questions. If \
you cannot run it within the pass's bounds, write {problem} instead of guessing.

{frame}
Output:
- Write the complete revised artifact, frontmatter included, to {artifact_output}. \
Do not edit the artifact's file: code checks your text. If the \
pass changes nothing, write the text unchanged.
- Write the pass's report to {report}, as the pass describes it, followed by \
the items you noticed but did not apply. {no_writes}
"""

LIST_PROMPT = """\
List the candidates of one simplification pass over one artifact. Nobody will \
answer questions. If you cannot, write {problem} instead of guessing.

{frame}
Do the pass up to the list it returns, marked keep or replace with the reason, \
and apply nothing: the operator strikes entries before any is applied.

Output:
- Write the list to {list_output}: one top-level `- ` item per candidate, \
holding the passage, the proposed replacement, keep or replace, and the \
reason; continuation lines are indented under their item. With no candidate, \
write the single line `{none}`. {no_writes}
"""

APPLY_PROMPT = """\
Apply the operator-approved list of one simplification pass to one artifact. \
Nobody will answer questions. If you cannot, write {problem} instead of guessing.

{frame}
The pass's list for this text was {proposed_input}. The operator struck \
entries by deleting them; the list they left is {approved_input}. Apply only \
the entries left there marked replace, as the pass directs; apply no struck \
entry and no new one.

Output:
- Write the complete revised artifact, frontmatter included, to {artifact_output}. \
Do not edit the artifact's file: code checks your text.
- Write the pass's report to {report}, as the pass describes it, followed by \
the entries the operator struck, one line each. {no_writes}
"""


def entries(listed: str) -> int:
    """The number of top-level `- ` items in a strike list."""
    return len(re.findall(r"^- ", listed, re.MULTILINE))


# --- Checking texts --------------------------------------------------------------------------

def artifact_bounds(root: Path, artifact: str, start: str, text: str, baseline: set[str]) -> list[str]:
    """The hard bounds a revised artifact breaks; empty when it keeps them.

    An artifact with frontmatter keeps the note bounds of `edits.bounds`:
    frontmatter title, type and brief declaration, the H1, `user-verified` dropped on a body
    change, no new validation failure. No pass may change the title: the one
    that judges titles proposes them in its report. An artifact without
    frontmatter gains none, keeps its first H1 and adds no validation failure.
    """
    if not text.strip():
        return ["the revised artifact is empty"]
    if frontmatter.opens_frontmatter(start):
        return bounds(root, artifact, start, text, baseline)
    problems = ["the artifact has no frontmatter; add none"] if frontmatter.opens_frontmatter(text) else []
    title, start_title = results.note_parts(text) or {}, results.note_parts(start) or {}
    if title.get("title") != start_title.get("title"):
        problems.append(f"the H1 changed; keep `# {start_title.get('title')}`")
    return problems + [f"validation: {fail}" for fail in sorted(validation_fails(root, artifact, text) - baseline)]


# --- The workflow ------------------------------------------------------------------------------

def _rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _assessment_request(artifact: str, text: str, purpose: str | None, defend: list[str],
                        known: dict[str, Pass], brief: dict[str, str]) -> tuple[str, dict[str, str]]:
    """The captured request, also bound into the final publication approval."""
    inputs = {"artifact": text, "criterion": (library_root() / INSTRUCTION_REL).read_text(encoding="utf-8"),
              "passes": catalog(known), **brief}
    if purpose:
        inputs["purpose"] = purpose
    if defend:
        inputs["defend"] = "".join(f"- {claim}\n" for claim in defend)
    prompt = ASSESS_PROMPT.format(
        problem=PROBLEM_REF, artifact=artifact, artifact_input=input_ref("artifact"),
        criterion_input=input_ref("criterion"), passes_input=input_ref("passes"),
        purpose=(f"The operator's purpose is {input_ref('purpose')}. " if purpose
                 else "The operator named no purpose: propose one as the instruction directs. "),
        defend=f"The operator marks these claims as defended: {input_ref('defend')}. " if defend else "",
        brief=f"The write brief is {input_ref('brief')}. " if brief else "",
        assessment=output_ref("assessment"), plan=output_ref("plan"), no_writes=NO_WRITES)
    return prompt, inputs


def _assess(run: Run, prompt: str, inputs: dict[str, str], known: dict[str, Pass], profile: Profile) -> Answer:
    """Ask or replay the assessment and plan; keep the assessment and return its answer identity."""
    data, answer = decide(run, "assessment", prompt, PLAN_SCHEMA, output="plan", also=["assessment"],
                          check=lambda data, _text: plan_checks(data, known), attempts=ATTEMPTS, inputs=inputs,
                          profile=profile)
    if data is None:
        raise Stop(f"assessment: worker problem: {answer.problem}")
    run.accept(ASSESSMENT, answer.outputs["assessment"])
    return answer


def _ask(run: Run, job: str, template: str, frame: str, root: Path, artifact: str, start: str, baseline: set[str],
         inputs: dict[str, str], profile: Profile, **fields) -> Answer:
    prompt = template.format(problem=PROBLEM_REF, frame=frame, artifact_output=output_ref("artifact"),
                             report=output_ref("report"), no_writes=NO_WRITES, **fields)
    return run.checked(job, lambda problems: prompt + rejection(problems),
                       lambda answer: artifact_bounds(root, artifact, start, answer.outputs["artifact"], baseline),
                       ["artifact", "report"], attempts=ATTEMPTS, inputs=inputs, profile=profile)


def _strike(run: Run, current: Pass, frame: str, root: Path, artifact: str, start: str, baseline: set[str],
            inputs: dict[str, str], profile: Profile, state: PassState, report: ReviseReport,
            context: dict) -> Answer | None:
    """The apply answer of a strike pass; None when it stops for the operator or has nothing to apply."""
    prompt = LIST_PROMPT.format(problem=PROBLEM_REF, frame=frame, list_output=output_ref("list"),
                                none=NO_CANDIDATES, no_writes=NO_WRITES)

    def check(answer: Answer) -> list[str]:
        listed = answer.outputs["list"].strip()
        return [] if listed == NO_CANDIDATES or entries(listed) else [
            f"the list has no top-level `- ` item; with no candidate, write only `{NO_CANDIDATES}`"]
    listed = run.checked(f"{current.name}/list", lambda problems: prompt + rejection(problems), check, ["list"],
                         attempts=ATTEMPTS, inputs=inputs, profile=profile)
    if listed.problem is not None:
        return listed
    proposed = listed.outputs["list"]
    selection = {"pass": current.name, "key": listed.key, "proposed": proposed, "approved": None}
    context["selections"].append(selection)
    if proposed.strip() == NO_CANDIDATES:
        state.state, state.reason = "no-change", "the pass found no candidate"
        return None
    name = f"{current.name}-list-{listed.key[:12]}.md"      # a list made for another text waits again
    approved = operator.answer(run, name, proposed, key=listed.key)
    selection["approved"] = approved
    if approved is None:
        state.state = "waiting"
        report.waiting_for = operator.waiting(
            run, root, name, f"Strike entries of the {current.name} list: delete each entry's `- ` line and the "
            "lines indented under it, and leave the entries you approve.", REPEAT.format(artifact=artifact))
        return None
    if operator.edited(run, name):
        report.unapproved_edits.append(operator.waiting(run, root, name, UNAPPROVED, REPEAT.format(artifact=artifact)))
    if not entries(approved):
        state.state, state.reason = "no-change", "the operator struck every entry"
        return None
    return _ask(run, f"{current.name}/apply", APPLY_PROMPT, frame, root, artifact, start, baseline,
                {**inputs, "proposed": proposed, "approved": approved}, profile,
                proposed_input=input_ref("proposed"), approved_input=input_ref("approved"))


def _passes(run: Run, root: Path, artifact: str, start: str, plan: dict, known: dict[str, Pass],
            profiles: dict[str, Profile], report: ReviseReport, brief: dict[str, str], instruction: str,
            context: dict) -> str:
    """Run the plan's passes from `start`; return the text the last accepted pass left."""
    run.accept(START, start)
    baseline = validation_fails(root, artifact, start)
    text = start
    report.passes = [PassState(entry["pass"], entry["scope"], known[entry["pass"]].effort) for entry in plan["passes"]]
    defend = "".join(f"- {claim}\n" for claim in plan["defend"])
    for state in report.passes:
        current = known[state.name]
        if current.name in INTERACTIVE or (current.name == CONVERSATION and not defend):
            state.state = "skipped"
            state.reason = ("left for the interactive path: "
                            + INTERACTIVE.get(current.name, "its evidence is the conversation, and the plan's "
                                              "`defend` list is empty"))
            continue
        inputs = {"artifact": text, "criterion": current.text, "purpose": plan["purpose"],
                  "workflow": instruction, **brief,
                  **({"defend": defend} if defend else {}), **({"scope": state.scope} if state.scope else {})}
        frame = FRAME.format(
            artifact=artifact, artifact_input=input_ref("artifact"), pass_rel=current.rel,
            criterion_input=input_ref("criterion"), purpose_input=input_ref("purpose"),
            workflow_input=input_ref("workflow"),
            brief=f"The write brief is {input_ref('brief')}." if brief else "",
            defend=(f"Defend these claims; the pass may not narrow them: {input_ref('defend')}." if defend
                    else "No claim is marked as defended."),
            scope=(f"Apply the pass only to this part of the artifact: {input_ref('scope')}." if state.scope
                   else "Apply the pass to the whole artifact."))
        profile = profiles[current.effort]
        try:
            if current.name in STRIKE:
                answer = _strike(run, current, frame, root, artifact, start, baseline, inputs, profile, state, report,
                                 context)
                if answer is None:
                    if state.state == "waiting":
                        return text
                    continue
            else:
                answer = _ask(run, current.name, PASS_PROMPT, frame, root, artifact, start, baseline, inputs, profile)
        except OutOfAttempts as spent:
            state.state, state.reason = "problem", str(spent)
            continue
        context["pass-answers"].append({"pass": current.name, "key": answer.key, "outputs": answer.outputs})
        used = answer.record["profile"]
        state.profile = {"harness": used["harness"], "launch-model": used["launch_model"], "effort": used["effort"]}
        state.model = answer.record["model"]
        if answer.problem is not None:
            state.state, state.reason = "problem", f"worker problem: {answer.problem}"
            raise Stop(f"{current.name}: {state.reason}")
        state.report = _rel(root, run.accept(f"reports/{current.name}.md", answer.outputs["report"]))
        revised = answer.outputs["artifact"]
        if revised == text:
            state.state = "no-change"
            continue
        state.text = report.proposed = _rel(root, run.accept(f"texts/{current.name}.md", revised))
        state.state, text = "applied", revised
    return text


def revise(root: Path, artifact: str, profiles: dict[str, Profile], run_dir: Path, *, purpose: str | None = None,
           defend: list[str] = (), named_plan: str | None = None,
           timeout: float | None = None, harnesses=HARNESSES) -> ReviseReport:
    """Revise the repository-relative `artifact` in the run at `run_dir`, new or continued.

    The artifact's current text is the start text. Validated plans run
    automatically; `named_plan` bypasses assessment and explicitly replaces its
    plan. Editing the captured plan is not an override. Strike selections and
    final publication require explicit approval. `profiles` maps each effort
    to its profile; the assessment is a judgment ask.
    """
    root = root.resolve()
    report = ReviseReport(_rel(root, run_dir.resolve()), artifact,
                          mode="fixed-plan" if named_plan is not None else "assess")
    known = passes()
    before = gates.checkout_state(root)
    start = (root / artifact).read_text(encoding="utf-8")
    final = None
    try:
        brief = capture_brief(root, artifact, start)
        with Run(run_dir, root, profiles["judgment"], timeout=timeout, harnesses=harnesses) as run:
            instruction = (library_root() / EXECUTION_REL).read_text(encoding="utf-8")
            context = {"mode": report.mode, "execution": instruction, **brief,
                       "pass-answers": [], "selections": []}
            if named_plan is None:
                prompt, inputs = _assessment_request(artifact, start, purpose, list(defend), known, brief)
                context.update({"assessment": inputs, "assessment-prompt": prompt})
                assessed = _assess(run, prompt, inputs, known, profiles["judgment"])
                proposed = assessed.outputs["plan"]
                context["assessment-answer"] = {"key": assessed.key, "outputs": assessed.outputs}
            else:
                proposed = named_plan
            plan = report.plan = read_plan(proposed, known)
            context["plan"] = plan
            relevant = known if named_plan is None else {entry["pass"]: known[entry["pass"]] for entry in plan["passes"]}
            efforts = set(profiles) if named_plan is None else {current.effort for current in relevant.values()}
            context["passes"] = {name: asdict(current) for name, current in relevant.items()}
            context["profiles"] = {name: asdict(profiles[name]) for name in sorted(efforts)}
            run.accept(PLAN, proposed)
            if plan["stop"]:
                report.stop = plan["stop"]
                report.override = {
                    "what": "The plan stops. To run passes instead, supply a validated replacement with --plan; "
                            "editing artifact/plan.yaml alone does not override the plan.",
                    "command": REPEAT.format(artifact=artifact) + " --plan <replacement-plan.yaml>",
                }
            else:
                final = _passes(run, root, artifact, start, plan, known, profiles, report, brief, instruction,
                                context)
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

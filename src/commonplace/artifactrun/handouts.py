"""Hand-outs: the prompt and paths a worker receives for one model attempt.

The prompt keeps the shape the analysis workers already follow. A hand-out
is reconstructible from its attempt id, so a coordinator that lost the
response to an invocation can retrieve the open hand-outs again.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib.note_parser import parse_document
from commonplace.lib.reading_batches import (
    READ_BATCH_BYTES,
    reading_batches,
    reading_ranges,
)

from .plan import HANDOUT_PREFIXES, PLACEHOLDER, PROMPT_SECTION_INPUT, ModelJob
from .run import Run

WORKER_RUNTIME = "worker-runtime.json"


@dataclass(frozen=True)
class Handout:
    """A hand-out is an open model attempt's prompt and output paths."""

    attempt: str
    job: str
    prompt: Path
    outputs: Mapping[str, Path]
    problem: Path
    worker_runtime: Path



def _substitute(value: str, values: Mapping[str, str], parameters: Mapping[str, str]) -> str:
    def one(match) -> str:
        name = match.group(1)
        if name.startswith("param:"):
            return parameters[name.removeprefix("param:")]
        return values[name]
    return PLACEHOLDER.sub(one, value)


ABSENT_LINE = "absent"
"""The value the frame prints for an optional input that is missing."""
CONDITION = re.compile(r"\[([A-Za-z0-9][A-Za-z0-9_-]*)\]")


def prompt_line_names(job: ModelJob) -> set[str]:
    """The `name = value` lines the frame prints for every attempt of `job`.

    `previous-<output>` lines exist only on a retry, so they are only
    conditions, never slots.
    """
    names = {"job", "attempt", "run-id", "output", "problem", "worker-runtime", "workspace", "artifact", "scratch",
             *job.parameters, *(f"output-{name}" for name in job.outputs[1:])}
    names |= {name for name in job.inputs if name not in (job.instruction, PROMPT_SECTION_INPUT)}
    return names | ({"role"} if job.role else set())


def render_prompt_section(text: str, lines: Mapping[str, str], *, conditions: set[str] | None = None) -> str:
    """The plan's prompt section filled from the frame's own lines.

    Frontmatter is dropped. A paragraph whose first line is `[<name>]` is
    kept, without that line, only when the frame prints `<name>` with a
    value other than `absent`. Every `{<name>}` is that line's value; an
    unknown name raises KeyError. With `conditions`, the names some job of
    the plan can print, a condition outside them and outside the frame's
    `output-*` and `previous-*` families raises KeyError too: that is the
    start-time check; at hand-out a missing condition drops its paragraph.
    """
    document, _ = parse_document(text)
    body = document.body if document is not None else text
    paragraphs = []
    for paragraph in body.strip().split("\n\n"):
        first, _, rest = paragraph.partition("\n")
        condition = CONDITION.fullmatch(first.strip())
        if condition:
            name = condition.group(1)
            if (conditions is not None and name not in lines and name not in conditions
                    and not name.startswith(HANDOUT_PREFIXES)):
                raise KeyError(name)
            if lines.get(name, ABSENT_LINE) == ABSENT_LINE:
                continue
            paragraph = rest
        paragraphs.append(paragraph)
    return PLACEHOLDER.sub(lambda match: lines[match.group(1)], "\n\n".join(paragraphs))


def _open(run: Run, job: ModelJob) -> Handout:
    """Open an attempt and write its hand-out prompt.

    The prompt keeps the shape the analysis workers already follow: one line
    naming the instruction, then `name = value` lines for the job, its
    parameters, every input, the outputs, the problem file and the workspace,
    then reading batches over the inputs.
    """
    store = run.store
    seq = store.next_seq()
    attempt = f"{seq:06d}-{job.name}"
    directory = store.handout_dir(attempt)
    scratch = directory / "scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    (directory / "outputs").mkdir(parents=True, exist_ok=True)
    pins = {name: run.resolve(name, job.inputs) for name in job.inputs}
    paths: dict[str, Path | None] = {}
    for name, pinned in pins.items():
        if pinned.data is None:
            paths[name] = None
            continue
        store.put(pinned.data)
        spec = job.inputs[name]
        if spec.address == "file":
            # A file is handed at its own path, so an instruction's relative
            # links still resolve. Its pinned version is recorded; a method
            # that changes mid-run makes the run unpublishable anyway.
            paths[name] = run.file_path(spec)
            continue
        path = directory / "inputs" / f"{name}.md"
        store.write_bytes(path, pinned.data)
        paths[name] = path
    outputs = {name: directory / "outputs" / f"{name}.md" for name in job.outputs}
    problem = directory / "problem.md"
    worker_runtime = directory / WORKER_RUNTIME
    run_values = {"run": str(store.run_dir), "run-id": store.run_dir.name,
                  "artifact": str(store.artifact_dir), "workspace": f"{directory}/"}
    values = {"job": job.name, **({"role": job.role} if job.role else {}),
              "attempt": attempt, "run-id": store.run_dir.name}
    values |= {key: _substitute(value, run_values, run.parameters) for key, value in job.parameters.items()}
    framed = {job.instruction, PROMPT_SECTION_INPUT}
    values |= {name: (str(path) if path else "absent") for name, path in paths.items() if name not in framed}
    values["output"] = str(outputs[job.outputs[0]])
    values |= {f"output-{name}": str(path) for name, path in outputs.items() if name != job.outputs[0]}
    values |= {"problem": str(problem), "worker-runtime": str(worker_runtime),
               "workspace": f"{directory}/", "artifact": str(store.artifact_dir), "scratch": f"{scratch}/"}
    previous = run.latest_completed(job.name)
    if previous is not None:
        for name, version in previous["outputs"].items():
            path = directory / "previous" / f"{name}.md"
            store.write_bytes(path, store.get(version))
            values[f"previous-{name}"] = str(path)
    instruction = paths[job.instruction]
    lines = [f"Follow {instruction} with:", *(f"{key} = {value}" for key, value in values.items())]
    section = pins.get(PROMPT_SECTION_INPUT)
    if section is not None and section.data is not None:
        # The plan's section fills one part of the engine's frame, from the frame's own lines.
        lines += ["", render_prompt_section(section.data.decode("utf-8"), values)]
    readable = [str(path) for name, path in paths.items() if path is not None and name not in framed]
    readable += [value for key, value in values.items() if key.startswith("previous-")]
    if readable:
        lines += ["", "## Input reading batches", "",
                  f"Read the named job instruction {instruction} before these reading batches.", "",
                  ("Load inputs in these batches to avoid truncated reads. Use one tool "
                   "call per batch, return the complete command result, and recover any "
                   "truncation before continuing. Read oversized files in bounded ranges."), ""]
        lines += [f"{number}. " + ", ".join(batch) for number, batch in enumerate(reading_batches(readable), 1)]
        oversized = [Path(path) for path in readable if Path(path).stat().st_size > READ_BATCH_BYTES]
        if oversized:
            lines += ["", "Oversized-file ranges:",
                      ("Read each range in a separate tool call. A single oversized line "
                       "still needs a smaller read if delivery is truncated.")]
            for path in oversized:
                spans = "; ".join(f"{start}-{end}" for start, end in reading_ranges(path))
                lines.append(f"- {path}: lines {spans}")
    lines += ["", "If you cannot produce the output, write the problem to the problem path.",
              ('Write a JSON object to the worker-runtime path with exactly the string fields "model" and "effort": '
               'the exact model ID and the effort level your runtime instructions or environment state, or '
               '"not stated" for each value they do not state. Do not infer either from the requested worker '
               'profile; a supplied instruction may say where your harness states them. Do not scan session '
               'logs or edit engine-owned run metadata.')]
    prompt = directory / "prompt.md"
    store.write_bytes(prompt, ("\n".join(lines) + "\n").encode("utf-8"))
    store.open_attempt({
        "id": attempt, "seq": seq, "job": job.name, "kind": "model",
        "pins": {name: pinned.pin() for name, pinned in pins.items()},
        "previous_outputs": {} if previous is None else dict(previous["outputs"]),
    })
    return Handout(attempt, job.name, prompt, outputs, problem, worker_runtime)


def handout_for(run: Run, record: dict) -> Handout:
    """The hand-out of an open attempt, from its record and the hand-out layout."""
    job = run.jobs.job(record["job"])
    directory = run.store.handout_dir(record["id"])
    outputs = {name: directory / "outputs" / f"{name}.md" for name in job.outputs}
    return Handout(record["id"], job.name, directory / "prompt.md", outputs, directory / "problem.md",
                   directory / WORKER_RUNTIME)

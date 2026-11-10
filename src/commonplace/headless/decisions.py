"""Decisions: asks whose answer steers the workflow, parsed and checked by code.

A workflow branches only on what code can parse. `decide()` asks for one
output that is either a markdown file whose YAML frontmatter carries the
decision, or a YAML mapping as the whole file, and checks the mapping against
a declared schema: each field is required and takes one of a closed set of
values or a value of the given type. A violation is the rejection the next
attempt answers, through `checked()`, so a malformed decision costs one
corrected attempt rather than a crashed run. `check(data, text)` adds the
checks a schema cannot state, such as a field required only for one choice or
a section the markdown body must have.

The prompt is the caller's. `decide()` appends the schema's fields, so a
worker sees the closed choices it must pick from, and on a retry the problems
of the attempt before.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any

import yaml

from commonplace.headless.harness import Profile
from commonplace.headless.jobs import Answer, Run
from commonplace.lib import frontmatter

Schema = Mapping[str, Any]
"""Field name -> a type, a tuple of types, or a collection of allowed values (which may include None)."""


def _is_types(spec: Any) -> bool:
    return isinstance(spec, type) or (isinstance(spec, tuple) and bool(spec) and all(isinstance(t, type) for t in spec))


def _render(value: Any) -> str:
    return "null" if value is None else str(value).lower() if isinstance(value, bool) else str(value)


def describe(schema: Schema) -> str:
    """The schema's fields as one line each, for the prompt."""
    lines = []
    for name, spec in schema.items():
        if _is_types(spec):
            types = spec if isinstance(spec, tuple) else (spec,)
            allowed = " or ".join("null" if t is type(None) else t.__name__ for t in types)
            lines.append(f"- `{name}`: a {allowed} value")
        else:
            lines.append(f"- `{name}`: one of {', '.join(_render(value) for value in spec)}")
    return "\n".join(lines)


def parse(text: str) -> Any:
    """The decision: the frontmatter of a markdown text, or the whole text as YAML; a mapping when valid."""
    if frontmatter.opens_frontmatter(text):
        parsed = frontmatter.parse(text)
        if not parsed.ok:
            raise ValueError(f"frontmatter does not parse: {'; '.join(parsed.errors)}")
        data = parsed.data
    else:
        try:
            data = yaml.safe_load(text)
        except yaml.YAMLError as error:
            raise ValueError(f"YAML does not parse: {error}") from None
    return data


def violations(data: Mapping, schema: Schema) -> list[str]:
    """Each schema field that is missing or outside its declared values; empty when the data conforms."""
    found = []
    for name, spec in schema.items():
        if name not in data:
            found.append(f"`{name}` is missing")
            continue
        value = data[name]
        if _is_types(spec):
            types = spec if isinstance(spec, tuple) else (spec,)
            bad_bool = isinstance(value, bool) and bool not in types   # YAML true is not an int here
            if bad_bool or not isinstance(value, types):
                found.append(f"`{name}` must be {describe({name: spec}).split(': ', 1)[1]}, not {_render(value)!r}")
        elif not any(value == allowed and type(value) is type(allowed) for allowed in spec):
            found.append(f"`{name}` must be one of {', '.join(_render(v) for v in spec)}, not {_render(value)!r}")
    return found


def decide(run: Run, job: str, prompt: str, schema: Schema, *, output: str = "decision",
           inputs: dict[str, str] | Callable | None = None, check: Callable[[dict, str], list[str]] | None = None,
           attempts: int = 3, profile: Profile | None = None) -> tuple[dict | None, Answer]:
    """Ask for the decision output, check it, and return the parsed mapping with the answer.

    A worker problem returns `(None, answer)` unchecked, as `checked()` does.
    Out of attempts raises `OutOfAttempts` with the last violations.
    `profile`, when given, is the worker profile of this ask (see `Run.ask`).
    """
    fields = f"\nThe decision fields, each required:\n{describe(schema)}\n"

    def build(problems: list[list[str]]) -> str:
        text = prompt + fields
        if problems:
            text += "\nAn earlier answer was rejected. Write it again, correcting:\n"
            text += "".join(f"- {problem}\n" for problem in problems[-1])
        return text

    def found(answer: Answer) -> list[str]:
        text = answer.outputs[output]
        try:
            data = parse(text)
        except ValueError as error:
            return [str(error)]
        if not isinstance(data, dict):
            return ["the decision must be a YAML mapping"]
        problems = violations(data, schema)
        return problems or (list(check(data, text)) if check else [])

    answer = run.checked(job, build, found, [output], attempts=attempts, inputs=inputs, profile=profile)
    return (None if answer.problem is not None else parse(answer.outputs[output])), answer

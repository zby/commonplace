"""Expand a compact plan into the full plan the engine runs.

A compact plan lists the jobs that write and the consumer's own code jobs;
the structural jobs between them are derived from the type's layout. The
engine receives the expansion and fixes it in the run metadata, so status,
judgments and attempt records see ordinary job names. The design and its
syntax are kb/reference/proposals/plans-without-structural-wrapper-code.md.

A `jobs` entry takes one of three forms:

- `role: R` fills role R with a model job named R. Unless R verifies other
  roles, a derived `check-R` judges each candidate; a verifying role gets
  `apply-R`, which applies its verdicts instead.
- `job: N` runs a standard handler over roles, such as the artifact check.
- `name: N` is a job in the engine's full form, kept as written.

A plan without any `role:` or `job:` entry is already full and is returned
unchanged.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

from commonplace.artifactrun.plan import PlanError, reject_underscored_keys
from commonplace.lib.directory_layout import Layout, parse_layout
from commonplace.lib.note_parser import parse_document
from commonplace.lib.type_resolver import SCHEMA_URI_SCHEME

STANDARD = "commonplace.artifactrun.handlers"
CHECK = f"{STANDARD}.check"
APPLY = f"{STANDARD}.apply_verdict"
ARTIFACT_CHECK = f"{STANDARD}.artifact_check"
HANDLER_OUTPUTS = {ARTIFACT_CHECK: ["findings"]}
"""Outputs a `job:` entry gets when it declares none."""
CHECK_GROUP = "check"
"""The plan-level criteria group every derived job receives besides its type closure."""
MODES = ("required", "optional", "order-only")
ROLE_KEYS = {"role", "instruction", "max-attempts", "outputs", "reads", "criteria", "files",
             "parameters", "verified-by", "checks", "feedback"}
JOB_KEYS = {"job", "handler", "inputs", "outputs"}
PLAN_KEYS = {"type", "criteria", "inputs", "defaults", "frozen-source", "prompt-section", "jobs"}


def is_compact(data: Mapping[str, Any]) -> bool:
    """A plan is compact when any entry is a `role:` or `job:` entry."""
    return any(isinstance(entry, dict) and ("role" in entry or "job" in entry) and "name" not in entry
               for entry in data.get("jobs") or [])


def expand_text(text: str, *, library: Path, plan_dir: Path) -> str:
    """The full declaration for a plan's text; a full plan comes back unchanged."""
    data = yaml.safe_load(text)
    if not isinstance(data, dict) or not is_compact(data):
        return text
    return yaml.safe_dump(expand(data, library=library, plan_dir=plan_dir), sort_keys=False)


def expand(data: Mapping[str, Any], *, library: Path, plan_dir: Path) -> dict:
    """Expand a compact plan; `plan_dir` resolves entries' instruction paths."""
    reject_underscored_keys(data)
    unknown = set(data) - PLAN_KEYS
    if unknown:
        raise PlanError(f"unknown keys {sorted(unknown)}")
    type_spec = data.get("type")
    if not isinstance(type_spec, str):
        raise PlanError("type must name the artifact's type, relative to the KB root")
    layout = _layout(library, type_spec)
    expansion = _Expansion(data, layout=layout, library=library.resolve(), plan_dir=plan_dir.resolve(),
                           type_spec=type_spec)
    return expansion.run()


def _layout(library: Path, type_spec: str) -> Layout:
    document, error = parse_document((library / type_spec).read_text(encoding="utf-8"))
    if document is None or not document.frontmatter or "layout" not in document.frontmatter:
        raise PlanError(f"{type_spec}: not a type with a layout ({error or 'no layout'})")
    return parse_layout(document.frontmatter["layout"], where=f"{type_spec}: layout")


def type_closure(library: Path, type_paths: list[str]) -> list[str]:
    """Each type spec, its schema and every schema those reference, as library paths."""
    seen: list[str] = []

    def add(path: str) -> None:
        if path in seen or not (library / path).is_file():
            return
        seen.append(path)
        text = (library / path).read_text(encoding="utf-8")
        if path.endswith(".md"):
            document, _ = parse_document(text)
            schema = (document.frontmatter or {}).get("schema") if document is not None else None
            if isinstance(schema, str):
                add(_relative(path, schema))
        else:
            for ref in _refs(yaml.safe_load(text)):
                target = ref.partition("#")[0]
                # The validator's resolver reads `commonplace:<path>` from the library root.
                prefix = f"{SCHEMA_URI_SCHEME}:"
                add(target[len(prefix):] if target.startswith(prefix) else _relative(path, target))

    for path in type_paths:
        add(path)
    return seen


def _relative(origin: str, target: str) -> str:
    joined = PurePosixPath(origin).parent / target
    parts: list[str] = []
    for part in joined.parts:
        if part == "..":
            parts.pop()
        elif part != ".":
            parts.append(part)
    return "/".join(parts)


def _refs(node: Any) -> list[str]:
    if isinstance(node, dict):
        found = [node["$ref"]] if isinstance(node.get("$ref"), str) and not node["$ref"].startswith("#") else []
        return found + [ref for value in node.values() for ref in _refs(value)]
    if isinstance(node, list):
        return [ref for value in node for ref in _refs(value)]
    return []


def _criterion_name(path: str) -> str:
    return "criterion-" + re.sub(r"[^A-Za-z0-9]+", "-", path).strip("-")


class _Expansion:
    def __init__(self, data: Mapping[str, Any], *, layout: Layout, library: Path, plan_dir: Path,
                 type_spec: str) -> None:
        self.data = data
        self.layout = layout
        self.library = library
        self.plan_dir = plan_dir
        self.type_spec = type_spec
        self.groups = data.get("criteria") or {}
        self.defaults = data.get("defaults") or {}
        self.frozen = data.get("frozen-source")
        if self.frozen is not None and self.frozen not in layout.roles:
            raise PlanError(f"frozen-source {self.frozen} is not a role of the type")
        self.entries = list(data.get("jobs") or [])
        self.outputs: dict[str, list[str]] = {}
        self.fillers: dict[str, str] = {}
        for entry in self.entries:
            name, outputs, role = self._shape(entry)
            if name in self.outputs:
                raise PlanError(f"two jobs are named {name}")
            self.outputs[name] = outputs
            if role is not None:
                self.fillers[role] = name
        self.derived = {f"{prefix}-{entry['role']}" for entry in self.entries if "role" in entry and "name" not in entry
                        for prefix in ("check", "apply")}
        clash = sorted(self.derived & set(self.outputs))
        if clash:
            raise PlanError(f"jobs {clash} are derived from the layout; declare a role's own check with `checks`")

    def _shape(self, entry: Any) -> tuple[str, list[str], str | None]:
        if not isinstance(entry, dict):
            raise PlanError("each job must be a mapping")
        if "name" in entry:
            return entry["name"], list(entry.get("outputs") or []), entry.get("role")
        if "role" in entry:
            role = entry["role"]
            if role not in self.layout.roles:
                raise PlanError(f"role {role} is not a role of the type")
            return role, list(entry.get("outputs") or [role]), role
        if "job" in entry:
            return entry["job"], list(entry.get("outputs") or HANDLER_OUTPUTS.get(entry.get("handler"), [])), None
        raise PlanError("a job entry needs role:, job: or name:")

    # Reads

    def read(self, source: str, mode: Any) -> tuple[str, dict]:
        """One read as an input name and the engine's input form."""
        mode = mode or "required"
        if mode not in MODES:
            raise PlanError(f"read {source}: mode must be one of {', '.join(MODES)}")
        if source.startswith("refusal:"):
            role = source.removeprefix("refusal:")
            if role not in self.fillers:
                raise PlanError(f"read {source}: no job fills {role}")
            name, spec = f"{role}-refusal", {"address": "refusal", "source": self.fillers[role]}
        elif ":" in source:
            job, _, output = source.partition(":")
            if output not in self.outputs.get(job, []):
                raise PlanError(f"read {source}: no declared job {job} with output {output}")
            name = job if len(self.outputs[job]) == 1 else f"{job}-{output}"
            spec = {"address": "output", "source": source}
        else:
            if source not in self.layout.roles:
                raise PlanError(f"read {source}: not a role of the type")
            name, spec = source, {"address": "role", "source": source}
        if mode == "optional":
            spec["required"] = False
        elif mode == "order-only":
            spec["order-only"] = True
        return name, spec

    def reads(self, entry: Mapping[str, Any]) -> dict[str, dict]:
        role = self.layout.roles[entry["role"]]
        raw = entry.get("reads")
        if raw is None:
            raw = {source: "required" for source in
                   [*(s.role for s in role.identity), *role.cites] if source != role.name}
        if not isinstance(raw, dict):
            raise PlanError(f"role {role.name}: reads must map reads to modes")
        return dict(self.read(source, mode) for source, mode in raw.items())

    def check_inputs(self, entry: Mapping[str, Any]) -> dict[str, dict]:
        """Inputs that a declared check needs and only the derived job receives."""
        inputs = {}
        for check in entry.get("checks") or []:
            if isinstance(check, dict):
                for name, read in (check.get("inputs") or {}).items():
                    source, mode = (read["source"], read.get("mode")) if isinstance(read, dict) else (read, None)
                    inputs[name] = self.read(source, mode)[1]
        return inputs

    # Criteria

    def library_path(self, relative: Any, what: str) -> str:
        """A path written relative to the plan file, as a library path."""
        if not isinstance(relative, str) or not relative:
            raise PlanError(f"{what} must name a file relative to the plan")
        path = (self.plan_dir / relative).resolve()
        try:
            return path.relative_to(self.library).as_posix()
        except ValueError as error:
            raise PlanError(f"{what} {relative} is outside the library") from error

    def criteria(self, roles: list[str]) -> dict[str, dict]:
        types = [self.layout.roles[role].type for role in dict.fromkeys(roles)]
        own = (self.library / self.type_spec)
        document, _ = parse_document(own.read_text(encoding="utf-8"))
        schema = (document.frontmatter or {}).get("schema") if document is not None else None
        paths = type_closure(self.library, types)
        if isinstance(schema, str):
            paths += [p for p in type_closure(self.library, [_relative(self.type_spec, schema)]) if p not in paths]
        group = dict(self.groups.get(CHECK_GROUP) or {})
        given = set(group.values())
        return {**{_criterion_name(path): {"address": "file", "source": path} for path in paths if path not in given},
                **{name: {"address": "file", "source": path} for name, path in group.items()}}

    def options(self, entry: Mapping[str, Any]) -> dict:
        options: dict[str, Any] = {}
        if self.frozen is not None:
            options["frozen-source"] = self.frozen
        if entry.get("checks"):
            options["checks"] = entry["checks"]
        if entry.get("feedback"):
            options["feedback"] = entry["feedback"]
        return options

    # Jobs

    def run(self) -> dict:
        jobs = []
        for entry in self.entries:
            if "name" in entry:
                jobs.append(dict(entry))
            elif "role" in entry:
                jobs += self.role_jobs(entry)
            else:
                jobs.append(self.standard_job(entry))
        plan = {"type": self.type_spec}
        if self.data.get("prompt-section") is not None:
            plan["prompt-section"] = self.library_path(self.data["prompt-section"], "prompt-section")
        if self.groups:
            plan["criteria"] = dict(self.groups)
        plan["jobs"] = jobs
        return plan

    def role_jobs(self, entry: Mapping[str, Any]) -> list[dict]:
        unknown = set(entry) - ROLE_KEYS
        if unknown:
            raise PlanError(f"role {entry['role']}: unknown keys {sorted(unknown)}")
        role = self.layout.roles[entry["role"]]
        name, outputs = role.name, self.outputs[role.name]
        instruction = entry.get("instruction")
        if not isinstance(instruction, str):
            raise PlanError(f"role {role.name}: instruction must name a file")
        instruction_path = self.library_path(instruction, f"role {role.name}: instruction")
        reads = self.reads(entry)
        inputs: dict[str, dict] = {"instruction": {"address": "file", "source": instruction_path}}
        inputs.update(self.type_inputs(role.name, reads))
        files = entry.get("files") or {}
        typed = {spec["source"] for spec in inputs.values() if spec["address"] == "file"} - {instruction_path}
        listed = sorted(name for name, path in files.items() if path in typed)
        if listed:
            raise PlanError(f"role {role.name}: files {listed} name types the loader already hands out")
        inputs.update({key: {"address": "file", "source": value} for key, value in files.items()})
        inputs.update(dict(self.data.get("inputs") or {}))
        inputs.update(reads)
        for verifier in entry.get("verified-by") or []:
            if verifier not in self.layout.roles:
                raise PlanError(f"role {role.name}: verified-by {verifier} is not a role")
            gated = [source for source, spec in reads.items()
                     if spec["address"] == "role" and spec["source"] in self.layout.roles[verifier].verifies]
            if not gated:
                raise PlanError(f"role {role.name}: {verifier} verifies none of its reads")
            for read in gated:
                subject = reads[read]["source"]
                inputs[f"{subject}-verified"] = {"address": "judgment", "source": subject,
                                                 "relation": f"{verifier}:verifies:{subject}",
                                                 "outcome": "accepted"}
        parameters = {**(self.defaults.get("parameters") or {}), **(entry.get("parameters") or {})}
        model = {"name": name, "kind": "model", "role": role.name, "instruction": "instruction",
                 "max-attempts": entry.get("max-attempts", self.defaults.get("max-attempts")),
                 "outputs": outputs, "inputs": inputs}
        if parameters:
            model["parameters"] = parameters
        if model["max-attempts"] is None:
            del model["max-attempts"]
        if entry.get("criteria"):
            model["criteria"] = list(entry["criteria"])
        derived = self.apply_job(entry, reads) if role.verifies else self.check_job(entry)
        return [model, derived]

    def type_inputs(self, role: str, reads: Mapping[str, dict]) -> dict[str, dict]:
        """The types a model job writes and reads by: its member's and each read member's.

        Named `member-type` and `<role>-type`, so a prompt names them without
        a plan listing them. The artifact type is not among them: a producer's
        contract is its member type, the types of what it reads and the
        contracts those name.
        """
        inputs = {"member-type": {"address": "file", "source": self.layout.roles[role].type}}
        for spec in reads.values():
            if spec["address"] == "role" and spec["source"] != role:
                inputs[f"{spec['source']}-type"] = {"address": "file",
                                                    "source": self.layout.roles[spec["source"]].type}
        return inputs

    def _correction_inputs(self, name: str, outputs: list[str], attempt: str, *, trigger: bool) -> dict[str, dict]:
        """The candidate and what checking its correction answers needs.

        A check reads the producer's attempt record order-only: a rerun with
        identical bytes changes no candidate, answers or answered refusal,
        each a trigger of its own. A verdict's application keeps the record
        as a trigger, since the verifier's record names what it was handed.
        """
        record = {"address": "attempt", "source": name}
        if not trigger:
            record["order-only"] = True
        inputs = {"candidate": {"address": "output", "source": f"{name}:{outputs[0]}"},
                  attempt: record,
                  "answered-refusal": {"address": "handed", "source": f"{attempt}:refusal", "required": False}}
        if len(outputs) > 1:
            inputs["answers"] = {"address": "output", "source": f"{name}:{outputs[1]}", "required": False}
        return inputs

    def check_job(self, entry: Mapping[str, Any]) -> dict:
        role = self.layout.roles[entry["role"]]
        name = role.name
        inputs = self._correction_inputs(name, self.outputs[name], "producer-attempt", trigger=False)
        identity = [source.role for source in role.identity if source.role != name]
        for partner in identity:
            inputs[partner] = {"address": "role", "source": partner}
        for partner in role.cites:
            if partner != name and partner not in inputs:
                inputs[partner] = {"address": "role", "source": partner, "required": False}
        if self.frozen is not None and self.frozen != name and self.frozen not in inputs:
            inputs[self.frozen] = {"address": "role", "source": self.frozen}
        inputs.update(self.check_inputs(entry))
        partners = [spec["source"] for spec in inputs.values() if spec["address"] == "role"]
        inputs.update(self.criteria([name, *partners]))
        return {"name": f"check-{name}", "kind": "code", "handler": CHECK, "inputs": inputs, "outputs": [],
                "options": self.options(entry)}

    def apply_job(self, entry: Mapping[str, Any], reads: Mapping[str, dict]) -> dict:
        role = self.layout.roles[entry["role"]]
        name = role.name
        inputs = self._correction_inputs(name, self.outputs[name], "verifier-attempt", trigger=True)
        for read, spec in reads.items():
            if spec["address"] in ("role", "output"):
                handed = {"address": "handed", "source": f"verifier-attempt:{read}"}
                if spec.get("required") is False:
                    handed["required"] = False
                inputs[f"{read}-handed"] = handed
        missing = [subject for subject in role.verifies if subject not in reads]
        if missing:
            raise PlanError(f"role {name}: verifies {', '.join(missing)} but does not read them")
        # The frozen source comes handed when the verifier read its member, else live.
        if self.frozen is not None and self.frozen != name and f"{self.frozen}-handed" not in inputs:
            inputs[self.frozen] = {"address": "role", "source": self.frozen}
        inputs.update(self.check_inputs(entry))
        roles = [spec["source"] for read, spec in reads.items() if spec["address"] == "role"]
        inputs.update(self.criteria([name, *roles]))
        return {"name": f"apply-{name}", "kind": "code", "handler": APPLY, "inputs": inputs, "outputs": [],
                "options": self.options(entry)}

    def standard_job(self, entry: Mapping[str, Any]) -> dict:
        unknown = set(entry) - JOB_KEYS
        if unknown:
            raise PlanError(f"job {entry['job']}: unknown keys {sorted(unknown)}")
        raw = entry.get("inputs") or []
        pairs = [self.read(source, None) for source in raw] if isinstance(raw, list) else [
            self.read(source, mode) for source, mode in raw.items()]
        inputs = dict(pairs)
        roles = [spec["source"] for spec in inputs.values() if spec["address"] == "role"]
        if self.frozen is not None and self.frozen not in roles:
            inputs[self.frozen] = {"address": "role", "source": self.frozen}
            roles.append(self.frozen)
        inputs.update(self.criteria(roles))
        options = {"frozen-source": self.frozen} if self.frozen is not None else {}
        return {"name": entry["job"], "kind": "code", "handler": entry["handler"], "inputs": inputs,
                "outputs": self.outputs[entry["job"]], "options": options}

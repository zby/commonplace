"""A directory type's declared layout: its roles, their files and relations.

A directory type spec may carry ``layout`` in its frontmatter. Each role names
one direct child file of the artifact, the document type expected there, the
roles whose fields it must repeat (``identity``), the roles whose
declarations its references may resolve against (``cites``) and the roles
whose versions its verdict judges (``verifies``). An identity source named
``run`` binds fields to the run's values instead, the run parameters and
``run-id``, which only a caller inside a run supplies. The layout owns
membership and requiredness; the type's schema keeps the manifest's instance
metadata. A verifying role's document follows the verification protocol,
whose grammar is a layout finding.

Findings carry the role they belong to, so a caller that wants one member's
findings filters by role, and the repair the code that made them supplies.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import PurePosixPath
from typing import Any

from commonplace.lib.note_parser import ParsedDocument, section

MEMBERSHIP = ("open", "closed")
RUN = "run"
"""The identity source that names the run's values; no role may take the name."""


@dataclass(frozen=True)
class IdentitySource:
    role: str
    fields: tuple[str, ...]


@dataclass(frozen=True)
class Role:
    name: str
    path: str
    type: str
    identity: tuple[IdentitySource, ...] = ()
    cites: tuple[str, ...] = ()
    verifies: tuple[str, ...] = ()
    run_binding: tuple[str, ...] = ()


@dataclass(frozen=True)
class Requirement:
    always: tuple[str, ...] = ()
    when_role: str | None = None
    when_field: str | None = None
    values: Mapping[str, tuple[str, ...]] = field(default_factory=dict)


GENERIC_REPAIR = "correct the named field, section or citation to satisfy the stated rule and supplied type contract"
"""The repair a finding carries when the code that made it supplies none."""


@dataclass(frozen=True)
class Finding:
    """One layout or relation finding; ``role`` is None for files no role matches
    and for findings about the artifact as a whole. ``absent`` marks a required
    member that is not there yet, which a working instance expects. ``info``
    marks what standing validation reports without failing, such as evidence
    whose pinned bytes are not on this machine."""

    role: str | None
    message: str
    absent: bool = False
    info: bool = False
    repair: str = field(default=GENERIC_REPAIR, compare=False)
    warn: bool = False

    def render(self) -> str:
        """Identical diagnostic text for self-check and workflow acceptance."""
        return f"{self.message}\nRepair: {self.repair}"


@dataclass(frozen=True)
class Layout:
    roles: Mapping[str, Role]
    required: Requirement
    membership: str

    def role_at(self, filename: str) -> Role | None:
        return next((role for role in self.roles.values() if role.path == filename), None)

    def path(self, role: str) -> str:
        return self.roles[role].path

    def requirement(self, members: Mapping[str, ParsedDocument]) -> tuple[set[str], set[str] | None]:
        """Roles this instance requires, and the roles it permits (None: all).

        A declared discriminator selects a value list: that instance requires
        and permits ``always`` plus the list. When the discriminating member
        is absent, only ``always`` is required and every role is permitted.
        """
        required = set(self.required.always)
        if self.required.when_role is None:
            return required, None
        document = members.get(self.path(self.required.when_role))
        if document is None:
            return required, None
        value = (document.frontmatter or {}).get(self.required.when_field)
        selected = set(self.required.values.get(value, ()) if isinstance(value, str) else ())
        return required | selected, required | selected


def _names(value: Any, where: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
        raise ValueError(f"{where}: must be a list of names")
    if len(set(value)) != len(value):
        raise ValueError(f"{where}: names must be unique")
    return tuple(value)


def _mapping(value: Any, where: str, allowed: set[str], required: set[str] = frozenset()) -> dict:
    if not isinstance(value, dict):
        raise TypeError(f"{where}: must be a mapping")
    unknown = set(value) - allowed
    if unknown:
        raise ValueError(f"{where}: unknown keys {sorted(unknown)}")
    missing = required - set(value)
    if missing:
        raise ValueError(f"{where}: missing keys {sorted(missing)}")
    return value


def parse_layout(value: Any, *, where: str = "layout") -> Layout:
    """Read a type spec's ``layout`` value; ValueError names the first defect."""
    data = _mapping(value, where, {"membership", "roles", "required"}, {"membership", "roles"})
    if data["membership"] not in MEMBERSHIP:
        raise ValueError(f"{where}.membership: must be one of {', '.join(MEMBERSHIP)}")
    raw_roles = data["roles"]
    if not isinstance(raw_roles, dict) or not raw_roles:
        raise ValueError(f"{where}.roles: must be a nonempty mapping")
    roles: dict[str, Role] = {}
    for name, raw in raw_roles.items():
        at = f"{where}.roles.{name}"
        if not isinstance(name, str) or not name:
            raise ValueError(f"{where}.roles: role names must be nonempty strings")
        if name == RUN:
            raise ValueError(f"{at}: {RUN} names the run's values, not a role")
        entry = _mapping(raw, at, {"path", "type", "identity", "cites", "verifies"}, {"path", "type"})
        path = entry["path"]
        if (not isinstance(path, str) or PurePosixPath(path).name != path
                or path.startswith(".") or not path.endswith(".md")):
            raise ValueError(f"{at}.path: must name a direct Markdown file")
        if not isinstance(entry["type"], str) or not entry["type"].endswith(".md"):
            raise ValueError(f"{at}.type: must be a type path ending in .md")
        identity, run_binding = [], ()
        raw_identity = entry.get("identity", [])
        if not isinstance(raw_identity, list):
            raise TypeError(f"{at}.identity: must be a list of sources")
        for index, source in enumerate(raw_identity):
            source = _mapping(source, f"{at}.identity[{index}]", {"from", "fields"}, {"from", "fields"})
            fields = _names(source["fields"], f"{at}.identity[{index}].fields")
            if source["from"] == RUN:
                run_binding += fields
            else:
                identity.append(IdentitySource(source["from"], fields))
        cites = _names(entry.get("cites", []), f"{at}.cites")
        verifies = _names(entry.get("verifies", []), f"{at}.verifies")
        if name in verifies:
            raise ValueError(f"{at}.verifies: a role cannot verify itself")
        roles[name] = Role(name, path, entry["type"], tuple(identity), cites, verifies, run_binding)
    paths = [role.path for role in roles.values()]
    if len(set(paths)) != len(paths):
        raise ValueError(f"{where}.roles: two roles share a path")
    for role in roles.values():
        for target in (*(source.role for source in role.identity), *role.cites, *role.verifies):
            if target not in roles:
                raise ValueError(f"{where}.roles.{role.name}: names unknown role {target!r}")
    raw_required = _mapping(data.get("required", {}), f"{where}.required", {"always", "when"})
    always = _names(raw_required.get("always", []), f"{where}.required.always")
    when_role = when_field = None
    values: dict[str, tuple[str, ...]] = {}
    if "when" in raw_required:
        when = _mapping(raw_required["when"], f"{where}.required.when", {"role", "field", "values"}, {"role", "field", "values"})
        when_role, when_field = when["role"], when["field"]
        if not isinstance(when_field, str) or not when_field:
            raise ValueError(f"{where}.required.when.field: must be a field name")
        if not isinstance(when["values"], dict):
            raise ValueError(f"{where}.required.when.values: must map values to role lists")
        values = {
            str(key): _names(names, f"{where}.required.when.values.{key}")
            for key, names in when["values"].items()
        }
    for name in (*always, *((when_role,) if when_role else ()), *(n for names in values.values() for n in names)):
        if name not in roles:
            raise ValueError(f"{where}.required: names unknown role {name!r}")
    return Layout(roles, Requirement(always, when_role, when_field, values), data["membership"])


PROTOCOL_SECTIONS = ("Blockers", "Limits")
"""The sections of a verifying role's document, each exactly `none` or a list of `- ` entries."""


def protocol_sections(body: str) -> dict[str, str | None]:
    """Each protocol section's text, stripped; None when its heading is absent."""
    return {title: section(body, title).strip() if re.search(rf"(?m)^## {title}[ \t]*$", body) else None
            for title in PROTOCOL_SECTIONS}


def blocker_entries(blockers: str) -> list[str]:
    """The `- ` entries of a Blockers list, continuation lines joined; `none` has none."""
    entries = []
    for line in blockers.splitlines():
        if line.startswith("- "):
            entries.append(line)
        elif entries and line.strip():
            entries[-1] += "\n" + line
    return entries


def addressee(entry: str) -> str:
    """The role a `- <role>: ...` blocker addresses."""
    return entry[2:].partition(":")[0].strip()


def protocol_findings(role: Role, body: str) -> list[Finding]:
    """How a verifying role's document departs from the verification protocol.

    With more than one verified role, every blocker starts with the one it addresses.
    """
    findings = []
    sections = protocol_sections(body)
    for title, text in sections.items():
        if text is None:
            findings.append(Finding(role.name, f"{role.path}: ## {title} is missing",
                                    repair=f"add ## {title} with none or one '- ' entry per finding"))
        elif text != "none" and (not text.startswith("- ") or any(
                line.strip() and not line.startswith(("- ", " ", "\t")) for line in text.splitlines())):
            findings.append(Finding(role.name, f"{role.path}: {title} must be exactly none or a Markdown list",
                                    repair=f"write none or one '- ' entry per {title.lower()} finding; "
                                           "indent continuation lines"))
    blockers = sections["Blockers"]
    if blockers and blockers != "none" and len(role.verifies) > 1:
        for entry in blocker_entries(blockers):
            if addressee(entry) not in role.verifies:
                findings.append(Finding(
                    role.name, f"{role.path}: blocker addresses none of {', '.join(role.verifies)}: "
                               f"{entry.splitlines()[0]}",
                    repair="start the blocker with the one member whose text must change, as '- <member>: '"))
            elif not entry.partition(":")[2].strip():
                findings.append(Finding(
                    role.name, f"{role.path}: blocker addressed to {addressee(entry)} states no finding",
                    repair="follow the addressee with the finding, its records and its evidence"))
    return findings


def layout_findings(layout: Layout, members: Mapping[str, ParsedDocument],
                    run_values: Mapping[str, str] | None = None) -> list[Finding]:
    """Membership, document types, requiredness and identity over the members present.

    Fields bound to the run are checked only when ``run_values`` is given.
    """
    findings: list[Finding] = []
    for name in sorted(members):
        if layout.role_at(name) is None and layout.membership == "closed":
            findings.append(Finding(None, f"{name}: no layout role; this type has closed membership",
                                    repair="remove the file, or write it at the path of the role it fills"))
    required, permitted = layout.requirement(members)
    discriminator = (
        f"{layout.path(layout.required.when_role)} {layout.required.when_field}"
        if layout.required.when_role else ""
    )
    for role in layout.roles.values():
        document = members.get(role.path)
        if document is None:
            if role.name in required:
                findings.append(Finding(role.name, f"{role.path}: required member is absent", absent=True,
                                        repair="supply the member at its declared path"))
            continue
        if permitted is not None and role.name not in permitted:
            value = (members[layout.path(layout.required.when_role)].frontmatter or {}).get(layout.required.when_field)
            findings.append(Finding(role.name, f"{role.path}: not a member when {discriminator} is {value!r}",
                                    repair="remove this member, which that value does not admit"))
        actual = (document.frontmatter or {}).get("type")
        if actual != role.type:
            findings.append(Finding(role.name, f"{role.path}: type {actual!r} does not match the layout's {role.type}",
                                    repair=f"set the member's type to {role.type}"))
        if role.verifies:
            findings += protocol_findings(role, document.body)
        values = document.frontmatter or {}
        for name in role.run_binding if run_values is not None else ():
            if values.get(name) != run_values.get(name):
                findings.append(Finding(
                    role.name,
                    f"{role.path}: identity field {name} {values.get(name)!r} does not match "
                    f"the run; expected {run_values.get(name)!r}",
                    repair="use the run's value shown, which the prompt prints as the line of that name",
                ))
        for source in role.identity:
            source_role = layout.roles[source.role]
            origin = members.get(source_role.path)
            if origin is None:
                findings.append(Finding(
                    role.name,
                    f"{role.path}: cannot check identity fields {', '.join(source.fields)}; "
                    f"source member {source_role.path} is absent",
                    repair="supply the named source member before checking this dependent identity",
                ))
                continue
            expected_values = origin.frontmatter or {}
            for name in source.fields:
                if values.get(name) != expected_values.get(name):
                    findings.append(Finding(
                        role.name,
                        f"{role.path}: identity field {name} {values.get(name)!r} does not match "
                        f"{source_role.path}; expected {expected_values.get(name)!r}",
                        repair="use the expected identity value from the named source member",
                    ))
    return findings

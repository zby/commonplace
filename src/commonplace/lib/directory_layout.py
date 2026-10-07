"""A directory type's declared layout: its roles, their files and relations.

A directory type spec may carry ``layout`` in its frontmatter. Each role names
one direct child file of the artifact, the document type expected there, the
roles whose fields it must repeat, and the roles whose declarations its
references may resolve against. The layout owns membership and requiredness;
the type's schema keeps the manifest's instance metadata.

Findings carry the role they belong to, so a caller that wants one member's
findings filters by role.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import PurePosixPath
from typing import Any

from commonplace.lib.note_parser import ParsedDocument

MEMBERSHIP = ("open", "closed")


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


@dataclass(frozen=True)
class Requirement:
    always: tuple[str, ...] = ()
    by_role: str | None = None
    by_field: str | None = None
    values: Mapping[str, tuple[str, ...]] = field(default_factory=dict)


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
    repair: str = ""
    warn: bool = False

    def __post_init__(self) -> None:
        if not self.repair:
            repairs = {
                "unresolved record": "use the full ID of a declaration in this role's citation scope; remove unsupported references",
                "duplicate": "keep one declaration per ID and give distinct records distinct names",
                "required member is absent": "supply the member at its declared path",
                "identity field": "use the expected identity value from the named source member",
                "source member": "supply the named source member before checking this dependent identity",
                "does not match": "use the expected value shown for this slot",
                "unverified": "make the boundary's pinned source bytes available and check again",
                "limit not carried": "carry the named limit and its affected IDs into synthesis Limitations",
                "missing field": "supply the named field with an answer or an explicit evidence limit",
            }
            object.__setattr__(self, "repair", next(
                (text for phrase, text in repairs.items() if phrase in self.message),
                "correct the named field, section or citation to satisfy the stated rule and supplied type contract",
            ))

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
        if self.required.by_role is None:
            return required, None
        document = members.get(self.path(self.required.by_role))
        if document is None:
            return required, None
        value = (document.frontmatter or {}).get(self.required.by_field)
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
        entry = _mapping(raw, at, {"path", "type", "identity", "cites"}, {"path", "type"})
        path = entry["path"]
        if (not isinstance(path, str) or PurePosixPath(path).name != path
                or path.startswith(".") or not path.endswith(".md")):
            raise ValueError(f"{at}.path: must name a direct Markdown file")
        if not isinstance(entry["type"], str) or not entry["type"].endswith(".md"):
            raise ValueError(f"{at}.type: must be a type path ending in .md")
        identity = []
        raw_identity = entry.get("identity", [])
        if not isinstance(raw_identity, list):
            raise TypeError(f"{at}.identity: must be a list of sources")
        for index, source in enumerate(raw_identity):
            source = _mapping(source, f"{at}.identity[{index}]", {"from", "fields"}, {"from", "fields"})
            identity.append(IdentitySource(source["from"], _names(source["fields"], f"{at}.identity[{index}].fields")))
        cites = _names(entry.get("cites", []), f"{at}.cites")
        roles[name] = Role(name, path, entry["type"], tuple(identity), cites)
    paths = [role.path for role in roles.values()]
    if len(set(paths)) != len(paths):
        raise ValueError(f"{where}.roles: two roles share a path")
    for role in roles.values():
        for target in (*(source.role for source in role.identity), *role.cites):
            if target not in roles:
                raise ValueError(f"{where}.roles.{role.name}: names unknown role {target!r}")
    raw_required = _mapping(data.get("required", {}), f"{where}.required", {"always", "by"})
    always = _names(raw_required.get("always", []), f"{where}.required.always")
    by_role = by_field = None
    values: dict[str, tuple[str, ...]] = {}
    if "by" in raw_required:
        by = _mapping(raw_required["by"], f"{where}.required.by", {"role", "field", "values"}, {"role", "field", "values"})
        by_role, by_field = by["role"], by["field"]
        if not isinstance(by_field, str) or not by_field:
            raise ValueError(f"{where}.required.by.field: must be a field name")
        if not isinstance(by["values"], dict):
            raise ValueError(f"{where}.required.by.values: must map values to role lists")
        values = {
            str(key): _names(names, f"{where}.required.by.values.{key}")
            for key, names in by["values"].items()
        }
    for name in (*always, *((by_role,) if by_role else ()), *(n for names in values.values() for n in names)):
        if name not in roles:
            raise ValueError(f"{where}.required: names unknown role {name!r}")
    return Layout(roles, Requirement(always, by_role, by_field, values), data["membership"])


def layout_findings(layout: Layout, members: Mapping[str, ParsedDocument]) -> list[Finding]:
    """Membership, document types, requiredness and identity over the members present."""
    findings: list[Finding] = []
    for name in sorted(members):
        if layout.role_at(name) is None and layout.membership == "closed":
            findings.append(Finding(None, f"{name}: no layout role; this type has closed membership"))
    required, permitted = layout.requirement(members)
    discriminator = (
        f"{layout.path(layout.required.by_role)} {layout.required.by_field}"
        if layout.required.by_role else ""
    )
    for role in layout.roles.values():
        document = members.get(role.path)
        if document is None:
            if role.name in required:
                findings.append(Finding(role.name, f"{role.path}: required member is absent", absent=True))
            continue
        if permitted is not None and role.name not in permitted:
            value = (members[layout.path(layout.required.by_role)].frontmatter or {}).get(layout.required.by_field)
            findings.append(Finding(role.name, f"{role.path}: not a member when {discriminator} is {value!r}"))
        actual = (document.frontmatter or {}).get("type")
        if actual != role.type:
            findings.append(Finding(role.name, f"{role.path}: type {actual!r} does not match the layout's {role.type}"))
        values = document.frontmatter or {}
        for source in role.identity:
            source_role = layout.roles[source.role]
            origin = members.get(source_role.path)
            if origin is None:
                findings.append(Finding(
                    role.name,
                    f"{role.path}: cannot check identity fields {', '.join(source.fields)}; "
                    f"source member {source_role.path} is absent",
                ))
                continue
            expected_values = origin.frontmatter or {}
            for name in source.fields:
                if values.get(name) != expected_values.get(name):
                    findings.append(Finding(
                        role.name,
                        f"{role.path}: identity field {name} {values.get(name)!r} does not match "
                        f"{source_role.path}; expected {expected_values.get(name)!r}",
                    ))
    return findings

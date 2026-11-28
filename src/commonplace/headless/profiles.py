"""Resolve one roster identity with only the calling workflow's harness grant."""

from pathlib import Path

import yaml

from commonplace.headless.harness import Profile

WORKER_PROFILES = "instructions/worker-profiles.yaml"  # relative to the library (or pinned worktree KB)


def resolve_profile(data: bytes, name: str | None, workflow: str) -> tuple[str, Profile]:
    config = yaml.safe_load(data)
    roster = config.get("profiles") if isinstance(config, dict) else None
    if not isinstance(roster, dict) or not roster:
        raise ValueError("worker profiles need a nonempty profiles mapping")
    policies = config.get("workflows")
    policy = policies.get(workflow) if isinstance(policies, dict) else None
    if not isinstance(policy, dict):
        raise ValueError(f"no workflow policy for {workflow!r}")  # noqa: TRY004 - invalid config
    chosen = name if name is not None else policy.get("default")
    if chosen not in roster:
        raise ValueError(f"unknown worker profile {chosen!r}; choose one of {', '.join(sorted(roster))}")
    entry = roster[chosen]
    fields = {"harness", "launch-model", "effort"}
    if (not isinstance(entry, dict) or set(entry) != fields
            or any(not isinstance(value, str) or not value.strip() for value in entry.values())):
        raise ValueError(f"worker profile {chosen} needs only harness, launch-model and effort")
    grants = policy.get("harnesses")
    flags = grants.get(entry["harness"]) if isinstance(grants, dict) else None
    if not isinstance(flags, dict):
        raise ValueError(f"no {workflow} grant for harness {entry['harness']!r}")  # noqa: TRY004 - invalid config
    return chosen, Profile.from_yaml_entry({**entry, "flags": flags})


def load_profile(path: Path, name: str | None, workflow: str) -> Profile:
    return resolve_profile(path.read_bytes(), name, workflow)[1]

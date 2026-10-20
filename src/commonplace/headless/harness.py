"""Worker profiles as Workjig command workers for the harnesses' headless modes.

A worker profile names a harness, a launch model and an effort, as in
kb/agentic-system-analyses/instructions/analyse-agentic-system/worker-profiles.yaml.
`Harness.worker()` turns a profile into a `workjig.CommandWorker`: the
harness's print-mode command with its machine-readable output, so Workjig
classifies the launch from the harness's terminal event. `model_used()` reads
the model the harness itself recorded for a finished launch, from the launch's
retained stdout or the harness's session file; that is the run's provenance.

Workers load their normal configuration. The working directory is the
prepared worktree, so the harness reads the project's AGENTS.md / CLAUDE.md,
skills, settings and permissions exactly as an interactive session there
would. Nothing here strips ambient context: no --safe-mode,
--ignore-user-config, --no-skills or --no-context-files.

Adapted from mdflow (MIT): the command builder that turns a dictionary of
flags into arguments (src/command-builder.ts), the per-harness print-mode
defaults (src/adapters/{claude,codex,pi}.ts) and Claude's background-task
ceiling disabled (src/adapters/claude.ts).
"""

from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path

from workjig import CommandWorker, LaunchRecord
from workjig.adapters import parse_evidence

POINTER = ("Read the complete invocation at `{prompt}` and follow it. "
           "Recover any truncated read before proceeding.")
"""The prompt argument; Workjig fills `{prompt}` with each launch's frame file."""


@dataclass
class Profile:
    harness: str                      # claude-code, codex or pi
    launch_model: str                 # the name the harness selects a model by
    effort: str
    flags: dict = field(default_factory=dict)   # extra harness flags, as in mdflow frontmatter

    @classmethod
    def from_yaml_entry(cls, entry: dict) -> Profile:
        return cls(entry["harness"], entry["launch-model"], entry["effort"], dict(entry.get("flags", {})))


# --- Building commands (ported from mdflow's src/command-builder.ts) ---------

# Variadic flags consume every following argument, so they are written as
# --flag=value; otherwise `--add-dir x PROMPT` would take the prompt as a directory.
VARIADIC_FLAGS = {"allowed-tools", "allowedTools", "disallowed-tools", "disallowedTools",
                  "tools", "add-dir", "betas", "mcp-config", "plugin-dir"}


def to_flag(key: str) -> str:
    """"model" -> "--model", "p" -> "-p"; a key that already starts with "-" is kept."""
    if key.startswith("-"):
        return key
    return f"-{key}" if len(key) == 1 else f"--{key}"


def build_args(flags: dict) -> list[str]:
    """Each key becomes a flag. True -> the bare flag; False or None -> omitted;
    a list -> the flag repeated per value; anything else -> the flag and its value.
    Keys starting with "_" are for the builder (_subcommand, _env), not the harness;
    dictionaries are skipped, since they do not map to flags."""
    args: list[str] = []
    for key, value in flags.items():
        if key.startswith("_") or value is None or value is False or isinstance(value, dict):
            continue
        flag = to_flag(key)
        if value is True:
            args.append(flag)
            continue
        if isinstance(value, str) and key in VARIADIC_FLAGS:
            # mdflow splits "Read,Edit" and "Bash(git commit:*), Bash(git add:*)".
            value = value.split(", ") if ", " in value else value.split(",")
        for v in value if isinstance(value, list) else [value]:
            args.extend([f"{flag}={str(v).strip()}"] if key in VARIADIC_FLAGS else [flag, str(v)])
    return args


def subcommands(flags: dict) -> list[str]:
    sub = flags.get("_subcommand")
    if not sub:
        return []
    return [str(s) for s in sub] if isinstance(sub, list) else [str(sub)]


@dataclass
class Harness:
    """A harness's executable, its print-mode defaults and how a profile maps onto its flags.

    `translate(profile)` returns the profile's flags for this harness.
    Precedence, as in mdflow: defaults < translation < profile.flags.
    `protocol` names the Workjig output protocol of the harness's stdout, or
    None to classify by exit status and the file protocol alone.
    `model_used(launch)` reads the model the harness recorded for a finished
    launch, or None when it recorded none.
    """
    executable: str
    defaults: dict
    translate: Callable[[Profile], dict]
    protocol: str | None = None
    model_used: Callable[[LaunchRecord], str | None] | None = None

    def worker(self, profile: Profile) -> CommandWorker:
        flags = {**self.defaults, **self.translate(profile), **profile.flags}
        env = {str(k): str(v) for k, v in (flags.get("_env") or {}).items()}
        argv = (self.executable, *subcommands(flags), *build_args(flags), POINTER)
        return CommandWorker(argv=argv, name=profile.harness, env=env, output_protocol=self.protocol)


def _claude(profile: Profile) -> dict:
    return {"model": profile.launch_model, "effort": profile.effort}


def _codex(profile: Profile) -> dict:
    return {"model": profile.launch_model, "config": [f"model_reasoning_effort={profile.effort}"],
            "output-last-message": "{launch_dir}/last-message.md"}


def _pi(profile: Profile) -> dict:
    # pi takes the thinking level as a ":<level>" suffix on the model.
    return {"model": f"{profile.launch_model}:{profile.effort}"}


def stdout(launch: LaunchRecord) -> str:
    path = Path(launch.launch_dir) / "stdout.log"
    return path.read_text(encoding="utf-8", errors="replace") if path.is_file() else ""


def _models(values: set[str]) -> str | None:
    """One recorded model, or every recorded model joined, so a mixed launch shows as such."""
    return ", ".join(sorted(values)) or None


def _claude_model(launch: LaunchRecord) -> str | None:
    """Claude Code's result event lists the models used under `modelUsage`."""
    evidence = parse_evidence("claude", stdout(launch))
    usage = evidence.get("model_usage")
    if isinstance(usage, dict) and usage:
        return _models(set(usage))
    reported = evidence.get("reported_model")
    return reported if isinstance(reported, str) else None


def _codex_model(launch: LaunchRecord) -> str | None:
    """codex writes `payload.model` on its turn_context events in the session file under ~/.codex/sessions."""
    session = parse_evidence("codex", stdout(launch)).get("session_id")
    if not isinstance(session, str):
        return None
    models = set()
    for path in (Path.home() / ".codex" / "sessions").rglob(f"*{session}*.jsonl"):
        for line in path.read_text(errors="replace").splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            value = event.get("payload") if isinstance(event, dict) else None
            if isinstance(value, dict) and isinstance(value.get("model"), str):
                models.add(value["model"])
    return _models(models)


def _pi_model(launch: LaunchRecord) -> str | None:
    """pi's assistant `message_end` events carry the model that answered."""
    evidence = parse_evidence("pi", stdout(launch))
    model = evidence.get("served_model") or evidence.get("reported_model")
    return model if isinstance(model, str) else None


HARNESSES = {
    "claude-code": Harness("claude", {
        "print": True, "output-format": "stream-json", "verbose": True,
        # Print mode ends the run when background tasks are still alive after
        # 600 s; "0" disables that ceiling (mdflow's claude adapter).
        "_env": {"CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS": "0"},
    }, _claude, "claude-stream-json", _claude_model),
    "codex": Harness("codex", {"_subcommand": "exec", "json": True}, _codex, "codex-json", _codex_model),
    "pi": Harness("pi", {"print": True, "mode": "json"}, _pi, "pi-json", _pi_model),
}


def model_used(profile: Profile, launch: LaunchRecord, harnesses=HARNESSES) -> str | None:
    """The model the profile's harness recorded for `launch`, or None."""
    reader = harnesses[profile.harness].model_used
    return reader(launch) if reader else None

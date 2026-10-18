"""Run one agent job through a harness's headless mode.

A worker profile names a harness, a launch model and an effort, as in
kb/agentic-system-analyses/instructions/analyse-agentic-system/worker-profiles.yaml.
`launch()` starts that harness once, non-interactively, in the given working
directory, and waits for it. `run_with_retries()` repeats a launch only after
a transient provider failure.

Workers load their normal configuration. The working directory is the
prepared worktree, so the harness reads the project's AGENTS.md / CLAUDE.md,
skills, settings and permissions exactly as an interactive session there
would. Unlike mdflow (../../../../treadle/external/mdflow, MIT), whose process
handling this adapts, nothing here strips ambient context: no --safe-mode,
--ignore-user-config, --no-skills or --no-context-files.

Adapted from mdflow: the command builder that turns a dictionary of flags
into arguments (src/command-builder.ts), the per-harness print-mode defaults
(src/adapters/{claude,codex,pi}.ts), stdin closed for print-mode engines and a
process group killed on timeout (src/command.ts), and Claude's background-task
ceiling disabled (src/adapters/claude.ts).
"""

from __future__ import annotations

import json
import os
import shlex
import signal
import subprocess
import time
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable


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

@dataclass
class CommandSpec:
    executable: str
    subcommands: list[str]            # e.g. ["exec"] for codex exec
    args: list[str]                   # flags and their values
    positionals: list[str]            # the prompt
    env: dict[str, str]               # merged over os.environ at launch

    def argv(self) -> list[str]:
        return [self.executable, *self.subcommands, *self.args, *self.positionals]

    def display(self) -> str:
        return shlex.join(self.argv())


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

    `translate(profile, attempt_dir)` returns the profile's flags for this
    harness and the session ID chosen in advance, or None if the harness
    reports one itself. Precedence, as in mdflow: defaults < translation < profile.flags.
    """
    executable: str
    defaults: dict
    translate: Callable[[Profile, Path], tuple[dict, str | None]]
    session_from_output: Callable[[str], str | None] | None = None

    def command(self, profile: Profile, prompt: str, attempt_dir: Path) -> tuple[CommandSpec, str | None]:
        translated, session = self.translate(profile, attempt_dir)
        flags = {**self.defaults, **translated, **profile.flags}
        env = {str(k): str(v) for k, v in (flags.get("_env") or {}).items()}
        return CommandSpec(self.executable, subcommands(flags), build_args(flags), [prompt], env), session


def _claude(profile: Profile, attempt_dir: Path) -> tuple[dict, str]:
    session = str(uuid.uuid4())
    return {"model": profile.launch_model, "effort": profile.effort, "session-id": session}, session


def _codex(profile: Profile, attempt_dir: Path) -> tuple[dict, None]:
    return {"model": profile.launch_model, "config": [f"model_reasoning_effort={profile.effort}"],
            "output-last-message": str(attempt_dir / "last-message.md")}, None


def _pi(profile: Profile, attempt_dir: Path) -> tuple[dict, str]:
    session = str(uuid.uuid4())
    # pi takes the thinking level as a ":<level>" suffix on the model.
    return {"model": f"{profile.launch_model}:{profile.effort}", "session-id": session}, session


def _codex_session(stdout: str) -> str | None:
    """The session ID from codex's --json events; it names the rollout file under ~/.codex/sessions."""
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict):
            for key in ("thread_id", "session_id", "conversation_id"):
                if isinstance(event.get(key), str):
                    return event[key]
    return None


HARNESSES = {
    "claude-code": Harness("claude", {
        "print": True, "output-format": "json",
        # Print mode ends the run when background tasks are still alive after
        # 600 s; "0" disables that ceiling (mdflow's claude adapter).
        "_env": {"CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS": "0"},
    }, _claude),
    "codex": Harness("codex", {"_subcommand": "exec", "json": True}, _codex, _codex_session),
    "pi": Harness("pi", {"print": True}, _pi),
}


@dataclass
class Launch:
    argv: list[str]
    session: str | None               # the harness's session ID, for finding its transcript
    exit_code: int | None             # None: killed at the timeout
    stdout: str
    stderr: str
    started: float
    seconds: float
    attempt_dir: str

    @property
    def ok(self) -> bool:
        return self.exit_code == 0


def launch(profile: Profile, prompt: str, cwd: Path, attempt_dir: Path,
           timeout: float | None = None, harnesses=HARNESSES) -> Launch:
    """Start the harness once and wait for it. Never raises on worker failure."""
    attempt_dir.mkdir(parents=True, exist_ok=True)
    harness = harnesses[profile.harness]
    spec, session = harness.command(profile, prompt, attempt_dir)
    argv = spec.argv()
    started = time.time()
    proc = subprocess.Popen(
        argv, cwd=cwd, env={**os.environ, **spec.env}, text=True,
        stdin=subprocess.DEVNULL,           # codex exec otherwise waits for stdin EOF
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        start_new_session=True,             # own process group, so a timeout kills its children
    )
    try:
        stdout, stderr = proc.communicate(timeout=timeout)
        exit_code = proc.returncode
    except subprocess.TimeoutExpired:
        _kill_group(proc)
        stdout, stderr = proc.communicate()
        exit_code = None
    if harness.session_from_output:
        session = harness.session_from_output(stdout)
    result = Launch(argv, session, exit_code, stdout, stderr, started,
                    time.time() - started, str(attempt_dir))
    (attempt_dir / "launch.json").write_text(json.dumps(asdict(result), indent=2))
    return result


def _kill_group(proc: subprocess.Popen, grace: float = 10) -> None:
    for sig in (signal.SIGTERM, signal.SIGKILL):
        try:
            os.killpg(proc.pid, sig)
        except ProcessLookupError:
            return
        try:
            proc.wait(timeout=grace)
            return
        except subprocess.TimeoutExpired:
            continue


# Provider failures that establish no task defect, from the analysis driver's
# transient-worker rule. Matched only in a failed launch's stderr, not in the
# worker's own output, so an analyst quoting these words does not qualify.
TRANSIENT = (
    "Our servers are currently overloaded. Please try again later.",
    "An error occurred while processing your request.",
    "OpenAI Responses stream ended before a terminal response event",
)

# After the first transient failure wait 30 s, after the second 120 s, after the third stop.
BACKOFF = (30, 120)


def is_transient(result: Launch) -> bool:
    return result.exit_code not in (0, None) and any(m in result.stderr for m in TRANSIENT)


class LaunchFailed(Exception):
    def __init__(self, launches: list[Launch]):
        last = launches[-1]
        reason = "timed out" if last.exit_code is None else f"exit {last.exit_code}"
        super().__init__(f"{reason} after {len(launches)} launch(es): {last.stderr.strip()[-500:]}")
        self.launches = launches


@dataclass
class Delivered:
    launch: Launch
    failed: list[Launch] = field(default_factory=list)   # transient failures before it


def run_with_retries(profile: Profile, prompt: str, cwd: Path, attempt_dir: Path,
                     timeout: float | None = None, backoff=BACKOFF, sleep=time.sleep,
                     harnesses=HARNESSES) -> Delivered:
    """Launch, and relaunch the same prompt only after a transient provider failure.

    Any other failure (a nonzero exit without a transient message, or a
    timeout, whose effects are uncertain) raises LaunchFailed at once.
    """
    launches: list[Launch] = []
    for n in range(len(backoff) + 1):
        result = launch(profile, prompt, cwd, attempt_dir / f"launch-{n + 1}", timeout, harnesses)
        launches.append(result)
        if result.ok:
            return Delivered(result, launches[:-1])
        if not is_transient(result) or n == len(backoff):
            raise LaunchFailed(launches)
        sleep(backoff[n])
    raise AssertionError("unreachable")

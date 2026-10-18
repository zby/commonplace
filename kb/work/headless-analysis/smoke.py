"""Run one tiny real job per harness, with no API-key variables in the environment.

    python3 smoke.py codex pi          # any of: claude-code codex pi

Each job runs in a fresh temporary directory, so the run proves the harness
works from its subscription login (ChatGPT for codex and pi's openai
provider, claude.ai for Claude Code), not from a key inherited from the shell.
It checks that the output file is written and that the recorded session ID
names a real session.
"""

import os
import sys
import tempfile
from pathlib import Path

from headless import Profile
from jobs import Run

# Removed before any launch; workers inherit os.environ.
STRIPPED = ("OPENAI_API_KEY", "OPENAI_BASE_URL", "OPENAI_ORG_ID", "OPENAI_PROJECT_ID",
            "OPENROUTER_API_KEY", "ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CODEX_API_KEY")

PROFILES = {
    "claude-code": Profile("claude-code", "haiku", "low", {"permission-mode": "acceptEdits"}),
    # codex exec refuses a directory outside a Git repository without the flag,
    # and its default sandbox is read-only.
    "codex": Profile("codex", "gpt-6-luna", "low",
                     {"skip-git-repo-check": True, "sandbox": "workspace-write"}),
    "pi": Profile("pi", "gpt-6-luna", "low"),
}


def session_exists(harness: str, session: str | None) -> bool:
    if not session:
        return False
    roots = {"codex": Path.home() / ".codex" / "sessions",
             "pi": Path.home() / ".pi" / "agent" / "sessions",
             "claude-code": Path.home() / ".claude" / "projects"}
    return any(session in p.name for p in roots[harness].rglob("*.jsonl"))


def main(names):
    for var in STRIPPED:
        os.environ.pop(var, None)
    failures = 0
    for name in names:
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            run = Run(tmp / "run", tmp, PROFILES[name], timeout=300)
            try:
                a = run.ask("smoke", "Write the single word hello to the output file. Do nothing else.",
                            ["word"])
            except Exception as e:                  # report and go on to the next harness
                failures += 1
                print(f"{name}: FAILED: {e}")
                continue
            word = a.outputs.get("word", "").strip()
            found = session_exists(name, a.record["session"])
            ok = word.lower().strip(".") == "hello" and found
            failures += not ok
            print(f"{name}: {'ok' if ok else 'FAILED'}: word={word!r} session={a.record['session']} "
                  f"session-file-found={found} seconds={a.record['seconds']:.0f}")
    return failures


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["codex", "pi"]))

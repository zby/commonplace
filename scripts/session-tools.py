#!/usr/bin/env python3
"""Extract tool calls from a Claude Code session log.

Usage:
    # Most recent session (excluding the current one):
    python3 scripts/session-tools.py

    # Specific session by ID prefix:
    python3 scripts/session-tools.py ba134a26

    # Show only Read calls:
    python3 scripts/session-tools.py --tool Read

    # List recent sessions to pick from:
    python3 scripts/session-tools.py --list
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path


def find_project_dir() -> Path:
    """Find the Claude project directory for the current working directory."""
    cwd = Path.cwd().resolve()
    slug = str(cwd).replace("/", "-")
    return Path.home() / ".claude" / "projects" / slug


def list_sessions(project_dir: Path, limit: int = 10) -> list[tuple[Path, str, str]]:
    """List recent sessions with timestamps and first prompts."""
    sessions = []
    for p in sorted(project_dir.glob("*.jsonl"), key=os.path.getmtime, reverse=True):
        if "subagent" in str(p):
            continue
        ts = datetime.fromtimestamp(os.path.getmtime(p)).strftime("%H:%M:%S")
        first_msg = ""
        with open(p) as f:
            for line in f:
                obj = json.loads(line)
                if obj.get("type") == "queue-operation" and obj.get("operation") == "enqueue":
                    first_msg = obj.get("content", "")[:80]
                    break
        sessions.append((p, ts, first_msg))
        if len(sessions) >= limit:
            break
    return sessions


def extract_tool_calls(session_path: Path, tool_filter: str | None = None) -> list[dict]:
    """Extract tool calls from a session log, including subagent logs."""
    calls = []

    def _extract_from_file(path: Path, agent_label: str = ""):
        with open(path) as f:
            for line in f:
                obj = json.loads(line)
                msg = obj.get("message", {})
                if isinstance(msg, str):
                    try:
                        msg = json.loads(msg)
                    except (json.JSONDecodeError, TypeError):
                        continue
                if not isinstance(msg, dict):
                    continue
                content = msg.get("content", [])
                if not isinstance(content, list):
                    continue
                for block in content:
                    if not isinstance(block, dict) or block.get("type") != "tool_use":
                        continue
                    name = block.get("name", "")
                    if tool_filter and name != tool_filter:
                        continue
                    inp = block.get("input", {})
                    calls.append({"name": name, "input": inp, "agent": agent_label})

    # Main session
    _extract_from_file(session_path)

    # Subagent logs
    subagent_dir = session_path.with_suffix("") / "subagents"
    if subagent_dir.is_dir():
        for sub in sorted(subagent_dir.glob("*.jsonl")):
            agent_id = sub.stem.replace("agent-", "")[:8]
            _extract_from_file(sub, agent_label=f"sub:{agent_id}")

    return calls


def format_call(call: dict) -> str:
    """Format a single tool call for display."""
    name = call["name"]
    inp = call["input"]
    agent = call["agent"]
    prefix = f"  [{agent}] " if agent else "  "

    if name == "Read":
        path = inp.get("file_path", "")
        # Shorten absolute paths
        cwd = str(Path.cwd()) + "/"
        if path.startswith(cwd):
            path = path[len(cwd):]
        return f"{prefix}Read: {path}"
    elif name == "Grep":
        pattern = inp.get("pattern", "")
        path = inp.get("path", "")
        cwd = str(Path.cwd()) + "/"
        if path.startswith(cwd):
            path = path[len(cwd):]
        return f'{prefix}Grep: "{pattern}" in {path}'
    elif name == "Glob":
        return f"{prefix}Glob: {inp.get('pattern', '')}"
    elif name == "Write":
        path = inp.get("file_path", "")
        cwd = str(Path.cwd()) + "/"
        if path.startswith(cwd):
            path = path[len(cwd):]
        return f"{prefix}Write: {path}"
    elif name == "Edit":
        path = inp.get("file_path", "")
        cwd = str(Path.cwd()) + "/"
        if path.startswith(cwd):
            path = path[len(cwd):]
        return f"{prefix}Edit: {path}"
    elif name == "Skill":
        return f"{prefix}Skill: {inp.get('skill', '')}"
    elif name == "Bash":
        return f"{prefix}Bash: {inp.get('command', '')[:100]}"
    else:
        return f"{prefix}{name}: {json.dumps(inp)[:120]}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract tool calls from a Claude Code session log.",
    )
    parser.add_argument(
        "session_id",
        nargs="?",
        help="Session ID prefix (default: most recent non-current session)",
    )
    parser.add_argument(
        "--tool",
        help="Filter to a specific tool name (e.g. Read, Grep, Write)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        dest="list_sessions",
        help="List recent sessions instead of extracting tools",
    )
    args = parser.parse_args()

    project_dir = find_project_dir()
    if not project_dir.is_dir():
        print(f"No project directory found at {project_dir}", file=sys.stderr)
        return 1

    if args.list_sessions:
        sessions = list_sessions(project_dir)
        for path, ts, msg in sessions:
            sid = path.stem[:12]
            print(f"  {ts}  {sid}...  {msg}")
        return 0

    # Find the target session
    if args.session_id:
        matches = [
            p
            for p in project_dir.glob("*.jsonl")
            if p.stem.startswith(args.session_id) and "subagent" not in str(p)
        ]
        if not matches:
            print(f"No session matching '{args.session_id}'", file=sys.stderr)
            return 1
        session_path = max(matches, key=os.path.getmtime)
    else:
        sessions = list_sessions(project_dir, limit=2)
        if not sessions:
            print("No sessions found", file=sys.stderr)
            return 1
        # Most recent session
        session_path = sessions[0][0]

    # Extract and display
    print(f"Session: {session_path.stem}")
    sessions_info = list_sessions(project_dir, limit=10)
    for path, ts, msg in sessions_info:
        if path == session_path:
            print(f"  Time: {ts}  Prompt: {msg}")
            break
    print()

    calls = extract_tool_calls(session_path, tool_filter=args.tool)
    if not calls:
        print("  (no tool calls found)")
        return 0

    for call in calls:
        print(format_call(call))

    # Summary
    print()
    tool_counts: dict[str, int] = {}
    for call in calls:
        tool_counts[call["name"]] = tool_counts.get(call["name"], 0) + 1
    print(f"Total: {len(calls)} tool calls —", ", ".join(f"{n}: {c}" for n, c in sorted(tool_counts.items())))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

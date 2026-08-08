#!/usr/bin/env bash
# Bootstrap the llm-commonplace dev install for Claude Code cloud sessions.
#
# This only runs in cloud sessions, where CLAUDE_CODE_REMOTE=true. It installs
# the checkout through the same user-level editable uv-tool path used by local
# development, then exports the job-local tool directory to later Bash calls.
set -u

[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || exit 0

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/.." && pwd)}"
cd "$PROJECT_DIR" || exit 0

uv tool install --reinstall --python ">=3.11" --editable . \
  || echo "commonplace: editable tool install failed" >&2

# A SessionStart hook cannot update a parent shell. Publish uv's tool executable
# directory through Claude's environment handoff so later tool calls inherit it.
COMMONPLACE_TOOL_BIN="$(uv tool dir --bin 2>/dev/null || true)"
if [ -n "$COMMONPLACE_TOOL_BIN" ] \
  && [ -x "$COMMONPLACE_TOOL_BIN/commonplace-validate" ] \
  && [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "PATH=$COMMONPLACE_TOOL_BIN:$PATH" >> "$CLAUDE_ENV_FILE"
fi

exit 0

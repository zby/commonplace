#!/usr/bin/env bash
# Bootstrap the llm-commonplace dev install for Claude Code cloud sessions.
#
# Local sessions use direnv + a checked-out .venv (see AGENTS.md / INSTALL.md),
# so this only runs in cloud sessions, where CLAUDE_CODE_REMOTE=true. It is
# idempotent: a present venv short-circuits the install, so it costs one
# executable check on a snapshot that already has .venv (see the environment
# caching / setup-script split in code.claude.com/docs/en/claude-code-on-the-web).
set -u

[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || exit 0

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/.." && pwd)}"
cd "$PROJECT_DIR" || exit 0

# Create the venv + editable install only when it is missing (e.g. a fresh
# environment with no cached snapshot). uv's project-local cache keeps reinstalls
# fast; a present venv makes this a no-op.
if [ ! -x .venv/bin/commonplace-validate ]; then
  uv venv && uv pip install -e . || echo "commonplace: dev install failed" >&2
fi

# A SessionStart hook cannot `source .venv/bin/activate` — each Bash tool call is
# a fresh shell with no session to source into. The documented equivalent is to
# append PATH to $CLAUDE_ENV_FILE, which subsequent Bash calls inherit. This makes
# bare-name commonplace-* calls resolve, as AGENTS.md expects.
if [ -x .venv/bin/commonplace-validate ] && [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "PATH=$PROJECT_DIR/.venv/bin:$PATH" >> "$CLAUDE_ENV_FILE"
fi

exit 0

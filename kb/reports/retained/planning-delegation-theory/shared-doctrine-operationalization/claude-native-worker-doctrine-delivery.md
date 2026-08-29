# Claude native-worker doctrine delivery

## Result

Root Commonplace doctrine is delivered to Claude Code's native fresh workers
on the multistage skill's ordinary in-process path. The earlier Bash-launched
probe was inconclusive and does not govern this path.

This result was produced on 2026-08-29 with Claude Code 2.1.251 from
`/home/zby/llm/commonplace`. The parent launched two concurrent native `Agent`
workers with `subagent_type: "general-purpose"`; neither used the `fork`
subagent type.

## Probe

Both workers received the same packet. Before using a tool or opening a file,
they were asked to quote the ambient rules assigning parent scheduling,
integration, and recovery and governing nested delegation when authority is
silent. The packet named those subjects but did not contain the rule text.

Both workers returned these live sentences:

> The parent retains scheduling, integration, and recovery; parallel writers need disjoint ownership or an explicit coordination rule.

> Nested delegation requires explicit authorization; silence means no.

Each worker attributed the text to project instructions automatically loaded
from `CLAUDE.md`, which is the repository symlink to `AGENTS.md`. Each reported
no inherited parent conversation. Claude's harness reported zero tool uses for
both workers, and neither opened a file. Comparison after their return found no
word or punctuation difference from the live Delegation section; only the
source file's hard-wrap whitespace was absent from the quotations.

## Scope

The verified path is Claude Code 2.1.251 in-process `Agent` workers using a
non-fork `general-purpose` context from this checkout's working directory. It
is the native fresh-worker mechanism used by the multistage parent for its
source reconstructor, consolidated author, and independent reviewer.

Both workers ran on `claude-opus-5[1m]`: no subagent-model override was
configured in `.claude/settings.json`, `.claude/settings.local.json`, or
`~/.claude/settings.json`, so they inherited the parent session model. The
probed `AGENTS.md` was commit `530c01e979eebb3053f0569617107732e05f3973` with
a clean working tree for that path. The result is bounded by that model
partition; a provider-model or context-assembly change requires a fresh probe.

This result does not cover a `claude` Bash subprocess, a different working
directory, remote or worktree isolation, or custom agent definitions with
different context assembly. It proves delivery and provenance, not compliance
under task pressure. The workers also received user-level instructions,
memory, environment, tool, and skill listings, so the verified context is not
doctrine-only.

## Consequence

The Claude path may inherit the same generic delegation defaults already
verified for Codex. The earlier pilot's consumption-path objection to removing
those defaults from the shared multistage skill is superseded within this
scope. The later [lean candidate](./multistage-pilot.md) reduced the skill and
matched the baseline in fresh Codex and native-Claude behavioral traces.

The request and raw reply were exchanged through `kb/messages/`, which is
session-local and not retained. This report carries every boundary condition
the exchange established; the message files were deleted once consumed.

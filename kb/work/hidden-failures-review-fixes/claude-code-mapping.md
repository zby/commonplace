# Claude Code mapping for the hidden-failures review

Draft of the harness-specific material that
[Review recent Pi logs for hidden failures](../../instructions/review-recent-logs-for-hidden-failures.md)
lacks. It was supplied ad hoc in the 2026-11-07 worker brief and is retained
here so the instruction can absorb it (item D in the [README](./README.md)).

- Sessions live under `~/.claude/projects/<cwd-slug>/` as one JSONL per
  session. Worker transcripts live under `<session-id>/subagents/agent-<id>.jsonl`
  next to the parent file. There is no JSON-mode stream variant.
- Scanner: `python3 scripts/scan_tools/scan_claude_code_tool_failures.py <file>...`
  from the checkout; no `--format` flag. Pass files directly: piping through
  `xargs` replaces the scanner's exit 2 with xargs's 123.
- Project identity: `cwd` and `sessionId` on records; `first_timestamp` and
  `last_timestamp` from the scanner. File mtime moves when untimestamped
  cost records are appended, so it is not activity evidence.
- Branch model: records carry `uuid` and `parentUuid`; rewinds leave several
  children under one parent. Claude Code writes one assistant record per
  content block sharing a `message.id`, and attachment records may sit between
  a tool call and its result.
- Compaction: a `system` record with subtype `compact_boundary`;
  `logicalParentUuid` points at the pre-compaction tail and `compactMetadata`
  gives trigger and token count. Scanner list `compactions`.
- Provider errors: assistant records with `isApiErrorMessage: true`. Retry
  attempts are not persisted, so an empty `api_errors` list is not proof of
  no retries.
- Interruptions: user records whose text starts `[Request interrupted by user`.
  Tool results containing "The user doesn't want to proceed" are user
  rejections and "Permission for this action was denied" are harness denials;
  signals, not command failures.
- Shell exit codes: failed Bash output is prefixed `Exit code N`; successful
  output carries no exit code, so a wrapper that masked a failure looks like
  success. Sample successful pipelines.
- Worker launches: the parent's `toolUseResult.agentId`; scanner list
  `worker_ids`. Check the matching subagent file exists; list it as a missing
  child otherwise. Workers launched inside a worktree write to that worktree's
  own project directory, which needs separate authorization.
- Operator communications for the visibility assessment: the final assistant
  text of each turn and `system` records with subtype `away_summary`.

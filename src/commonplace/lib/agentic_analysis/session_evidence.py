"""Read only the native session assigned to a Workjig launch. Never copy it."""
from __future__ import annotations

import json
from hashlib import file_digest, sha256
from pathlib import Path

from commonplace.lib.agentic_analysis import claude_code_tool_failures, tool_failures


def file_hash(path: Path) -> str | None:
    if not path.is_file():
        return None
    with path.open('rb') as stream:
        return file_digest(stream, 'sha256').hexdigest()


def inspect_session(harness: str, identifier: str, path: Path) -> tuple[dict, dict]:
    """Reject foreign identities before exposing any findings or authorizing the path."""
    found = False
    calls = set()
    last = {}
    hashed = sha256()
    errors = 0
    with path.open('rb') as stream:
        for line in stream:
            hashed.update(line)
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except ValueError:
                errors += 1
                continue
            if not isinstance(event, dict):
                errors += 1
                continue
            kind = event.get('type')
            if not isinstance(kind, str):
                errors += 1
                continue
            if harness == 'pi':
                ids = [event.get('id')] if kind == 'session' else []
                if kind in {'message_end', 'tool_execution_start', 'tool_execution_end'}:
                    raise ValueError('expected a native Pi session')
            else:
                ids = [event[k] for k in ('sessionId', 'session_id') if k in event]
                if kind in ('assistant', 'user') and 'sessionId' not in event:
                    raise ValueError('expected a native Claude session')
            if ids:
                if any(value != identifier for value in ids):
                    raise ValueError('native session identity mismatch')
                found = True
            message = event.get('message')
            if isinstance(message, dict) and message.get('role') == 'assistant':
                content = message.get('content')
                if not isinstance(content, list):
                    errors += 1
                    continue
                last = message
                for block in content:
                    if isinstance(block, dict) and block.get('type') in ('toolCall', 'tool_use'):
                        if isinstance(block.get('id'), str):
                            calls.add(block['id'])
                        else:
                            errors += 1
    if not found:
        raise ValueError('missing native session identity')
    report = tool_failures.scan(path, 'pi-session') if harness == 'pi' else claude_code_tool_failures.scan(path)
    if report['format'] != ('pi-session' if harness == 'pi' else 'claude-code-session') or any(
        issue['message'].startswith('no recognized') for issue in report['input_issues']
    ):
        raise ValueError('unsupported native session format')
    digest = hashed.hexdigest()
    if path.resolve() != path or file_hash(path) != digest:
        raise ValueError('native session changed during scan')
    return {'trace': str(path), 'trace_sha256': digest, 'tool_calls': len(calls),
            'parse_errors': errors, 'model': last.get('responseModel') or last.get('model'),
            'terminal_assistant': (bool(last) and not any(b.get('type') in ('toolCall', 'tool_use')
                                   for b in last.get('content', []) if isinstance(b, dict))
                                   and (harness != 'pi' or last.get('stopReason') == 'stop'))}, report
